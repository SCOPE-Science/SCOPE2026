#!/usr/bin/env python3
"""Reproduce binary16 signed-accumulator transition and small exact-sketch moments."""
import itertools
import math
import struct

K = 2048


def half(x):
    return struct.unpack('>e', struct.pack('>e', x))[0]


def check_binary16_transitions():
    tests = 0
    for zeta in (1, 4):
        h = 1.0 / math.sqrt(zeta)
        for j in range(-K, K + 1):
            for s in (-1, 1):
                expected = max(-K, min(K, j + s)) * h
                observed = half(h * j + h * s)
                assert observed == expected, (zeta, j, s, observed, expected)
                tests += 1
    return tests


def exact_moments(n, m, zeta):
    assert m % zeta == 0
    b = m // zeta
    choices = [(bucket, sign) for bucket in range(b) for sign in (-1, 1)]
    raw_sum = 0
    raw_sum2 = 0
    total = (2 * b)**(n * zeta)
    for assignment in itertools.product(choices, repeat=n * zeta):
        a = [[0] * b for _ in range(zeta)]
        for index, (bucket, sign) in enumerate(assignment):
            a[index % zeta][bucket] += sign
        integer_q = sum(v * v for layer in a for v in layer)
        raw_sum += integer_q
        raw_sum2 += integer_q * integer_q
    mean = raw_sum / (total * zeta)
    var = raw_sum2 / (total * zeta * zeta) - mean * mean
    expected_variance = 2 * n * (n - 1) / m
    assert mean == n, (n, m, zeta, mean)
    assert abs(var - expected_variance) < 1e-12, (n, m, zeta, var, expected_variance)
    return total, mean, var


def check_absorption():
    out = []
    for zeta in (1, 4):
        h = 1.0 / math.sqrt(zeta)
        state = 0.0
        for _ in range(K + 10):
            state = half(state + h)
        assert state == K * h
        for _ in range(K + 10):
            state = half(state - h)
        assert state == -10 * h  # after K+10 downward steps from K
        out.append((zeta, K * h))
    return out


def check_stationary_second_moment():
    total_squares = sum(j*j for j in range(-K, K+1))
    avg_squares = total_squares / (2*K+1)
    assert avg_squares == K*(K+1)/3
    return avg_squares


if __name__ == '__main__':
    print('binary16 transition checks:', check_binary16_transitions())
    print('saturation checks:', check_absorption())
    for params in ((3, 2, 1), (3, 3, 1), (2, 4, 4), (2, 8, 4)):
        print('exact sketch moments', params, exact_moments(*params))
    print('uniform reflected-walk second moment:', check_stationary_second_moment())
    print('ALL CHECKS PASSED')
