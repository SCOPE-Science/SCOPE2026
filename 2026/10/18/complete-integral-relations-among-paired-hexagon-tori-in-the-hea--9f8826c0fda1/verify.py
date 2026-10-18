#!/usr/bin/env python3
"""Exact integral presentation for paired-hexagon torus classes of a Fano incidence graph.

Dependencies: Python 3.10+, numpy, sympy. Indexing and orientations are reconstructed
from the incidence structure; no external graph tables or saved matrices are required.
"""
from collections import Counter
from itertools import permutations

import numpy as np
from sympy import Matrix


def rank_mod(A, p):
    A = np.asarray(A, dtype=np.int64).copy() % p
    m, n = A.shape
    k = 0
    for j in range(n):
        if k >= m:
            break
        choices = np.flatnonzero(A[k:, j])
        if not len(choices):
            continue
        a = k + int(choices[0])
        A[[k, a], :] = A[[a, k], :]
        A[k, j:] = (A[k, j:] * pow(int(A[k, j]), -1, p)) % p
        ix = np.flatnonzero(A[k + 1:, j]) + k + 1
        A[ix, j:] = (A[ix, j:] - A[ix, j, None] * A[k, j:]) % p
        k += 1
    return k


def build():
    # Fano plane as the seven translates of the (7,3,1) difference set.
    lines = tuple(frozenset(((i + d) % 7) for d in (0, 1, 3)) for i in range(7))
    assert len(set(lines)) == 7
    assert all(len(a & b) == 1 for i, a in enumerate(lines) for b in lines[i + 1:])
    edges = tuple(sorted((p, 7 + i) for i, line in enumerate(lines) for p in line))
    assert len(edges) == 21
    ei = {e: i for i, e in enumerate(edges)}
    adj = tuple(set() for _ in range(14))
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    assert all(len(v) == 3 for v in adj)

    # Every unoriented simple cycle appears exactly once: minimum first,
    # then the direction with smaller second vertex than last vertex.
    cycles = []
    for s in range(14):
        def visit(path):
            for v in sorted(adj[path[-1]]):
                if v == s:
                    if len(path) >= 3 and path[1] < path[-1]:
                        cycles.append(tuple(path))
                elif v > s and v not in path:
                    visit(path + [v])
        for v in sorted(adj[s]):
            if v > s:
                visit([s, v])
    assert Counter(map(len, cycles)) == {6: 28, 8: 21, 10: 84, 12: 56, 14: 24}
    hexagons = [(i, c) for i, c in enumerate(cycles) if len(c) == 6]
    assert len(hexagons) == 28

    # Ordered basis: (vertex,edge) in dimension 1 and (edge,edge)
    # in dimension 2, with edge pairs in ascending edge-index order.
    zero_cells = tuple((a, b) for a in range(14) for b in range(a + 1, 14))
    one_cells = tuple((v, i) for v in range(14) for i, (a, b) in enumerate(edges) if v not in (a, b))
    two_cells = tuple((i, j) for i in range(21) for j in range(i + 1, 21) if not set(edges[i]) & set(edges[j]))
    assert (len(zero_cells), len(one_cells), len(two_cells)) == (91, 252, 168)
    one_index = {x: i for i, x in enumerate(one_cells)}
    two_index = {x: i for i, x in enumerate(two_cells)}
    B = np.zeros((252, 168), dtype=np.int64)
    for col, (i, j) in enumerate(two_cells):
        a, b = edges[i]
        c, d = edges[j]
        # Signed cellular boundary of oriented square e_i x e_j.
        B[one_index[(b, j)], col] += 1
        B[one_index[(a, j)], col] -= 1
        B[one_index[(d, i)], col] -= 1
        B[one_index[(c, i)], col] += 1

    # Undirected 1-skeleton connectivity, validating the relevant CW model.
    graph0 = {v: set() for v in zero_cells}
    for v, i in one_cells:
        a, b = edges[i]
        u1, u2 = tuple(sorted((v, a))), tuple(sorted((v, b)))
        graph0[u1].add(u2)
        graph0[u2].add(u1)
    seen = {zero_cells[0]}
    boundary = [zero_cells[0]]
    for q in boundary:
        for t in graph0[q] - seen:
            seen.add(t)
            boundary.append(t)
    assert len(seen) == 91

    # Canonical oriented edge chain of every cycle.
    cycle_chains = []
    for c in cycles:
        chain = {}
        for k, a in enumerate(c):
            b = c[(k + 1) % len(c)]
            edge = tuple(sorted((a, b)))
            chain[ei[edge]] = 1 if edge == (a, b) else -1
        cycle_chains.append(chain)

    # All pairs of vertex-disjoint cycles (not merely hexagon pairs).
    cycle_pairs = [(i, j) for i, c in enumerate(cycles) for j in range(i + 1, len(cycles))
                   if set(c).isdisjoint(cycles[j])]
    assert len(cycle_pairs) == 42
    assert all(len(cycles[i]) == len(cycles[j]) == 6 for i, j in cycle_pairs)
    assert len(set(cycle_pairs)) == 42
    T = np.zeros((168, 42), dtype=np.int64)
    for column, (i, j) in enumerate(cycle_pairs):
        for e, se in cycle_chains[i].items():
            for f, sf in cycle_chains[j].items():
                x, y = sorted((e, f))
                T[two_index[(x, y)], column] = se * sf * (1 if e < f else -1)
    assert np.all((B @ T) == 0)
    assert all(np.count_nonzero(T[:, k]) == 36 for k in range(42))

    # The three cycle-disjoint partners of each hexagon supply one
    # three-term relation. Signs are fixed by canonical cycle orientations.
    neighbors = {i: [] for i, _ in hexagons}
    for k, (i, j) in enumerate(cycle_pairs):
        neighbors[i].append(k)
        neighbors[j].append(k)
    assert all(len(neighbors[i]) == 3 for i, _ in hexagons)
    R = np.zeros((42, 28), dtype=np.int64)
    for k, (i, _) in enumerate(hexagons):
        x, y, z = neighbors[i]
        a, b, c = T[:, x], T[:, y], T[:, z]
        possibilities = ((np.array_equal(a + b, c), (1, 1, -1)),
                         (np.array_equal(a - b, c), (1, -1, -1)),
                         (np.array_equal(a + b, -c), (1, 1, 1)),
                         (np.array_equal(a - b, -c), (1, -1, 1)))
        matches = [s for yes, s in possibilities if yes]
        assert len(matches) == 1, (i, x, y, z)
        R[[x, y, z], k] = matches[0]
    assert np.all(T @ R == 0)
    assert all(np.count_nonzero(R[:, k]) == 3 for k in range(28))
    assert all(np.count_nonzero(R[k, :]) == 2 for k in range(42))

    # The dual graph of hexagons: 28 vertices, 42 edges, valence 3.
    six_index = {i: k for k, (i, _) in enumerate(hexagons)}
    adj6 = {i: set() for i in range(28)}
    for i, j in cycle_pairs:
        a, b = six_index[i], six_index[j]
        adj6[a].add(b)
        adj6[b].add(a)
    seen = {0}
    frontier = [0]
    for a in frontier:
        for b in adj6[a] - seen:
            seen.add(b)
            frontier.append(b)
    assert len(seen) == 28 and all(len(adj6[i]) == 3 for i in range(28))

    # Integral unit minor: it certifies a primitive rank-14 sublattice
    # of the 2-chain group without relying on a floating-point rank.
    rows14 = [0, 2, 3, 5, 8, 16, 17, 19, 23, 48, 49, 54, 62, 65]
    cols14 = [0, 1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 24]
    assert int(Matrix(T[np.ix_(rows14, cols14)]).det()) == 1
    assert rank_mod(B, 3) == 154
    # Fourteen independent cycles and 154 independent boundaries sum to 168.
    # Since ker_Z(B) is saturated, the unimodular minor implies
    # image_Z(T)=ker_Z(B) exactly; no hidden integral index is possible.

    # Local relations: 28 independent columns over Q, but their
    # saturation in the 42-dimensional relation module has index two.
    rows28 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19,
              21, 24, 25, 26, 27, 28, 30, 31, 33, 36]
    assert int(Matrix(R[rows28, :]).det()) == -2
    assert rank_mod(R, 2) == 27
    # Therefore every maximal minor is even, and one equals +/-2;
    # their gcd is exactly 2. The missing primitive relation is the
    # half-sum of the 28 three-term relations.
    local_sum = R @ np.ones(28, dtype=np.int64)
    assert np.all(local_sum % 2 == 0)
    half_sum = local_sum // 2
    assert (Counter(map(int, half_sum)) == {0: 20, 1: 11, -1: 11})
    assert np.all(T @ half_sum == 0)
    # It is not in span_Z(R): the 28 local columns are independent
    # and its unique rational coordinates are all 1/2.

    # Full Fano incidence automorphisms: 168 collineations and one duality.
    line_lookup = {line: i for i, line in enumerate(lines)}
    automorphisms = []
    for p in permutations(range(7)):
        images = {frozenset(p[x] for x in line) for line in lines}
        if images != set(lines):
            continue
        q = tuple(line_lookup[frozenset(p[x] for x in line)] for line in lines)
        automorphisms.append(tuple(p) + tuple(7 + j for j in q))
    assert len(automorphisms) == 168
    duality = tuple(7 + ((-x) % 7) for x in range(7)) + tuple((-x) % 7 for x in range(7))
    automorphisms += [tuple(duality[g[v]] for v in range(14)) for g in automorphisms]
    assert len(set(automorphisms)) == 336
    assert all({tuple(sorted((g[a], g[b]))) for a, b in edges} == set(edges)
               for g in automorphisms)
    pair_lookup = {frozenset((frozenset(cycles[i]), frozenset(cycles[j]))): k
                   for k, (i, j) in enumerate(cycle_pairs)}
    orbit = set()
    i0, j0 = cycle_pairs[0]
    for g in automorphisms:
        k = frozenset((frozenset(g[v] for v in cycles[i0]),
                       frozenset(g[v] for v in cycles[j0])))
        orbit.add(pair_lookup[k])
    assert len(orbit) == 42

    print('VERIFY_OK_HEAWOOD_COMPLETE_TORUS_RELATIONS')
    print('ABRAMS_CELLS_91_252_168 CONNECTED B2_RANK_MOD3_154')
    print('CYCLES_28_HEXAGONS ALL_DISJOINT_PAIRS_42_HEXAGON_PAIRS')
    print('TORUS_CHAIN_RANK_14 UNIT_MINOR_DETERMINANT_PLUS_ONE H2_Z14')
    print('LOCAL_RELATIONS_28 INDEPENDENT_RANK28 DET_MINUS_TWO MOD2_RANK27')
    print('RELATION_SATURATION_INDEX_TWO EXTRA_HALF_SUM_22_TERMS')
    print('AUTOMORPHISMS_336 SINGLE_ORBIT_OF_42_CARRIERS')


if __name__ == '__main__':
    build()
