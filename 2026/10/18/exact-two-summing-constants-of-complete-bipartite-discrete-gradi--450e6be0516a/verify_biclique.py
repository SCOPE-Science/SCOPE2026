#!/usr/bin/env python3
"""Finite checks for the complete-bipartite gradient norm formula.
Uses rational arithmetic for projection/second-moment identities and floating
point arithmetic only for the square-root witness normalization.
No external dependencies. Run: python3 verify_biclique.py
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt, isclose


def add(X, Y):
    return [[x+y for x,y in zip(row,other)] for row,other in zip(X,Y)]

def scale(c,X):
    return [[c*x for x in row] for row in X]

def mmul(X,Y):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]

def trans(X):
    return [list(x) for x in zip(*X)]

def outer(x):
    return [[u*v for v in x] for u in x]

def proj(a,b):
    n=a+b
    eye=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    pa=[[F(int(i==j and i<a))-F(int(i<a and j<a),a) for j in range(n)] for i in range(n)]
    pb=[[F(int(i==j and i>=a))-F(int(i>=a and j>=a),b) for j in range(n)] for i in range(n)]
    w=[F(1,a)]*a+[-F(1,b)]*b
    cc=F(1,a)+F(1,b)
    pc=[[w[i]*w[j]/cc for j in range(n)] for i in range(n)]
    allones=[[F(1,n) for j in range(n)] for i in range(n)]
    assert add(add(pa,pb),pc)==add(eye,scale(-1,allones))
    for p in (pa,pb,pc):
        assert mmul(p,p)==p
    for p,q in ((pa,pb),(pa,pc),(pb,pc)):
        assert mmul(p,q)==scale(0,p)
    return (pa,pb,pc)

def mv(P,x):
    return [sum(t*v for t,v in zip(row,x)) for row in P]

def maxedge(x,a,b):
    return max(abs(x[i]-x[j]) for i in range(a) for j in range(a,a+b))

identities=0
witnesses=0
for a,b in product(range(1,9),repeat=2):
    n=a+b
    PA,PB,PC=proj(a,b)
    edges=[]
    for i in range(a):
        for j in range(a,n):
            v=[F(0)]*n
            v[i]=F(1);v[j]=-F(1)
            edges.append(v)
    # Independently sum the edge covariance directly, then compare with orbit-decomposed expression.
    moment=[[F(0) for j in range(n)] for i in range(n)]
    for v in edges:moment=add(moment,outer(v))
    moment=scale(F(1,a*b),moment)
    RHS=add(add(scale(F(1,a),PA),scale(F(1,b),PB)),scale(F(1,a)+F(1,b),PC))
    assert moment==RHS
    identities+=n*n
    # Directly evaluate the explicitly norming family from orthogonal blocks.
    S=(a-1)/sqrt(a)+(b-1)/sqrt(b)+sqrt(1/a+1/b)
    blocks=[(PA, S/sqrt(a) if a>1 else 0),
            (PB, S/sqrt(b) if b>1 else 0),
            (PC, S*sqrt(1/a+1/b))]
    xs=[]
    for v in edges:
        u=[0.0]*n
        for P,lam in blocks:
            if lam:
                w=mv(P,v)
                for i in range(n):u[i]+=float(w[i])/lam
        x=[S/sqrt(a*b)*t for t in u]
        assert isclose(sum(float(t)*y for t,y in zip(v,x)), S/sqrt(a*b), rel_tol=2e-11, abs_tol=2e-11)
        assert isclose(maxedge(x,a,b),S/sqrt(a*b),rel_tol=2e-11,abs_tol=2e-11)
        xs.append(x)
        witnesses+=1
    gram=[[sum(v[i]*v[j] for v in xs) for j in range(n)] for i in range(n)]
    target=add(add(PA,PB),PC)
    for i in range(n):
        for j in range(n):
            assert isclose(gram[i][j],float(target[i][j]),rel_tol=4e-11,abs_tol=4e-11),(a,b,i,j,gram[i][j],target[i][j])
    identities+=n*n
    assert isclose(sum(maxedge(v,a,b)**2 for v in xs),S*S,rel_tol=2e-11)
print(f'PASS: {identities} rational/projector and floating Gram entries and {witnesses} norming-edge checks over 64 bicliques (a,b<=8).')
