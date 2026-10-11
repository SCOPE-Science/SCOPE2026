"""Finite exact checks for the weighted rule-128 fixed-point-basin theorem.
Run with Python 3.10 or later; no third-party dependencies.
These tests do not replace the infinite-volume analytic proof.
"""
from itertools import product
from fractions import Fraction


def evolve(x):
    n = len(x)
    return tuple(x[(i-1) % n] & x[i] & x[(i+1) % n] for i in range(n))


def run_matrix(m, z):
    A = [[0]*m for _ in range(m)]
    for j in range(m):
        A[j][0] = 1
        if j+1 < m:
            A[j][j+1] = z
    return A


def multiply(A, B):
    m = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(m))
             for j in range(m)] for i in range(m)]


def trace_power(A, n):
    m = len(A)
    P = [[int(i == j) for j in range(m)] for i in range(m)]
    for _ in range(n):
        P = multiply(P, A)
    return sum(P[i][i] for i in range(m))


def direct_weighted_partition(n, p, z):
    ans = 0
    for x in product((0, 1), repeat=n):
        y = x
        for _ in range(p):
            y = evolve(y)
        if y == evolve(y):
            ans += z**sum(x)
    return ans


def forbidden_weighted_partition(n, m, z):
    ans = 0
    for x in product((0, 1), repeat=n):
        if any(all(x[(j+k) % n] for k in range(m)) for j in range(n)):
            continue
        ans += z**sum(x)
    return ans


def verify():
    checks = 0
    for p in range(1, 5):
        m = 2*p+1
        for n in range(3, 13):
            for z in (1, 2, 3, 5):
                a = direct_weighted_partition(n, p, z)
                b = forbidden_weighted_partition(n, m, z) + z**n
                c = trace_power(run_matrix(m, z), n) + z**n
                assert a == b == c, (p, n, z, a, b, c)
                checks += 2
        # Verify the critical-point polynomial and density slope as rational equalities.
        z = m
        lam = m
        assert sum(Fraction(z**r, lam**(r+1)) for r in range(m)) == 1
        checks += 1
        weighted_r = sum(Fraction(r, m) for r in range(m))
        weighted_r_plus_one = sum(Fraction(r+1, m) for r in range(m))
        rho = weighted_r / weighted_r_plus_one
        assert rho == Fraction(p, p+1)
        checks += 1
    # Full individual-configuration iterate identities, including wrapped neighborhoods.
    for p in range(1, 5):
        for n in range(3, 11):
            for x in product((0, 1), repeat=n):
                y = x
                for _ in range(p):
                    y = evolve(y)
                predicted = tuple(int(all(x[(i+j) % n] for j in range(-p, p+1)))
                                  for i in range(n))
                assert y == predicted, (p, n, x)
                checks += 1
    print(f'PASS: {checks} exact assertions')

if __name__ == '__main__':
    verify()
