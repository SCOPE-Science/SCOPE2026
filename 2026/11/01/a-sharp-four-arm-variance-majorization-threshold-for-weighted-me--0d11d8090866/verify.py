#!/usr/bin/env python3
"""Exact symbolic and rational checks for arclength-distance moments on metric stars.
Run: python verify.py ; requires sympy for the polynomial-identity checks.
Finite examples are diagnostic; the universal proof is given in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations
import sympy as sp


def moments_formula(lengths):
    T = sum(lengths)
    p = [Q(v, T) if isinstance(v, int) else v / T for v in lengths]
    S = lambda k: sum((v**k for v in p), Q(0))
    mu = S(2) - Q(2, 3) * S(3)
    raw2 = Q(2, 3) * S(3) + Q(1, 2) * S(2)**2 - S(4)
    return mu, raw2, raw2 - mu**2


def moments_by_integrals(lengths):
    T = sum(lengths)
    j1 = j2 = Q(0)
    for i, a in enumerate(lengths):
        j1 += a**3 / 3
        j2 += a**4 / 6
        for j, b in enumerate(lengths):
            if i == j:
                continue
            j1 += (a*a*b + a*b*b) / 2
            j2 += (a**3*b + a*b**3) / 3 + a*a*b*b / 2
    mu = j1 / T**3
    raw2 = j2 / T**4
    return mu, raw2, raw2 - mu**2


checks = 0
for m in range(2, 9):
    for seed in range(1, 32):
        lengths = [Q(((seed + j*3) % 11) + 1, (j % 3) + 1) for j in range(m)]
        assert moments_formula(lengths) == moments_by_integrals(lengths)
        checks += 1

x, y, z, w = sp.symbols('x y z w')
for m in (3, 4, 5):
    p = [x, y, z, w][:m] if m <= 4 else [x, y, z, w, sp.Symbol('v')]
    S = lambda k: sum(a**k for a in p)
    mu = S(2) - sp.Rational(2,3)*S(3)
    M2 = sp.Rational(2,3)*S(3) + sp.Rational(1,2)*S(2)**2 - S(4)
    qmu = sp.cancel((sp.diff(mu, x)-sp.diff(mu, y))/(x-y))
    qM2 = sp.cancel((sp.diff(M2, x)-sp.diff(M2, y))/(x-y))
    rem = sum(v for v in p if v not in (x, y))
    R2 = sum(v**2 for v in p if v not in (x,y))
    assert sp.expand((qmu - 2*rem).subs(rem, 1-x-y)) == 0 if m==3 else sp.expand(qmu - 2*(1-x-y)) == 0
    assert sp.expand(qM2 - 2*((x+y)*(1-x-y)+R2)).subs(p[-1], 1-sum(p[:-1])).expand() == 0
    checks += 2

p3=[x,y,z]
S=lambda k:sum(a**k for a in p3)
mu=S(2)-sp.Rational(2,3)*S(3)
M2=sp.Rational(2,3)*S(3)+sp.Rational(1,2)*S(2)**2-S(4)
V=sp.expand(M2-mu**2)
qV=sp.cancel((sp.diff(V,x)-sp.diff(V,y))/(x-y))
assert sp.expand((qV - sp.Rational(2,3)*z*(1+12*x*y*z)).subs(z,1-x-y)) == 0
checks += 1

p0=[Q(9,20),Q(9,20),Q(9,100),Q(1,100)]
q0=[Q(9,20),Q(9,20),Q(19,200),Q(1,200)]
delta=tuple(a-b for a,b in zip(moments_formula(q0),moments_formula(p0)))
assert delta == (Q(153,200000),Q(1683,4000000),-Q(203133,8000000000))
checks += 1

def majorizes(a,b):
    assert sum(a)==sum(b)
    a=sorted(a,reverse=True); b=sorted(b,reverse=True)
    return all(sum(a[:i]) >= sum(b[:i]) for i in range(1,len(a)))

for m in range(4,10):
    eps=Q(0) if m==4 else Q(1,1000)
    p=[(1-eps)*a for a in p0]+([] if m==4 else [eps/(m-4)]*(m-4))
    q=[(1-eps)*a for a in q0]+([] if m==4 else [eps/(m-4)]*(m-4))
    assert majorizes(q,p) and moments_formula(q)[2] < moments_formula(p)[2]
    u=[Q(1,m)]*m
    v=[Q(1,m)+Q(1,1000),Q(1,m)-Q(1,1000)]+[Q(1,m)]*(m-2)
    assert majorizes(v,u) and moments_formula(v)[2]>moments_formula(u)[2]
    checks += 2

print('PASS', checks, 'exact algebra/integral/majorization checks')
