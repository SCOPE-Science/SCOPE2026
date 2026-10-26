#!/usr/bin/env python3
"""Exact finite corroboration of a formula for Schemmel-totient iteration heights."""
from collections import defaultdict


def l2(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 0
    rest = n
    out = 1
    p = 3
    while p * p <= rest:
        if rest % p == 0:
            q = 1
            while rest % p == 0:
                rest //= p
                q *= p
            out *= (q // p) * (p - 2)
        p += 2
    if rest > 1:
        out *= rest - 2
    return out


def height(n):
    assert n > 1 and n % 2 == 1
    count = 0
    while n != 1:
        n = l2(n)
        count += 1
        assert n >= 1
        assert count < 1000
    return count


def formula(a, b, c):
    if b == c == 0:
        return a
    if b > 0:
        return b + c + max(a, 1)
    return c + max(a, 2)


def run():
    # Every exponent vector in [0,9]^3, except the unit element.
    cubes = 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                if not (a or b or c):
                    continue
                n = 3**a * 5**b * 7**c
                assert height(n) == formula(a, b, c), (a, b, c)
                cubes += 1
    # Entire infinite-semigroup height levels up to k=16 can be
    # enumerated within finite exponent bounds since all heights
    # are at least the largest exponent for each of the 3 primes.
    levels = defaultdict(list)
    for a in range(18):
        for b in range(18):
            for c in range(18):
                if a or b or c:
                    levels[height(3**a * 5**b * 7**c)].append(3**a * 5**b * 7**c)
    assert len(levels[1]) == 1
    assert len(levels[2]) == 3
    for k in range(3, 17):
        assert len(levels[k]) == k*(k+3)//2, (k, len(levels[k]))
    for k in range(2, 17):
        assert len(levels[k]) == len(set(levels[k]))
        expected = 15 * 7**(k-2)
        assert max(levels[k]) == expected
        assert levels[k].count(expected) == 1
    print('VERIFY_OK', 'exponent_cube', cubes,
          'complete_levels', 16, 'unique_maxima', 15)


if __name__ == '__main__':
    run()
