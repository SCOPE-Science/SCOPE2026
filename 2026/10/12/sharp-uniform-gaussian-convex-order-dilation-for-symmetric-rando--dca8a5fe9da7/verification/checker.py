#!/usr/bin/env python3
"""Exact rational certificate for finite Gaussian quantile cut comparisons.
Uses Machin's arctangent identity and Taylor inequalities, no floating-point trust.
"""
from fractions import Fraction as F
from math import factorial

def atan_partial(x,k):
    return sum(((-1)**i*x**(2*i+1)/F(2*i+1) for i in range(k+1)),F(0))
# alternating expansions: even k upper and odd k lower for positive x.
a5lo,a5hi=atan_partial(F(1,5),11),atan_partial(F(1,5),10)
a239lo,a239hi=atan_partial(F(1,239),3),atan_partial(F(1,239),2)
pi_lo=16*a5lo-4*a239hi
pi_hi=16*a5hi-4*a239lo
assert F(314159,100000)<pi_lo<pi_hi<F(314160,100000)
slo,shi=F(25066,10000),F(25067,10000)
assert slo*slo < 2*pi_lo and shi*shi > 2*pi_hi

def exp_taylor(x,k):
    return sum(((-x)**i/F(factorial(i)) for i in range(k+1)),F(0))
def lower_exp(x):return exp_taylor(x,15)
def upper_exp(x):return exp_taylor(x,14)
def gauss_integral(z,k):
    return sum(((-1)**i*z**(2*i+1)/F((2*i+1)*2**i*factorial(i)) for i in range(k+1)),F(0))
def assert_lower_I(p,z,A_upper):
    # Lower bound on Gaussian integral certifies the true |normal quantile| < z.
    assert gauss_integral(z,15) > shi*(F(1,2)-p), (p,'quantile bracket')
    lower_I=lower_exp(z*z/2)/shi
    c3lo=F(10853,10000)
    assert lower_I> A_upper/c3lo, (p,'profile inequality',float(lower_I),float(A_upper/c3lo))
    return float(lower_I)

# Sharp 3-step comparison: upper binomial cut p=1/8, plus p=1/2 equality.
assert_lower_I(F(1,8),F(117,100),F(1733,1000)/8)
# Four-step: positive upper-binomial cuts 1/16 and 5/16.
assert_lower_I(F(1,16),F(156,100),F(1,8))
assert_lower_I(F(5,16),F(1,2),F(3,8))
# Five-step: positive upper cuts 1/32, 3/16; central equality cut checked algebraically.
assert_lower_I(F(1,32),F(19,10),F(2237,1000)/32)
assert_lower_I(F(3,16),F(91,100),F(2237,1000)/8)
# c_5(center)< c_3 since 15/(4 sqrt(15)) = sqrt(15)/4 <1.
assert 15<16
# c3 bounds from 3 pi / 8; c3=sqrt(6*pi)/4.
assert F(10853,10000)**2 < 3*pi_lo/8
assert F(10855,10000)**2 > 3*pi_hi/8
# c2 >= c3: true normal quartile quantile > .64; hence I(1/4) less than phi(.64).
z=F(64,100)
assert gauss_integral(z,14)< slo*F(1,4)
upper_I=upper_exp(z*z/2)/slo
# The two-step upper-tail first moment is sqrt2/4 > 1.4142/4.
assert F(14142,10000)**2 <2
assert upper_I < (F(14142,10000)/4)/F(10855,10000)
# The other two-step cut p=1/2 has ratio sqrt(pi)/2 < c2, certified via c2 > c3 >sqrt(pi)/2.
assert F(10853,10000)**2>pi_hi/4
# Internal finite laws and upper-tail integrated quantiles.
from math import comb
for n in (2,3,4,5):
    mass=sum((F(comb(n,j),2**n) for j in range(n+1)), F(0))
    assert mass==1
    # Upper-tail first-moment identity in unnormalised units: sum_{j<=k}(n-2j) C(n,j) = n C(n-1,k)
    for k in range(n):
        lhs=sum((F((n-2*j)*comb(n,j)) for j in range(k+1)),F(0))
        rhs=F(n*comb(n-1,k))
        assert lhs==rhs
print('PASS: pi, Gaussian quantile brackets, 2/3/4/5-step tail cuts, c2>c3, combinatorial identities')
