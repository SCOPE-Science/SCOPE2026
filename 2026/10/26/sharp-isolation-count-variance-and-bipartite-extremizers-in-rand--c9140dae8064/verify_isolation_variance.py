#!/usr/bin/env python3
"""Exact arithmetic checks for pairwise-isolation formulas in weighted random subgraphs.

This verifies finite instances independently of the general analytic proof.
"""
from fractions import Fraction
from itertools import permutations
from math import comb

def independent_pair_probability(d, t):
    # Two nonadjacent vertices, t shared neighbors. All variables are iid
    # continuous; ranks exhaust their joint orderings.
    m = 2 + 2 * d - t
    wins = 0
    for p in permutations(range(m)):
        a, b = p[0], p[1]
        both = True
        for j in range(2, 2+d-t):
            both &= p[j] < a
        for j in range(2+d-t, 2+2*(d-t)):
            both &= p[j] < b
        for j in range(2+2*(d-t), m):
            both &= p[j] < a and p[j] < b
        wins += bool(both)
    from math import factorial
    return Fraction(wins, factorial(m))

def adjacent_integral(d):
    # Evaluate the triangular integral via an exact binomial expansion.
    # Integrate x^(d-1) * (1-(1-x)^d) / d from zero to one.
    return Fraction(1, d*d) - sum(
        (Fraction((-1)**j * comb(d, j), d*(d+j))
         for j in range(d+1)), Fraction(0))

checks = 0
for d in range(1, 4):
    for t in range(d+1):
        observed = independent_pair_probability(d,t)
        asserted = Fraction(2, (d+1)*(2*d-t+2))
        assert observed == asserted, (d,t,observed,asserted)
        checks += 1
for d in range(1, 30):
    j = adjacent_integral(d)
    formula = Fraction(1, d*d) * (1-Fraction(1, comb(2*d,d)))
    assert j == formula, (d,j,formula)
    r = Fraction((2*d+1)*(d*d+d+2), d*(d+1)*(d+2)) - Fraction(d+1, d*comb(2*d,d))
    direct = (Fraction(d,d+1) + d*(d+1)*(j-Fraction(1,(d+1)**2))
              + Fraction(d*(d-1), (d+1)*(d+2)))
    assert r == direct and Fraction(0)<r<Fraction(2)
    checks += 3
# Verify equality of all ordered pair moment contributions for K_(d,d).
for d in range(1,30):
    n=2*d
    j=Fraction(1,d*d)*(1-Fraction(1,comb(2*d,d)))
    pairjoint=Fraction(2,(d+1)*(d+2))
    var = (n*Fraction(d,(d+1)**2)
           +n*d*(j-Fraction(1,(d+1)**2))
           +n*(d-1)*(pairjoint-Fraction(1,(d+1)**2)))
    r = Fraction((2*d+1)*(d*d+d+2),d*(d+1)*(d+2))-Fraction(d+1,d*comb(2*d,d))
    assert var == Fraction(n,d+1)*r
    checks += 1
print('VERIFY_OK',checks,'exact independent-rank, integral, and variance comparisons')
