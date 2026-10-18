#!/usr/bin/env python3
"""Reproduce finite checks for dyadic rotation-complete Rudin--Shapiro blocks.

Run: python3 verify_rudin_rotations.py
The infinite assertion is proved in RESULT.md, not inferred from these tests.
"""
from collections import Counter

H = {'a': 'ab', 'b': 'ac', 'c': 'db', 'd': 'dc'}
CODE = {'a': '0', 'b': '0', 'c': '1', 'd': '1'}
LETTERS = 'abcd'
PAIR = ['ab', 'ac', 'db', 'dc']


def expand(s, steps):
    for _ in range(steps):
        s = ''.join(H[x] for x in s)
    return s


def coded(s):
    return ''.join(CODE[x] for x in s)


def blocks(k):
    return {x: coded(expand(x, k)) for x in LETTERS}


def q4(s):
    return sum((s + s[:3])[i:i+4] == '0100' for i in range(len(s)))


def pure_power(s):
    n = len(s)
    return any(s == s[:d] * (n // d) for d in range(1, n) if n % d == 0)


def rotations(w):
    return {w[i:] + w[:i] for i in range(len(w))}


def direct_rs(n):
    return ''.join(str((i & (i >> 1)).bit_count() & 1) for i in range(n))


def run():
    state = expand('a', 9)
    assert all(state.find(x) >= 0 for p in PAIR for x in [p + p[0], p[1] + p])
    for k in range(3, 13):
        B = blocks(k)
        for x, w in B.items():
            assert len(w) == (1 << k)
            assert not pure_power(w)
        Q = tuple(q4(B[x]) for x in LETTERS)
        counts = tuple(B[x].count('1') for x in LETTERS)
        if k % 2 == 0:
            m = k // 2
            goal = (2**(k-1) - 2**(m-1),)*2 + (2**(k-1) + 2**(m-1),)*2
            assert counts == goal
            assert Q[0] - Q[1] == Q[2] - Q[3] == (1 << (m-2))
        else:
            m = (k - 1) // 2
            goal = (2**(k-1)-2**m, 2**(k-1), 2**(k-1), 2**(k-1)+2**m)
            assert counts == goal
            assert Q[1] - Q[2] == 1 << (m-1)
        assert len({(counts[i], Q[i]) for i in range(4)}) == 4
        if k + 2 <= 12:
            next_Q = tuple(q4(blocks(k+2)[x]) for x in LETTERS)
            T = ((2,1,1,0), (1,2,0,1), (1,0,2,1), (0,1,1,2))
            assert next_Q == tuple(sum(T[i][j]*Q[j] for j in range(4)) for i in range(4))
        # Direct factor-set verification is independent of the triple-witness argument.
        if k <= 9:
            n = 1 << k
            prefix = direct_rs(1 << (k + 7))
            F = set(prefix[i:i+n] for i in range(len(prefix)-n+1))
            for x in LETTERS:
                assert rotations(B[x]) <= F, (k, x)
            if k <= 8:
                state_prefix = coded(expand('a', k+7))
                assert state_prefix == prefix
        print(f'k={k:2d} length={1<<k:5d} weights={counts} cyclic0100={Q} PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
