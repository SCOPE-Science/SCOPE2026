#!/usr/bin/env python3
"""Direct brute-force monophonic and maximal-set enumeration for clique-corona cycles.

Usage: python3 verify.py
All arithmetic is exact. No external packages are needed.
"""
from itertools import combinations
from math import comb


def addpoly(a, b, coeff=1, shift=0):
    for i, v in enumerate(b):
        a[i + shift] += coeff * v


def mulpoly(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def closed_form(t):
    n = len(t)
    T = sum(t)
    A = []
    for k in t:
        p = [comb(k, j) for j in range(k + 1)]
        p[0] = 0
        A.append(p)
    p = [comb(T, k) for k in range(T + n + 1)]
    addpoly(p, [1], n, 1)
    addpoly(p, [1], comb(n, 2), 2)
    for x in A:
        addpoly(p, x, n, 1)
        addpoly(p, x, 1, 2)
    for i in range(n):
        addpoly(p, mulpoly(A[i], A[(i + 1) % n]), n - 2, 1)
    f = [0] * (T + n + 1)
    f[2] += comb(n, 2) - n
    for k in t:
        f[k + 1] += 1
        f[k + 2] += 1
    for i in range(n):
        f[1 + t[i] + t[(i + 1) % n]] += n - 2
    f[T] += 1
    return p, f


def graph(t):
    n = len(t)
    N = n + sum(t)
    adj = [set() for _ in range(N)]
    def edge(u, v):
        adj[u].add(v)
        adj[v].add(u)
    for i in range(n):
        edge(i, (i + 1) % n)
    nxt = n
    for i, k in enumerate(t):
        leaves = list(range(nxt, nxt + k))
        for v in leaves:
            edge(i, v)
        for u, v in combinations(leaves, 2):
            edge(u, v)
        nxt += k
    return adj


def forbidden_triples(adj):
    N = len(adj)
    triples = set()
    def walk(path):
        if len(path) >= 3:
            for a, b, c in combinations(path, 3):
                triples.add((1 << a) | (1 << b) | (1 << c))
        last = path[-1]
        for v in adj[last]:
            if v in path:
                continue
            if any(v in adj[w] for w in path[:-1]):
                continue
            walk(path + [v])
    for s in range(N):
        walk([s])
    return tuple(triples)


def brute(t):
    adj = graph(t)
    N = len(adj)
    triples = forbidden_triples(adj)
    p = [0] * (N + 1)
    f = [0] * (N + 1)
    feasible = [False] * (1 << N)
    for mask in range(1 << N):
        good = not any((mask & q) == q for q in triples)
        feasible[mask] = good
        if good:
            p[mask.bit_count()] += 1
    for mask, good in enumerate(feasible):
        if good and all(not feasible[mask | (1 << j)]
                        for j in range(N) if not (mask & (1 << j))):
            f[mask.bit_count()] += 1
    return p, f, len(triples), sum(p)


def run():
    samples = [
        (5, [1] * 5),
        (6, [1] * 6),
        (7, [1] * 7),
        (5, [2] * 5),
        (5, [1, 2, 1, 1, 2]),
        (5, [1, 1, 3, 1, 1]),
        (6, [1, 2, 1, 1, 2, 1]),
    ]
    total = 0
    for n, t in samples:
        assert len(t) == n and n >= 5 and min(t) >= 1
        actual_p, actual_f, q, feasible = brute(t)
        claim_p, claim_f = closed_form(t)
        assert actual_p == claim_p, ('all-set', t, actual_p, claim_p)
        assert actual_f == claim_f, ('facets', t, actual_f, claim_f)
        total += (1 << (n + sum(t)))
        print('PASS', t, 'vertices', n + sum(t), 'forbidden_triples', q,
              'valid_sets', feasible, 'maximal_sets', sum(actual_f))
    print('VERIFICATION_OK cases=%d subsets=%d' % (len(samples), total))


if __name__ == '__main__':
    run()
