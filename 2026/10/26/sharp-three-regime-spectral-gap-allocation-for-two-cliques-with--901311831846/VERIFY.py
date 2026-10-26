#!/usr/bin/env python3
"""Checks the proposed exact solution for the two-clique biclique-gateway graph.
The all-parameter theorem is proved in RESULT.md, not inferred from this test.
Requires numpy and sympy.
"""
import math
import numpy as np
import sympy as sp


def edges(n,k):
    E=[]
    for o in (0,n):
        for i in range(n):
            for j in range(i+1,n):
                label='a' if i<k and j<k else ('c' if i>=k and j>=k else 'd')
                E.append((o+i,o+j,label))
    for i in range(k):
        for j in range(k):E.append((i,n+j,'b'))
    return E


def lap(n,k,w):
    L=np.zeros((2*n,2*n))
    for i,j,c in edges(n,k):
        q=w[c];L[i,i]+=q;L[j,j]+=q;L[i,j]-=q;L[j,i]-=q
    return L


def optimal(n,k,B=1.):
    assert n>=3 and 1<=k<n and B>0
    u=n-k;r=u/k
    tau=1/math.sqrt(2*(k+1))
    if r>=1/6:
        t=.5
    else:
        disc=(1-3*r)**2-8*r*r
        tminus=2*r/(1-3*r+math.sqrt(disc))
        t=max(tminus,tau)
    H=.5+r*(t+1.5+.5/t)
    F=n/2+u/(2*t)+2*u*(t+1)+(k-1)*max(0,1-H)
    val=B/F
    w={'a':val/k*max(0,1-H), 'c':0., 'd':val*(t+1)/k,
       'b':val*(n*(t+1)/k-1)/(2*k*t)}
    budget=(k*(k-1)*w['a']+u*(u-1)*w['c']+2*k*u*w['d']+k*k*w['b'])
    return val,t,w,budget

cases=0
for n in range(3,21):
    for k in range(1,n):
        v,t,w,b=optimal(n,k)
        l2=np.linalg.eigvalsh(lap(n,k,w))[1]
        assert abs(v-l2)<=2e-9,(n,k,v,l2,w)
        assert abs(b-1)<2e-11,(n,k,b)
        cases+=1
print('PASS full Laplacian eigenvalue and budget tests:',cases)

# Independently verify against unconstrained asymmetric weight vectors.
rng=np.random.default_rng(20261023)
checks=0
for n in range(3,12):
    for k in range(1,n):
        v,_,_,_=optimal(n,k)
        E=edges(n,k)
        for _ in range(45):
            w=rng.dirichlet(np.ones(len(E))*.8)
            L=np.zeros((2*n,2*n))
            for (i,j,_),z in zip(E,w):
                L[i,i]+=z;L[j,j]+=z;L[i,j]-=z;L[j,i]-=z
            assert np.linalg.eigvalsh(L)[1]<=v+1e-10,(n,k)
            checks+=1
print('PASS asymmetric global upper-bound samples:',checks)

# Symbolic invariant quotient and scalar derivative certificates.
k,u,d,b,z,t=sp.symbols('k u d b z t',positive=True)
Q=sp.Matrix([[u*d,-u*d,0,0],[-k*d,k*d,0,0],
             [0,0,u*d+2*k*b,-u*d],[0,0,-k*d,k*d]])
char=sp.factor((z*sp.eye(4)-Q).det())
assert sp.simplify(char-z*(z-(k+u)*d)*(z**2-((k+u)*d+2*k*b)*z+2*k*k*b*d))==0
print('PASS 4 by 4 equitable symbolic characteristic polynomial')
K,U,T=sp.symbols('K U T',positive=True)
R=U/K
H=sp.Rational(1,2)+R*(T+sp.Rational(3,2)+1/(2*T))
F0=(K+U)/2+U/(2*T)+2*U*(T+1)
F1=sp.factor(F0+(K-1)*(1-H))
assert sp.simplify(sp.diff(F1,T)-U*(1+1/K-1/(2*K*T**2)))==0
assert sp.simplify((F0-F0.subs(T,1/(2*T)))-U*(T-1/(2*T)))==0
print('PASS scalar stationary and involution identities')

for n,k in ((7,5),(7,6),(8,7),(9,8),(11,10),(15,14),(28,24),(27,24)):
    v,t,w,_=optimal(n,k)
    print(f'CASE n={n} k={k} u={n-k}: t={t:.12g}, lambda={v:.12g}, a={w["a"]:.12g}')
print('ALL CHECKS PASS')
