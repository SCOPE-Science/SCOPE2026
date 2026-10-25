#!/usr/bin/env python3
"""Exact finite reduction check for minimum flimsy witnesses with two zero bits.
No external packages. The finite cases can be rechecked by reading this file.
"""
from itertools import product
from collections import Counter

ODD_MULTIPLIERS = (3, 5, 7, 9)


def number(a, b, c):
    # Binary least-significant-bit first: 1^a,0,1^b,0,1^c.
    assert a >= 1 and b >= 0 and c >= 1
    return ((1 << a) - 1) + (((1 << b) - 1) << (a + 1)) + (((1 << c) - 1) << (a + b + 2))


def predicted(a, b, c):
    assert a + b + c + 2 >= 7
    if b >= 1:
        if a >= 2:
            return 3
        return 5 if c >= 2 else None
    if c == 1:
        return 7
    if a >= 3:
        return 5
    return 9


def transducer_weight(n, k):
    """Bit-serial multiplication, independently of Python's n*k popcount."""
    carry, ones, source = 0, 0, n
    while source:
        bit = source & 1
        y = k * bit + carry
        ones += y & 1
        carry = y >> 1
        source >>= 1
    return ones + carry.bit_count()


def check():
    checked = 0
    tally = Counter()
    for a, b, c in product(range(1, 5), range(5), range(1, 5)):
        L = a + b + c + 2
        if L < 7:
            continue
        n = number(a, b, c)
        assert n.bit_length() == L
        assert n.bit_count() == L - 2
        vals = {}
        for k in ODD_MULTIPLIERS:
            value = (k * n).bit_count()
            assert value == transducer_weight(n, k), (a, b, c, k)
            vals[k] = value
        observed = next((k for k in ODD_MULTIPLIERS if vals[k] < n.bit_count()), None)
        assert observed == predicted(a, b, c), (a, b, c, vals, observed, predicted(a, b, c))
        checked += 1
        tally[observed] += 1
    assert checked == 70, checked
    assert tally == {3: 47, 5: 17, 7: 1, 9: 3, None: 2}, tally
    # Independent finite sampling is a stress test, NOT part of the infinite proof.
    for L in range(7, 81):
        for a in range(1, L - 2):
            for c in range(1, L - a - 1):
                b = L - a - c - 2
                if b < 0:
                    continue
                n = number(a, b, c)
                observed = next((k for k in ODD_MULTIPLIERS if (k * n).bit_count() < n.bit_count()), None)
                assert observed == predicted(a, b, c), (L, a, b, c)
    print('VERIFIED: 70 exhaustive capped cases, 4 odd multipliers, independent bit-serial product; L=7..80 stress tests.')


if __name__ == '__main__':
    check()
