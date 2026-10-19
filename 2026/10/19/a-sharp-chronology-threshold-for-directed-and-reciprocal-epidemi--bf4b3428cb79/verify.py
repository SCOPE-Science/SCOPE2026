#!/usr/bin/env python3
"""Exact checks for chronological invasion thresholds in two-group SIS systems."""
import itertools
import math
import sympy as sp

TWO = sp.Integer(2)
s = sp.sqrt(2)
A = sp.diag(2,1)
B = sp.Matrix([[1,1],[0,1]])
C = sp.Matrix([[1,0],[1,1]])
H = sp.Matrix([[s,1],[1,s]])
D = sp.diag(1,2)

def perron(P):
    t, d = sp.trace(P), P.det()
    return sp.simplify((t + sp.sqrt(t*t-4*d))/2)

def check():
    assert A*B*C == sp.Matrix([[4,2],[1,1]])
    assert A*C*B == sp.Matrix([[2,2],[1,2]])
    assert sp.trace(A*B*C)==5 and sp.trace(A*C*B)==4
    assert (A*B*C).det()==(A*C*B).det()==2
    assert sp.simplify(perron(A*B*C)-(5+sp.sqrt(17))/2)==0
    assert sp.simplify(perron(A*C*B)-(2+sp.sqrt(2)))==0
    assert float(perron(A*B*C))>4>float(perron(A*C*B))
    P, Q = A*H*D*H, A*D*H*H
    assert P==sp.Matrix([[8,6*s],[3*s,5]])
    assert Q==sp.Matrix([[6,4*s],[4*s,6]])
    assert sp.trace(P)==13 and sp.trace(Q)==12
    assert P.det()==Q.det()==4
    assert float(perron(P))>12>float(perron(Q))
    assert sp.simplify(perron(P)-(13+3*sp.sqrt(17))/2)==0
    assert sp.simplify(perron(Q)-(6+4*sp.sqrt(2)))==0
    # Every permutation of three invertible symmetric matrices is isospectral.
    S = [sp.Matrix([[2,1],[1,3]]), sp.Matrix([[3,2],[2,4]]), sp.Matrix([[4,1],[1,2]])]
    specs=set()
    for z in itertools.permutations(S):
        M=z[0]*z[1]*z[2]
        specs.add((sp.trace(M),M.det()))
    assert len(specs)==1
    # Exact trace differences in the two parametric families.
    u, v, y, z, c, h = sp.symbols('u v y z c h',real=True)
    a=sp.diag(u,1)
    b=sp.eye(2)+y*sp.Matrix([[0,1],[0,0]])
    cc=sp.eye(2)+z*sp.Matrix([[0,0],[1,0]])
    assert sp.expand(sp.trace(a*b*cc)-sp.trace(a*cc*b)-y*z*(u-1))==0
    d=sp.diag(1,v)
    hh=sp.Matrix([[c,h],[h,c]])
    assert sp.expand(sp.trace(a*hh*d*hh)-sp.trace(a*d*hh*hh)-h*h*(u-1)*(v-1))==0
    print('PASS: exact products, determinant/spectral checks, permutation invariance and parametric trace laws')
if __name__=='__main__': check()
