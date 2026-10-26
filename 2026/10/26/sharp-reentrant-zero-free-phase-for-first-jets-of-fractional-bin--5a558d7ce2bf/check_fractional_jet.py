#!/usr/bin/env python3
"""Reproducibility checks for the fractional-kernel first-jet zero-free phase."""
from fractions import Fraction as F
from cmath import exp
from math import acos, asin, pi, sqrt


def numerator(beta, t, a, b):
    return (1-a*b)**2 + beta*t*(a+b)*(1-a*b) + beta*t*t*(1+beta*a*b)


def real_torus(beta, t, psi):
    s = __import__('math').sin(psi)
    return beta*t*t*(beta+1) - (4+2*beta*t*t)*s*s


def imaginary_torus(beta,t,psi,delta):
    from math import sin,cos
    return -2*beta*t*sin(psi)*(2*cos(delta)+t*cos(psi))


def exact_factor_test():
    for beta in [F(1,11),F(1,3),F(1,2),F(3,4),F(7,8),F(9,10)]:
        for X in [F(0),F(1,7),F(4),F(100),F(1000,3)]:
            L=beta*(1-beta)*X*X+4*(1-2*beta)*X-16
            R=beta*(1-beta)*(X-4/(1-beta))*(X+4/beta)
            assert L==R
        T=4/(1-beta)
        assert beta*(1-beta)*T*T+4*(1-2*beta)*T-16==0


def torus_zeros_and_offphase():
    for beta,t in [(0.1,0.5),(0.25,1),(0.5,1),(0.5,2),(0.75,1),(0.75,2),(0.9,1),(1.0,1),(1.0,4),(1.0,20)]:
        assert beta==1 or t<2/sqrt(1-beta)
        ss=beta*(beta+1)*t*t/(4+2*beta*t*t)
        assert 0<ss<1
        psi=asin(sqrt(ss)); cc=sqrt(1-ss)
        assert abs(t*cc/2)<1
        delta=acos(-t*cc/2)
        a=exp(1j*(psi+delta)); b=exp(1j*(psi-delta))
        assert abs(numerator(beta,t,a,b))<2e-11
        assert abs(real_torus(beta,t,psi))<2e-11
        assert abs(imaginary_torus(beta,t,psi,delta))<2e-11
        # Nonvanishing torus Jacobian entries ensure inward persistence.
        from math import sin,cos
        assert abs(-2*(4+2*beta*t*t)*sin(psi)*cos(psi))>1e-12
        assert abs(4*beta*t*sin(psi)*sin(delta))>1e-12
    for beta in [0.1,0.25,0.5,0.75,0.9]:
        t=2/sqrt(1-beta)
        c=sqrt(1-beta); s=sqrt(beta)
        for a in [-c+1j*s,-c-1j*s]:
            assert abs(abs(a)-1)<2e-15
            assert abs(numerator(beta,t,a,a))<2e-10


def validate_mixed_formula():
    for beta in (0.2,0.5,1.0):
        for t in (0.25,1.75,5.0):
            a=complex(0.34,0.12)
            b=complex(-0.27,0.38)
            u=a*b
            # Independent derivative expressions of (1-ab)^(-beta).
            value=(1-u)**(-beta)
            d_a=beta*b*(1-u)**(-beta-1)
            d_b=beta*a*(1-u)**(-beta-1)
            d_both=beta*(1+beta*u)*(1-u)**(-beta-2)
            direct=value+t*(d_a+d_b)+t*t*d_both
            reduced=numerator(beta,t,a,b)*(1-u)**(-beta-2)
            assert abs(direct-reduced)<3e-10


if __name__=='__main__':
    exact_factor_test()
    torus_zeros_and_offphase()
    validate_mixed_formula()
    print('CHECK_OK: rational factorization, boundary zeros, Jacobian checks, derivative identities')
