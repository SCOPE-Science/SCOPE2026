#!/usr/bin/env python3
"""Standalone finite checks of the weighted Bergman dyadic-circle estimates.
Analytical estimates in RESULT.md, not these finite tests, cover all degrees.
"""
from fractions import Fraction
from math import ceil, log2, lgamma, exp, log, isfinite

assertions = 0
cases = 0
minimum_ratios = {}
for beta in (0.5, 1.0, 2.0, 4.0):
    C = max(1.0, 2.0**beta*exp(lgamma(beta+1)))
    A = (1.0-2.0**(-beta))*4.0**(-beta)/(2.0*C)
    minimum = float('inf')
    for N in (1, 2, 3, 4, 7, 8, 15, 16, 31, 32, 63, 64, 127, 256, 512):
        J = ceil(log2(2*(N+1)))
        nodes = [(1-2**(-j), (2**(-j))**beta-(2**(-j-1))**beta) for j in range(1,J)]
        nodes.append((1-2**(-J), 2**(-J*beta)))
        assert len(nodes)==J; assertions+=1
        assert len({t for t,w in nodes})==J; assertions+=1
        assert all(0 < t < 1 and w > 0 for t,w in nodes); assertions+=1
        for k in range(N+1):
            mom=exp(lgamma(beta+1)+lgamma(k+1)-lgamma(k+beta+1))
            val=sum(w*t**k for t,w in nodes)
            ratio=val/mom
            assert A-1e-12 <= ratio <= 1+1e-10, (beta,N,k,ratio,A)
            assertions+=1
            minimum=min(minimum,ratio)
        cases+=1
    minimum_ratios[str(beta)] = minimum

# Exact rational replay for two entire finite-degree monomial spectra.
for beta in (1,2):
    for N in (3, 15, 63):
        J=ceil(log2(2*(N+1)))
        points=[(1-Fraction(1,2**j), Fraction(1,2**(j*beta))-Fraction(1,2**((j+1)*beta))) for j in range(1,J)]
        points.append((1-Fraction(1,2**J),Fraction(1,2**(J*beta))))
        for k in range(N+1):
            norm=Fraction(1,k+1) if beta==1 else Fraction(2,(k+1)*(k+2))
            val=sum((w*t**k for t,w in points),Fraction(0))
            assert norm>0 and val>0 and val<=norm
            assertions+=1

# The roots-of-unity angular average kills every cross term in degree <=N.
for N in (1,2,3,15,31,63):
    L=N+1
    for k in range(N+1):
        for m in range(N+1):
            assert ((k-m)%L==0)==(k==m)
            assertions+=1

# Dyadic bound, sampled densely including near the boundary.
for beta in (0.2,0.5,1.0,2.0,4.0,8.0):
    for J in (1,2,3,6,10,15):
        for r in range(200):
            x=10**(-6+9*r/199)
            terms=[exp((s*log(2))*beta-x*2**s) for s in range(J+1)]
            if max(terms)>0:
                assert sum(terms)/max(terms) < (exp(2*beta)/(1-2**(-beta))+(2/exp(1))**beta/(1-(2/exp(2))**beta))+1e-7
                assertions+=1

print('weighted_Bergman_dyadic_checker PASS')
print('tested_parameters_beta',','.join(map(str,(0.5,1.0,2.0,4.0))))
print('finite_degree_cases',cases)
print('assertions',assertions)
print('minimum_relative_eigenvalues',minimum_ratios)
print('limitations: finite samples are diagnostics, not the universal proof')
