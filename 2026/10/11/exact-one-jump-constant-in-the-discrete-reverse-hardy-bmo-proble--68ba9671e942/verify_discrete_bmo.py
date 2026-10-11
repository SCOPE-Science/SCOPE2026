#!/usr/bin/env python3
"""Exact finite certificates and rational logarithm bounds for the one-jump Cesaro BMO ratio."""
from fractions import Fraction as F

TARGET = F(3371, 6720)


def harmonic_table(n):
    h = [F(0)]
    for j in range(1, n + 1):
        h.append(h[-1] + F(1, j))
    return h


def exact_small_jump():
    # The analytic tail estimates reduce all candidate intervals to starts 1,2,3 and ends <=127.
    values = [F(1), F(1)] + [F(2, n) for n in range(3, 128)]
    prefix = [F(0)]
    for x in values:
        prefix.append(prefix[-1] + x)
    maxima = []
    for start in (1, 2, 3):
        best, best_end = F(0), None
        for end in range(start, 128):
            size = end - start + 1
            mean = (prefix[end] - prefix[start - 1]) / size
            oscillation = sum(abs(x - mean) for x in values[start - 1:end]) / size
            if oscillation > best:
                best, best_end = oscillation, end
        maxima.append((start, best_end, best))
    assert maxima == [
        (1, 8, F(3371, 13440)),
        (2, 6, F(76, 375)),
        (3, 10, F(1663, 13440)),
    ], maxima
    assert 2 * maxima[0][2] == TARGET
    return maxima


def exact_medium_jumps():
    # For m>=3 use the interval 1,...,4m and split k=floor(5m/3).
    h = harmonic_table(4 * 199)
    minimum = (F(1), -1)
    for m in range(3, 200):
        k = 5 * m // 3
        witness_ratio = F(1) + h[k] - h[m] - F(k, 4 * m) * (1 + h[4 * m] - h[m])
        assert witness_ratio > TARGET, (m, witness_ratio)
        if witness_ratio < minimum[0]:
            minimum = (witness_ratio, m)
    assert minimum == (F(167723, 332640), 3), minimum
    return minimum


def exact_log_bounds():
    # artanh expansion: log((1+y)/(1-y)) = 2 sum_{j>=0} y^(2j+1)/(2j+1).
    y = F(3, 5)                   # log(4)
    partial = 2 * sum((y**(2*j+1) / (2*j+1) for j in range(7)), F(0))
    upper = partial + 2 * y**15 / (15 * (1-y*y))
    assert upper < F(1387, 1000), upper
    z = F(997, 600)
    y = (z-1) / (z+1)
    lower = 2 * (y + y**3 / 3)
    assert lower > F(507, 1000), lower
    assert F(6089,12000) > TARGET
    # e^5 > 128: seven terms of the exponential series already suffice.
    from math import factorial
    assert sum((F(5)**j / factorial(j) for j in range(8)), F(0)) > 128
    return upper, lower


if __name__ == '__main__':
    a=exact_small_jump()
    b=exact_medium_jumps()
    c=exact_log_bounds()
    print('ONE_JUMP_DISCRETE_BMO_EXACT_CERTIFICATES_OK')
    print('small_interval_maxima', a)
    print('medium_minimum', b)
    print('rational_log_bounds_verified', True)
