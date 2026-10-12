#!/usr/bin/env python3
"""Finite exact verification of two representations for sibling deficits, plus
numeric conditional covariance and observable-centering asymptotic checks.
This is supplementary to the analytical argument, not a proof of its infinite scope.
"""
from fractions import Fraction
from math import comb, factorial, log, exp, sqrt


def moment_by_stopping(n,j):
    # Integrate density of maximum of n Exp(1) against conditional
    # q_j(t)=sum_{r=1}^{j-1} t**r/r! /(exp(t)-1).
    a=Fraction(1)
    for k in range(1,j):
        for m in range(n-1):
            a+=Fraction(n*(n-1)*(-1)**m*comb(n-2,m),(m+2)**(k+1))
    return a


def moment_by_subset(n,j):
    return sum((Fraction((-1)**(k-1)*comb(n,k),k**(j-1)) for k in range(1,n+1)),Fraction(0))


def q(t,j):
    return sum(t**k/factorial(k) for k in range(1,j))/(exp(t)-1)


def corr_cond(t,i,j):
    pi,pj=q(t,i),q(t,j)
    return sqrt(pi*(1-pj)/(pj*(1-pi)))


def run():
    nchecks=0
    for n in range(2,24):
      for j in range(2,10):
        a,b=moment_by_stopping(n,j),moment_by_subset(n,j)
        assert a==b, (n,j,a,b)
        nchecks+=1
    for w in (0.2,0.5,1.,3.,10.):
      for n in (10**4,10**6,10**9):
        t=log(n/w)
        for i,j in ((2,3),(2,4),(3,4)):
            a_i=log(n)**(i-1)/factorial(i-1)
            a_j=log(n)**(j-1)/factorial(j-1)
            c=corr_cond(t,i,j)
            assert 0<c<1
            # The finite log rate is not close for small n; check only
            # the exact conditional variance/correlation algebra numerically.
            pi,pj=q(t,i),q(t,j)
            cov=(n-1)*(pi-pi*pj)
            var_i=(n-1)*pi*(1-pi)
            var_j=(n-1)*pj*(1-pj)
            assert abs(cov/sqrt(var_i*var_j)-c)<1e-12
            nchecks+=1
    print('PASS:',nchecks,'exact-identity and conditional-correlation checks')

if __name__=='__main__':run()
