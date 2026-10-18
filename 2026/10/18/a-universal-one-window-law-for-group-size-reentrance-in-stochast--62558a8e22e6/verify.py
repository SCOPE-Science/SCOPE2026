#!/usr/bin/env python3
"""Reproduce exact finite checks for a random-geometric public-goods model.

Requires Python 3 standard library only. The analytic argument applies to
arbitrary compactly supported distributions; this program verifies the
specified rational two-atom witness, not that infinite theorem.
"""
from fractions import Fraction as F
from math import comb

R = F(9, 2)
P = F(4, 5)
A = F(11, 10)
B = F(9, 10)

def moment(n):
    assert n >= 1
    return P * A**(n-1) + (1-P) * B**(n-1)

def q(n):
    return R * moment(n) / n

def delta(n):
    return 9*(4*11**(n-1)+9**(n-1)) - n*10**n

def expected_marginal(n, x):
    # The binomial co-player marginal difference, for exact x.
    def avg_for(w):
        return sum(F(comb(n-1, k))*x**k*(1-x)**(n-1-k)*w**k
                   for k in range(n))
    return R / n * (P*avg_for(A)+(1-P)*avg_for(B)) - 1

def closed_marginal(n, x):
    return R/n*(P*(1+(A-1)*x)**(n-1)
                +(1-P)*(1+(B-1)*x)**(n-1)) - 1

# Every sampled phase sign agrees with the theorem, including endpoints.
assert all(delta(n)>0 for n in (5, 6))
assert all(delta(n)<0 for n in (7, 17))
assert delta(18)>0
assert [delta(n) for n in (5, 6, 7, 17, 18)] == [
     86125, 329277, -1440835, -29132543211735635,
     346187661271574877]
for n in range(5, 151):
    assert (q(n)>1) == (n in (5, 6) or n >= 18)

# Rational exact-ratio log convexity for 3 <= n <= 80.
for n in range(3, 81):
    assert q(n)**2 < q(n-1)*q(n+1)
    assert moment(n-1)*moment(n+1)-moment(n)**2 == (
        P*(1-P)*(A-B)**2*(A*B)**(n-2))

# Exact binomial-to-moment reduction at many group sizes and fractions.
xs=[F(0),F(1,11),F(1,3),F(1,2),F(3,4),F(1)]
for n in range(2, 18):
    for x in xs:
        assert expected_marginal(n,x)==closed_marginal(n,x)

# All interior signs in the disappearance gap are negative, independent of
# the particular initial frequency; these are sample checks only.
for n in range(7,18):
    for x in xs:
        if x < 1:
            assert closed_marginal(n,x)<0

print('PASS: integer witness, strict sampled log convexity, moment identity,')
print('      and binomial payoff reduction (all exact Fraction arithmetic).')
print('Exact phase boundaries: 5,6 | 7..17 | 18 and above.')
