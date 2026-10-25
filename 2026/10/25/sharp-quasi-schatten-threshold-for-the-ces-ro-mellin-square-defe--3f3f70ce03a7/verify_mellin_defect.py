"""Finite arithmetic checks for the Cesaro--Mellin square-defect formulas.

Run: python3 verify_mellin_defect.py
This is a finite arithmetic check, not a proof of infinite-dimensional assertions.
"""
from fractions import Fraction
from math import log, sqrt, fsum


def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def defect(n, k):
    if not (1 <= k <= n):
        return 0.0
    return (float(harmonic(n) - harmonic(k - 1)) - log(n / k)) / n


def split(n, k):
    if k > n:
        return 0.0
    return (float(sum((Fraction(1, t) for t in range(k, n)), Fraction(0)))
            - fsum(log((t + 1) / t) for t in range(k, n)) + 1 / n) / n


def main():
    identity_count = 0
    bound_count = 0
    for n in range(1, 91):
        for k in range(1, n + 1):
            a, b = defect(n, k), split(n, k)
            assert abs(a - b) < 2e-13, (n, k, a, b)
            identity_count += 1
        assert abs(defect(n, n) - 1 / n**2) < 1e-14
        for j in range(1, n):
            aj = 1 / j - log(1 + 1 / j)
            assert 0 < aj <= 1 / (2 * j**2) * (1 + 1e-13)
            bound_count += 1
    # Direct finite projection checks: D_N is triangular with exact diagonal.
    for N in (5, 11, 23, 47):
        mat = [[defect(n, k) if k <= n else 0.0
                for k in range(1, N + 1)] for n in range(1, N + 1)]
        assert all(abs(mat[i][i] - 1 / (i + 1)**2) < 1e-14
                   for i in range(N))
        assert all(abs(mat[i][j]) < 1e-14 for i in range(N)
                   for j in range(i + 1, N))
    try:
        import numpy as np
        from numpy.linalg import svd
    except ImportError:
        spectral_checks = 'not run (NumPy unavailable)'
    else:
        spectral_checks = 0
        for N in (16, 32, 64, 96):
            mat = np.array([[defect(n, k) if k <= n else 0.0
                             for k in range(1, N + 1)]
                            for n in range(1, N + 1)])
            singular = svd(mat, compute_uv=False)
            for p in (.5, .6, .75, 1.0):
                lhs = sum((k ** (-2 * p) for k in range(1, N + 1)))
                rhs = float(sum(s ** p for s in singular))
                assert lhs <= rhs * (1 + 2e-11), (N, p, lhs, rhs)
                spectral_checks += 1
    print(f'PASS: {identity_count} entrywise decomposition identities; '
          f'{bound_count} coefficient inequalities; '
          f'four triangular projection checks; '
          f'{spectral_checks} finite spectral-majorization checks.')
    print('These checks do not establish an infinite-dimensional Schatten claim.')


if __name__ == '__main__':
    main()
