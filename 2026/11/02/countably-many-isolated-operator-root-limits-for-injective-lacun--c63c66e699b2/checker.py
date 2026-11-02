#!/usr/bin/env python3
"""Finite exact consistency checks for lacunary bilateral weighted shifts.

The proof of the infinite-dimensional statement is analytic. The checker
verifies exact exponent sums and finite-window identities only.
"""
from fractions import Fraction

checks = 0

def check(condition):
    global checks
    assert condition
    checks += 1

def prefix(q, n):
    if n < 1:
        return 0
    p = 1
    total = 0
    while p <= n:
        total += p
        p *= q
    return total

def window(q, k, n):
    p, total = 1, 0
    while p <= k + n - 1:
        if p >= k:
            total += p
        p *= q
    return total

for q in range(2, 7):
    for j in range(7, 11):
        Q = q ** j
        for s in range(-8, 9):
            n = Q - s
            for k in range(-8, 9):
                observed = window(q, k, n)
                exact = prefix(q, n+k-1)-prefix(q, k-1)
                check(observed == exact)
                target = (q if k > s else 1)
                # An exact finite-size correction to the limiting exponent.
                formula = (q ** (j+1)-1)//(q-1) if k > s else (q**j-1)//(q-1)
                formula -= prefix(q, k-1)
                check(observed == formula)
                lhs = Fraction(observed, n) - Fraction(target, q-1)
                rhs = Fraction(target * s - 1, (q-1)*n) - Fraction(prefix(q,k-1),n)
                check(lhs == rhs)

for q in range(2,7):
    for j in range(4,11):
        Q=q**j
        for r in range(1,10):
            # Interior scalar locations indexed by rational u in (1,q).
            u=Fraction(q+r* (q-1), q+r)  # strictly between 1 and q
            n=(u.numerator*Q)//u.denominator
            if n < Q or n >= q*Q:continue
            for k in (-3, 0, 1, 3):
                check(window(q,k,n) == prefix(q,n+k-1)-prefix(q,k-1))
print('FINITE_ASSERTIONS_PASSED', checks)
