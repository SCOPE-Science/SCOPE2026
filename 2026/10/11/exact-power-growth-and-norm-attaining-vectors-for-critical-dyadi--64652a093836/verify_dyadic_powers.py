#!/usr/bin/env python3
"""Exact rational finite checks for a dyadic block weighted-shift power profile.

The infinite theorem requires the analytical block estimates in RESULT.md.
"""
from fractions import Fraction


def block_maximum(n, j):
    """Maximum p-th power contribution of output I_j, using independent input blocks."""
    a = 1 << j
    b = (a << 1) - 1
    left = a + n
    right = b + n
    ans = Fraction(0)
    for k in range(left.bit_length()-1, right.bit_length()):
        lo = max(a, (1 << k) - n)
        hi = min(b, (1 << (k+1)) - 1 - n)
        if lo <= hi:
            ans += Fraction(lo+n, lo)
    return ans


def expected(n):
    if n == 1:
        return Fraction(17, 6), 1
    if n == 5:
        return Fraction(37, 6), 1
    return Fraction(n+1), 0


def main():
    assert block_maximum(1, 1) == Fraction(17, 6)
    assert block_maximum(5, 1) == Fraction(37, 6)
    for n in range(1, 501):
        values = [block_maximum(n, j) for j in range(21)]
        biggest = max(values)
        want, winner = expected(n)
        assert biggest == want, (n, biggest, want)
        assert values.index(biggest) == winner, (n, values.index(biggest), winner)
        assert values.count(biggest) == 1, n
    for n in range(2, 501):
        assert Fraction(2)+Fraction(9*n,20) < n+1
    assert Fraction(2)+Fraction(9,20) < Fraction(17,6)
    assert Fraction(17,12)>Fraction(37,36)>1
    print('DYADIC_C0_EXACT_PROFILE_CHECK_OK')


if __name__ == '__main__':
    main()
