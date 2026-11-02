#!/usr/bin/env python3
"""Exact combinatorial and algebraic replay for a conic–six-line projective-rigidity theorem.
Requires Python 3 and SymPy. All arithmetic is exact. No finite-field extrapolation.
"""
from itertools import combinations, permutations
import sympy as s

V=range(6)
trips=list(combinations(V,3))
pairs=set(combinations(V,2))

def candidates(a):
    for H in combinations(trips,a):
        if all(len(set(t)&set(t2))<=1 for t,t2 in combinations(H,2)):
            yield H

def free_graph(H):
    forbidden={tuple(sorted(p)) for T in H for p in combinations(T,2)}
    return pairs-forbidden

def degree_profile(edges):
    return tuple(sum(v in e for e in edges) for v in V)

def cycles_on_free_edges(edges):
    out=[]
    for b in range(3,7):
        for subset in combinations(edges,b):
            deg=degree_profile(subset)
            if sorted(x for x in deg if x)>[] and set(deg)<={0,2}:
                out.append(subset)
    return out

all3=list(candidates(3)); all4=list(candidates(4))
assert len(all3)==120, len(all3)
assert len(all4)==30, len(all4)
for H in all3:
    E=free_graph(H)
    cyc=cycles_on_free_edges(E)
    assert len(cyc)==1 and len(cyc[0])==3, (H,cyc)
    connectors={line for line in V if sum(line in T for T in H)==2}
    leaves=set(V)-connectors
    expected={tuple(sorted(q)) for q in combinations(leaves,2)}
    assert set(cyc[0])==expected
for H in all4:
    E=free_graph(H)
    assert len(E)==3 and set(degree_profile(E))=={1}
# A=4, B>=2: 2B lines have one transverse conic intersection each,
# necessitating >=2B ordinary conic–line nodes, but N_CL=2.
print('PURE_LINE_TRIPLE_INCIDENCE_CLASSIFICATION_OK',len(all3),len(all4))

r,u,v=s.symbols('r u v')
Q=lambda X,Y,Z,U=u,W=v: s.expand(U**2*X**2+W**2*Y**2+Z**2-2*U*W*X*Y-2*U*X*Z-2*W*Y*Z)
E1=Q(1,1,1)
E2=Q(r,1,1)
E3=Q(r,1,r)
assert s.simplify((E2-E1)-u*(r-1)*((r+1)*u-2*v-2))==0
assert s.simplify((E3-E2)+(r-1)*(2*r*u-r+2*v-1))==0
U=(r+3)/(3*r+1)
W=(r-1)**2/(2*(3*r+1))
assert s.factor(E1.subs({u:U,v:W}))==(r-1)**2*(r**2-18*r+1)/(4*(3*r+1)**2)
poly=r*r-18*r+1

def mod_minpoly(expr):
    N,D=map(s.expand,s.cancel(expr).as_numer_denom())
    assert s.rem(D,poly,r)!=0
    return s.factor(s.rem(N,poly,r))
for P in ((1,1,1),(r,1,1),(r,1,r)):
    assert mod_minpoly(Q(*P,U,W))==0
assert mod_minpoly(U.subs(r,1/r)-W)==0
assert mod_minpoly(W.subs(r,1/r)-U)==0
assert s.expand(Q(0,s.Symbol('Y'),s.Symbol('Z'))-(v*s.Symbol('Y')-s.Symbol('Z'))**2)==0
assert s.expand(Q(s.Symbol('X'),0,s.Symbol('Z'))-(u*s.Symbol('X')-s.Symbol('Z'))**2)==0
assert s.expand(Q(s.Symbol('X'),s.Symbol('Y'),0)-(u*s.Symbol('X')-v*s.Symbol('Y'))**2)==0
M=s.Matrix([[u*u,-u*v,-u],[-u*v,v*v,-v],[-u,-v,1]])
assert s.factor(M.det())==-4*u*u*v*v
# The three line-only double points and three pure line triple points avoid Q.
for P in ((0,1,1),(1,0,1),(r,1,0),(1,0,0),(0,1,0),(0,0,1)):
    assert mod_minpoly(Q(*P,U,W))!=0, P
# All possible parameters have exactly two distinct roots, reciprocal to each other.
assert s.factor(poly.subs(r,0))!=0
assert s.factor(poly.subs(r,1))!=0
assert s.discriminant(poly,r)==320
assert s.expand(r*r*poly.subs(r,1/r))==poly
print('PROJECTIVE_NORMAL_FORM_AND_RECIPROCAL_ROOTS_OK')
# Arithmetic for m=8, k=1, d=6: r=4, tau=36, t+n3=9, n2=9-n3.
assert 4**2-4*7+7**2-1==36
for n3 in range(6,10):
    t=9-n3; n2=9-n3
    assert n2+2*t+3*n3==27 and n2+3*t+4*n3==36
    assert 8+n2+s.Rational(3,4)*n3>=6+s.Rational(5,2)*t
print('NEAR_FREE_NUMERICAL_CONSTRAINTS_OK')
print('RIGIDITY_REPLAY_OK')
