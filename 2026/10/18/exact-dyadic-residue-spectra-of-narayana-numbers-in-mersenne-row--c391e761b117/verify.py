#!/usr/bin/env python3
"""Exact integer verification for the Mersenne-row Narayana congruence theorem.
No external dependencies; finite checks supplement the unrestricted algebraic proof.
"""
from collections import Counter
from math import comb


def step_factors(s):
    assert s >= 2
    modulus = 1 << s
    blocks = 1 << (s - 1)
    prefix = [1]
    for m in range(1, blocks):
        a = m
        v = 0
        while not a & 1:
            a //= 2
            v += 1
        factor = (1 - (1 << (s - 1 - v)) * pow(a, -1, modulus)) % modulus
        prefix.append(prefix[-1] * factor % modulus)
    return prefix


def predicted(r, s, k, f=None):
    assert r >= s >= 2
    n = (1 << r) - 1
    assert 0 <= k < n
    t = 1 << (r - s + 1)
    if f is None:
        f = step_factors(s)
    if (k + 1) % t == 0:
        m = (k + 1) // t
        assert 1 <= m < (1 << (s - 1))
        return (f[m-1] * f[m]) % (1 << s)
    return pow(f[k // t], 2, 1 << s)


def histogram(r, s, f=None):
    assert r >= s >= 2
    t = 1 << (r - s + 1)
    M = 1 << s
    if f is None:
        f = step_factors(s)
    C = Counter()
    for x in f:
        C[x*x % M] += t - 1
    for x, y in zip(f, f[1:]):
        C[x*y % M] += 1
    return C


def actual_row_residues(r, s):
    n = (1 << r) - 1
    M = 1 << s
    B = 1
    for k in range(n):
        # At step k, B = C(n,k). Compute C(n,k+1) exactly.
        next_B = B * (n-k) // (k+1)
        numerator = B * next_B
        assert numerator % n == 0
        yield numerator // n % M
        B = next_B


def main():
    total_cases = 0
    for r in range(2, 13):
        for s in range(2, min(r, 8) + 1):
            F = step_factors(s)
            direct = list(actual_row_residues(r, s))
            guessed = [predicted(r, s, k, F) for k in range((1 << r) - 1)]
            assert direct == guessed, (r, s, next((k for k in range(len(direct)) if direct[k] != guessed[k]), None))
            assert Counter(direct) == histogram(r, s, F)
            assert sum(histogram(r, s, F).values()) == (1 << r) - 1
            total_cases += len(direct)
    for r in range(4, 13):
        c = histogram(r, 4)
        assert c == Counter({1: (1 << (r-1)) - 2,
                             9: (1 << (r-1)) - 2,
                             13: 2,
                             7: 1}), (r, c)
        n = (1 << r) - 1
        t = 1 << (r - 3)
        assert [predicted(r, 4, m*t-1) for m in range(1, 8)] == [9,13,1,7,1,13,9]
        assert sum(c.values()) == n
    print('VERIFY_OK cases={} rows=2..12 precisions=2..8'.format(total_cases))
    print('MOD16_COUNTS: 1=2^(r-1)-2, 9=2^(r-1)-2, 13=2, 7=1; r>=4')

if __name__ == '__main__':
    main()
