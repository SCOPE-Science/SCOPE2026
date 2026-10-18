#!/usr/bin/env python3
"""Exact coefficient and limiting-moment spot checks for radial Rodrigues descendants."""
from fractions import Fraction
from math import comb, factorial

def coeff(d,n,m,j):
    # coefficient t^(degree-j) of Q_{n,m}(t), with q=ceil(m/d)
    ell=n-j
    if d*ell < m:return 0
    return (-1)**j*comb(n,ell)*factorial(d*ell)//factorial(d*ell-m)

def moment_finite(d,n,m):
    nn=d*n-m
    a0=coeff(d,n,m,0)
    a1=coeff(d,n,m,1)
    a2=coeff(d,n,m,2)
    e1=-Fraction(a1,a0)
    e2=Fraction(a2,a0)
    # pushforward measure: each t root appears with weight d/(dn-m), zero omitted.
    return Fraction(d,nn)*e1, Fraction(d,nn)*(e1*e1-2*e2)

def moment_limit(d,alpha):
    kappa=alpha*(d-alpha)**(d-1)/d**d
    beta=(d-alpha)/alpha
    m1=(1+beta)*kappa
    m2=(1+beta)*(d+beta)*kappa**2
    return m1,m2

for d in (2,3,4):
    for alpha in (Fraction(1,2),Fraction(1),Fraction(3,2)):
        if alpha>=d:continue
        print('d',d,'alpha',alpha,'limit',moment_limit(d,alpha))
        for n in (20,100,400):
            m=int(alpha*n)
            m1,m2=moment_finite(d,n,m)
            lim1,lim2=moment_limit(d,alpha)
            print(' n',n,'m1',float(m1),'err1',float(m1-lim1),'m2',float(m2),'err2',float(m2-lim2))
print('checks done')
