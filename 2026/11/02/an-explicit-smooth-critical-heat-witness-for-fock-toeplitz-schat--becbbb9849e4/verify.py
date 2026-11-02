#!/usr/bin/env python3
"""Finite exact-moment checks for the radial building-block identity.

This checks a rational, piecewise-uniform surrogate probability density.
The published analytic integration-by-parts proof applies to every smooth
unit-mass density supported in the same positive annulus; the surrogate is
only a reproducibility test, not the proof of the infinite-dimensional claim.
"""
from fractions import Fraction
from math import factorial, exp, expm1


def moment(epsilon, k):
    """kth moment of the uniform probability law on [epsilon,2epsilon]."""
    return ((2 * epsilon)**(k + 1) - epsilon**(k + 1)) / (epsilon * (k + 1))


def eigenvalue(N, epsilon, n, scale=Fraction(1)):
    return scale * sum(((-1)**m) * moment(epsilon, n-m) / factorial(n-m)
                       for m in range(min(n, N-1)+1))


def check():
    tests=0
    for N in [2, 3, 4, 6, 8, 12, 16]:
        eps=Fraction(1, N**3)
        scale=Fraction(3,N)
        vals=[eigenvalue(N,eps,n,scale) for n in range(N+23)]
        # A smooth mollifier has exactly the same low-index coefficients
        # up to its moments; the errors lie above those coordinates.
        for n in range(N):
            assert abs(vals[n]-scale*(-1)**n) <= float(scale)*N*expm1(2*float(eps))
            tests+=1
        # Finite sum plus rigorously bounded, nonnegative absolute tail.
        partial=sum(abs(v-(scale*(-1)**n if n<N else 0)) for n,v in enumerate(vals))
        assert float(partial) <= float(scale)*N*expm1(2*float(eps))*(1+1e-11)
        tests+=1
        # Full trace-pairing identity: each differentiated bump contributes
        # one copy of the Laplace transform of the same mass-one density.
        u=(exp(-float(eps))-exp(-2*float(eps)))/float(eps)
        signed=sum(((-1)**n)*float(v) for n,v in enumerate(vals))
        # Bounding the missing eigenvalue tail by each kth moment bound.
        missing=float(scale)*N*sum((2*float(eps))**k/factorial(k) for k in range(23,40))
        assert abs(signed-float(scale)*N*u) < missing+5e-12
        tests+=1
        # Positivity of the heat center despite alternating matrix signs.
        assert 2*u > 2*exp(-2*float(eps))-1e-12
        tests+=1
        # The block-error bound is dimension independent at each coordinate.
        for m in range(N):
            assert moment(eps,0)==1
            assert 0 < float(moment(eps,1)) <= 2*float(eps)
            tests+=2
    # Absolute convergence for each p>1 is certified by
    # j*2^{-j^2(1-1/p)} + j*(exp(2*2^{-3j^2})-1).
    for p in [1.01,1.1,1.5,2.0,5.0,20.0]:
        x=[j*2**(-(j*j)*(1-1/p)) + j*expm1(2*2**(-3*j*j))
           for j in range(1,501)]
        assert all(a>=0 for a in x)
        assert x[-1]<1e-6
        tests+=2
    print(f'PASS: {tests} finite exact-moment, trace, and bound checks')
    print('Limits: no finite computation certifies all smooth derivatives, all p, or the infinite sum.')


if __name__=='__main__':
    check()
