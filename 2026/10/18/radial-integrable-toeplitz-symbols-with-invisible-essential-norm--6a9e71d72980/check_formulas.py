"""Finite exact checks accompanying the radial Toeplitz construction.

This script tests rational identities and truncated Berezin coefficients;
the infinite-dimensional assertions rely on the analytic proof.
"""
from fractions import Fraction
from math import comb, factorial, sqrt


def phi(n, x):
    x = Fraction(x)
    return (4*x/(1+x)**2)**n


def laplace_from_gamma_expansion(n, x):
    x = Fraction(x)
    return 4**n*sum(((-1)**k*comb(n-1,k)*Fraction(1,1)/(1+x)**(n+1+k)
                     for k in range(n)), Fraction(0))


def beta_integral(n):
    return Fraction(4**n*factorial(n-1)**2, factorial(2*n-1))


def check():
    count=0
    for n in range(2,11):
        for x in (Fraction(1,10),Fraction(1,3),Fraction(1,1),Fraction(3,2),Fraction(5,1),Fraction(13,1)):
            assert x*laplace_from_gamma_expansion(n,x)==phi(n,x)
            assert 0<phi(n,x)<=1
            count+=2
        assert beta_integral(n)**2*n<=16
        count+=1
    for k in (2,4,8,16,32,64):
        for n in (2,4,8):
            assert phi(n,Fraction(k,k))==1
            count+=1
            for m in (1,k-1,k,k+1,2*k,16*k):
                assert phi(n,Fraction(m,k))<=1
                count+=1
            for s in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(4,5),Fraction(9,10)):
                partial=Fraction(0)
                for idx in range(0,400):
                    partial+=(idx+1)*(1-s)**2*s**idx*phi(n,Fraction(idx+1,k))
                bound=4*(beta_integral(n)+Fraction(3,k))
                assert 0<=partial<=bound
                count+=1
    print('PASS',count,'finite exact rational assertions')

if __name__=='__main__':
    check()
