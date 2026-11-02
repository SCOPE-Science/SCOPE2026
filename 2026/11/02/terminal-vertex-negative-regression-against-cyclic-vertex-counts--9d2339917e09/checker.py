#!/usr/bin/env python3
"""Exact finite checks of cyclic-vertex/terminal-vertex identities.

Run with: python3 checker.py
Uses only the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, sqrt, pi, e


def falling(x, s):
    v = 1
    for j in range(s):
        v *= x - j
    return v


def cyclic_count(mapping):
    n = len(mapping)
    # Explicitly identify all vertices on cycles, independently of counting formulas.
    cyclic = set()
    for root in range(n):
        visited = {}
        cur = root
        while cur not in visited:
            visited[cur] = len(visited)
            cur = mapping[cur]
        if cur == root:
            cyclic.add(root)
    return len(cyclic)


def terminals(mapping):
    return len(mapping) - len(set(mapping))


def occupancy_law(n, m):
    if m == 0:
        return {0: Fraction(1)}
    ct = Counter()
    for vals in product(range(n), repeat=m - 1):
        ct[sum(j not in vals for j in range(m))] += 1
    return {ell: Fraction(ct[ell], n ** (m - 1)) for ell in ct}


def conditional_law(n, m):
    if m == 0:
        return {0: Fraction(1)}
    out = {}
    for ell in range(m + 1):
        total = sum((-1) ** j * comb(m - ell, j)
                    * Fraction(n - ell - j, n) ** (m - 1)
                    for j in range(m - ell + 1))
        out[ell] = comb(m, ell) * total
    return out


def c_pmf(n, k):
    if k < 1 or k > n:
        return Fraction(0)
    return Fraction(k * falling(n, k), n ** (k + 1))


def mean_c(n):
    if n <= 0:
        return Fraction(0)
    return sum((Fraction(falling(n, j), n ** j)
                for j in range(1, n + 1)), Fraction(0))


assertions = 0
mapping_count = 0
for n in range(1, 7):
    table = Counter()
    for f in product(range(n), repeat=n):
        table[(cyclic_count(f), terminals(f))] += 1
        mapping_count += 1
    total = n ** n
    marginal = Counter()
    for (k, ell), v in table.items():
        marginal[k] += v
    for k in range(1, n + 1):
        pk = Fraction(marginal[k], total)
        assert pk == c_pmf(n, k)
        assertions += 1
        m = n - k
        law = conditional_law(n, m)
        independent_occupancy = occupancy_law(n, m)
        for ell in range(m + 1):
            expected = Fraction(table[(k, ell)], marginal[k])
            assert expected == law.get(ell, 0) == independent_occupancy.get(ell, 0)
            assertions += 1
        for s in range(m + 1):
            exact = sum(Fraction(table[(k, ell)], marginal[k]) * falling(ell, s)
                        for ell in range(m + 1))
            if m == 0:
                target = Fraction(int(s == 0))
            else:
                target = falling(m, s) * Fraction(n - s, n) ** (m - 1)
            assert exact == target
            assertions += 1
    if n >= 2:
        el = Fraction(n - 1, n) ** n * n
        ec = mean_c(n)
        ecl = sum(Fraction(k * ell * ct, total) for (k, ell), ct in table.items())
        cov = ecl - el * ec
        target = el * (mean_c(n - 1) - ec)
        assert cov == target < 0
        assertions += 1
        for j in range(2, n + 1):
            mixed = sum(Fraction(ell * ct, total) for (k, ell), ct in table.items() if k >= j)
            tail = Fraction(falling(n, j), n ** j)
            smaller_tail = Fraction(falling(n - 1, j), (n - 1) ** j) if j <= n-1 else Fraction(0)
            assert mixed - el * tail == el * (smaller_tail - tail) < 0
            assertions += 1
        for m in range(n - 1):
            pm = conditional_law(n, m)
            pn = conditional_law(n, m + 1)
            for cutoff in range(n + 1):
                assert sum(pn.get(i, 0) for i in range(cutoff, n + 1)) >= sum(
                    pm.get(i, 0) for i in range(cutoff, n + 1))
                assertions += 1

# A numerical check of the scaling constant, not a substitute for the proof.
for n in (500, 2000, 10000):
    prev = 1.0
    ec_n = 0.0
    for j in range(1, n + 1):
        prev *= (n - j + 1) / n
        ec_n += prev
    prev = 1.0
    ec_old = 0.0
    for j in range(1, n):
        prev *= (n - j) / (n - 1)
        ec_old += prev
    covariance = n * (1 - 1 / n) ** n * (ec_old - ec_n)
    target = -sqrt(pi / 8) / e
    assert abs(covariance / sqrt(n) - target) < 0.0003
    assertions += 1

print('PASS: %d exact/numerical assertions, %d mappings exhaustively enumerated' %
      (assertions, mapping_count))
