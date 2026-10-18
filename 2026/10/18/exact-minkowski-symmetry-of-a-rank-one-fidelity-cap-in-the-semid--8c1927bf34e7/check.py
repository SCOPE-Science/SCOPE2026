#!/usr/bin/env python3
"""High-precision finite checks for the rank-one semidefinite cap formula.

These computations test selected instances only; the accompanying mathematical
argument, not numerical sampling, establishes the universal statement.
"""
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 70
ONE = Decimal(1)


def dec(fraction):
    return Decimal(fraction.numerator) / Decimal(fraction.denominator)


def alpha_value(d, delta):
    s = Decimal(d - 1)
    dd = Decimal(d)
    b = s - dd * delta
    return ((b * b + 4 * s * (ONE - delta)).sqrt() - b) / (2 * s)


def evaluate(d, delta):
    s = Decimal(d - 1)
    a = alpha_value(d, delta)
    q = delta / (ONE + a)
    b = q / s
    longitudinal = ONE - q
    tol = Decimal('1e-55')

    # Exact equation defining the claimed value, evaluated at high precision.
    poly = s * a * a + (s - d * delta) * a - (ONE - delta)
    assert abs(poly) < tol, (d, delta, 'root', poly)
    assert a > delta / s and 0 < q < min(delta, s / d)

    # The cap inequality and its sharp rank-one PSD constraint.
    assert abs((ONE + a) * q - delta) < tol
    G = (ONE - delta) / longitudinal + s * delta / q
    assert abs(G - (ONE + a) / a) < tol, (d, delta, 'rank-one', G)

    # For every pure state, the only potentially nontrivial PSD restriction
    # is the two-by-two block on the ray and its transverse direction.
    # Its determinant at the rim must vanish, whereas it is positive inside.
    for j in range(101):
        t = delta * Decimal(j) / 100
        aa = (ONE + a) * longitudinal - a * (ONE - t)
        bb = (ONE + a) * b - a * t
        det = aa * bb - a * a * t * (ONE - t)
        assert aa >= -tol and bb >= -tol and det >= -tol
        if j == 100:
            assert abs(det) < tol

    # For an inadmissible larger reflection factor, the cap bound forces
    # q smaller than the optimal q.  The rank-one test is then strictly worse.
    larger = a + Decimal('0.00001')
    q_upper = delta / (ONE + larger)
    G_upper = (ONE - delta) / (ONE - q_upper) + s * delta / q_upper
    assert G_upper > (ONE + larger) / larger
    return a


def main():
    dimensions = [2, 3, 4, 7, 14, 29]
    widths = [Fraction(1, 10000), Fraction(1, 100), Fraction(1, 10),
              Fraction(1, 3), Fraction(1, 2), Fraction(2, 3),
              Fraction(4, 5), Fraction(9999, 10000)]
    count = 0
    for d in dimensions:
        prev = None
        for width in widths:
            value = evaluate(d, dec(width))
            if prev is not None:
                assert value > prev  # monotone along selected parameters
            prev = value
            count += 1
    print('PASS: {} high-precision (dimension, width) cases, 101 rim/interior probes each'.format(count))
    print('NOTE: finite checks do not prove the all-parameter theorem.')


if __name__ == '__main__':
    main()
