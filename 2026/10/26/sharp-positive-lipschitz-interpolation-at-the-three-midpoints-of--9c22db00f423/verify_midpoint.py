#!/usr/bin/env python3
"""Finite spot-check of the exact Lipschitz extension theorem for obtuse isosceles triangles.

The accompanying mathematical proof, not this finite computation, establishes all heights.
Uses only the Python standard library and 70-digit Decimal arithmetic.
"""
from decimal import Decimal, localcontext
from itertools import combinations


def test_height(h):
    one, two = Decimal(1), Decimal(2)
    L = (one + h * h).sqrt()
    D = L + h * (L - one)
    p = L * h / (two * D)
    sharp = L * L / D
    coordinates = [(-one, Decimal(0)), (one, Decimal(0)), (Decimal(0), h),
                   (Decimal(0), Decimal(0)), (-one / two, h / two),
                   (one / two, h / two)]

    def value_at_all(f):
        a, b, c = f
        return (a, b, c, p * (a + b) + (one - two * p) * c,
                (a + c) / two, (b + c) / two)

    extremes = [(Decimal(0), -two, -L),
                (Decimal(0), -two, L - two),
                (Decimal(0), Decimal(0), -L),
                (Decimal(0), Decimal(0), L),
                (Decimal(0), two, two - L),
                (Decimal(0), two, L)]
    tol = Decimal('1e-55')
    max_ratio = Decimal(0)
    checks = 0
    for f in extremes:
        vals = value_at_all(f)
        for i, j in combinations(range(6), 2):
            dx = coordinates[i][0] - coordinates[j][0]
            dy = coordinates[i][1] - coordinates[j][1]
            dst = (dx * dx + dy * dy).sqrt()
            ratio = abs(vals[i] - vals[j]) / dst
            if ratio > max_ratio:
                max_ratio = ratio
            assert ratio <= sharp + tol, (str(h), i, j, str(ratio), str(sharp))
            checks += 1

    # Both lower-bound witnesses attain the sharp upper bound at the optimal weight.
    witness_c = value_at_all((L, L, Decimal(0)))
    witness_a = value_at_all((Decimal(0), two, L))
    assert abs(abs(witness_c[3] - witness_c[2]) / h - sharp) < tol
    assert abs(abs(witness_a[3] - witness_a[0]) - sharp) < tol
    assert abs(max_ratio - sharp) < tol

    # Strict comparison to ordinary Euclidean midpoint averaging.
    ordinary = L / h
    assert ordinary > sharp
    return checks


def main():
    with localcontext() as context:
        context.prec = 70
        heights = [Decimal(k) / 120 for k in range(1, 121)]
        heights += [Decimal('0.001'), Decimal('0.0001'), Decimal('0.125'),
                    Decimal('0.3333333333333333333333333333333333333333')]
        total = sum(test_height(h) for h in heights)
        assert total == len(heights) * 90
        print(f'FINITE_EXTREME_CHECK_OK heights={len(heights)} pair_checks={total}')


if __name__ == '__main__':
    main()
