#!/usr/bin/env python3
"""Exhaustive finite face-poset and homology verification for a Heawood 4-robust clique complex.

Usage: python robust4_verify.py morse_certificate.json
The certificate lists an explicit acyclic partial matching, using 14-bit vertex masks.
"""
import collections
import itertools
import json
import sys
from pathlib import Path

LINES = ((0, 1, 3), (0, 2, 5), (0, 4, 6), (1, 2, 4),
         (1, 5, 6), (2, 3, 6), (3, 4, 5))
N = 14


def bit_iter(mask):
    while mask:
        b = mask & -mask
        yield b
        mask ^= b


def construct():
    # Vertices 0,...,6 are points; vertex 7+j is line L_j.
    nb = [0] * N
    for j, line in enumerate(LINES):
        for i in line:
            nb[i] |= 1 << (7 + j)
            nb[7 + j] |= 1 << i
    assert len(set(LINES)) == 7
    assert all(len(set(L)) == 3 for L in LINES)
    assert all(sum(i in L for L in LINES) == 3 for i in range(7))
    assert all(sum({i, j}.issubset(L) for L in LINES) == 1
               for i, j in itertools.combinations(range(7), 2))
    # First membership test: enumerate independent 4-sets.
    forbidden = []
    for verts in itertools.combinations(range(N), 4):
        mask = sum(1 << v for v in verts)
        if all((nb[v] & mask) == 0 for v in verts):
            forbidden.append(mask)
    faces1 = {s for s in range(1 << N)
              if not any((q & s) == q for q in forbidden)}
    # Independent second test: maximum independent set via bit-DP.
    alpha = [0] * (1 << N)
    for s in range(1, 1 << N):
        b = s & -s
        v = b.bit_length() - 1
        alpha[s] = max(alpha[s ^ b], 1 + alpha[(s ^ b) & ~nb[v]])
    faces2 = {s for s in range(1 << N) if alpha[s] <= 3}
    assert faces1 == faces2, "two face tests disagree"
    return nb, forbidden, faces1


def rank_binary(columns):
    basis = {}
    for v in columns:
        while v:
            p = v.bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def homology(faces):
    dims = collections.defaultdict(list)
    for s in sorted(faces):
        if s:
            dims[s.bit_count() - 1].append(s)
    ranks = {0: 1}  # augmentation, for reduced homology
    for d in range(1, max(dims) + 1):
        target = {s: i for i, s in enumerate(dims[d - 1])}
        columns = []
        for s in dims[d]:
            v = 0
            for b in bit_iter(s):
                v ^= 1 << target[s ^ b]
            columns.append(v)
        ranks[d] = rank_binary(columns)
    bets = {d: len(ds) - ranks.get(d, 0) - ranks.get(d + 1, 0)
            for d, ds in dims.items()}
    return {d: len(x) for d, x in dims.items()}, ranks, bets


def certify(cert, faces):
    assert cert['lines'] == [list(L) for L in LINES]
    assert cert['n_vertices'] == N and cert['robustness'] == 4
    pairs = [tuple(pair) for pair in cert['matching_pairs']]
    crit = cert['critical_masks']
    assert all(isinstance(m, int) for pair in pairs for m in pair)
    assert all(isinstance(m, int) for m in crit)
    assert len(pairs) == 1469 and len(crit) == 93
    assert len(set(pairs)) == len(pairs)
    used = set(crit)
    assert not (0 in used)
    assert len(used) == len(crit)
    for low, high in pairs:
        assert low != 0 and low in faces and high in faces
        assert low.bit_count() + 1 == high.bit_count()
        assert (low & high) == low
        assert low not in used and high not in used
        used.add(low)
        used.add(high)
    assert used == faces - {0}, "matching does not exhaust faces"
    cdims = collections.Counter(s.bit_count() - 1 for s in crit)
    assert cdims == {0: 1, 5: 92}, cdims
    # Orient every Hasse cover downward except matched edges upward.
    # Kahn's algorithm exhaustively checks all oriented cover relations.
    faces_no_empty = faces - {0}
    outgoing = {s: [] for s in faces_no_empty}
    indegree = {s: 0 for s in faces_no_empty}
    mate = {low: high for low, high in pairs}
    count = 0
    for high in faces_no_empty:
        for b in bit_iter(high):
            low = high ^ b
            if not low:
                continue
            source, target = (low, high) if mate.get(low) == high else (high, low)
            outgoing[source].append(target)
            indegree[target] += 1
            count += 1
    queue = collections.deque(s for s in faces_no_empty if indegree[s] == 0)
    visited = 0
    while queue:
        s = queue.popleft()
        visited += 1
        for t in outgoing[s]:
            indegree[t] -= 1
            if not indegree[t]:
                queue.append(t)
    assert visited == len(faces_no_empty), f"matching cycle: {visited}/{len(faces_no_empty)}"
    return count, visited, cdims


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: python robust4_verify.py morse_certificate.json')
    cert = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    nb, forbidden, faces = construct()
    assert len(forbidden) == 147 and len(faces) == 3032
    f, ranks, betti = homology(faces)
    assert f == {0: 14, 1: 91, 2: 364, 3: 854, 4: 1092, 5: 616}, f
    assert betti == {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 92}, betti
    # Combinatorial Alexander dual: complements of nonfaces of the robust complex.
    universe = (1 << N) - 1
    dual = {universe ^ s for s in range(1 << N) if s not in faces}
    assert len(dual) == 13352
    assert all(s in dual for s in range(1 << N) if s.bit_count() <= 3)
    facets = [s for s in dual if not any((s | (1 << i)) in dual
              for i in range(N) if not s & (1 << i))]
    assert len(facets) == 147 and all(s.bit_count() == 10 for s in facets)
    covers, visited, cdims = certify(cert, faces)
    assert sum((-1)**d * k for d, k in f.items()) == -91
    print('graph_vertices=14 graph_edges=21 forbidden_independent_quadruples=147')
    print('faces_including_empty=3032')
    print('f_vector_nonempty=[14,91,364,854,1092,616]')
    print('matching_pairs=1469 critical_0=1 critical_5=92')
    print(f'oriented_hasse_covers={covers} topological_sort_visited={visited}')
    print('reduced_mod2_betti=[0,0,0,0,0,92]')
    print('alexander_dual_faces=13352 dual_facets=147 facet_size=10 full_two_skeleton=YES')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
