#!/usr/bin/env python3
"""Supplementary exact-arithmetic checks for a mixed-volume product identity.

Run with: python3 verify.py
The finite checks are not a substitute for the analytic theorem.
"""
from fractions import Fraction
from itertools import combinations
from random import Random


def determinant(matrix):
    """Integer determinant by exact fraction Gaussian elimination."""
    n = len(matrix)
    a = [[Fraction(x) for x in row] for row in matrix]
    sign = 1
    result = Fraction(1)
    for i in range(n):
        pivot = next((j for j in range(i, n) if a[j][i]), None)
        if pivot is None:
            return 0
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            sign *= -1
        p = a[i][i]
        result *= p
        for j in range(i + 1, n):
            factor = a[j][i] / p
            for k in range(i + 1, n):
                a[j][k] -= factor * a[i][k]
            a[j][i] = 0
    assert result.denominator == 1
    return sign * result.numerator


def zonotope_volume(columns):
    n = len(columns[0])
    return sum(abs(determinant([[columns[j][i] for j in pick]
                                for i in range(n)]))
               for pick in combinations(range(len(columns)), n))


def truncated_polynomial_product(data):
    poly = {(0, 0): Fraction(1)}
    for a, b, c in data:
        factor = {(0, 0): Fraction(1), (1, 0): a,
                  (0, 1): b, (1, 1): c}
        new = {}
        for (p, q), x in poly.items():
            for (r, s), y in factor.items():
                if p + r <= 1 and q + s <= 1:
                    key = (p + r, q + s)
                    new[key] = new.get(key, Fraction(0)) + x * y
        poly = new
    return poly


def run():
    rng = Random(150700765)
    checks = 0
    for n in range(2, 8):
        basis = [tuple(int(i == j) for i in range(n)) for j in range(n)]
        for j in range(n):
            for k in range(j + 1, n):
                # Two segments in distinct factors attain the sharp constant.
                v, w = basis[j], basis[k]
                cross = sum(abs(v[i] * w[t] - v[t] * w[i])
                            for i in range(n) for t in range(i + 1, n))
                ratio = Fraction(n * cross,
                                 (n - 1) * sum(abs(x) for x in v)
                                 * sum(abs(x) for x in w))
                assert ratio == Fraction(n, n - 1)
                checks += 1
        for _ in range(550):
            v = tuple(rng.randint(-5, 5) for _ in range(n))
            w = tuple(rng.randint(-5, 5) for _ in range(n))
            if not any(v) or not any(w):
                continue
            sx = sum(abs(x) for x in v)
            sy = sum(abs(x) for x in w)
            cross = sum(abs(v[i] * w[j] - v[j] * w[i])
                        for i in range(n) for j in range(i + 1, n))
            # Bound from the exact mixed-volume coefficient on a box.
            assert cross <= sx * sy
            assert Fraction(n * cross, (n - 1) * sx * sy) <= Fraction(n, n - 1)
            checks += 1
    # Independent zonotope-volume expansion with genuine integer determinants.
    for n in range(2, 6):
        axes = [tuple(int(i == j) for i in range(n)) for j in range(n)]
        v0 = zonotope_volume(axes)
        assert v0 == 1
        for _ in range(80):
            v = tuple(rng.randint(-3, 3) for _ in range(n))
            w = tuple(rng.randint(-3, 3) for _ in range(n))
            vx = zonotope_volume(axes + [v])
            wx = zonotope_volume(axes + [w])
            both = zonotope_volume(axes + [v, w])
            cross = sum(abs(v[i] * w[j] - v[j] * w[i])
                        for i in range(n) for j in range(i + 1, n))
            assert vx - v0 == sum(abs(x) for x in v)
            assert wx - v0 == sum(abs(x) for x in w)
            assert both - vx - wx + v0 == cross
            checks += 3
    # Two-variable product rule under the exact Minkowski-polynomial normalization.
    for factors in range(2, 7):
        for _ in range(250):
            data = [(Fraction(rng.randrange(1, 10), rng.randrange(1, 7)),
                     Fraction(rng.randrange(1, 10), rng.randrange(1, 7)),
                     Fraction(rng.randrange(1, 10), rng.randrange(1, 7)))
                    for _ in range(factors)]
            result = truncated_polynomial_product(data)
            a = sum(x[0] for x in data)
            b = sum(x[1] for x in data)
            c = sum(x[2] for x in data)
            cross = sum(data[i][0] * data[j][1]
                        for i in range(factors) for j in range(factors)
                        if i != j)
            assert result[(1, 0)] == a
            assert result[(0, 1)] == b
            assert result[(1, 1)] == c + cross
            checks += 3
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    run()
