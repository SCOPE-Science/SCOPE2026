#!/usr/bin/env python3
"""Standalone finite checks for the noisy binary nearest-neighbour ring theorem.

Only standard-library dependencies. This is a finite test, not a proof for all lengths.
"""
from collections import Counter
from math import gcd


def update(v, n):
    mask = (1 << n) - 1
    return (((v << 1) | (v >> (n - 1))) ^
            ((v >> 1) | (v << (n - 1)))) & mask


def pivots(vectors):
    basis = {}
    for v in vectors:
        while v:
            k = v.bit_length() - 1
            if k in basis:
                v ^= basis[k]
            else:
                basis[k] = v
                break
    return basis


def observed_rank(n, d, t):
    a, b = 1, 1 << d
    vec = []
    for _ in range(t):
        vec.extend((a, b))
        a, b = update(a, n), update(b, n)
    return len(pivots(vec))


def codimension(n, d):
    if n % 2:
        return (gcd(n, d) - 1) // 2
    h = gcd(n, 2 * d)
    return h // 2 - (d % h != 0)


def check_ranks():
    comparisons = 0
    for n in range(3, 101):
        for d in range(1, n):
            actual = observed_rank(n, d, n)
            expected = n - codimension(n, d)
            assert actual == expected, (n, d, actual, expected)
            assert (actual == n) == (gcd(n, d) == 1), (n, d)
            comparisons += 1
            if gcd(n, d) == 1:
                for t in range(1, (n + 1) // 2 + 1):
                    assert observed_rank(n, d, t) == min(2 * t, n), (n, d, t)
                    comparisons += 1
    return comparisons


def check_transition_probabilities():
    # Count all fair-noise histories exactly: count of each outcome must be
    # 2^(2*t-n) at the claimed first complete-randomization time.
    tested = 0
    for n in range(3, 9):
        t = (n + 1) // 2
        for d in range(1, n):
            if gcd(n, d) != 1:
                continue
            for x0 in (0, (1 << n) - 1):
                law = {x0: 1}
                for _ in range(t):
                    after = Counter()
                    for x, c in law.items():
                        base = update(x, n)
                        for noise in (0, 1, 1 << d, 1 | (1 << d)):
                            after[base ^ noise] += c
                    law = after
                assert len(law) == 1 << n, (n, d, x0)
                assert set(law.values()) == {1 << (2*t-n)}, (n,d,x0)
                tested += 1
    return tested


def check_symmetric_orbits():
    # Directly enumerate reflection-invariant vectors in the dual space.
    comparisons = 0
    for n in range(3, 13):
        for d in range(1, n):
            cnt = 0
            for v in range(1 << n):
                if v & (1 | (1 << d)):
                    continue
                if any(((v >> j) ^ (v >> ((-j) % n))) & 1 for j in range(n)):
                    continue
                if any(((v >> j) ^ (v >> ((2*d-j) % n))) & 1 for j in range(n)):
                    continue
                cnt += 1
            assert cnt == (1 << codimension(n, d)), (n, d, cnt)
            comparisons += 1
    return comparisons


if __name__ == '__main__':
    a = check_ranks()
    b = check_transition_probabilities()
    c = check_symmetric_orbits()
    print('PASS: rank/time checks', a)
    print('PASS: exact noise-history laws', b)
    print('PASS: dual dihedral orbit counts', c)
