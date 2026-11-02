#!/usr/bin/env python3
"""Finite independent integer diagnostics for characteristic-two pole semigroups.

The verification samples are not an infinite proof. All calculations use integers.
"""
from math import gcd


def generated_semigroup(generators, limit):
    membership = [False] * (limit + 1)
    membership[0] = True
    for h in range(1, limit + 1):
        membership[h] = any(h >= d and membership[h-d] for d in generators)
    return membership


def apery(membership, modulus):
    out = [None] * modulus
    for h, ok in enumerate(membership):
        if ok and out[h % modulus] is None:
            out[h % modulus] = h
    assert all(v is not None for v in out)
    return out


def ceil_div(a, b):
    return -((-a) // b)


def F(g, b):
    return max(0, ceil_div(g-b, 4))


def test_pair(M, D):
    assert M % 2 and D % 2 and M >= 5 and M//2 < D < M
    genus = 3 * (M - 1) // 2
    C = 3 * M - 2 * D
    assert 4 * D > 2 * M and C > D
    for lam_nonzero, generators, expected_apery, expected_a in [
        (False, (4, M), (0, M, 2*M, 3*M), F(genus, 0)+F(genus, M)),
        (True, (4, 2*D, C), (0, 2*D, C, 3*M),
         F(genus, 0)+F(genus, 2*D)+F(genus, C))
    ]:
        mem = generated_semigroup(generators, 4*genus+4*M)
        assert set(apery(mem, 4)) == set(expected_apery)
        assert sum(not mem[t] for t in range(2*genus)) == genus
        assert sum(mem[t] for t in range(genus)) == expected_a


for M in range(5, 106, 2):
    for D in range((M // 2)+1, M):
        if D % 2:
            test_pair(M, D)

for s in range(81):
    M, D = 8*s+5, 6*s+3
    genus = 12*s+6
    assert 2*D == genus and 3*M-2*D == genus+3
    assert F(genus, 0)+F(genus, M) == 4*s+3
    assert F(genus, 0)+F(genus, 2*D)+F(genus, 3*M-2*D) == 3*s+2
    assert (4*s+3)-(3*s+2) == s+1

print('VERIFY_OK')
