#!/usr/bin/env python3
"""Supplementary finite tests for critical Blaschke Fourier fourth moments.

Uses only Python's standard library. These are mathematical consistency checks;
they do not replace the uniform stationary-phase proof.
"""
import math
import cmath
from fractions import Fraction
from math import comb

def uv(roots):
    return (sum(2*a*(1+a)/(1-a)**3 for a in roots),
            sum(2*a*(1-a)/(1+a)**3 for a in roots))

def factor_coeffs(a, n, kmax):
    num = [comb(n,j) * (-a)**(n-j) for j in range(n+1)]
    denom = [comb(n+k-1,k)*a**k for k in range(kmax+1)]
    return [sum(num[j]*denom[k-j] for j in range(min(k,n)+1))
            for k in range(kmax+1)]

def multiply(a,b,N):
    return [sum(a[j]*b[k-j] for j in range(k+1)) for k in range(N+1)]

def coefficients(roots,n,N):
    coeff = [Fraction(1)] + [Fraction(0)]*N
    for a in roots:
        coeff = multiply(coeff, factor_coeffs(a,n,N), N)
    return coeff

def coeff_fourth(roots,n,N):
    c=coefficients(roots,n,N)
    return sum(float(x)**4 for x in c)

def check():
    assert uv([Fraction(1,2)]) == (Fraction(12), Fraction(4,27))
    assert uv([Fraction(1,5),Fraction(1,2)]) == (Fraction(207,16),Fraction(1,3))
    for roots in [(Fraction(1,2),),(Fraction(1,5),Fraction(1,2))]:
        for n in [1,2,3]:
            N=90
            c=coefficients(roots,n,N)
            assert abs(sum(float(z*z) for z in c)-1) < 2e-11
            assert c[0] == math.prod((-a)**n for a in roots)
            assert c[1] == c[0] * n*sum(a-1/a for a in roots)
            # Exact fourth power equals the constant Fourier mode of
            # the autocorrelation polynomial squared.
            w=[x*x for x in c]
            assert sum(z*z for z in w) == sum(z**4 for z in c)
            # Quadrature of the periodic autocorrelation reproduces Parseval.
            M=512
            estimated=0.0
            for j in range(M):
                theta=2*math.pi*j/M
                A=sum(float(w[k])*cmath.exp(1j*k*theta) for k in range(N+1))
                estimated+=abs(A)**2/M
            assert abs(estimated-sum(float(z**4) for z in c))<1e-9
    print('PASS: exact U/V, finite coefficient mass and Parseval tests for one and two roots')

if __name__=='__main__':
    check()
