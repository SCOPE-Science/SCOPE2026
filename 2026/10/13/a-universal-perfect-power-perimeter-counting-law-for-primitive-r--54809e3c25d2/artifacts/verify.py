#!/usr/bin/env python3
"""Exact regression checks for perfect-power perimeters of primitive right triangles."""
from math import gcd


def through_euclid(max_m, exponents):
    max_perimeter = 4 * max_m * max_m
    target = {}
    for k in exponents:
        powers = set()
        t = 1
        while t**k <= max_perimeter:
            powers.add(t**k)
            t += 1
        target[k] = powers
    solutions = {k: set() for k in exponents}
    for m in range(2, max_m + 1):
        for n in range(1 + m % 2, m, 2):
            if gcd(m, n) > 1:
                continue
            perimeter = 2 * m * (m + n)
            for k in exponents:
                if perimeter in target[k]:
                    solutions[k].add((m, n, perimeter))
    return solutions


def through_power_parameters(max_m, k):
    solutions = set()
    u = 1
    while (2**(k - 1)) * (u**k) <= max_m:
        m = (2**(k - 1)) * (u**k)
        for v in range(1, 2*u, 2):
            if gcd(u, v) != 1:
                continue
            vk = v**k
            if m < vk < 2*m:
                n = vk - m
                solutions.add((m, n, (2*u*v)**k))
        u += 1
    return solutions


def main():
    max_m = 2200
    exponents = (2, 3, 4, 5)
    direct = through_euclid(max_m, exponents)
    total = 0
    for k in exponents:
        via_params = through_power_parameters(max_m, k)
        assert via_params == direct[k], (k, direct[k] ^ via_params)
        total += len(direct[k])
        for bound in (100000, 2000000, 9000000):
            assert sum(1 for _, _, perimeter in via_params if perimeter <= bound) == sum(
                1 for _, _, perimeter in direct[k] if perimeter <= bound
            )
    assert (108, 17, 27000) in direct[3]
    assert (2048, 353, 56**4) in direct[4]
    assert 2*16384 * (16384+423) == 56**5
    assert gcd(16384, 423) == 1
    assert 0 < 423 < 16384
    print('EXACT_POWER_PERIMETER_OK Euclid_max_m=2200 exponents=2..5 '
          'bounds=100000,2000000,9000000 total_matched=%d examples=2,3,4,5' % total)
    print('Counts_by_exponent:', ', '.join('%d:%d' % (k, len(direct[k])) for k in exponents))

if __name__ == '__main__':
    main()
