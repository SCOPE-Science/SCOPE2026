#!/usr/bin/env python3
"""Reproducible exact and numerical checks for a two-node exponential sweep."""
from fractions import Fraction
import math


def recurrence(m, u):
    assert m >= 0 and u > 0
    value = 1 - 2 * u
    for _ in range(m):
        value = 1 - u * (1 + value)
    return value


def formula(m, u):
    return (1 - u + 2 * (-1) ** (m + 1) * u ** (m + 2)) / (1 + u)


def update(state, a, b, h, m):
    """Two-node multiplicative SPIDeC, including zero-sweep predictor."""
    x, y = state
    g0 = a * (y / x - 1)
    g1 = b * (x / y - 1)
    X, Y = x * math.exp(h * g0), y * math.exp(h * g1)
    for _ in range(m):
        old0, old1 = a * (Y / X - 1), b * (X / Y - 1)
        X = x * math.exp(0.5 * h * (g0 + old0))
        Y = y * math.exp(0.5 * h * (g1 + old1))
    return X, Y


def run():
    total = 0
    # Exact recurrence, strict inequalities, and the critical boundary.
    for den in range(2, 18):
        for num in range(1, 4 * den):
            u = Fraction(num, den)
            for m in range(16):
                r = recurrence(m, u)
                assert r == formula(m, u)
                if u < 1:
                    assert -1 < r < 1
                elif u == 1:
                    assert r == (-1 if m % 2 == 0 else 1)
                else:
                    assert r < -1 if m % 2 == 0 else r > 1
                total += 1
    # The nonlinear map is checked directly, without using the derivative
    # recurrence in its implementation, for symmetric and asymmetric rates.
    for a, b in [(1., 1.), (2., 1.), (0.1, 4.), (3., 7.)]:
        for u in (0.1, 0.4, 0.9, 1., 1.1, 1.4):
            h = 2 * u / (a + b)
            for m in range(6):
                eps = 1e-8
                p = update((1 + eps * a, 1 - eps * b), a, b, h, m)
                n = update((1 - eps * a, 1 + eps * b), a, b, h, m)
                observed = (p[0] - n[0]) / (2 * eps * a)
                expected = float(recurrence(m, Fraction(str(u))))
                assert abs(observed - expected) < 1e-5 * (1 + abs(expected))
                assert min(*p, *n) > 0
                total += 2
    # The implicit-collocation multiplier is a different limit for u >= 1.
    for u in (Fraction(1, 10), Fraction(9, 10), Fraction(1), Fraction(3, 2)):
        collocation = (1 - u) / (1 + u)
        assert -1 < collocation < 1
        total += 1
    assert recurrence(1, Fraction(3, 2)) == Fraction(5, 2)
    assert (1 - Fraction(3, 2)) / (1 + Fraction(3, 2)) == Fraction(-1, 5)
    total += 2
    print(f'PASS: {total} exact-algebra, inequality, and direct nonlinear-map checks')


if __name__ == '__main__':
    run()
