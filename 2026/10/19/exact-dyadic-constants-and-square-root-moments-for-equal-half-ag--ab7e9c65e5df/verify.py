#!/usr/bin/env python3
"""Certified dyadic intervals for equal-half aggregation-fragmentation moments.
Only standard-library exact integer arithmetic; no stochastic simulation.
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import comb

S = 10**120
STEPS = 150
# Each represented interval is [lo/S, hi/S] with outward integer rounding.
alo = ahi = S//2
plo = phi = S
intervals=[]

def upper_div(a,b):
    return -(-a//b)

for n in range(1, STEPS+1):
    # a_{n} = a_{n-1}(1-a_{n-1})/2; increasing on [0,1/2].
    alo = alo*(S-alo)//(2*S)
    ahi = upper_div(ahi*(S-ahi),2*S)
    assert 0 < alo <= ahi < S//2
    # P_n = prod_{j=1}^n (1-2 a_j).
    plo = plo*(S-2*ahi)//S
    phi = upper_div(phi*(S-2*alo),S)
    assert 0 < plo <= phi <= S
    # n-level dyadic bracket: 2^n a_n (1-2a_n) <= sigma <= 2^n a_n.
    lower_sigma = Fraction(2**n*alo*(S-2*ahi), S*S)
    upper_sigma = Fraction(2**n*ahi,S)
    # tail product from j=n+1; a_{n+1} <= a_n/2, hence sum_{j>=n+1} 2a_j <= 2a_n.
    # A conservative lower bound P >= P_n (1 - 2 a_n) holds.
    lower_P = Fraction(plo*(S-2*ahi), S*S)
    upper_P = Fraction(phi,S)
    assert 0 < lower_P <= upper_P < 1
    intervals.append((n,lower_sigma,upper_sigma,lower_P,upper_P))

# Independently check original n-moment recursion exactly through n=13.
A=[Fraction(0),Fraction(1)]
for n in range(2,14):
    num=sum(comb(n,k)*A[k]*A[n-k] for k in range(1,n))
    # multiply by (1-2^(1-n))^-1
    val=Fraction(num*2**(n-1), 2**(n-1)-1)
    A.append(val)
for n in range(2,14):
    assert Fraction(A[n]*(2**(n-1)-1), 2**(n-1)) == sum(comb(n,k)*A[k]*A[n-k] for k in range(1,n))

with localcontext() as ctx:
    ctx.prec=75
    pi_lo=Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640')
    pi_hi=Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781642')
    print('n | sigma lower | sigma upper | B lower | B upper | interval widths')
    for n in [16,32,64,96,128,150]:
        _, sL,sU,pL,pU = intervals[n-1]
        dec=lambda f:Decimal(f.numerator)/Decimal(f.denominator)
        # pi and product bounds, B = (2 sqrt(pi P))^-1.
        B_lo=1/(2*(pi_hi*dec(pU)).sqrt())
        B_hi=1/(2*(pi_lo*dec(pL)).sqrt())
        print(n,format(dec(sL),'.33f'), format(dec(sU),'.33f'),format(B_lo,'.30f'),format(B_hi,'.30f'), 'widths',format(dec(sU-sL),'.3e'),format(B_hi-B_lo,'.3e'))
    n,sL,sU,pL,pU=intervals[-1]
    assert float(sL) > .1 and float(sU) < .25
    assert float(pL) > 0
    print('moments',A)
    print('sigma rational interval numerator/denominator bit lengths:',sL.numerator.bit_length(),sL.denominator.bit_length(),sU.numerator.bit_length(),sU.denominator.bit_length())
    print('product rational interval numerator/denominator bit lengths:',pL.numerator.bit_length(),pL.denominator.bit_length())
