#!/usr/bin/env python3
"""Exact consistency checks for a logistic-prey period-two theorem.

General nonexistence and every-parameter existence are proved in RESULT.md;
finite checks here do not establish universal assertions.
"""
from fractions import Fraction as Q


def iterate(point, growth, intercept, slope):
    x, y = point
    return (x * (growth - x - y), y * (intercept + slope * x))


def affine_witness(growth, midpoint, epsilon):
    x, u = midpoint + epsilon, midpoint - epsilon
    y = growth - x - u / x
    v = growth - u - x / u
    assert x > 0 and u > 0 and y > 0 and v > 0
    b, c = v / y, y / v
    slope = (b - c) / (x - u)
    intercept = b - slope * x
    assert Q(0) < intercept < Q(1) and slope > 0
    first, second = (x, y), (u, v)
    assert first != second
    assert iterate(first, growth, intercept, slope) == second
    assert iterate(second, growth, intercept, slope) == first
    return first, second, intercept, slope


def main():
    growth = Q(4)
    first = (Q(12, 5), Q(29, 40))
    second = (Q(21, 10), Q(53, 70))
    intercept = Q(538, 1537)
    slope = Q(6225, 21518)
    assert Q(0) < intercept < Q(1) and slope > 0
    assert iterate(first, growth, intercept, slope) == second
    assert iterate(second, growth, intercept, slope) == first
    assert intercept + slope * first[0] == Q(212, 203)
    assert intercept + slope * second[0] == Q(203, 212)
    assert (second[1] - first[1]) == (
        first[0] - second[0]
    ) * (Q(1) - Q(1) / first[0] - Q(1) / second[0])

    # Exact rational constructions at three supercritical growth values.
    for growth, midpoint, epsilon in (
        (Q(31, 10), Q(201, 100), Q(1, 100000)),
        (Q(7, 2), Q(21, 10), Q(1, 1000)),
        (Q(5), Q(9, 4), Q(1, 100)),
    ):
        assert Q(2) < midpoint < min(growth - 1, (growth + 3) / 3)
        affine_witness(growth, midpoint, epsilon)
    print('PASS: exact two-cycle witness and three independent rational constructions')


if __name__ == '__main__':
    main()
