#!/usr/bin/env python3
from fractions import Fraction
from math import comb

def m(k):
    z=(4*k*k+4)//5
    if (z-k)&1:
        z+=1
    return z

def r_num_denexp(k):
    N=m(k)-2; h=k-2
    assert N>=0 and (N-h)%2==0
    lo=(N-h)//2; hi=(N+h)//2
    return sum(comb(N,j) for j in range(lo,hi+1)),N

D=[Fraction(0),Fraction(1,5),Fraction(4,5),Fraction(9,5),Fraction(6,5),Fraction(1),Fraction(6,5),Fraction(9,5),Fraction(4,5),Fraction(1,5)]
L=[Fraction(7,4),Fraction(5,4),Fraction(3,4),Fraction(11,4),Fraction(9,4),Fraction(7,4),Fraction(5,4),Fraction(13,4),Fraction(11,4),Fraction(9,4)]
for r in range(10):
    k=100+r
    assert Fraction(5*m(k)-4*k*k,5)==D[r]
    assert Fraction(2*k+3)-Fraction(5,4)*(m(k+1)-m(k))==L[r]
assert min(L)==Fraction(3,4)
prev=None
for k in range(2,81):
    cur=r_num_denexp(k)
    if prev is not None:
        a,na=prev; b,nb=cur
        assert b*(1<<na)>a*(1<<nb),(k-1,k)
    prev=cur
print('VERIFY_OK')
