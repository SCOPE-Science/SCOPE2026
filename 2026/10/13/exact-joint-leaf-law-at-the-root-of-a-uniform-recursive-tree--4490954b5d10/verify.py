#!/usr/bin/env python3
"""Exact-rational finite checks for the root-singleton/global-leaf law.

Usage: python3 verify.py
No external packages are required. Exhaustive finite checks supplement,
but cannot substitute for, the general combinatorial argument.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial


def eulerian(m):
    """Coefficients by descents, independently from the tree enumeration."""
    row = [1]
    for size in range(1, m + 1):
        new = [0] * size
        for d in range(size):
            if d < len(row):
                new[d] += (d + 1) * row[d]
            if d > 0:
                new[d] += (size - d) * row[d - 1]
        row = new
    return row


def predicted_counts(n):
    """Integer coefficients of (n-1)! E[u^Q z^L]."""
    data = Counter()
    for k in range(n):
        if k == n - 1:
            weights = [(n - 1, 1)]
            prefactor = 1
        else:
            weights = [(k + 1 + d, a) for d, a in enumerate(eulerian(n - k - 1))]
            prefactor = comb(n - 1, k)
        for q in range(k + 1):
            base = prefactor * comb(k, q) * (-1) ** (k - q)
            for leaves, coeff in weights:
                data[q, leaves] += base * coeff
    return +data


def count_trees(n):
    stats = Counter()
    for ancestors in product(*(range(j) for j in range(1, n))):
        counts = [0] * n
        for par in ancestors:
            counts[par] += 1
        q = sum(counts[v] == 0 and ancestors[v - 1] == 0 for v in range(1, n))
        leaves = sum(c == 0 for c in counts)
        stats[q, leaves] += 1
    return stats


def falling(q, k):
    value = 1
    for j in range(k):
        value *= q - j
    return value


def verify(n):
    stats = count_trees(n)
    assert sum(stats.values()) == factorial(n - 1)
    prediction = predicted_counts(n)
    assert stats == prediction, (n, stats, prediction)
    assert sum(prediction.values()) == factorial(n - 1)
    for k in range(0, n):
        lhs = Counter()
        for (q, ell), multiplicity in stats.items():
            lhs[ell] += multiplicity * falling(q, k)
        rhs = Counter()
        if k == n - 1:
            rhs[n - 1] = factorial(n - 1)
        else:
            ratio = factorial(n - 1) // factorial(n - k - 1)
            for d, coefficient in enumerate(eulerian(n - k - 1)):
                rhs[k + 1 + d] = ratio * coefficient
        assert +lhs == +rhs, (n, k, lhs, rhs)
    if n >= 3:
        total = factorial(n - 1)
        eq = Fraction(sum(q * v for (q, ell), v in stats.items()), total)
        el = Fraction(sum(ell * v for (q, ell), v in stats.items()), total)
        eql = Fraction(sum(q * ell * v for (q, ell), v in stats.items()), total)
        e2l = Fraction(sum(ell * ell * v for (q, ell), v in stats.items()), total)
        assert eq == 1 and el == Fraction(n, 2)
        assert eql - eq * el == Fraction(1, 2)
        assert e2l - el * el == Fraction(n, 12)
    return sum(stats.values())


if __name__ == "__main__":
    totals = [verify(n) for n in range(2, 10)]
    assert sum(totals) == 46233, sum(totals)
    print("VERIFY_OK: exact bivariate coefficients and factorial transforms through n=9")
    print("Counts by n=2,...,9:", totals)
    print("COV_OK: Cov(Q,L)=1/2, Var(L)=n/12 for n=3,...,9")
