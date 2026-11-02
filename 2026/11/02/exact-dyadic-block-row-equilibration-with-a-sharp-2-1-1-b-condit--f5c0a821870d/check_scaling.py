#!/usr/bin/env python3
"""Reproduce finite exact-arithmetic and extremal tests for block-row radix scaling.

Uses only the Python standard library. This checker supplements the analytic proof;
its finite tests are not a proof of the all-matrix theorem.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random
from math import isclose


def inverse(A):
    n = len(A)
    rows = [[Q(v) for v in A[i]] + [Q(i == j) for j in range(n)]
            for i in range(n)]
    for j in range(n):
        piv = next((i for i in range(j, n) if rows[i][j]), None)
        if piv is None:
            raise ValueError('singular')
        rows[j], rows[piv] = rows[piv], rows[j]
        v = rows[j][j]
        rows[j] = [x / v for x in rows[j]]
        for i in range(n):
            if i == j:
                continue
            v = rows[i][j]
            rows[i] = [x - v * y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def floor_log2_positive_ratio(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while Q(2) ** k > x:
        k -= 1
    while Q(2) ** (k+1) <= x:
        k += 1
    return k


def instance(A, groups):
    n = len(A)
    inv = inverse(A)
    a = [max(sum(abs(Q(z)) for z in A[i]) for i in G) for G in groups]
    c = [[sum(abs(inv[i][j]) for j in G) for G in groups]
         for i in range(n)]
    b = len(groups)
    def objective(k):
        d = [Q(2) ** v for v in k]
        return max(d[q] * a[q] for q in range(b)) * max(
            sum(c[i][q] / d[q] for q in range(b)) for i in range(n))
    candidates = [tuple(floor_log2_positive_ratio(a[s] / a[q]) for q in range(b))
                  for s in range(b)]
    exact = min(objective(k) for k in candidates)
    continuous = max(sum(a[q] * c[i][q] for q in range(b)) for i in range(n))
    assert continuous <= exact
    assert float(exact / continuous) <= 2 ** (1-1/b) + 1e-12
    return exact, continuous, objective, candidates


def run():
    rng = Random(0x5A12)
    instances = 0
    exhaustive_checks = 0
    for n, b, repetitions in [(2, 2, 34), (3, 2, 35), (3, 3, 35),
                              (4, 2, 30), (4, 3, 30), (4, 4, 8)]:
        groups = [list(range(q * n // b, (q + 1) * n // b)) for q in range(b)]
        for _ in range(repetitions):
            A = [[rng.randrange(-5, 6) for j in range(n)] for i in range(n)]
            try:
                exact, cont, fun, candidates = instance(A, groups)
            except ValueError:
                continue
            # Invariance under a common exponent makes this bounded exhaustive
            # search an independent check of the finite candidate formula.
            exhaustive = min(fun((0,) + ex) for ex in product(range(-5, 6), repeat=b-1))
            assert exact == exhaustive, (A, groups, exact, exhaustive, candidates)
            instances += 1
            exhaustive_checks += 11 ** (b - 1)

    # Equal circular gaps make the dimension-dependent bound sharp. For each
    # b, the diagonal example gives a direct expression without matrix inversion.
    sharp_cases = 0
    for b in range(1, 10):
        a = [2 ** (j / b) for j in range(b)]
        K = min(max(a[q] * 2 ** (int(((__import__('math').log2(a[s] / a[q])) // 1))) for q in range(b)) /
                min(a[q] * 2 ** (int(((__import__('math').log2(a[s] / a[q])) // 1))) for q in range(b))
                for s in range(b))
        assert isclose(K, 2 ** (1-1/b), rel_tol=2e-13, abs_tol=2e-13), (b, K)
        sharp_cases += 1
    print('PASS: %d invertible rational matrices, %d exhaustive exponent candidates, %d sharp diagonal examples' %
          (instances, exhaustive_checks, sharp_cases))

if __name__ == '__main__':
    run()
