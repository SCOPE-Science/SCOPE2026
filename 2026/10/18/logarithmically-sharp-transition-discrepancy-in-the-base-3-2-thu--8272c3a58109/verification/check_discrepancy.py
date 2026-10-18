#!/usr/bin/env python3
"""Reproduce finite checks for the base-3/2 Thue--Morse transition discrepancy.

Only Python's standard library is used. The infinite theorem requires the
algebraic proof in RESULT.md; these checks independently exercise its steps.
"""
from functools import lru_cache


def make_word(length):
    """Return the first length symbols using the original 2-to-3 recursion."""
    a = bytearray(length)
    for i in range(1, length):
        m, r = divmod(i, 3)
        a[i] = a[2*m] if r in (0, 1) else 1-a[2*m+1]
    return a


@lru_cache(None)
def error(n):
    """Exact normalized discrepancy from the independently derived recursion."""
    assert n >= 1
    if n == 1:
        return 0
    m, r = divmod(n, 3)
    if r == 0:
        return -error(2*m)-1
    return -error(2*m+1)-(2 if r == 2 else 0)


def smaller(n):
    m, r = divmod(n, 3)
    return 2*m + (r != 0)


def main():
    length = 150000
    word = make_word(length)
    changes = 0
    for n in range(1, length+1):
        if n > 1:
            changes += (word[n-2] != word[n-1])
        assert 5*changes - 2*(n-1) == error(n), n

    shifts = [0, 1, 1, 1, 2, 2, 3, 3, 3]
    offsets = [0, 0, -2, 1, 1, -1, -1, 2, 0]
    for n in range(2, length+1):
        m, r = divmod(n, 9)
        assert error(n) == error(4*m+shifts[r])+offsets[r], n
        # Integer contraction and the claimed local bound for all n.
        j = smaller(smaller(n))
        assert 9*(j-1) <= 4*(n-1), n
        assert abs(error(n)-error(j)) <= 2, n

    for j in range(1, 121):
        parity = j % 2
        low = (4**(j+parity)-1)//5
        high = (4**parity * 9**j-1)//5
        assert 1 <= low < high <= 9**j
        state = low
        for i in range(j):
            assert state % 4 == 3
            state = (9*state+1)//4
            assert 5*state+1 == 9**(i+1) * 4**(j+parity-i-1)
        assert state == high
        assert error(high)-error(low) == 2*j
    print('VERIFIED: 150000 direct prefix counts from the original word recurrence')
    print('VERIFIED: two-step identity, contraction and local bound for n=2..150000')
    print('VERIFIED: 120 exact repunit-gap certificates with unbounded integer sizes')
    print('CHECK_OK')


if __name__ == '__main__':
    main()
