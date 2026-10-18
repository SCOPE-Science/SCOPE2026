#!/usr/bin/env python3
"""Exact finite checks for the published residue-fibre theorem.

This code checks finitely many cases; the accompanying proof covers all k.
"""
from collections import Counter


def derangements_mod(m, limit):
    a = 1
    out = [a]
    for n in range(1, limit):
        a = (n * a + (-1 if n & 1 else 1)) % m
        out.append(a)
    return out


def v2(z):
    assert z
    return (abs(z) & -abs(z)).bit_length() - 1


def derivative_mod(n, modulus=8, terms=28):
    p, dp = 1, 0
    total = 0
    for j in range(terms):
        if j:
            dp = (dp * (n - j + 1) + p) % modulus
            p = p * (n - j + 1) % modulus
        total = (total + ((-1) ** j) * dp) % modulus
    return total


def main():
    fibre_cases = 0
    for k in range(3, 13):
        m = 1 << k
        counts = Counter(derangements_mod(m, m))
        expected = Counter({a: (1 if a % 2 == 0 else 4)
                            for a in range(m) if a % 2 == 0 or a % 8 == 1})
        assert counts == expected, (k, counts, expected)
        assert sum(counts.values()) == m
        assert len(counts) == 5 * (1 << (k - 3))
        fibre_cases += m

    for n in range(64):
        d = derivative_mod(n)
        assert (d % 2 == 1) if n % 2 else (d % 4 == 2), (n, d)

    # Exact integer counts for moderately small arguments provide independent
    # checks of the local valuation identities within their stated domains.
    f = [1]
    for n in range(1, 80):
        f.append(1 - n * f[-1])
    pairs = 0
    for i in range(80):
        for j in range(i + 1, 80):
            if i & 1 and j & 1:
                assert v2(f[i] - f[j]) == v2(j - i), (i, j)
                pairs += 1
            if (i - j) % 4 == 0 and i % 2 == 0:
                assert v2(f[i] - f[j]) == v2(j - i) + 1, (i, j)
                pairs += 1
    print(f"VERIFY_OK: {fibre_cases} residues counted; 64 derivative checks; {pairs} local-distance pairs")


if __name__ == '__main__':
    main()
