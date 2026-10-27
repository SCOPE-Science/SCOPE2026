#!/usr/bin/env python3
"""Exact finite checks for a complete-bipartite random-walk cover endpoint law.

Uses only Python standard-library rational arithmetic.  These finite checks do
not prove any asymptotic statement; those are established analytically.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, factorial

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def formula(a, b):
    """Independent inclusion-exclusion formula for the opposite-side mass."""
    return sum(((-1)**(i+j))*comb(a,i)*comb(b,j)*Q(i*b, i*b+j*a-i*j)
               for i in range(1,a+1) for j in range(1,b+1))


@lru_cache(None)
def dp(a,b,i,j):
    """First-step Markov recurrence: i newly seen A, j seen B."""
    if i==a-1:
        return Q(1) if j < b else Q(0)
    if j==b:
        return Q(0)
    pa=Q(a-1-i,a)
    pb=Q(b-j,b)
    stationary=(1-pa)*(1-pb)
    ans=Q(0)
    for di in [0,1]:
        for dj in [0,1]:
            if di==dj==0:
                continue
            p=(pa if di else 1-pa)*(pb if dj else 1-pb)
            if di and dj and i+1==a-1 and j+1==b:
                # The B discovery precedes the A discovery in a round.
                q=Q(0)
            else:
                q=dp(a,b,i+di,j+dj)
            ans+=p*q
    return ans/(1-stationary)


def tie_rational(m):
    """Finite expression based on the 2003 Myers-Wilf coupon tie evaluation."""
    if m==1:
        return Q(1)
    c=m-1
    coeff={r:Q((-1)**(c-r)*r**c*comb(c,r),factorial(c)) for r in range(1,c+1)}
    return Q(factorial(m)**2,m**(2*m))*sum(
        coeff[r]*coeff[s]/(1-Q(r*s,m*m))
        for r in range(1,c+1) for s in range(1,c+1))

for a in range(1,9):
    for b in range(1,9):
        left=formula(a,b)
        right=dp(a,b,0,0) if a>=2 else Q(1)
        verify(left==right,f"independent exact methods disagree at ({a},{b}): {left}, {right}")
        verify(0<=left<=1,f"invalid probability at ({a},{b})")

for b in range(1,18):
    target=Q(1)-Q(2,comb(2*b,b))
    verify(formula(2,b)==target,f"two-vertex side formula fails for b={b}")

for m in range(2,12):
    rho=tie_rational(m)
    verify(formula(m,m)==(1+rho)/2,f"balanced collision identity fails for m={m}")
    verify(rho <= Q(1,2*m-1),f"Young convolution bound fails for m={m}")
    verify((rho==Q(1,2*m-1))==(m==2),f"strictness boundary fails at m={m}")
    if m>=3:
        a_v=(1-rho)/Q(2*(m-1))
        b_v=(1+rho)/Q(2*m)
        verify(a_v>b_v,f"balanced per-vertex direction fails at m={m}")

verify(tie_rational(2)==Q(1,3),'m=2 tie')
verify(tie_rational(3)==Q(11,70),'m=3 tie')
verify(tie_rational(4)==Q(9,91),'m=4 tie')
verify(formula(3,3)==Q(81,140),'m=3 last B')
verify(formula(4,4)==Q(50,91),'m=4 last B')
verify(formula(3,4)==Q(133,165),'3,4 check')
print(f"PASS: {checks} exact integer/rational assertions")
for m in (2,3,4,5,6):
    print(f"m={m}: opposite-side endpoint mass={formula(m,m)}, two-collector tie={tie_rational(m)}")
