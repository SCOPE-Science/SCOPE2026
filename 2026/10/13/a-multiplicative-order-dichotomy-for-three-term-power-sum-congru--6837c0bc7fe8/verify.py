#!/usr/bin/env python3
"""Finite consistency checks for the multiplicative-order zero-sum dichotomy.

These computations do not replace the proof for unbounded n or q.
"""
from math import gcd
from sympy import symbols, cyclotomic_poly, resultant, n_order

X = symbols('X')

nonmultiple_orders = (1, 2, 4, 5, 7, 8, 10, 11)
resultants_tested = 0
for n in nonmultiple_orders:
    for a in range(n):
        for b in range(a, n):
            poly = 1 + X**a + X**b
            r = abs(int(resultant(X**n - 1, poly, X)))
            assert 0 < r <= 3**n, (n, a, b, r)
            resultants_tested += 1

construction_cases = 0
for n in (3, 6, 9, 12, 15, 18, 21, 24):
    for q in (2, 3, 4, 5, 7, 10, 13):
        if n % 2 == 0 and q % 3 != 1:
            continue
        c = int(cyclotomic_poly(n, X).subs(X, q))
        e = c if n % 2 else 3*c
        assert e > 1 and gcd(q, e) == 1
        assert int(n_order(q, e)) == n, (n, q, e)
        assert (1 + pow(q, n//3, e) + pow(q, 2*n//3, e)) % e == 0
        assert all((1+pow(q, k, e))%e != 0 for k in range(n))
        construction_cases += 1

# Exhaustive modulo e for all pairs (e, q mod e) with e <= 120.
# Only the bound and the sharp dichotomy's finite-side necessity are tested.
residue_pairs_checked = 0
triples_checked = 0
for e in range(2, 121):
    for q in range(1, e):
        if gcd(q, e) != 1:
            continue
        residue_pairs_checked += 1
        powers = [1]
        a = q % e
        while a != 1:
            powers.append(a)
            a = (a * q) % e
        n = len(powers)
        has3 = any((-1-x) % e in powers for x in powers)
        has2 = (-1) % e in powers
        if has3 and not has2 and e != 1:
            triples_checked += 1
            assert n % 3 == 0 or e <= 3**n, (e, q, n)
print('VERIFY_OK')
print('resultant_pairs_checked=',resultants_tested)
print('cyclotomic_construction_cases_checked=',construction_cases)
print('residue_pairs_checked=',residue_pairs_checked)
print('minimal_three_cases_in_small_census=',triples_checked)
print('non_exhaustive_infinite_check=True')
