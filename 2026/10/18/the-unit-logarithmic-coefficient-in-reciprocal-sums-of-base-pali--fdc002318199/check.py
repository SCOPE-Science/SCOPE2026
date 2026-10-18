#!/usr/bin/env python3
"""Exact finite verification for the palindrome reciprocal asymptotic theorem.
Scientific proof is supplied separately: enumeration is not an infinite argument.
"""
from fractions import Fraction as Q


def palindrome(n, b):
    digits = []
    while n:
        n, r = divmod(n, b)
        digits.append(r)
    return digits == digits[::-1]


def block(b, k):
    return sum((Q(1, n) for n in range(b ** (k - 1), b ** k)
                if palindrome(n, b)), Q(0))


def verify():
    for b in range(2, 7):
        h = sum((Q(1, a) for a in range(1, b)), Q(0))
        y = sum((Q(1, m) for m in range(b, b * b)), Q(0))
        z = y - Q(b - 1, b * b)
        values = {k: block(b, k) for k in range(1, 8)}
        assert values[1] == h and values[2] == h / (b + 1)
        for k in range(4, 8):
            assert z / b ** (k // 2) <= values[k] <= y / b ** (k // 2)
        d3 = y / b - values[3]
        assert 0 <= h - b**3 * d3 <= 2
        g = Q(b + 2, b + 1) * h + (Q(1, b) + Q(2, b*b)) * y
        partial = sum(values.values(), Q(0))
        upper_tail = 2 * y / (b**4 * (1 - Q(1, b)))
        scaled_lower = b**3 * (partial - g)
        scaled_upper = scaled_lower + b**3 * upper_tail
        center = 2 * y - h
        assert center - 4 <= scaled_lower <= scaled_upper <= center + 4
        print('PASS base', b, 'exact intervals and block bounds')
    print('ALL_PASS')


if __name__ == '__main__':
    verify()
