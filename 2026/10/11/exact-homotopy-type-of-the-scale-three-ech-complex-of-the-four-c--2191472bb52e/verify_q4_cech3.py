#!/usr/bin/env python3
"""Exact verification for the scale-three graph Čech complex of the four-cube."""
from collections import Counter, deque
from functools import lru_cache
import json

N = 4
VERTICES = tuple(range(1 << N))
TOGGLE_ORDER = (15, 8, 13, 4, 14, 6, 7, 0, 11, 3, 1, 2, 12, 9, 10, 5)


def hamming(a, b):
    return (a ^ b).bit_count()


def vertex_set(mask):
    return [v for v in VERTICES if (mask >> v) & 1]


def incidence(face, cell):
    """Oriented simplicial incidence [face:cell], for a codimension-one face."""
    vs = vertex_set(cell)
    missing = [v for v in vs if not ((face >> v) & 1)]
    assert len(missing) == 1
    return -1 if (vs.index(missing[0]) & 1) else 1


def build_complex():
    edges = []
    facets = []
    for a in VERTICES:
        for b in range(a + 1, 1 << N):
            if hamming(a, b) == 1:
                edges.append((a, b))
                facet = 0
                for x in VERTICES:
                    if hamming(x, a) <= 1 or hamming(x, b) <= 1:
                        facet |= 1 << x
                facets.append(facet)
    assert len(edges) == 32
    assert len(set(facets)) == 32
    assert all(f.bit_count() == 8 for f in facets)

    faces = set()
    for facet in facets:
        sub = facet
        while sub:
            faces.add(sub)
            sub = (sub - 1) & facet
    return edges, facets, faces


def staged_toggle_matching(faces):
    unmatched = set(faces)
    pairs = []
    for v in TOGGLE_ORDER:
        bit = 1 << v
        # Snapshot order is irrelevant: candidates have disjoint partners at a fixed stage.
        for low in list(unmatched):
            high = low | bit
            if (low & bit) == 0 and low in unmatched and high in unmatched:
                unmatched.remove(low)
                unmatched.remove(high)
                pairs.append((low, high))
    return pairs, unmatched


def hasse_covers(faces):
    covers = []
    for high in faces:
        if high.bit_count() < 2:
            continue
        for v in vertex_set(high):
            low = high & ~(1 << v)
            assert low in faces
            covers.append((low, high))
    return covers


def verify_acyclic(faces, covers, pairs):
    pairset = set(pairs)
    assert len(pairset) == len(pairs)
    touched = set()
    for low, high in pairs:
        assert low in faces and high in faces
        assert high.bit_count() == low.bit_count() + 1
        assert (low, high) in cover_set
        assert low not in touched and high not in touched
        touched.add(low); touched.add(high)

    adj = {f: [] for f in faces}
    indeg = {f: 0 for f in faces}
    for low, high in covers:
        if (low, high) in pairset:
            u, w = low, high       # matched Hasse edge is reversed
        else:
            u, w = high, low       # all other Hasse edges point downward
        adj[u].append(w)
        indeg[w] += 1
    q = deque([f for f in faces if indeg[f] == 0])
    seen = 0
    while q:
        u = q.popleft(); seen += 1
        for w in adj[u]:
            indeg[w] -= 1
            if indeg[w] == 0:
                q.append(w)
    assert seen == len(faces), "matching orientation contains a directed cycle"
    return seen


def morse_boundary_4_to_3(critical, pairs):
    up = {low: high for low, high in pairs}
    down = {high: low for low, high in pairs}
    critical3 = tuple(f for f in critical if f.bit_count() == 4)
    critical4 = tuple(f for f in critical if f.bit_count() == 5)
    assert len(critical3) == 1 and len(critical4) == 24
    target = critical3[0]

    @lru_cache(None)
    def contribution(cell4):
        out = 0
        matched_down = down.get(cell4)
        for v in vertex_set(cell4):
            face3 = cell4 & ~(1 << v)
            if face3 == matched_down:
                continue
            a = incidence(face3, cell4)
            if face3 == target:
                out += a
                continue
            next4 = up.get(face3)
            if next4 is None:
                continue
            b = incidence(face3, next4)
            # Eliminate the matched face: multiplier -a/b; b is ±1.
            out += (-a * b) * contribution(next4)
        return out

    coeffs = [contribution(c) for c in critical4]
    return target, critical4, coeffs


