#!/usr/bin/env python3
"""Exact factorial-ratio identities and finite asymptotic diagnostics for the stated Gaussian theorem.

The analytic proof, not finite checking, establishes the infinite-domain results.
"""
from fractions import Fraction
from math import factorial, prod


def ratio(m, n, N, cabs_sq=1):
    return Fraction(factorial(N+m)**2, cabs_sq*factorial(N)*factorial(N+m+n))


def ratio_product(m, n, N, cabs_sq=1):
    return Fraction(prod(range(N+1,N+m+1)), cabs_sq*prod(range(N+m+1,N+m+n+1)))


def weighted_bracket(p, N):
    a = Fraction(factorial(N+p),factorial(N+2*p))
    return a*a*factorial(N+3*p)/factorial(N+p)-1


def weighted_bracket_product(p, N):
    return prod((Fraction(N+2*p+r,N+p+r) for r in range(1,p+1))) - 1


def symbolic_norm(p, N):
    alpha=Fraction(factorial(N+p),factorial(N+2*p))
    return (factorial(N+p)-2*alpha*factorial(N+2*p)+alpha*alpha*factorial(N+3*p))


trials=0
for m in range(1,9):
    for n in range(1,9):
        for N in (0,1,2,7,23):
            assert ratio(m,n,N)==ratio_product(m,n,N)
            trials += 1
for p in range(1,10):
    for N in (0,1,5,25):
        b=weighted_bracket(p,N)
        assert b==weighted_bracket_product(p,N)>0
        assert symbolic_norm(p,N)==factorial(N+p)*b
        trials += 1
for p in (1,2,3,4,5,6):
    q=1.0
    for ell in range(1,6001):
        N=2*p*(ell-1)
        q *= float(ratio_product(p,p,N))
    scaled=q*(6000**(p/2))
    assert scaled>0
    print(f"balanced_order={p}, scaled_energy_at_6000={scaled:.12g}")
print(f"PASS: {trials} exact factorial and Fourier norm identities; finite diagnostics completed.")
