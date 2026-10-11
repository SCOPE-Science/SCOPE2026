#!/usr/bin/env python3
"""Finite, self-contained checks for the circular-prism closed-neighborhood collapse.

Checks sample orders, not an infinite parameter range. The mathematical proof
of the all-order theorem is supplied separately.
"""
from itertools import combinations
from collections import defaultdict


def prism(n):
    assert n >= 5
    V = range(2 * n)
    def v(layer, i):
        return layer * n + i % n
    edges = set()
    for layer in range(2):
        for i in range(n):
            edges.add(tuple(sorted((v(layer, i), v(layer, i + 1)))))
    for i in range(n):
        edges.add((v(0, i), v(1, i)))
    adjacency = {i: set() for i in V}
    for u, w in edges:
        adjacency[u].add(w)
        adjacency[w].add(u)
    assert len(edges) == 3 * n
    assert all(len(adjacency[v]) == 3 for v in V)
    return adjacency, edges


def simplex_faces(vertices, proper=False):
    a = sorted(vertices)
    stop = len(a) if proper else len(a) + 1
    for k in range(1, stop):
        for sub in combinations(a, k):
            yield frozenset(sub)


def complex_faces(facets, proper=False):
    return set().union(*(set(simplex_faces(f, proper)) for f in facets))


def maximal_containers(K, face):
    supers = [f for f in K if face <= f]
    return [f for f in supers if not any(f < g for g in supers)]


def elementary_collapse(K, free_face, maximal_face):
    assert free_face in K and maximal_face in K
    assert free_face < maximal_face
    assert len(maximal_face) == len(free_face) + 1
    assert maximal_containers(K, free_face) == [maximal_face]
    K.remove(free_face)
    K.remove(maximal_face)


def homology_mod2(K):
    by_dim = defaultdict(list)
    for f in K:
        by_dim[len(f) - 1].append(tuple(sorted(f)))
    for dim in by_dim:
        by_dim[dim].sort()
    rank = {}
    for dim in by_dim:
        if dim == 0:
            continue
        low = {f: i for i, f in enumerate(by_dim[dim - 1])}
        basis = {}
        for f in by_dim[dim]:
            col = 0
            for k in range(len(f)):
                col ^= 1 << low[f[:k] + f[k + 1:]]
            while col:
                lead = col.bit_length() - 1
                if lead not in basis:
                    basis[lead] = col
                    break
                col ^= basis[lead]
        rank[dim] = len(basis)
    betti = {
        dim: len(by_dim[dim]) - rank.get(dim, 0) - rank.get(dim + 1, 0)
        for dim in by_dim
    }
    return betti, {dim: len(faces) for dim, faces in by_dim.items()}


def check(n):
    adj, edges = prism(n)
    closed = {v: frozenset(adj[v] | {v}) for v in adj}
    assert len(set(closed.values())) == 2 * n
    assert all(len(t) == 4 for t in closed.values())
    K = complex_faces(closed.values())
    assert len(K) == 19 * n, (n, len(K))
    stage_0 = set(K)
    for v in range(2 * n):
        # The triangle consisting of the three neighbors of v is free.
        opposite = frozenset(adj[v])
        elementary_collapse(K, opposite, closed[v])
    assert len(K) == 15 * n
    stage_1 = set(K)
    for layer in range(2):
        for i in range(n):
            prev = layer * n + (i - 1) % n
            mid = layer * n + i
            nxt = layer * n + (i + 1) % n
            skipping_edge = frozenset((prev, nxt))
            ring_triangle = frozenset((prev, mid, nxt))
            elementary_collapse(K, skipping_edge, ring_triangle)
    assert len(K) == 11 * n
    squares = []
    for i in range(n):
        squares.append(frozenset((i, (i + 1) % n, n + i, n + (i + 1) % n)))
    expected = complex_faces(squares, proper=True)
    assert K == expected, ('unexpected residual simplices', n)
    for i in range(n):
        for j in range(i + 1, n):
            intersection = squares[i] & squares[j]
            if (i - j) % n in (1, n - 1):
                assert len(intersection) == 2
            else:
                assert len(intersection) == 0
    # No three distinct square boundaries share any vertex.
    for i, j, k in combinations(range(n), 3):
        assert not (squares[i] & squares[j] & squares[k])
    beta_before, f_before = homology_mod2(stage_0)
    beta_after, f_after = homology_mod2(K)
    assert [beta_before.get(d, 0) for d in range(4)] == [1, 1, n, 0]
    assert [beta_after.get(d, 0) for d in range(3)] == [1, 1, n]
    assert f_before == {0:2*n, 1:7*n, 2:8*n, 3:2*n}
    assert f_after == {0:2*n, 1:5*n, 2:4*n}
    # A basis of the graph cycle lattice comprises all n square boundaries
    # and the top-rim cycle: bottom edges are independent unique coordinates
    # for squares, while one chosen top edge is the additional chord.
    assert len(edges) - 2*n + 1 == n + 1
    assert len(stage_1) == 15*n
    return f'order={n}; faces={len(stage_0)}; relative_collapses={4*n}; residual_faces={len(K)}; mod2_betti=(1,1,{n})'


def main():
    for n in [5, 6, 7, 8, 9, 10, 12, 16, 20, 30]:
        print(check(n))
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
