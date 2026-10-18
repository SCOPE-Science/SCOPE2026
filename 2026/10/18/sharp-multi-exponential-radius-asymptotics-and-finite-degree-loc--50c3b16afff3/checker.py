#!/usr/bin/env python3
"""Numerical checks of a large-negative-index optimal-approximant radius theorem.
Pure mathematical computation; numerical tests do not replace the proof.
"""
import math
import numpy as np
from scipy.linalg import eigh_tridiagonal

def normalized_radius(s, n=600):
    # first Jacobi edge is (3/2)^(s/2), then (4/3)^(s/2), etc.
    # Divide all edges by first edge before diagonalization.
    k = np.arange(n-1, dtype=float)
    ratios = (k+3)/(k+2)/(1.5)
    edges = np.exp(0.5*s*np.log(ratios))
    roots = eigh_tridiagonal(np.zeros(n), edges, eigvals_only=True,
                            select='i', select_range=(n-1,n-1),
                            check_finite=False)[0]
    return 1.0/roots

def expansion(s):
    return 1-0.5*(8/9)**s+0.375*(64/81)**s-0.5*(20/27)**s

checks=0
for s in (16,20,24,30,36,44,52,64,80,100):
    numeric=normalized_radius(s)
    approx=expansion(s)
    remainder=(512/729)**s
    err=abs(numeric-approx)
    assert err < 3.0*remainder + 1.e-12
    if s>=20:
        assert abs(numeric-1) <= (8/9)**s
    print('s=%3d normalized=%.14f asymptotic=%.14f residual=%.3e res/err_scale=%.4f'%
          (s,numeric,approx,err,err/remainder))
    checks+=2
# Published Bergman s=1 check: predicted J norm =3/sqrt(2).
s=1
n=4000
k=np.arange(n-1, dtype=float)
edges=np.sqrt((k+3)/(k+2))
lam=eigh_tridiagonal(np.zeros(n),edges,eigvals_only=True,
                    select='i',select_range=(n-1,n-1),check_finite=False)[0]
known=3/math.sqrt(2)
assert abs(lam-known)<5.e-13,(lam,known)
print('Bergman s=1 norm=%.13f exact=%.13f'% (lam, known))
checks+=1
# Rank-four approximation isolates first three edges and predicts cubic-order errors.
for s in (25,35,50,65):
    e1=(8/9)**(s/2)
    e2=(5/6)**(s/2)
    local=eigh_tridiagonal(np.zeros(4), np.array([1.,e1,e2]),
                          eigvals_only=True)[-1]
    full=1/normalized_radius(s)
    assert 0<=full-local< 5*(8/9)**s*(5/6)**s*(4/5)**s+1.e-12
    print('4-site truncation s=%d bound_gap=%.3e'%(s,full-local))
    checks+=1
print('PASS %d checked assertions with scipy tridiagonal eigen-solves'%checks)