def rank_mod_p(columns, row_index, p):
    pivots = {}
    rank = 0
    for cell in columns:
        col = {}
        for v in vertex_set(cell):
            face = cell & ~(1 << v)
            r = row_index[face]
            val = incidence(face, cell) % p
            if val:
                col[r] = val
        while col:
            pivot = max(col)
            if pivot not in pivots:
                inv = pow(col[pivot], -1, p)
                if inv != 1:
                    col = {r: (c * inv) % p for r, c in col.items() if (c * inv) % p}
                pivots[pivot] = col
                rank += 1
                break
            factor = col[pivot]
            pc = pivots[pivot]
            for r, c in pc.items():
                nv = (col.get(r, 0) - factor * c) % p
                if nv:
                    col[r] = nv
                elif r in col:
                    del col[r]
    return rank


def betti_mod_p(faces, p):
    by_dim = {}
    maxdim = 0
    for f in faces:
        d = f.bit_count() - 1
        maxdim = max(maxdim, d)
        by_dim.setdefault(d, []).append(f)
    ranks = {0: 0, maxdim + 1: 0}
    for d in range(1, maxdim + 1):
        rows = sorted(by_dim[d - 1])
        row_index = {f: i for i, f in enumerate(rows)}
        ranks[d] = rank_mod_p(sorted(by_dim[d]), row_index, p)
    betti = []
    for d in range(maxdim + 1):
        betti.append(len(by_dim.get(d, [])) - ranks.get(d, 0) - ranks.get(d + 1, 0))
    return betti, ranks


edges, facets, faces = build_complex()
covers = hasse_covers(faces)
cover_set = set(covers)
pairs, critical = staged_toggle_matching(faces)
seen = verify_acyclic(faces, covers, pairs)

f_vector = [0] * 8
for f in faces:
    f_vector[f.bit_count() - 1] += 1
critical_vector = Counter(f.bit_count() - 1 for f in critical)
assert f_vector == [16, 112, 448, 1016, 1264, 800, 256, 32]
assert len(covers) == 18800
assert len(pairs) == 1959
assert critical_vector == Counter({4: 24, 3: 1, 0: 1})
assert seen == 3944

target3, critical4, morse_coeffs = morse_boundary_4_to_3(critical, pairs)
assert morse_coeffs == [0] * 24

modular = {}
for p in (2, 3, 5):
    betti, ranks = betti_mod_p(faces, p)
    assert betti == [1, 0, 0, 1, 24, 0, 0, 0]
    modular[str(p)] = {"betti": betti, "boundary_ranks": [ranks.get(d, 0) for d in range(0, 9)]}

result = {
    "vertices": 16,
    "hypercube_edges": len(edges),
    "maximal_cech_simplices": len(facets),
    "maximal_simplex_vertices": 8,
    "nonempty_faces": len(faces),
    "f_vector": f_vector,
    "hasse_covers": len(covers),
    "toggle_order": list(TOGGLE_ORDER),
    "matched_pairs": len(pairs),
    "critical_counts_by_dimension": {str(k): v for k, v in sorted(critical_vector.items())},
    "critical_3_cell": vertex_set(target3),
    "critical_4_cells": [vertex_set(c) for c in sorted(critical4)],
    "morse_boundary_4_to_3": morse_coeffs,
    "modular_homology": modular,
    "conclusion": "The verified Morse CW model has one 0-cell, one 3-cell and twenty-four 4-cells, with zero 4-to-3 Morse boundary. Since the 3-skeleton is S^3 and degree classifies maps S^3 -> S^3, every 4-cell attaches null-homotopically."
}
print(json.dumps(result, indent=2, sort_keys=True))
