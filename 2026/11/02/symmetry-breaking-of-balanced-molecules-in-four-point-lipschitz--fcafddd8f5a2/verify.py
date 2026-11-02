#!/usr/bin/env python3
"""Exact affine certificate for the four-vertex equilateral p-transport formula.
No external packages or numerical tolerance are used.
"""
from itertools import combinations, permutations
from fractions import Fraction
V = range(4)
EDGES = list(combinations(V,2))
# coefficients at vertices: 1,1,-1-t,-1+t
A = ((1,0),(1,0),(-1,-1),(-1,1))
TARGET = ((0,1),(1,-1),(1,0))  # t, 1-t, 1

def plus(xs):
    xs=list(xs)
    return (sum(z[0] for z in xs), sum(z[1] for z in xs))
def nonnegative_on_unit(z):
    return z[0]>=0 and z[0]+z[1]>=0
def abs_affine(z):
    if nonnegative_on_unit(z): return z
    assert nonnegative_on_unit((-z[0],-z[1]))
    return -z[0],-z[1]
def diff(x,y):return x[0]-y[0],x[1]-y[1]
def reach(source,edges):
    seen={source}
    while True:
        nxt=seen|{b for a,b in edges if a in seen}|{a for a,b in edges if b in seen}
        if nxt==seen:return seen
        seen=nxt
certs=[]
for edges in combinations(EDGES,3):
    if len(reach(0,edges))!=4:continue
    vals=[]
    for removed in edges:
        component=reach(removed[0],tuple(e for e in edges if e!=removed))
        vals.append(abs_affine(plus(A[i] for i in component)))
    winner=None
    for assignment in permutations(range(3)):
        if all(nonnegative_on_unit(diff(vals[assignment[j]],TARGET[j])) for j in range(3)):
            winner=assignment
            break
    assert winner is not None,(edges,vals)
    certs.append((edges,vals,winner))
assert len(certs)==16
assert any(all(vals[assignment[j]]==TARGET[j] for j in range(3)) for _,vals,assignment in certs)
print('EXACT_SYMBOLIC_TREE_CERTIFICATE_OK',len(certs),'trees')
# Exact sign and endpoint checks for the unique critical point equation:
# on 0<t<1/2, A=t^(p-1)-(1-t)^(p-1) positive strictly decreasing;
# S=1+t^p+(1-t)^p strictly increasing; t/(2+t^2) strictly increasing.
# Analytic inequalities appear in RESULT.md; finite tests below are diagnostics.
import math
for p in (0.2,0.35,0.5,0.75,0.95):
    def fun(t):
        s=1+t**p+(1-t)**p
        return (t**(p-1)-(1-t)**(p-1))/s-t/(2+t*t)
    lo,hi=1e-12,.5
    assert fun(lo)>0 and fun(hi)<0
    for _ in range(100):
        mid=(lo+hi)/2
        if fun(mid)>0:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    def R(x): return (1+x**p+(1-x)**p)**(1/p)/math.sqrt(4+2*x*x)
    assert 0<t<.5 and R(t)>R(0) and R(t)>R(.5) and R(t)>R(1)
    print('DIAGNOSTIC',p,round(t,12),round(R(t),12))
print('ALL_CHECKS_OK')
