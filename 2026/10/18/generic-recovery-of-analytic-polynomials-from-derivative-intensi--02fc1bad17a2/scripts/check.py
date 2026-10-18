#!/usr/bin/env python3
"""Exact witnesses for the spectral-factor sampling argument.

All coefficients and coefficient comparisons are symbolic rational Gaussian.
Finite checks illustrate but do not prove the general theorem.
"""
import sympy as sp
from itertools import combinations
F = sp.Rational

def mul(a, b):
    out = [sp.Integer(0)] * (len(a) + len(b) - 1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out

def spectral_factor(roots, flipset):
    coeff = [sp.Integer(1)]
    for j,r in enumerate(roots):
        coeff = mul(coeff, [sp.Integer(-1), sp.Integer(r)] if j in flipset else [sp.Integer(-r),sp.Integer(1)])
    return coeff

def integral_coeff(q):
    return [sp.Integer(0)] + [v/F(j+1) for j,v in enumerate(q)]

def normsq(z):
    return sp.expand(z*sp.conjugate(z))

def moment1(c):
    return sp.expand(sum(c[j]*sp.conjugate(c[j-1]) for j in range(1,len(c))))

def moment0(c):
    return sp.expand(sum(normsq(v) for v in c))

for degree in range(3,8):
    roots=list(range(2, degree+1))
    trueq=spectral_factor(roots, frozenset())
    truep=integral_coeff(trueq)
    truep[0]=1+sp.I
    first=moment1(truep); energy=moment0(truep)
    assert len(trueq)==degree
    checked=0
    for cardinality in range(1, degree):
        for inds in combinations(range(degree-1),cardinality):
            q=spectral_factor(roots,frozenset(inds))
            p=integral_coeff(q)
            a=q[0]
            assert a!=0 and abs(a)!=abs(trueq[0])
            internal=moment1(p)
            # first Fourier moment = q[0]*conjugate(c0)+internal.
            p[0]=sp.conjugate((first-internal)/a)
            assert sp.simplify(moment1(p)-first)==0
            assert sp.simplify(moment0(p)-energy)!=0, (degree, inds)
            assert sp.simplify(normsq(trueq[0]/a)-1)!=0
            checked+=1
    print(f'degree={degree}, roots={roots}, alternate_factors={checked}, all_energy_tests=nonzero')
print('PASS: Gaussian-rational exact arithmetic and finite spectral-factor checks.')
