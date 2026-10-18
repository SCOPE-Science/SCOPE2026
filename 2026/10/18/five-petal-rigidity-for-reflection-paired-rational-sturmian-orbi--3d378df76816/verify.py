#!/usr/bin/env python3
"""Exact finite diagnostics for rational mechanical orbits; not an infinite proof."""
from fractions import Fraction
from math import gcd


def mechanical_orbit(n, k):
    word = ''.join(str(((i + 1) * k) // n - (i * k) // n) for i in range(n))
    den = (1 << n) - 1
    return {Fraction(int(word[i:] + word[:i], 2), den) for i in range(n)}


def predecessor_digits(points):
    previous = {(2 * x) % 1: x for x in points}
    assert len(previous) == len(points), 'not a bijective periodic union'
    return ''.join('1' if previous[y] >= Fraction(1, 2) else '0'
                   for y in sorted(points))


def main():
    checked = 0
    for n in range(3, 24):
        for k in range(1, n):
            if gcd(n, k) != 1 or 2 * k == n:
                continue
            orb = mechanical_orbit(n, k)
            together = orb | {(1 - x) % 1 for x in orb}
            assert len(orb) == n
            assert len(together) == 2 * n
            m = min(k, n - k)
            expected = '1' * m + '0' * (n - 2 * m) + '1' * m
            expected += '0' * m + '1' * (n - 2 * m) + '0' * m
            actual = predecessor_digits(together)
            assert actual == expected, (n, k, actual, expected)
            jumps = sum(actual[i] != actual[i+1] for i in range(len(actual)-1))
            jumps += (actual[-1] == actual[0])
            assert jumps == 5
            checked += 1
    assert checked == 170
    print('PASS: 170 exact rational orbit/reflection/cardinality/label/jump checks')


if __name__ == '__main__':
    main()
