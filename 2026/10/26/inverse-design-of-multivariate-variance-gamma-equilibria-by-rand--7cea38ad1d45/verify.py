"""Finite arithmetic checks for inverse-design of Brownian reset stationary laws.
Run with Python 3 standard library. Finite checks do not prove the theorem."""
from fractions import Fraction as F
import math

def poch(q,n):
    p=F(1)
    for k in range(n): p*=q+k
    return p

def u_even(q,h,n):
    if n==0: return F(1)
    if q==1: return 1-h
    return 1-h+h*(q-1)/(q+n-1)

checks=0
for q in (F(1),F(5,4),F(3,2),F(2),F(11,3),F(7)):
    for h in (F(1),F(1,2),F(2,3),F(1,5),F(9,10)):
        for n in range(1,65):
            m=u_even(q,h,n)
            # Characteristic-transform coefficient on both sides of
            # E phi(Ut) = (1+h*beta*t*t) phi(t) with beta normalized to one.
            assert poch(q,n)*m == poch(q,n)-h*n*poch(q,n-1)
            assert F(0)<=m<=1
            assert m<=u_even(q,h,n-1)
            checks+=3
for q in (F(1,4),F(1,2),F(3,4)):
    for h in (F(1,5),F(1,2),F(1)):
        m1=1-h/q
        m2=1-2*h/(q+1)
        assert m2>m1
        checks+=1
# Separate numerical integral check for the beta-law Fourier identity.
for q in (1.25,1.5,2.,3.,7.):
    a=2*(q-1)
    for h in (0.2,0.5,1.0):
        for z in (0.1,1.,4.,15.):
            n=40000
            # W uniform, U=W^(1/a): midpoint quadrature of E phi(Ut).
            mean=sum((1+z*((k+0.5)/n)**(2/a))**(-q) for k in range(n))/n
            lhs=(1-h)*(1+z)**(-q)+h*mean
            rhs=(1+h*z)*(1+z)**(-q)
            assert abs(lhs-rhs)<7e-5*max(rhs,0.02), (q,h,z,lhs,rhs)
            checks+=1
print(f'PASS {checks} exact/numerical identity checks')
