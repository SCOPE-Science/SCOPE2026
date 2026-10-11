#!/usr/bin/env python3
"""Finite exact checks for the finite Cesaro inverse; NOT an infinite theorem proof."""
from fractions import Fraction as F
import math


def c(n):
    return [[F(1, i) if j <= i else F(0) for j in range(1, n + 1)] for i in range(1, n + 1)]


def b(n):
    return [[F(i) if j == i else (F(-(i - 1)) if j == i - 1 else F(0)) for j in range(1, n + 1)] for i in range(1, n + 1)]


def multiply(a, b):
    n = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(n)), F(0)) for j in range(n)] for i in range(n)]


def matrices_equal(a, b):
    return all(x == y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def finite_checks():
    for n in range(2, 13):
        cc, bb = c(n), b(n)
        identity = [[F(i == j) for j in range(n)] for i in range(n)]
        assert matrices_equal(multiply(cc, bb), identity)
        assert matrices_equal(multiply(bb, cc), identity)
        for shift in (0, 1, 3):
            z = [F(0)] + [F((7 * i + shift) % 13 - 6, 2 * i + 1) for i in range(1, n + 1)]
            x = [z[i] / i for i in range(1, n + 1)]
            bx = [sum((bb[i][j] * x[j] for j in range(n)), F(0)) for i in range(n)]
            q = sum(((z[i] - z[i - 1]) ** 2 for i in range(1, n + 1)), F(0))
            m = sum((x[i] ** 2 for i in range(n)), F(0))
            assert sum((v * v for v in bx), F(0)) == q
            assert m == sum((z[i] ** 2 / (i * i) for i in range(1, n + 1)), F(0))
            u = [0.0] + [float(z[i]) / math.sqrt(i) for i in range(1, n + 1)]
            kinetic = sum(math.sqrt(i * (i - 1)) * (u[i] - u[i - 1]) ** 2 for i in range(2, n + 1))
            potential = sum(i * (2 - math.sqrt(1 - 1 / i) - math.sqrt(1 + 1 / i) - 1 / (4 * i * i)) * u[i] ** 2 for i in range(1, n))
            potential += (n * (1 - math.sqrt(1 - 1 / n)) - 1 / (4 * n)) * u[n] ** 2
            assert abs(float(q - m / 4) - (kinetic + potential)) < 3e-11 * max(1, float(q))
    for i in range(2, 1001):
        t = 1 / i
        assert 2 - math.sqrt(1 - t) - math.sqrt(1 + t) + 1e-14 >= t * t / 4
    print('FINITE_IDENTITY_CHECK_OK')


if __name__ == '__main__':
    finite_checks()
