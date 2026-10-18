"""Exact small cases for graph/hypergraph lattice-bottleneck norm certificates.

Requires Python 3 standard library only. This is not a proof of the universal
norm identity; the mathematical proof is supplied separately.
"""
from itertools import combinations, product
from fractions import Fraction as Q


def f_power(a, edges):
    return max((min(a[i] for i in edge) for edge in edges), default=Q(0))


def verify_hypergraph(n, edges, weights, dual):
    assert len(weights) == len(edges) and len(dual) == n
    edges = tuple(tuple(e) for e in edges)
    weights = tuple(Q(w) for w in weights)
    dual = tuple(Q(y) for y in dual)
    assert all(w >= 0 for w in weights)
    assert all(y >= 0 for y in dual)
    assert all(sum((weights[j] for j, e in enumerate(edges) if i in e), Q(0)) <= 1 for i in range(n))
    assert all(sum((dual[i] for i in e), Q(0)) >= 1 for e in edges)
    assert sum(weights, Q(0)) == sum(dual, Q(0))
    rows = []
    for e, w in zip(edges, weights):
        if w:
            a = [Q(0)] * n
            for i in e:
                a[i] = w
            rows.append(a)
    assert all(sum((row[i] for row in rows), Q(0)) <= 1 for i in range(n))
    assert sum((f_power(row, edges) for row in rows), Q(0)) == sum(weights, Q(0))
    return sum(weights, Q(0)), len(rows)


def all_graphs_small():
    checked = 0
    for n in range(2, 6):
        edges = list(combinations(range(n), 2))
        m = len(edges)
        count = 1 << m
        # Each edge weight is 0, 1/2 or 1. Record half-integer primal
        # packing objective at its exact support, then take subset maxima.
        primal = [-1] * count
        primal[0] = 0
        for h in product(range(3), repeat=m):
            if any(sum(h[j] for j, e in enumerate(edges) if i in e) > 2 for i in range(n)):
                continue
            mask = sum(1 << j for j, v in enumerate(h) if v)
            primal[mask] = max(primal[mask], sum(h))
        for j in range(m):
            for mask in range(count):
                if mask & (1 << j):
                    primal[mask] = max(primal[mask], primal[mask ^ (1 << j)])
        dual = [1000000] * count
        # Every small-graph fractional vertex cover has a half-integral
        # optimum. Enumerate candidate half-integral covers independently.
        for y in product(range(3), repeat=n):
            covered = sum(1 << j for j, (i, k) in enumerate(edges) if y[i] + y[k] >= 2)
            dual[covered] = min(dual[covered], sum(y))
        for j in range(m):
            for mask in range(count):
                if not mask & (1 << j):
                    dual[mask] = min(dual[mask], dual[mask | (1 << j)])
        for mask in range(count):
            assert primal[mask] == dual[mask], (n, mask, primal[mask], dual[mask])
            checked += 1
    return checked


def special_cases():
    checked = 0
    for n in range(2, 13):
        # Complete graph. Explicit odd-cycle + matching solutions.
        edges = tuple(combinations(range(n), 2))
        w = [Q(0)] * len(edges)
        lookup = {e: j for j, e in enumerate(edges)}
        if n % 2:
            for e in [(0, 1), (1, 2), (0, 2)]:
                w[lookup[e]] = Q(1, 2)
            start = 3
        else:
            start = 0
        for i in range(start, n, 2):
            w[lookup[i, i + 1]] = Q(1)
        score, rows = verify_hypergraph(n, edges, w, [Q(1, 2)] * n)
        assert score == Q(n, 2)
        assert rows == (n + 3) // 2 if n % 2 else rows == n // 2
        checked += 1
    for n in range(3, 14):
        edges = tuple(tuple(sorted((i, (i+1) % n))) for i in range(n))
        w = [Q(1, 2)] * n if n % 2 else [Q(i % 2) for i in range(n)]
        score, rows = verify_hypergraph(n, edges, w, [Q(1, 2)] * n)
        assert score == Q(n, 2)
        assert rows == n if n % 2 else rows == n // 2
        checked += 1
    for m in range(1, 20):
        n = m+1
        edges = [(0, i) for i in range(1, n)]
        weights = [Q(1)] + [Q(0)] * (m-1)
        dual = [Q(1)] + [Q(0)] * m
        score, rows = verify_hypergraph(n, edges, weights, dual)
        assert (score, rows) == (Q(1), 1)
        checked += 1
    for n in range(3, 10):
        for r in range(1, n+1):
            edges = tuple(combinations(range(n), r))
            w = Q(1, len(tuple(combinations(range(n-1), r-1))))
            score, rows = verify_hypergraph(n, edges, [w] * len(edges), [Q(1, r)] * n)
            assert score == Q(n, r)
            checked += 1
    fano = ((0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5))
    value, length = verify_hypergraph(7, fano, [Q(1,3)]*7, [Q(1,3)]*7)
    assert value == Q(7,3) and length == 7
    # Distinct Fano lines share exactly one point. Its incidence Gram
    # matrix is 2I+J, so all optimum weights are uniquely 1/3.
    assert all(len(set(a) & set(b)) == 1 for a,b in combinations(fano,2))
    checked += 1
    return checked

if __name__ == '__main__':
    a=all_graphs_small()
    b=special_cases()
    print(f'PASS: {a} small graph primal-dual equalities; {b} parametric exact certificates.')
