#!/usr/bin/env python3
"""Finite checks for radial Toeplitz moments on generalized Hartogs triangles.

These tests supplement, but do not replace, proofs for all parameters.
Run: python3 checker.py
"""
from fractions import Fraction
from math import sqrt, exp, isclose, gcd


def moment_from_q(q, beta=0.0):
    # Radial probability measure has density 2q*r**(2q-1) on (0,1).
    return q / (q + beta / 2.0)


def numerical_moment(q, beta):
    # Integrate in t=-log r, with 10000 midpoint slices and a long tail.
    # The common prefactor cancels in the ratio.
    T = 24.0 / (2.0*q)
    n = 10000
    h = T/n
    normal = sum(exp(-2*q*(i+0.5)*h) for i in range(n))*h
    weighted = sum(exp(-(2*q+beta)*(i+0.5)*h) for i in range(n))*h
    return weighted / normal


def reduced_spectrum(beta, numerator, n):
    return [(k/(k+numerator*beta/2.0)) for k in range(1,n+1)]


def find_indices(numerator, denominator, k):
    assert gcd(numerator, denominator) == 1
    for m in range(numerator * 2+1):
        if (denominator * (m+1)-k) % numerator == 0:
            n = (k - denominator*(m+1))//numerator - 1
            return m,n
    raise AssertionError('missing residue class')


def run():
    checks = 0
    for gamma in (Fraction(1,1),Fraction(2,3),Fraction(5,4),Fraction(7,11)):
        P,Q = gamma.numerator,gamma.denominator
        for k in range(1,51):
            m,n = find_indices(P,Q,k)
            q = n+1+(m+1)*Q/P
            assert q > 0 and abs(q-k/P)<1e-12
            checks += 2
            for beta in (0.25,1.0,2.0,4.25):
                actual = numerical_moment(q,beta)
                expected = moment_from_q(q,beta)
                assert abs(actual-expected)<5.0e-6, (gamma,k,beta,actual,expected)
                checks += 1
        for R in (0.2, 0.5, 0.83, 0.975):
            s0=R**(2.0/P)
            collar=[s0**k for k in range(1,51)]
            assert isclose(collar[0], s0, rel_tol=1e-14)
            assert all(0 < y < x for x,y in zip(collar,collar[1:]))
            assert all((x-y)/2 <= 1-s0+1e-14 for x,y in zip(collar,collar[1:]))
            # The missing interval between the top eigenvalue and 1
            # dominates all half-gaps, yielding exact Hausdorff distance.
            assert max((x-y)/2 for x,y in zip(collar,collar[1:])) <= 1-s0 + 1e-14
            checks += 4
        for beta in (0.2,0.5,1.0,5.0):
            vals=reduced_spectrum(beta,P,150)
            first=1.0/(1.0+P*beta/2.0)
            assert isclose(vals[0],first,rel_tol=1e-13)
            assert all(x<y for x,y in zip(vals,vals[1:]))
            assert all(y-x<=first+1e-12 for x,y in zip(vals,vals[1:]))
            assert first >= max((y-x)/2 for x,y in zip(vals,vals[1:]))
            checks += 4
    # Numerical evidence for irrational rotation mod 1; density is proved analytically.
    for gamma in (sqrt(2),sqrt(3),sqrt(5)):
        f=sorted((m+1)/gamma%1.0 for m in range(40000))
        gaps=[f[0],1-f[-1]]+[f[i+1]-f[i] for i in range(len(f)-1)]
        assert max(gaps)<0.002
        assert all(0<=t<=1 for t in f)
        checks += 2
    print('PASS:',checks,'finite assertions')

if __name__=='__main__':
    run()
