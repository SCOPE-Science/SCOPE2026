#!/usr/bin/env python3
"""Exact arithmetic checks for a rank-one spectral preconditioner on spiked quadratics.

All universal claims are established analytically; these are reproducible finite checks.
"""
from fractions import Fraction as F
from itertools import product
from math import atan, pi, sqrt
from random import Random

COUNT = 0
for n in (2, 3, 4):
    for kappa in (F(2), F(3), F(7), F(13)):
        vectors = product((-2, -1, 0, 1, 2), repeat=n)
        for v in vectors:
            s = sum(x*x for x in v)
            if not s: continue
            gamma = F(1) + (kappa-F(1))*F(v[0]*v[0],s)
            rstar = min(F(1),(kappa+F(1)-gamma)/gamma)
            assert 0 < rstar <= 1
            expected = ((kappa-gamma)*(gamma-1)/(gamma*(kappa+1-gamma))
                        if gamma > (kappa+1)/2 else ((kappa-1)/(kappa+1))**2)
            def factor_squared(r):
                tr=kappa+1-gamma+gamma*r
                det=kappa*r
                return F(1)-4*det/(tr*tr)
            assert factor_squared(rstar)==expected
            assert rstar==1 if gamma <= (kappa+1)/2 else rstar<1
            for r in (F(1,32),F(1,8),F(1,3),F(1,2),F(2,3),F(7,8),F(1)):
                assert factor_squared(r)>=expected
            # Exact trace of A(I-(1-r)vv^T/||v||^2), extracting two active eigenvalues.
            diagonal = [kappa]+[F(1)]*(n-1)
            tr_all = sum(diagonal[i]*(1-(1-rstar)*F(v[i]*v[i],s)) for i in range(n))
            assert tr_all-(n-2)==kappa+1-gamma+gamma*rstar
            COUNT+=1

# Independently check one power-step angular probabilities for n=2 and n=3.
rng=Random(731241)
checks=[]
for n,kappa,t in ((2,3,0),(2,5,1),(3,4,1),(3,2,2)):
    total=50000
    success=0
    for _ in range(total):
        g=[rng.gauss(0,1) for __ in range(n)]
        success += (kappa**(2*t)*g[0]*g[0]>sum(x*x for x in g[1:]))
    theoretical=(2/pi)*atan(kappa**t) if n==2 else 1-1/sqrt(1+kappa**(2*t))
    empirical=success/total
    assert abs(empirical-theoretical)<0.012,(n,kappa,t,empirical,theoretical)
    checks.append((n,kappa,t,round(empirical,5),round(theoretical,5)))
print(f'VERIFY_OK exact spectral identities / global scalar optimality: {COUNT} cases; Gaussian power probabilities: {checks}')
