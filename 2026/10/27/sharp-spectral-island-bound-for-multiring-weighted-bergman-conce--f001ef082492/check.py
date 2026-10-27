#!/usr/bin/env python3
"""Numerical consistency checks for annular Bergman concentration spectra.

The infinite-dimensional assertions rely on the analytic proof in RESULT.md;
these tests verify formulas and one explicit sharpness witness.
"""
from fractions import Fraction
from math import gamma
import mpmath as mp

mp.mp.dps = 70
checks = 0

def assert_true(v, description):
    global checks
    assert v, description
    checks += 1

# Formula check by independent numerical quadrature for a nonintegral weight.
for alpha in (mp.mpf('0'), mp.mpf('0.5'), mp.mpf('2.3')):
    for k in range(0,9):
        a,b=mp.mpf('.18'),mp.mpf('.41')
        lam_formula=mp.betainc(k+1,alpha+1,a,b,regularized=True)
        lam_integral=mp.quad(lambda t:t**k*(1-t)**alpha,[a,b])/mp.beta(k+1,alpha+1)
        assert_true(abs(lam_formula-lam_integral)<mp.mpf('1e-52'),
                    f'Incomplete-beta identity alpha={alpha}, k={k}')

# For alpha=0 and rational endpoints, verify exact formulas using Fractions.
for k in range(0,20):
    a,b=Fraction(1,5),Fraction(2,5)
    lam = b**(k+1)-a**(k+1)
    delta = (b**(k+2)-a**(k+2))-lam
    endpt=(1-a)*a**(k+1)-(1-b)*b**(k+1)
    assert_true(delta==endpt,f'exact eigenvalue first difference, k={k}')

# Explicit three-annulus spectral islands at threshold 1/2, alpha=0.
A=mp.mpf('0.1');B=mp.mpf('10')
K=[10_000,100_000_000,1_000_000_000_000]
intervals=[(1-B/mp.mpf(h),1-A/mp.mpf(h)) for h in K]
assert_true(all(0<a<b<1 for a,b in intervals), 'all annuli inside disk')
assert_true(all(intervals[i][1]<intervals[i+1][0] for i in (0,1)),
            'three annuli disjoint and ordered')
def eigenvalue(k):
    s=mp.mpf(k+1)
    return sum(mp.exp(s*mp.log(b))-mp.exp(s*mp.log(a)) for a,b in intervals)
witnesses=[0,K[0]-1,10**6-1,K[1]-1,10**10-1,K[2]-1]
vals=[eigenvalue(k) for k in witnesses]
expected=[False,True,False,True,False,True]
for k,v,high in zip(witnesses,vals,expected):
    assert_true((v>mp.mpf('0.5'))==high,
                f'level .5 witness k={k}, expected high={high}, value={v}')
# Diagonal rank and no extra spectral clusters follow from the proof, not finite sampling.
print('PASS',checks,'checks')
for k,v in zip(witnesses,vals):
    print('k=',k,' concentration=',mp.nstr(v,25))
print('Theorem scope: all alpha>-1, m>=1, thresholds 0<c<1; analytical proof required.')
