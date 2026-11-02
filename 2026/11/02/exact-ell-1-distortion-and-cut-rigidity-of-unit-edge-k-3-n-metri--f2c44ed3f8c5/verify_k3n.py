#!/usr/bin/env python3
"""Exact arithmetic checks for the unit-edge K_(3,n) L1 distortion theorem.

Standard library only.  Direct cut enumeration is independent of orbit formulas.
Finite checks are supplementary; the symbolic proof covers all n >= 3.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb

checks = 0

def ok(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)

def parameters(n):
    k = (n + 1) // 3
    alpha = F(n*(n-1) - (2*n+1)*k + 3*k*k, 2*n*(n-1))
    t = F(n) - F(3*k*(n-k), n-1)
    D = 1 + 2*alpha
    return k, alpha, t, D

def orbit(a, b, n):
    u = F(a*(3-a), 3)
    v = F(2*b*(n-b), n*(n-1))
    w = F(a*(n-b) + b*(3-a), 3*n)
    return u, v, w

def direct_orbit_distance(a, b, n, i, j):
    A = tuple(range(3)); B = tuple(range(3, n+3))
    total = 0
    for SA in combinations(A, a):
        for SB in combinations(B, b):
            mask = frozenset(SA + SB)
            total += ((i in mask) != (j in mask))
    return F(total, comb(3,a)*comb(n,b))

for n in range(3, 301):
    k, alpha, t, D = parameters(n)
    ok(1 <= k <= n-1 and alpha > 0 and t >= 0, ('bounds',n))
    ok(k == min(range(n+1), key=lambda b: (3*b*b-(2*n+1)*b)), ('min',n))
    ok(D == F(2) - F(k*(2*n+1-3*k), n*(n-1)), ('formula',n))
    piece = F(5,3)- (F(2,3*n) if n%3 == 1 else F(2,3*(n-1)))
    ok(D == piece, ('piecewise',n))
    ok(F(1) < D < F(5,3), ('distortion bounds',n))
    for a in range(4):
        for b in range(n+1):
            u,v,w = orbit(a,b,n)
            ok(w - alpha*u - v/2 >= 0, ('dual',n,a,b))
    u,v,w=orbit(1,k,n); u0,v0,w0=orbit(0,1,n)
    ok(3*u+t*u0 == 2, ('primal U',n))
    ok(3*v+t*v0 == 2, ('primal V',n))
    ok(3*w+t*w0 == D, ('primal W',n))
    ok(w - alpha*u - v/2 == 0, ('complementarity',n))

# Independent enumeration from the actual subsets, not merely orbit formulas.
for n in range(3, 10):
    k,alpha,t,D=parameters(n)
    for i,j in combinations(range(n+3), 2):
        rho = 3*direct_orbit_distance(1,k,n,i,j)+t*direct_orbit_distance(0,1,n,i,j)
        target = F(2) if (i<3)==(j<3) else D
        ok(rho == target, ('direct',n,i,j,rho,target))

print('CHECK_OK', checks, 'exact rational assertions for n=3..300; direct cut enumeration n=3..9')
