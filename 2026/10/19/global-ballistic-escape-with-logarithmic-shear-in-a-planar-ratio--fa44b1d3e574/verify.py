#!/usr/bin/env python3
"""Finite consistency checks for a rational planar map's escape laws.

The proof of infinite-time behavior is mathematical, not based on these checks.
"""
from fractions import Fraction
from math import log, isfinite


def step(a, c, x, y):
    return x * (1 + a / (1 + y * y)), y + c * x


def exact_checks():
    a, c = Fraction(2), Fraction(3)
    x, y = Fraction(1), Fraction(0)
    expected = [(Fraction(3), Fraction(3)),
                (Fraction(18, 5), Fraction(12)),
                (Fraction(2646, 725), Fraction(114, 5))]
    for pair in expected:
        x, y = step(a, c, x, y)
        assert (x, y) == pair, ((x, y), pair)
    # A zero first coordinate is fixed for every second coordinate.
    for y in (Fraction(0), Fraction(-3, 2), Fraction(13, 7)):
        assert step(a, c, Fraction(0), y) == (0, y)
    return len(expected) + 3


def asymptotic_checks():
    cases = [(1., 1., 1., 0.),
             (2., 3., -1., 1.),
             (.7, -2.5, 1.3, -3.),
             (3., -1.25, -2., 5.)]
    n = 8000
    assertions = 0
    for a, c, x, y in cases:
        x0, direction = x, c * x
        ys, xs = {}, {}
        for k in range(1, 4 * n + 1):
            x_next, y_next = step(a, c, x, y)
            assert x_next * x0 > 0
            assert abs(x_next) > abs(x)
            assert (y_next - y) * direction > 0
            x, y = x_next, y_next
            if k in (n, 2 * n, 4 * n):
                xs[k], ys[k] = x, y
        assertions += 3 * 4 * n
        xlimit = xs[4 * n] + a / (c * c * xs[4 * n] * (4 * n))
        assert isfinite(xlimit) and xlimit * x0 > 0
        # Differences cancel the unobserved limit X or affine trajectory.
        tail_difference = 2 * n * (xs[2 * n] - xs[n])
        tail_prediction = a / (c * c * xlimit)
        assert abs(tail_difference / tail_prediction - 1) < .02
        dyadic = ys[4*n] - 3 * ys[2*n] + 2 * ys[n]
        dyadic_prediction = a * log(2) / (c * xlimit)
        assert abs(dyadic / dyadic_prediction - 1) < .03, (dyadic, dyadic_prediction)
        assertions += 3
    return assertions


if __name__ == '__main__':
    count = exact_checks() + asymptotic_checks()
    print('Finite exact and numerical consistency assertions passed:', count)
    print('Infinite-time claims are established by the proof in RESULT.md.')
