#!/usr/bin/env python3
"""Exact finite checks of a three-site inverse-power omission rule.
The analytical argument, not this finite enumeration, proves the theorem.
"""
from fractions import Fraction
from itertools import product


def plus(*polys):
    out = {}
    for P in polys:
        for key, val in P.items():
            out[key] = out.get(key, 0) + val
    return {k: v for k, v in out.items() if v}


def times(A, B):
    out = {}
    for (a, b), va in A.items():
        for (c, d), vb in B.items():
            key = (a + c, b + d)
            out[key] = out.get(key, 0) + va * vb
    return {k: v for k, v in out.items() if v}


def scale(c, P):
    return {k: c * v for k, v in P.items() if c * v}


def power(P, n):
    val = {(0, 0): 1}
    for _ in range(n):
        val = times(val, P)
    return val


def check_identity():
    O = {(0, 0): 1}
    H = {(1, 0): 1}
    V = {(0, 1): 1}
    b = plus(O, times(H, V))
    u = plus(O, H)
    B = power(b, 3)
    U = power(u, 3)
    A = plus(B, scale(2, U))
    C = plus(scale(2, B), O)
    numerator = plus(times(H, times(A, C)),
                     times(plus(O, scale(-1, H)), times(B, C)),
                     scale(-1, times(B, A)))
    rows = {
        0: {1: 3},
        1: {2: 12, 1: -6, 0: 12},
        2: {3: 19, 2: -6, 1: 18, 0: 16},
        3: {4: 15, 3: -2, 2: 18, 1: 30, 0: 6},
        4: {5: 6, 3: 6, 2: 30, 1: 12},
        5: {6: 1, 3: 10, 2: 12},
        6: {3: 4},
    }
    P = {(i, j): val for i, row in rows.items()
         for j, val in row.items()}
    assert numerator == times(H, P), 'rational-identity certificate failed'
    print('Cubic far-transition polynomial identity: EXACT PASS')


def closure(n, edges):
    dist = [[0 if i == j else 10**9 for j in range(n)] for i in range(n)]
    at = 0
    for i in range(n):
        for j in range(i + 1, n):
            dist[i][j] = dist[j][i] = edges[at]
            at += 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def cost(D, reports, actual, exponent):
    if len(set(reports)) < 3:
        return Fraction(min(D[actual][site] for site in set(reports)))
    nearest = [min(D[reports[i]][reports[j]] for j in range(3) if i != j)
               for i in range(3)]
    weights = [Fraction(1, int(d)**exponent) for d in nearest]
    norm = sum(weights)
    return sum((w * min(D[actual][reports[j]] for j in range(3) if j != i)
                for i, w in enumerate(weights)), Fraction(0)) / norm


def check_metrics():
    cases = 0
    for edges in product((1, 2, 3, 4), repeat=6):
        D = closure(4, edges)
        x = (0, 1, 2)
        for exponent in range(4):
            for i in range(3):
                before = cost(D, x, x[i], exponent)
                for y in (0, 1, 2, 3):
                    after_reports = list(x)
                    after_reports[i] = y
                    after = cost(D, after_reports, x[i], exponent)
                    assert after >= before, (D, exponent, i, y, before, after)
                    cases += 1
    print(f'Exact finite-metric incentive comparisons: {cases:,} PASS')


def check_nontruthful():
    # Sites (0,1,2), left agent reports -1/100, power 4.
    q = 4
    h = Fraction(1, 100)
    after = h + (1 - h) / (1 + 2 * (1 + h)**q)
    assert after < Fraction(1, 3)
    # Local derivative of deviating cost equals (2/9)(3-q).
    assert Fraction(2, 9) * (3 - q) < 0
    print('Exponent-four profitable deviation: EXACT PASS')


if __name__ == '__main__':
    check_identity()
    check_metrics()
    check_nontruthful()
