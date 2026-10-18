#!/usr/bin/env python3
"""Exact arithmetic checks for a local quartic Delannoy congruence.
Requires only the Python 3 standard library. Finite examples are supplemental.
"""
from fractions import Fraction as F
from math import comb

def a(k): return F(k*(k+1))
def b(k): return F((k-1)*k*(k+1)*(k+2),4)
def c(k): return F((k-2)*(k-1)*k*(k+1)*(k+2)*(k+3),36)
def f(k,j):
    A=a(k); B=b(k); C=c(k)
    coefficient = {1:4*A,2:6*A*A+4*B,3:4*A**3+12*A*B+4*C}[j]
    return (2*k+1)*coefficient

def S(p,j):
    if j==1:return F(4*p*(p*p-1))
    if j==2:return F(p*(p*p-1)*(7*p*p-16))
    return F(2*p*(p*p-1)*(32*p**4-191*p*p+324),9)

# Both sides of each finite-difference identity have degree at most 8.
# Equality at ten distinct integer arguments certifies the polynomial identity.
for j in (1,2,3):
    assert S(1,j)==0
    for p in range(10):
        assert S(p+2,j)-S(p,j)==-f(p,j)+f(p+1,j),(p,j)
    for p in range(1,16,2):
        assert S(p,j)==sum(((-1)**k)*f(k,j) for k in range(p))

def D(k,x):
    return sum(comb(k,j)*comb(k+j,j)*x**j for j in range(k+1))

def H(p,x):
    left=sum((-1)**k*(2*k+1)*D(k,x)**4 for k in range(p))
    right=p*sum((-1)**j*comb(2*j,j)**2*(x*(x+1))**j*(2*x+1)**(2*j)
                for j in range((p-1)//2+1))
    return left-right

# Verify exact exceptional low-degree coefficients directly by polynomial arithmetic.
def pol_mul(A,B,cap=3):
    C=[0]*(min(cap,len(A)+len(B)-2)+1)
    for i,a0 in enumerate(A):
        for j,b0 in enumerate(B):
            if i+j<len(C):C[i+j]+=a0*b0
    return C

def local_coefficients(p):
    left=[0]*4
    for k in range(p):
        dk=[comb(k,j)*comb(k+j,j) if j<=k else 0 for j in range(4)]
        d4=[1]
        for _ in range(4): d4=pol_mul(d4,dk)
        for j in range(4):left[j]+=(-1)**k*(2*k+1)*d4[j]
    x2x=[0,1,1]; u=[1,2]
    right=[0]*4
    for j in range((p-1)//2+1):
        a0=[1];b0=[1]
        for _ in range(j): a0=pol_mul(a0,x2x)
        for _ in range(2*j):b0=pol_mul(b0,u)
        term=pol_mul(a0,b0)
        for k in range(4):right[k]+=p*(-1)**j*comb(2*j,j)**2*(term[k] if k<len(term) else 0)
    return [l-r for l,r in zip(left,right)]

for p in (3,5,7,11,13):
    H0,H1,H2,H3=local_coefficients(p)
    assert H0==0 and H1==4*p**3,(p,H1)
    assert H2%p**3==0 and H3%p**3==0,(p,H2,H3)
    for depth in (1,2,3):
        for t in (1,2,4):
            if t%p==0:continue
            x=p**depth*t
            modulus=p**(depth+4)
            val=H(p,x)
            assert val%modulus==(4*p**3*x)%modulus,(p,depth,t)
            assert (val//p**(depth+3))%p==(4*t)%p
            assert H(p,-1-x)==val,(p,depth,t)
print('VERIFY_OK: exact polynomial identities, exceptional coefficients, p-adic depths and reflection')
