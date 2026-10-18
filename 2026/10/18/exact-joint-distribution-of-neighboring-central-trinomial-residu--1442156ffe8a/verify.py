#!/usr/bin/env python3
"""Exact finite checks for the central-trinomial residue-pair theorem.

All checks use Python's standard library and exact integer/rational arithmetic.
"""
from collections import Counter
from fractions import Fraction
from math import comb

W = (1, 1, 3, 2, 4)
A = {1: 1, 2: 2, 3: 1, 4: 3}
B = {1: 2, 2: 4, 3: 3, 4: 4}


def digit_product(n):
    z = 1
    while n:
        z = z * W[n % 5] % 5
        n //= 5
    return z


def count_formula(L, u, v):
    r = v * pow(u, -1, 5) % 5
    e, o = (L + 1) // 2, L // 2
    baseline_numerator = 5**L - 1 - 4 * L
    assert baseline_numerator % 16 == 0
    baseline = baseline_numerator // 16
    return (baseline + e * (u == A[r]) + o * (u == B[r])
            + (u == ((-1) ** L) % 5 and v == 1))


def trinomial_binomial(n):
    return sum(comb(n, 2*j) * comb(2*j, j) for j in range(n//2 + 1))


def independent_trinomial_recurrence(N):
    t = [1, 1]
    for n in range(1, N):
        num = (2*n+1)*t[-1] + 3*n*t[-2]
        assert num % (n+1) == 0
        t.append(num // (n+1))
    return t


def verify():
    # The intrinsic arithmetic recurrence is independent of digit factorization.
    t = independent_trinomial_recurrence(260)
    for n in range(261):
        assert t[n] == trinomial_binomial(n), ('integer recurrence', n)
        assert t[n] % 5 == digit_product(n), ('Lucas factorization', n)
    assert Counter(W) == Counter({1: 2, 2: 1, 3: 1, 4: 1})
    # Independent exhaustive enumeration of every adjacent residue pair.
    for L in range(8):
        q = 5**L
        counts = Counter((digit_product(n), digit_product(n+1))
                         for n in range(q))
        assert sum(counts.values()) == q
        for u in range(1, 5):
            for v in range(1, 5):
                assert counts[u, v] == count_formula(L, u, v), (L, u, v)
        tv = Fraction(sum(abs(16*counts[u,v]-q)
                          for u in range(1, 5)
                          for v in range(1, 5)), 32*q)
        expected = (Fraction(15, 16) if L == 0 else
                    Fraction(11, 16) if L == 1 else
                    Fraction(4*L+1, 2*q))
        assert tv == expected, ('TV', L, tv, expected)
        if L >= 2:
            assert all(counts[u, v] > 0 for u in range(1, 5)
                       for v in range(1, 5))
    # Check the carry classes and their lookup arrays exactly.
    for parity, tab in [(0, A), (1, B)]:
        r_list = []
        for d in range(4):
            g = ((-1)**parity * W[d]) % 5
            r = W[d+1] * pow(g, -1, 5) % 5
            assert tab[r] == g
            r_list.append(r)
        assert sorted(r_list) == [1, 2, 3, 4]
    print('VERIFY_OK: integer recurrence, digit product, all 16 pair counts L=0..7, exact TV, carry classes')


if __name__ == '__main__':
    verify()
