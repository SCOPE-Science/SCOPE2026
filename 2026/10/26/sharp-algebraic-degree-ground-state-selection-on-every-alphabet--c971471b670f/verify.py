#!/usr/bin/env python3
"""Finite reproducibility tests for an algebraic zero-temperature family.

The infinite-family theorem uses a symbolic characteristic-polynomial argument
and Selmer irreducibility. These tests do not certify irreducibility for all N.
"""
import math


def graph(n):
    assert n >= 3
    K = [[0] * n for _ in range(n)]
    for i in range(n - 1):
        K[i][i + 1] = 1
    K[n - 1][0] = 1
    K[n - 2][0] = 1
    return K


def root(n):
    lo, hi = 1.0, 2.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid ** n - mid - 1 > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def determinant(mat):
    # Exact integer Bareiss elimination.
    a = [r[:] for r in mat]
    size = len(a)
    old = 1
    sign = 1
    for k in range(size - 1):
        if a[k][k] == 0:
            swap = next((j for j in range(k + 1, size) if a[j][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, size):
            for j in range(k + 1, size):
                num = pivot * a[i][j] - a[i][k] * a[k][j]
                assert num % old == 0
                a[i][j] = num // old
        for i in range(k + 1, size):
            a[i][k] = 0
        old = pivot
    return sign * a[-1][-1]


def check(n):
    K = graph(n)
    rho = root(n)
    r = [rho ** i for i in range(n - 1)] + [1 / rho]
    ell = [rho ** (-i) for i in range(n)]
    for i in range(n):
        assert abs(sum(K[i][j] * r[j] for j in range(n)) - rho * r[i]) < 1e-6
        assert abs(sum(ell[j] * K[j][i] for j in range(n)) - rho * ell[i]) < 1e-6
    p = [ell[i] * r[i] / sum(ell[j] * r[j] for j in range(n)) for i in range(n)]
    assert abs(sum(p) - 1) < 1e-12
    assert abs(p[-1] - 1 / ((n - 1) * rho + n)) < 1e-12
    for beta in (0.0, 1.0, 4.0, 10.0, 20.0):
        q = math.exp(-beta)
        decay = 1 / (1 + q * rho)
        P = [[((1 if i == j else 0) + q * K[i][j] * r[j] / r[i]) * decay
              for j in range(n)] for i in range(n)]
        assert max(abs(sum(row) - 1) for row in P) < 1e-10
        for j in range(n):
            assert abs(sum(p[i] * P[i][j] for i in range(n)) - p[j]) < 1e-10
        jump = q * rho / (1 + q * rho)
        for i in range(n):
            assert abs(sum(P[i][j] for j in range(n) if i != j) - jump) < 1e-10
    return p[-1]


def main():
    # Exact characteristic-polynomial checks at integer arguments, plus
    # analytic graph-cycle determinant identity in the accompanying proof.
    for n in range(3, 12):
        K = graph(n)
        for x in (-2, -1, 0, 1, 2, 3):
            det = determinant([[x * (i == j) - K[i][j] for j in range(n)]
                               for i in range(n)])
            assert det == x ** n - x - 1, (n, x, det)
    for n in range(3, 61):
        check(n)
    print('VERIFY_OK determinant_samples=54 numerical_dimensions=58')


if __name__ == '__main__':
    main()
