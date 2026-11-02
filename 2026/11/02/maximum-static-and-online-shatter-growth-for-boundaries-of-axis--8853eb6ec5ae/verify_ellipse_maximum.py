#!/usr/bin/env python3
"""Exact rational finite witness for the maximal trace theorem for ellipse curves.

The all-cardinality theorem is proved separately by a perturbation argument;
this script checks a ten-point rational witness without floating-point arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations
from math import lcm, comb


def witness(n=10):
    if not 1 <= n <= 10:
        raise ValueError('the packaged finite witness has 1..10 points')
    points = []
    for j in range(1, n + 1):
        t = F(j, 20)
        stretch = 1 + F(j ** 3, 10 ** 6)
        x = stretch * (1 - t * t) / (1 + t * t)
        y = stretch * 2 * t / (1 + t * t)
        points.append((x, y))
    return points


def lifted_row(point):
    x, y = point
    values = (x * x, y * y, x, y, F(1))
    den = lcm(*(z.denominator for z in values))
    return tuple(int(z * den) for z in values)


def determinant(matrix):
    """Fraction-free Bareiss determinant, with exact division."""
    a = [list(row) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sgn = 1
    denom = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            p = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sgn = -sgn
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % denom == 0
                a[i][j] = numerator // denom
            a[i][k] = 0
        denom = pivot
    return sgn * a[n - 1][n - 1]


def kernel4(rows):
    vec = tuple(((-1) ** j) * determinant([[row[k] for k in range(5) if k != j] for row in rows]) for j in range(5))
    assert any(z != 0 for z in vec)
    assert all(sum(a * b for a, b in zip(row, vec)) == 0 for row in rows)
    return vec


def run():
    points = witness(10)
    rows = [lifted_row(p) for p in points]
    total_four, total_five = 0, 0
    for I in combinations(range(len(points)), 4):
        w = kernel4([rows[i] for i in I])
        assert w[0] * w[1] > 0, (I, 'not an axis-aligned ellipse')
        # Constant coefficient must have opposite sign from the quadratic terms.
        assert w[0] * w[4] < 0, (I, 'no real ellipse')
        assert all(sum(a * b for a, b in zip(rows[j], w)) != 0 for j in range(10) if j not in I)
        total_four += 1
    for I in combinations(range(len(points)), 5):
        assert determinant([rows[i] for i in I]) != 0, (I, 'five-fold incidence')
        total_five += 1
    assert total_four == comb(10, 4)
    assert total_five == comb(10, 5)
    # Four-element real ellipses and full rank five-point incidences ensure
    # that every subset of size <=4 can be isolated by a small perturbation
    # of an equation in the homogeneous coefficient space.
    total_traces = sum(comb(10, j) for j in range(5))
    assert total_traces == 386
    print('AXIS_ELLIPSE_EXACT_WITNESS_PASS points=10 quadruples=210 quintets=252 traces=386')
    print('ALL_DETERMINANT_CHECKS_RATIONAL_PASS')


if __name__ == '__main__':
    run()
