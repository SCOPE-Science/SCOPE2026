#!/usr/bin/env python3
"""Reproduce finite residue-fiber checks for sums of two even powers."""
from collections import Counter

EXPONENTS = (4, 6, 8, 10, 12, 14, 20)


def predicted(k: int, r: int, a: int) -> int:
    if r == 0:
        assert a == 0
        return 1
    assert k >= 4 and k % 2 == 0 and r >= 1 and 0 <= a < (1 << r)
    if r == 1:
        return 2
    s = (k & -k).bit_length() - 1
    h = s + 2
    if r < h:
        if a == 0 or a == 2:
            return 1 << (2 * r - 2)
        if a == 1:
            return 1 << (2 * r - 1)
        return 0
    mask = (1 << h) - 1
    if a & mask == 1:
        return 1 << (s + 1 + r)
    if a & mask == 2:
        return 1 << (s + r)
    if r < k:
        return (1 << (2 * r - 2)) if a == 0 else 0
    if a % (1 << k) != 0:
        return 0
    return (1 << (2 * (k - 1))) * predicted(k, r - k, a >> k)


def check():
    cases = 0
    for k in EXPONENTS:
        for r in range(1, 11):
            m = 1 << r
            power_counts = Counter(pow(x, k, m) for x in range(m))
            # Exact cyclic convolution of an independently enumerated histogram.
            actual = [sum(count_x * power_counts.get((a-xpow) % m, 0)
                          for xpow, count_x in power_counts.items())
                      for a in range(m)]
            theoretical = [predicted(k, r, a) for a in range(m)]
            assert actual == theoretical, (k, r)
            assert sum(actual) == m * m, (k, r, 'mass')
            cases += m
            if r <= 6:
                direct = [0] * m
                for x in range(m):
                    for y in range(m):
                        direct[(pow(x,k,m)+pow(y,k,m)) % m] += 1
                assert direct == actual, (k, r, 'direct')
    # Exact finite consistency of mixture masses: (1/2+1/4)/(1-1/4)=1.
    from fractions import Fraction
    assert (Fraction(1, 2) + Fraction(1, 4)) / (1 - Fraction(1, 4)) == 1
    print(f'VERIFY_OK: {len(EXPONENTS)} even exponents, {cases} complete residue-fiber checks')


if __name__ == '__main__':
    check()
