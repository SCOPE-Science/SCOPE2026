#!/usr/bin/env python3
"""Reproducible finite checks for the three-flip hypercube Rips fixed-locus theorem.

The implementation constructs orbit compatibility from the original Hamming metric,
then independently constructs maximal faces from cube edges and cross-polytope facets.
No third-party dependencies are used.
"""
from itertools import combinations


def cube_edges(m):
    return [(u, u ^ (1 << j)) for u in range(1 << m) for j in range(m) if not (u >> j) & 1]


def orbit_label(c, u):
    # First three coordinates: 0, lower two bits of c.
    return c | (u << 3)


def raw_pair_compatible(c, u, d, v):
    a = orbit_label(c, u)
    b = orbit_label(d, v)
    flip = 7
    return max((a ^ b).bit_count(), (a ^ (b ^ flip)).bit_count()) <= 3


def facets_for_m(m):
    # Each Q_m edge supports a join of four zero-spheres, the boundary of a 4-crosspolytope.
    facets = set()
    for u, v in cube_edges(m):
        for pattern in range(16):
            facets.add(tuple(sorted(((v if pattern & (1 << c) else u) * 4 + c) for c in range(4))))
    return facets


def faces_by_dim(facets):
    fs = [set() for _ in range(4)]
    for f in facets:
        for d in range(1, 5):
            fs[d - 1].update(combinations(f, d))
    return [sorted(F) for F in fs]


def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            pivot = col.bit_length() - 1
            if pivot in pivots:
                col ^= pivots[pivot]
            else:
                pivots[pivot] = col
                break
    return len(pivots)


def ranks_and_betti(faces):
    ranks = [0]
    for d in range(1, 4):
        idx = {face: i for i, face in enumerate(faces[d - 1])}
        cols = []
        for face in faces[d]:
            col = 0
            for j in range(d + 1):
                col ^= 1 << idx[face[:j] + face[j + 1:]]
            cols.append(col)
        ranks.append(rank_mod2(cols))
    ranks.append(0)
    betti = [len(faces[d]) - ranks[d] - ranks[d + 1] for d in range(4)]
    return ranks, betti


def maximal_cliques_raw(m):
    # Independent Bron--Kerbosch enumeration on the raw orbit metric graph.
    vertices = list(range(4 * (1 << m)))
    neighbors = {a: set() for a in vertices}
    for a in vertices:
        u, c = divmod(a, 4)
        for b in vertices[a + 1:]:
            v, d = divmod(b, 4)
            if raw_pair_compatible(c, u, d, v):
                neighbors[a].add(b)
                neighbors[b].add(a)
    result = set()
    def bk(R, P, X):
        if not P and not X:
            result.add(tuple(sorted(R)))
            return
        pivot = max(P | X, key=lambda z: len(P & neighbors[z])) if P or X else None
        for v in list(P - (neighbors[pivot] if pivot is not None else set())):
            bk(R | {v}, P & neighbors[v], X & neighbors[v])
            P.remove(v)
            X.add(v)
    bk(set(), set(vertices), set())
    return result


def main():
    for m in range(1, 6):
        N = 1 << m
        E = m * (1 << (m - 1))
        vertices = [(c, u) for u in range(N) for c in range(4)]
        # Exact agreement of raw orbit metric with claimed graph.
        for i, (c, u) in enumerate(vertices):
            for d, v in vertices[i + 1:]:
                actual = raw_pair_compatible(c, u, d, v)
                expected = (c != d and (u ^ v).bit_count() <= 1)
                if actual != expected:
                    raise AssertionError(('orbit_adjacency', m, (c, u), (d, v), actual, expected))
        facets = facets_for_m(m)
        if m <= 3:
            assert maximal_cliques_raw(m) == facets, ('all_maximal_cliques', m)
        assert len(facets) == 16 * E - N*(m - 1), ('facets-count', m, len(facets))
        fs = faces_by_dim(facets)
        # Every maximal clique of the orbit graph appears as a facet in our list.
        # Given the graph projection to Q_m, each clique is supported on one cube edge.
        # Here check the asserted complete 3-dimensional f-vector independently.
        f_formula = [E*x - (2*E - N)*y for x,y in zip((8,24,32,16),(4,6,4,1))]
        f_actual = [len(F) for F in fs]
        assert f_actual == f_formula, ('f', m, f_actual, f_formula)
        ranks, betti = ranks_and_betti(fs)
        b1, b3 = E-N+1, E
        assert betti == [1,b1,0,b3], ('betti',m,betti,(1,b1,0,b3))
        print('m=%d n=%d orbits=%d edge_blocks=%d facets=%d f=%s ranks=%s betti=%s' %
              (m, m+3, 4*N, E, len(facets), f_actual, ranks, betti))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
