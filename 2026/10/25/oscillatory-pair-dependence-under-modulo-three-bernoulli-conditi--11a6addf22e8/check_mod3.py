#!/usr/bin/env python3
"""Exact-rational checks for conditional covariances under weight modulo three.
No external dependencies.  This is supporting finite verification, not a proof.
"""
from fractions import Fraction as F
from math import comb

# Q[omega], with omega^2+omega+1=0, represented as a+b*omega.
def add(x, y):
    return (x[0]+y[0], x[1]+y[1])
def neg(x):
    return (-x[0], -x[1])
def mul(x, y):
    a,b = x
    c,d = y
    return (a*c-b*d, a*d+b*c-b*d)
def power(x, n):
    result = (F(1), F(0))
    while n:
        if n & 1: result = mul(result, x)
        x = mul(x, x)
        n >>= 1
    return result
def real(x):
    return x[0]-x[1]/2
def norm(x):
    a,b = x
    return a*a-a*b+b*b

def residue_probability(p, n, r):
    q = 1-p
    return sum((F(comb(n,k))*p**k*q**(n-k)
                for k in range(n+1) if k%3==r%3), F(0))

def direct_covariance(p, n, r):
    a = residue_probability(p, n, r)
    assert a > 0
    b = residue_probability(p, n-1, r-1)
    c = residue_probability(p, n-2, r-2)
    return p*p * (c*a-b*b)/(a*a)

def spectral_covariance(p, n, r):
    q=1-p
    one=(F(1),F(0))
    omega=(F(0),F(1))
    z=(q,p)
    omega_inverse_r=power(omega, (3-r)%3)
    factor=power(add(one,neg(omega)),2)
    a=mul(mul(factor,omega_inverse_r),power(z,n-2))
    b=mul(omega_inverse_r,power(z,n))
    den=(1+2*real(b))**2
    return p*p*q*q*(2*real(a)-3*norm(z)**(n-2))/den

def check():
    cases=0
    for p in [F(1,10),F(1,5),F(1,3),F(1,2),F(2,3),F(4,5),F(9,10)]:
        for n in range(3,31):
            for r in (0,1,2):
                left=direct_covariance(p,n,r)
                right=spectral_covariance(p,n,r)
                assert left == right,(p,n,r,left,right)
                if p == F(1,2):
                    m=(n-3-2*r)%6
                    predicted_sign=1 if m in (0,1,5) else -1
                    sign=1 if left>0 else -1 if left<0 else 0
                    assert sign == predicted_sign,(n,r,left)
                cases+=1
    print('exact finite covariance identity and fair-coin six-cycle: PASS')
    print('independent exact rational cases:',cases)
    print('fair-coin, residue zero (n=3,...,14):',
          [int((direct_covariance(F(1,2),n,0)>0))*2-1 for n in range(3,15)])
if __name__=='__main__':check()
