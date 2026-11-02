#!/usr/bin/env python3
"""Exact symbolic and numerical checks for the friendship-graph Connes metric."""
import sympy as s
import numpy as np
from fractions import Fraction

a,b=s.symbols('a b', real=True)

def commutator(p):
    n=len(p); K=s.zeros(n)
    for u,v in [(0,1),(0,2),(1,2)] + ([(0,3),(0,4),(3,4)] if n==5 else []):
        K[u,v]=p[v]-p[u];K[v,u]=-K[u,v]
    return K

# Check all principal-minor reduction matrices and exact characteristic polynomials.
K3=commutator([0,a,b]);K5=commutator([0,a,b,-a,-b])
L3=s.expand(a*a+b*b+(a-b)**2)
L5=s.expand(2*(a*a+b*b)+(a-b)**2)
assert s.factor(K3.charpoly().as_expr())==s.factor(s.Symbol('lambda')*(s.Symbol('lambda')**2+L3))
lam=s.Symbol('lambda')
assert s.expand(K5.charpoly(lam).as_expr()-lam*(lam*lam+(a-b)**2)*(lam*lam+L5))==0
# Exact optimizations as completed squares.
assert s.simplify(L3.subs(b,a/s.Integer(2))-s.Rational(3,2)*a*a)==0
assert s.simplify(L3.subs(b,-a).subs(a,a/s.Integer(2))-s.Rational(3,2)*a*a)==0  # a is here the leaf contrast
assert s.simplify(L5-s.Rational(8,3)*a*a-3*(b-a/3)**2)==0
# Tests for every friendship graph from one to eight triangles at exact optimizer.
for m in range(1,9):
    n=2*m+1
    edges=[]
    for i in range(m):
        u,v=1+2*i,2+2*i
        edges += [(0,u),(0,v),(u,v)]
    def norm(x):
        A=np.zeros((n,n))
        for u,v in edges:
            A[u,v]=x[v]-x[u];A[v,u]=-A[u,v]
        return np.linalg.svd(A,compute_uv=False)[0]
    root=np.zeros(n);root[1]=np.sqrt(2/3);root[2]=root[1]/2
    assert abs(norm(root)-1)<1e-12
    within=np.zeros(n);within[1]=np.sqrt(1/6);within[2]=-within[1]
    assert abs(norm(within)-1)<1e-12
    if m>=2:
        cross=np.zeros(n);cross[1]=np.sqrt(3/8);cross[2]=cross[1]/3;cross[3]=-cross[1];cross[4]=-cross[2]
        assert abs(norm(cross)-1)<1e-12
        assert abs(cross[1]-cross[3]-np.sqrt(3/2))<1e-12
print('PASS: exact 3x3 and 5x5 characteristic polynomials, three completed-square optimizations, and all pair-type sharp optimizers for 1..8 petals.')
