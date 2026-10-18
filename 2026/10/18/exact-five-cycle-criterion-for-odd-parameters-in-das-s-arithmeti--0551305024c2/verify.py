#!/usr/bin/env python3
"""Finite exact regression for odd-parameter period-five cycles.

The argument proving the unbounded classification appears in RESULT.md.
"""
from math import isqrt


def sieve_largest(limit):
    lp = [0] * (limit + 1)
    for p in range(2, limit + 1):
        if not lp[p]:
            for j in range(p, limit + 1, p):
                lp[j] = p
    return lp


def phi(n, k, lp):
    return n + k if lp[n] == n else lp[n]


def test():
    K = 5000
    lp = sieve_largest(4 * K + 100)
    primes = [p for p in range(2, K + 1) if lp[p] == p]
    qualifying = []
    for k in range(1, K + 1, 2):
        q = lp[k + 1]
        has_candidate = lp[k + 2] == k + 2 and q != 2 and ((k + q) & (k + q - 1)) == 0
        expected = (2, k + 2, 2 * (k + 1), q, q + k) if has_candidate else None
        cycles = set()
        for p in primes:
            if p > k + 2:
                break
            seen = []
            x = p
            for _ in range(5):
                if x > 4 * K + 100:
                    raise ValueError('sieve interval insufficient')
                seen.append(x)
                x = phi(x, k, lp)
            if x == p and len(set(seen)) == 5:
                cycles.add(tuple(sorted(seen)))
        actual = {tuple(sorted(expected))} if has_candidate else set()
        assert cycles == actual, (k, cycles, actual)
        if has_candidate:
            qualifying.append((k, q, (k + q).bit_length() - 1))
    assert qualifying[:5] == [(5, 3, 3), (21, 11, 5), (51, 13, 6), (59, 5, 6), (1365, 683, 11)]
    print('PASS: complete period-five cycle census for odd 1 <= k <= 5000 from every starting prime p <= k+2')
    print('PASS: predicted formula matches; qualifying k, P(k+1), m:', qualifying)
    print('Finite checks do not establish the classification for unbounded k.')

if __name__ == '__main__':
    test()
