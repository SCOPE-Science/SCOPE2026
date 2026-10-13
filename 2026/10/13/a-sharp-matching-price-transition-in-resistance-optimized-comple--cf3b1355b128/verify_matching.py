#!/usr/bin/env python3
"""Exact finite checks of a priced perfect-matching Kirchhoff-index formula.

Uses Python's standard-library Fraction arithmetic only. These checks are
illustrative; the all-size, all-price proof is in RESULT.md.
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    M = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        q = next(j for j in range(k, n) if M[j][k])
        M[k], M[q] = M[q], M[k]
        pivot = M[k][k]
        M[k] = [v / pivot for v in M[k]]
        for i in range(n):
            if i == k:
                continue
            f = M[i][k]
            if f:
                M[i] = [v - f * u for v, u in zip(M[i], M[k])]
    return [row[n:] for row in M]


def objective(n, a, b):
    if b <= 0 or a < 0:
        raise ValueError('positive connectivity required')
    L = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            w = a if i // 2 == j // 2 else b
            L[i][i] += w
            L[j][j] += w
            L[i][j] -= w
            L[j][i] -= w
    A = [[L[i][j] + F(1, n) for j in range(n)] for i in range(n)]
    inv = inverse(A)
    return n * (sum(inv[i][i] for i in range(n)) - 1)


def spectrum_formula(n, a, b):
    m, d = n // 2, n - 2
    return n * (F(m, 1) / (2 * a + d * b) + F(m - 1, 1) / (n * b))


def optimum(n, r):
    """Choose price t=2/(1+r**2), making the exact interior ratio rational."""
    m, d = n // 2, n - 2
    t = F(2) / (1 + r * r)
    x = max(F(0), (n * r - d) / 2)
    b = 1 / (m * (t * x + d))
    a = x * b
    tc = F(n * n, n * n - 2 * n + 2)
    assert (a > 0) == (t < tc)
    val = n * (n * n + d * d) / 4 if t >= tc else F(n, 8) * t * (n + d * r)**2
    return t, tc, a, b, val, x


def main():
    checks = 0
    comparisons = 0
    rs = [F(p, q) for p, q in [(1, 5), (1, 3), (1, 2), (2, 3), (3, 4),
                                 (4, 5), (1, 1), (6, 5), (3, 2), (2, 1), (5, 2), (4, 1)]]
    grid = [F(0), F(1, 20), F(1, 5), F(1, 2), F(1), F(3, 2), F(2), F(4), F(8), F(20)]
    for n in range(4, 14, 2):
        for r in rs:
            t, tc, a, b, Kstar, x = optimum(n, r)
            m, d = n // 2, n - 2
            assert m * (t * a + d * b) == 1
            assert objective(n, a, b) == spectrum_formula(n, a, b) == Kstar
            assert Kstar <= n * (n * n + d * d) / 4
            if t < tc:
                assert F(n, 8) * t * (n + d * r)**2 == Kstar
                delta = F(n, 8) * t * (n * r - d)**2
                assert Kstar + delta == n * (n * n + d * d) / 4
            for test_x in grid + [x]:
                bb = 1 / (m * (t * test_x + d))
                aa = test_x * bb
                Ktest = spectrum_formula(n, aa, bb)
                assert Ktest >= Kstar
                comparisons += 1
            checks += 1
    # Equality threshold r=(n-2)/n is tested exactly, including a=0.
    for n in range(4, 16, 2):
        t, tc, a, b, Kstar, x = optimum(n, F(n-2, n))
        assert t == tc and a == x == 0 and Kstar == objective(n, a, b)
        checks += 1
    print(f'VERIFY_OK {checks} exact cases, {comparisons} budget-constrained comparisons; spectrum, matrix inverse, and threshold')


if __name__ == '__main__':
    main()
