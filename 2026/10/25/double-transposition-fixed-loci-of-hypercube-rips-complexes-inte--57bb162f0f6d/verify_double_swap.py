#!/usr/bin/env python3
"""Exact checks for double-transposition fixed loci of hypercube Rips complexes.

Standard-library only. No random search or numerical approximation is used.
The fixed-point simplicial model is obtained from orbit barycenters.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

EXPECTED = {
    4: ((8, 16, 8), (1, 1), 15),
    5: ((16, 52, 48, 8), (1, 1, 4), 59),
    6: ((32, 152, 208, 84, 16), (1, 1, 20), 235),
    7: ((64, 416, 768, 512, 192, 32), (1, 1, 68, 4), 955),
}


def swap(x):
    return x ^ (3 if ((x >> 0) ^ (x >> 1)) & 1 else 0) ^ (
        12 if ((x >> 2) ^ (x >> 3)) & 1 else 0
    )


def orbits(n):
    orbit_set = {tuple(sorted({x, swap(x)})) for x in range(1 << n)}
    return sorted(o for o in orbit_set if all((a ^ b).bit_count() <= 2
                                                  for a in o for b in o))


def orbit_graph(n):
    O = orbits(n)
    assert len(O) == 8 * (1 << (n - 4))
    adj = [0] * len(O)
    for i in range(len(O)):
        for j in range(i):
            # Direct four-bit/full-word orbit-union distance test.
            direct = all((a ^ b).bit_count() <= 2 for a in O[i] for b in O[j])
            # Independent factorization by the last n-4 coordinates.
            pi, pj = O[i][0] >> 4, O[j][0] >> 4
            base = max(((a & 15) ^ (b & 15)).bit_count()
                       for a in O[i] for b in O[j])
            product = base + (pi ^ pj).bit_count() <= 2
            assert direct == product
            if direct:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    return O, adj


def maximal_cliques(adj):
    out = []
    def rec(R, P, X):
        if not (P or X):
            out.append(R)
            return
        PX = P | X
        u = max((i for i in range(len(adj)) if PX >> i & 1),
                key=lambda i: (P & adj[i]).bit_count())
        choices = P & ~adj[u]
        while choices:
            vbit = choices & -choices
            v = vbit.bit_length() - 1
            rec(R | vbit, P & adj[v], X & adj[v])
            P &= ~vbit
            X |= vbit
            choices &= ~vbit
    rec(0, (1 << len(adj)) - 1, 0)
    return out


def faces_from_facets(facets):
    faces = set()
    for facet in facets:
        verts = [i for i in range(facet.bit_length()) if facet >> i & 1]
        for size in range(1, len(verts) + 1):
            for f in combinations(verts, size):
                faces.add(sum(1 << i for i in f))
    return faces


def morse_matching(faces, nv):
    unused = set(faces)
    pairs = []
    # Deterministic lexicographic vertex toggles.
    for v in range(nv):
        bit = 1 << v
        for f in sorted(unused):
            if not f & bit and f | bit in unused and f in unused:
                unused.remove(f)
                unused.remove(f | bit)
                pairs.append((f, f | bit))
    return unused, pairs


def check_acyclic(faces, pairs):
    # Matched Hasse incidences point up; all other incidences down.
    inv = {upper: lower for lower, upper in pairs}
    indeg = {f: 0 for f in faces}
    outgoing = defaultdict(list)
    incidences = 0
    for upper in faces:
        t = upper
        while t:
            bit = t & -t
            t ^= bit
            lower = upper ^ bit
            if not lower:
                continue
            if inv.get(upper) == lower:
                a, b = lower, upper
            else:
                a, b = upper, lower
            outgoing[a].append(b)
            indeg[b] += 1
            incidences += 1
    todo = deque(x for x, d in indeg.items() if d == 0)
    count = 0
    while todo:
        a = todo.popleft()
        count += 1
        for b in outgoing[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                todo.append(b)
    assert count == len(faces), (count, len(faces))
    return incidences


def signed_boundary(simplex):
    x = simplex
    j = 0
    while x:
        b = x & -x
        x ^= b
        if simplex != b:
            yield simplex ^ b, (-1 if j % 2 else 1)
        j += 1


def check_integral_morse_boundary(critical, pairs):
    pair = dict(pairs)
    all_stats = []
    max_dim = max(c.bit_count() - 1 for c in critical)
    for d in range(1, max_dim + 1):
        @lru_cache(maxsize=None)
        def reduce_face(a):
            if a not in pair:
                return {a: 1}
            b = pair[a]
            boundary = dict(signed_boundary(b))
            pivot = boundary[a]
            assert abs(pivot) == 1
            out = defaultdict(int)
            for w, coeff in boundary.items():
                if w == a:
                    continue
                for v, reduced in reduce_face(w).items():
                    out[v] -= pivot * coeff * reduced
            return {k: v for k, v in out.items() if v}
        top = [c for c in critical if c.bit_count() - 1 == d]
        for cell in top:
            reduced = defaultdict(int)
            for face, coeff in signed_boundary(cell):
                for v, val in reduce_face(face).items():
                    reduced[v] += coeff * val
            assert not any(reduced.values()), (d, cell, reduced)
        all_stats.append((d, len(top), reduce_face.cache_info().currsize))
    return all_stats


def rank_mod_two(faces):
    by_dim = defaultdict(list)
    for f in faces:
        by_dim[f.bit_count() - 1].append(f)
    maxdim = max(by_dim)
    ranks = {}
    for d in range(1, maxdim + 1):
        index = {f: i for i, f in enumerate(by_dim[d - 1])}
        basis = {}
        for simplex in by_dim[d]:
            vec = 0
            for f, _ in signed_boundary(simplex):
                vec ^= 1 << index[f]
            while vec:
                pivot = vec.bit_length() - 1
                if pivot not in basis:
                    basis[pivot] = vec
                    break
                vec ^= basis[pivot]
        ranks[d] = len(basis)
    betti = tuple(len(by_dim[d]) - ranks.get(d, 0) - ranks.get(d + 1, 0)
                  for d in range(maxdim + 1))
    return betti


def run():
    for n, (f_expected, crit_expected, pairs_expected) in EXPECTED.items():
        O, adj = orbit_graph(n)
        facets = maximal_cliques(adj)
        faces = faces_from_facets(facets)
        counts = Counter(f.bit_count() - 1 for f in faces)
        f_vector = tuple(counts[d] for d in range(max(counts) + 1))
        assert f_vector == f_expected, (n, f_vector)
        # Exhaustive independent clique recognition.
        for f in faces:
            vertices = [i for i in range(len(O)) if f >> i & 1]
            assert all(adj[a] >> b & 1 for a, b in combinations(vertices, 2))
        critical, pairs = morse_matching(faces, len(O))
        assert len(pairs) == pairs_expected
        assert len(faces) == 2 * len(pairs) + len(critical)
        cr_counts = Counter(x.bit_count() - 1 for x in critical)
        critical_vector = tuple(cr_counts[d] for d in range(max(cr_counts) + 1))
        assert critical_vector == crit_expected, (n, critical_vector)
        incidences = check_acyclic(faces, pairs)
        reductions = check_integral_morse_boundary(critical, pairs)
        betti_mod2 = rank_mod_two(faces)
        assert betti_mod2[:len(crit_expected)] == crit_expected and not any(betti_mod2[len(crit_expected):]), (n, betti_mod2)
        print('CHECKED', n, 'orbits', len(O), 'facets', len(facets),
              'f_vector', f_vector, 'critical', critical_vector,
              'pairs', len(pairs), 'Hasse_incidences', incidences,
              'Morse_reductions', reductions, 'mod2', betti_mod2)
    print('VERIFY_OK integral_morse=zero acyclic=all raw_orbits=all mod2=all')


if __name__ == '__main__':
    run()
