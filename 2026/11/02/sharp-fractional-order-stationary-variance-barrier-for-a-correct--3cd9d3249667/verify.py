#!/usr/bin/env python3
"""Numerical cross-checks for the fractional OU stationary-variance formula.

Dependency: Python 3 and mpmath (pip install mpmath).
These finite checks are not proofs of the universal asymptotic statements.
"""
from fractions import Fraction
import mpmath as mp

mp.mp.dps = 75
checks = 0

def check(ok, label):
    global checks
    if not ok:
        raise AssertionError(label)
    checks += 1

def fgn_cov(H, k):
    if k == 0:
        return mp.mpf(1)
    return ((k+1)**(2*H)-2*k**(2*H)+(k-1)**(2*H))/2

def rational_factors(x,theta):
    A=1+theta*x
    B=1-(1-theta)*x
    return A,B,A+B,B/A

def var_ratio(H,x,theta):
    A,B,C,r=rational_factors(x,theta)
    assert 0 < r < 1
    return 2*x**(2*H+1)*mp.polylog(-2*H,r)/(mp.gamma(2*H+1)*A*B*C)

# Independent finite covariance sum is compared with the closed polylog formula.
for H in (mp.mpf('0.53'),mp.mpf('0.67'),mp.mpf('0.82'),mp.mpf('0.94')):
    for x in (mp.mpf('.3'),mp.mpf('.7'),mp.mpf('1.0')):
        for theta in (mp.mpf('.5'), mp.mpf('1'),mp.mpf('.5')+x/12):
            A,B,C,r=rational_factors(x,theta)
            if not 0<r<1: continue
            finite=1+2*sum(fgn_cov(H,k)*r**k for k in range(1,850))
            closed=(1-r)**2/r*mp.polylog(-2*H,r)
            check(abs(finite-closed)<mp.mpf('1e-38'), 'fractional covariance generating function')
            v1=x**(2*H)*(finite/A**2)/(1-r*r)
            v2=x**(2*H+1)*mp.polylog(-2*H,r)/(A*B*C)
            check(abs(v1-v2)<mp.mpf('1e-38'),'stationary variance via two expressions')

# Exactly rational amplification is positive and smaller than one for all tested x.
for k in range(1,301):
    x=Fraction(k,13)
    theta=Fraction(1,2)+x/12
    A,B,C,r=rational_factors(x,theta)
    check(0<r<1,'all-step stable corrected Padé amplification')
    check(r == (1-x/2+x*x/12)/(1+x/2+x*x/12),'Padé rational identity')

# Fractional noninteger leading coefficient convergence, checked with finer steps.
for H in (mp.mpf('.55'),mp.mpf('.7'),mp.mpf('.85'),mp.mpf('.95')):
    coefficient=mp.zeta(-2*H)/mp.gamma(2*H+1)
    check(coefficient<0,'negative fractional constant')
    errs=[]
    for x in (mp.mpf('.08'),mp.mpf('.04'),mp.mpf('.02'),mp.mpf('.01')):
        v=var_ratio(H,x,mp.mpf('.5')+x/12)
        errs.append(abs((v-1)/x**(2*H+1)-coefficient))
    check(all(errs[k+1]<errs[k] for k in range(3)),'sharp fractional coefficient convergence')
    check(errs[-1]<mp.mpf('.008'),'fractional coefficient within asymptotic tolerance')

# Distinguish theta-family x^2 coefficient, retaining x^(2H+1) separately.
for H in (mp.mpf('.63'),mp.mpf('.77'),mp.mpf('.92')):
    z=mp.zeta(-2*H)/mp.gamma(2*H+1)
    for c in (mp.mpf('-0.1'),mp.mpf('0'),mp.mpf('0.0833333333333333333333333333'),mp.mpf('.19')):
        xs=(mp.mpf('.07'),mp.mpf('.035'),mp.mpf('.0175'))
        vals=[]
        for x in xs:
            t=mp.mpf('.5')+c*x
            vals.append((var_ratio(H,x,t)-1-z*x**(2*H+1))/x*x**(-1))
        target=(1-H)*(mp.mpf(1)/6-2*c)
        check(abs(vals[-1]-target)<abs(vals[0]-target)+mp.mpf('1e-20'),'theta x^2 coefficient convergence')

# Continuous stationary OU variance is derived analytically; no Monte Carlo test.
print('VERIFY_OK',checks)
