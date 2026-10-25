#!/usr/bin/env python3
"""Numerical illustrations for the exact orbit-square-function constants.

Only test finite examples; this is not a proof of the infinite-dimensional theorem.
"""
import math
import random


def weights(k):
    return 0.6 * 4.0 ** (-abs(k))


def cyclic_constant(m, cutoff=180):
    mass = [0.0] * m
    for k in range(-cutoff, cutoff + 1):
        mass[k % m] += weights(k)
    return sum(math.sqrt(v) for v in mass)


def pair_defect_check(values):
    defect = sum(values) - math.sqrt(sum(v*v for v in values))
    for j in range(len(values)):
        for k in range(j + 1, len(values)):
            assert (2 - math.sqrt(2))*min(values[j], values[k]) <= defect + 1e-11
    pair_upper = sum(min(values[j], values[k]) for j in range(len(values)) for k in range(j+1, len(values)))
    assert defect <= pair_upper + 1e-11


if __name__ == '__main__':
    full_constant = 3.0 * math.sqrt(3.0 / 5.0)
    assert abs(cyclic_constant(1) - 1.0) < 1e-12
    assert abs(cyclic_constant(2) - (math.sqrt(17)+math.sqrt(8))/5) < 1e-12
    assert cyclic_constant(2) < cyclic_constant(8) < cyclic_constant(40) < full_constant
    random.seed(1701)
    for _ in range(2000):
        v = [random.random() ** 3 for _ in range(6)]
        pair_defect_check(v)
    print('finite cyclic constants and pairwise defect inequalities: PASS')
    for m in (1, 2, 3, 4, 8, 16, 40):
        print(m, format(cyclic_constant(m), '.14f'))
