#!/usr/bin/env python3
"""Finite exact and numerical tests for Fourier memory in 2D heterochaos baker maps.

The analytical arguments in RESULT.md establish the infinite statements.
The checks here verify Fourier transition weights, Catalan coefficients, variance
identities and a bounded Poisson solution in the contracting-center regime.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb, cos, pi, sqrt
import sympy as sp


def cat(m):
    return comb(2*m, m)//(m+1)


def forward_modes(k, a):
    beta = 1-2*a
    if k%2:
        return {2*k:beta}
    return {k//2:2*a, 2*k:beta}


def transition(n, k, a):
    d={k:Fraction(1)}
    for _ in range(n):
        e=defaultdict(Fraction)
        for mode,weight in d.items():
            for mode2,alpha in forward_modes(mode,a).items():
                e[mode2]+=weight*alpha
        d=dict(e)
    return d


def cov(n,a):
    return Fraction(0) if n%2 else Fraction(cat(n//2),2)*(2*a*(1-2*a))**(n//2)


def variance(N,a):
    return Fraction(N,2)+sum((N-2*m)*cat(m)*(2*a*(1-2*a))**m
        for m in range(1,(N-1)//2+1))

As=[Fraction(1,8),Fraction(1,5),Fraction(1,4),Fraction(1,3),Fraction(2,5),Fraction(9,20)]
num_mode_checks=0
for a in As:
    for k in (1,3,5,11):
        for n in range(25):
            d=transition(n,k,a)
            assert d.get(k,Fraction(0))==2*cov(n,a)
            assert all(mode%k==0 and (mode//k)&((mode//k)-1)==0 for mode in d)
            num_mode_checks+=1
    for N in range(1,35):
        V=variance(N,a)
        assert V>0
        if N>=3:
            assert V-2*variance(N-1,a)+variance(N-2,a)==2*cov(N-1,a)

x=sp.symbols('x', positive=True)
a=sp.symbols('a', positive=True)
Cat=(1-sp.sqrt(1-4*x))/(2*x)
for val in As:
    y=2*val*(1-2*val)
    summed=sp.simplify(Cat.subs(x,y))
    expected=1/max(2*val,1-2*val)
    assert summed==expected, (val,summed,expected)
    GK=sp.simplify(summed-sp.Rational(1,2))
    assert GK==expected-sp.Rational(1,2)

num_poisson_checks=0
for aa in [Fraction(3,10),Fraction(1,3),Fraction(2,5),Fraction(9,20)]:
    q=2*aa
    p=1-q
    def g(j): return Fraction(1,q)*(p/q)**j
    assert g(0)-q*g(1)==1
    for j in range(1,35):
        assert g(j)-p*g(j-1)-q*g(j+1)==0
        num_poisson_checks+=1

# Critical finite-variance asymptotic, tested independently of its proof.
crit=Fraction(1,4)
for N in (500,2000,10000):
    V=float(variance(N,crit))
    lead=1.5*N-4*sqrt(2*N/pi)
    assert abs(V-lead)<5, (N,V,lead)

# Direct stationary sample experiment. A fresh base digit has probabilities
# a, a, 1-2a and the center map is one of the three stated affine branches.
try:
    import numpy as np
    rng=np.random.default_rng(20261030)
    paths=130000
    max_error=0.0
    for aa in (1/4,1/3,2/5):
        z=rng.random(paths)
        init=np.cos(2*pi*z)
        for n in range(1,9):
            branch=rng.random(paths)
            z=np.where(branch<aa,z/2,np.where(branch<2*aa,(z+1)/2,(2*z)%1))
            empirical=float(np.mean(init*np.cos(2*pi*z)))
            target=float(cov(n,Fraction(str(aa)).limit_denominator(1000)))
            max_error=max(max_error,abs(empirical-target))
            assert abs(empirical-target)<0.01,(aa,n,empirical,target)
    print('MAX_STATIONARY_MONTE_CARLO_ERROR',format(max_error,'.7f'))
except ImportError:
    print('NUMERIC_CHECK_SKIPPED numpy unavailable')

print('EXACT_FOURIER_MODE_CHECKS',num_mode_checks)
print('EXACT_POISSON_CHECKS',num_poisson_checks)
print('EXACT_FINITE_VARIANCE_CHECKS',len(As)*34)
print('ORIGINAL_MAP_COV_0_TO_10',[str(cov(n,Fraction(1,3))) for n in range(11)])
print('ASYMPTOTIC_VARIANCE_a=1/4',sp.Rational(3,2))
print('ASYMPTOTIC_VARIANCE_a=1/3',sp.Integer(1))
print('PASS')
