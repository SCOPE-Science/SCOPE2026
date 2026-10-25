#!/usr/bin/env python3
"""Finite exact tests for constant-cut exclusion activity on simple graphs.

Run with Python 3.10 or later: python verify.py.  No third-party packages.
The theorem for arbitrary graph order uses the proof, not these tests.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations


def graph(n, edges):
    adj = [0] * n
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def boundary(adj, occ):
    return sum((adj[u] & ~occ).bit_count()
               for u in range(len(adj)) if occ & (1 << u))


def states(n, k):
    return [sum(1 << v for v in s) for s in combinations(range(n), k)]


def connected(adj):
    seen, frontier = 1, 1
    while frontier:
        new = 0
        for u in range(len(adj)):
            if frontier & (1 << u):
                new |= adj[u]
        frontier = new & ~seen
        seen |= frontier
    return seen == (1 << len(adj)) - 1


def prediction(adj, k):
    n = len(adj)
    degree = [a.bit_count() for a in adj]
    if k in (1, n - 1):
        return len(set(degree)) == 1
    if all(d == n - 1 for d in degree):
        return True
    return n == 2 * k and sorted(degree) == [1] * (n - 1) + [n - 1]


def rational_solve(A, b):
    n = len(b)
    aug = [[Fraction(x) for x in A[i]] + [Fraction(b[i])]
           for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[p] = aug[p], aug[j]
        q = aug[j][j]
        aug[j] = [x / q for x in aug[j]]
        for i in range(n):
            if i == j:
                continue
            q = aug[i][j]
            if q:
                aug[i] = [x - q * y for x, y in zip(aug[i], aug[j])]
    return [row[-1] for row in aug]


def exact_fano(adj, k):
    """Independent finite-state Poisson-equation check using exact fractions."""
    n = len(adj)
    masks = states(n, k)
    m = len(masks)
    index = {x: i for i, x in enumerate(masks)}
    # D-B is minus the continuous-time exclusion generator.
    A = [[Fraction(0) for _ in masks] for _ in masks]
    q = []
    for i, x in enumerate(masks):
        q.append(boundary(adj, x))
        for u in range(n):
            if not (x >> u & 1):
                continue
            for v in range(n):
                if adj[u] >> v & 1 and not (x >> v & 1):
                    y = x ^ (1 << u) ^ (1 << v)
                    j = index[y]
                    A[i][j] -= 1
                    A[i][i] += 1
    assert [int(A[i][i]) for i in range(m)] == q
    assert all(A[i][j] == A[j][i] for i in range(m) for j in range(m))
    mean = Fraction(sum(q), m)
    g = [Fraction(x) - mean for x in q]
    B = [[A[i][j] + Fraction(1, m) for j in range(m)] for i in range(m)]
    h = rational_solve(B, g)
    assert sum(h) == 0
    assert all(sum(A[i][j] * h[j] for j in range(m)) == g[i]
               for i in range(m))
    excess = Fraction(2, m) * sum(x * y for x, y in zip(g, h))
    fano = 1 + excess / mean
    assert (fano == 1) == prediction(adj, k)
    assert fano >= 1
    return fano


def run():
    totals = Counter()
    for n in (4, 5, 6):
        E = list(combinations(range(n), 2))
        for msk in range(1 << len(E)):
            adj = graph(n, [e for i, e in enumerate(E) if msk >> i & 1])
            if not connected(adj):
                continue
            for k in range(1, n):
                const = len({boundary(adj, s) for s in states(n, k)}) == 1
                assert const == prediction(adj, k), (n, k, msk)
                totals[(n, k, const)] += 1
    assert totals[(4, 2, True)] == 5
    assert totals[(5, 2, True)] == 1
    assert totals[(5, 3, True)] == 1
    assert totals[(6, 2, True)] == 1
    assert totals[(6, 3, True)] == 7
    assert totals[(6, 4, True)] == 1
    trials = [
        (4, [(0, 1), (0, 2), (0, 3)], 2),
        (5, [(0, 1), (0, 2), (0, 3), (0, 4)], 2),
        (6, [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5)], 3),
        (5, [(i, (i + 1) % 5) if i < 4 else (0, 4) for i in range(5)], 2),
        (6, [(i, i + 1) for i in range(5)] + [(0, 5)], 3),
        (5, [(i, j) for i in range(2) for j in range(2, 5)], 2),
        (5, [(i, i + 1) for i in range(4)], 2),
        (6, list(combinations(range(6), 2)), 3),
        (5, list(combinations(range(5), 2)), 2),
    ]
    for n, edges, k in trials:
        edges = [tuple(sorted(x)) for x in edges]
        assert len(edges) == len(set(edges))
        adj = graph(n, edges)
        val = exact_fano(adj, k)
        print('exact_fano', n, k, 'edges', len(edges), str(val))
    print('PASS: exhaustive connected simple graphs on 4, 5, 6 vertices;')
    print('PASS: nine independent exact-rational finite-generator Fano tests')
    print('LIMIT: no finite enumeration establishes the infinite-size theorem')


if __name__ == '__main__':
    run()
