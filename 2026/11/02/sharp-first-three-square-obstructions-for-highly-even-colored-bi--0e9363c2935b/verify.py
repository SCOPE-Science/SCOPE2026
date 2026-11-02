#!/usr/bin/env python3
"""Exact rational certificate for the initial three-square obstructions."""
from fractions import Fraction
from math import comb

def v2(a):
    if a == 0:
        raise ValueError('valuation of zero')
    if isinstance(a, Fraction):
        return v2(a.numerator)-v2(a.denominator)
    return (abs(a) & -abs(a)).bit_length()-1

def coeff_polynomials(limit=14):
    # exp(M*sum_{j>=1} ((2^{v2(j)+1}-1)/j)*X^j)
    p=[[Fraction(1)]]
    for n in range(1,limit+1):
        z=[Fraction(0)]*(n+1)
        for j in range(1,n+1):
            weight=2**(v2(j)+1)-1
            for deg,c in enumerate(p[n-j]):
                z[deg+1] += Fraction(weight,n)*c
        p.append(z)
    return p

def integer_coeffs(m,lim):
    z=[1]+[0]*lim
    for n in range(1,lim+1):
        weighted=sum((2**(v2(j)+1)-1)*z[n-j] for j in range(1,n+1))
        assert weighted*m%n==0
        z[n]=weighted*m//n
    return z

def three_square_obstruction(x):
    while x%4==0 and x>0:
        x//=4
    return x%8==7

def first(m,lim):
    z=integer_coeffs(m,lim)
    return next((i for i,x in enumerate(z) if three_square_obstruction(x)),None)

def direct_product(m,limit):
    """Expand colored-part product without logarithms or recurrences."""
    z=[1]+[0]*limit
    part=1
    while part<=limit:
        for _ in range(m):
            for n in range(part,limit+1):
                z[n]+=z[n-part]
        part*=2
    return z

def verify():
    p=coeff_polynomials(14)
    margins=[]
    for n in range(1,15):
        assert p[n][0]==0
        assert p[n][1]==Fraction(2**(v2(n)+1)-1,n)
        margin=min((v2(p[n][t])+6*(t-1)+v2(n) for t in range(2,len(p[n])) if p[n][t]),default=999)
        margins.append(margin)
        assert margin>=3
    assert margins==[999,6,5,5,4,4,4,4,3,3,3,3,3,3],margins
    cases_even={7:1,5:3,1:4,3:5}
    cases_odd={5:2,7:6,1:8,3:14}
    for k in range(6,11):
        for u in (1,3,5,7,9,11,13,15):
            arr=integer_coeffs((2**k)*u,14)
            for n in range(1,15):
                scale=2**(k-v2(n))
                assert arr[n]%scale==0
                predicted=(u*(2**(v2(n)+1)-1)*pow(n//2**v2(n),-1,8))%8
                assert arr[n]//scale%8==predicted,(k,u,n)
            expected=(cases_even if k%2==0 else cases_odd)[u%8]
            got=next((n for n,x in enumerate(arr) if three_square_obstruction(x)),None)
            assert got==expected,(k,u,got,expected)
    for m,limit in [(2,34),(4,10),(8,13),(16,4),(32,8),(64,14),(192,14),(320,14),(448,14)]:
        assert direct_product(m,limit)==integer_coeffs(m,limit),(m,limit)
    assert first(96,18)==18
    assert integer_coeffs(96,18)[18]==2427470414031893122928
    assert direct_product(96,18)==integer_coeffs(96,18)
    exceptions={2:(34,32192),4:(10,4464),8:(13,2292736),16:(4,6204),32:(8,169008476)}
    for m,(expected,value) in exceptions.items():
        arr=integer_coeffs(m,expected)
        assert arr[expected]==value
        assert not any(three_square_obstruction(x) for x in arr[:expected])
        assert three_square_obstruction(value)
    print('VERIFY_OK polynomial_degrees=14 margins='+','.join(map(str,margins[1:]))+' high_valuation_test_cases=40 exceptions=5 direct_product_crosschecks=10 sharp_low_boundary=96_to_18 maximum_first_index=14')

if __name__=='__main__': verify()
