#!/usr/bin/env python3
"""Exact enumeration checks for orientation-score moment identities.

Run: python3 check.py
No dependencies outside the standard library.
"""
from fractions import Fraction
from itertools import combinations
from math import comb

CHECKS = 0

def verify(condition, message):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message)


def inspect(n, edges, check_full_covariance=False):
    edges = sorted(tuple(sorted(e)) for e in edges)
    assert len(edges) == len(set(edges)) and all(0 <= u < v < n for u, v in edges)
    m = len(edges)
    degrees = [0] * n
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
        neighbors[u].add(v)
        neighbors[v].add(u)
    triangles = sum(1 for a, b, c in combinations(range(n), 3)
                    if b in neighbors[a] and c in neighbors[a] and c in neighbors[b])
    star_triangles = sum(comb(d, 3) for d in degrees)
    paircount = sum(comb(d, 2) for d in degrees)
    total = 1 << m
    sums = [0, 0, 0]
    hist_sum = None
    hist_products = None
    if check_full_covariance:
        verify(len(set(degrees)) == 1, 'regularity')
        d = degrees[0]
        hist_sum = [0] * (d + 1)
        hist_products = [[0] * (d + 1) for _ in range(d + 1)]

    for mask in range(total):
        out = [0] * n
        for i, (u, v) in enumerate(edges):
            out[v if ((mask >> i) & 1) else u] += 1
        # W=2(Q-EQ), using only integers.
        w = sum((2 * out[v] - degrees[v]) ** 2 - degrees[v] for v in range(n)) // 2
        sums[0] += w
        sums[1] += w*w
        sums[2] += w*w*w
        if hist_sum is not None:
            hist = [out.count(r) for r in range(d + 1)]
            for r in range(d + 1):
                hist_sum[r] += hist[r]
                for s in range(d + 1):
                    hist_products[r][s] += hist[r]*hist[s]

    verify(sums[0] == 0, f'centered mean n={n} edges={edges}')
    verify(sums[1] == paircount * total, f'variance n={n} edges={edges}')
    verify(sums[2] == 6 * (star_triangles - triangles) * total,
           f'third moment n={n} edges={edges}')
    if hist_sum is not None:
        for r in range(d + 1):
            p_r = Fraction(comb(d, r), 2**d)
            verify(Fraction(hist_sum[r], total) == n*p_r,
                   f'profile mean n={n} d={d} r={r}')
            for s in range(d + 1):
                p_s = Fraction(comb(d, s), 2**d)
                empirical = Fraction(hist_products[r][s], total) - \
                    Fraction(hist_sum[r]*hist_sum[s], total**2)
                predicted = n * (p_r*(r == s) - p_r*p_s *
                                 (1 + Fraction((2*r-d)*(2*s-d), d))) if d else 0
                verify(empirical == predicted,
                       f'profile covariance n={n} d={d} r={r} s={s}')

for n in range(1, 5):
    pairs = list(combinations(range(n), 2))
    for code in range(1 << len(pairs)):
        edges = [e for k,e in enumerate(pairs) if (code >> k) & 1]
        inspect(n, edges, all(sum(e.count(v) for e in edges) ==
                          sum(e.count(0) for e in edges) for v in range(n)))

# Larger regular examples separate graphs with the same vertex degree sequence.
prism = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
k33 = [(u,v) for u in range(3) for v in range(3,6)]
petersen = [(i, (i+1) % 5) for i in range(5)] + \
           [(i, i+5) for i in range(5)] + \
           [(i+5, ((i+2)%5)+5) for i in range(5)]
inspect(5, combinations(range(5), 2), True)
inspect(6, prism, True)
inspect(6, k33, True)
inspect(10, petersen, True)
print(f'PASS: {CHECKS} exact integer/rational assertions; all host graphs through 4 vertices, plus K5, prism, K3,3, and Petersen.')
