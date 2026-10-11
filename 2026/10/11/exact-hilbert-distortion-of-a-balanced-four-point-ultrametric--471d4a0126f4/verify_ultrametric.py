#!/usr/bin/env python3
"""Exact-rational finite cross-checks for a symmetric four-point metric.

The universal theorem requires the analytic optimization in RESULT.md.
This program evaluates a rational parameter grid without floating point.
"""
from fractions import Fraction as F


def pieces(s, a):
    assert 0 < s <= F(1, 2) and a > 0
    vertices = [a / 4,
                a * (1 - s) ** 2 / 4 + s ** 2,
                a * (1 - 2 * s) ** 2 / 4 + 2 * s ** 2]
    minimum = min(s ** 2, a / (2 * (a + 2)))
    return max(vertices), minimum


def verify():
    cases = 0
    for den in range(2, 31):
        for num in range(1, den // 2 + 1):
            s = F(num, den)
            a0 = 4 * s ** 2 / (1 - 2 * s ** 2)
            predicted = 2 + (1 - 2 * s) ** 2 / (1 - 2 * s ** 2)
            M, m = pieces(s, a0)
            assert m == s ** 2 and M / m == predicted
            assert M == a0 * (1 - 2 * s) ** 2 / 4 + 2 * s ** 2
            assert a0 <= 4 * s / (2 - 3 * s)
            assert a0 <= 2 * s / (1 - s)
            for k in (F(1, 7), F(1, 2), F(3, 4), F(1), F(5, 4), F(2), F(3), F(7)):
                a = a0 * k
                MK, mK = pieces(s, a)
                assert MK / mK >= predicted
                cases += 1
    print('FOUR_POINT_ULTRAMETRIC_EXACT_RATIONAL_OK', cases)


if __name__ == '__main__':
    verify()
