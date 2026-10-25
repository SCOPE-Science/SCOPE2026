"""Reproducibility checks for q-ary double-deletion ball fluctuations.

Uses only Python's standard library. Independent descendant enumeration is
compared against local collision identities and rational moment formulas.
"""
from itertools import product, combinations
from fractions import Fraction
from math import comb
from collections import Counter


def volume_direct(x):
    n = len(x)
    return len({tuple(x[i] for i in range(n) if i not in pair)
                for pair in combinations(range(n), 2)})


def local_statistics(x):
    n = len(x)
    k = sum(x[i] != x[i + 1] for i in range(n - 1))
    j = sum(x[i] == x[i + 2] for i in range(n - 2))
    return k, j


def volume_local(x):
    k, j = local_statistics(x)
    return comb(k, 2) + len(x) - 1 - j


def predicted_moments(q, n):
    m = n - 1
    p = Fraction(q - 1, q)
    avg = comb(m, 2) * p**2 + m - Fraction(m-1, q)
    variance = (comb(m, 2)*p**2*(1-p**2)
                + 6*comb(m, 3)*p**3*(1-p)
                + (m-1)*p*Fraction(q-2, q*q))
    return avg, variance


tested = 0
for q, maximum_n in ((2, 11), (3, 8), (4, 7), (5, 5)):
    for n in range(2, maximum_n + 1):
        volumes = []
        full = 0
        for x in product(range(q), repeat=n):
            b = volume_direct(x)
            assert b == volume_local(x), (q, n, x, b, volume_local(x))
            volumes.append(b)
            full += (b == comb(n, 2))
        count = len(volumes)
        mu = Fraction(sum(volumes), count)
        var = Fraction(sum(v*v for v in volumes), count) - mu**2
        pmu, pvar = predicted_moments(q, n)
        assert (mu, var) == (pmu, pvar), (q, n, mu, var, pmu, pvar)
        if n >= 3:
            expected = q*(q-1)*(q-2)**(n-2)
            assert full == expected, (q, n, full, expected)
        tested += count
        print('checked', q, n, count, 'mean', mu, 'variance', var)
print('TOTAL_WORDS', tested)
print('VERIFY_OK')
