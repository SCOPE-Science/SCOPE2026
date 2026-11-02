#!/usr/bin/env python3
"""Reproducible checks for the priced-matching complete-network design formulas.
Python 3 standard library only. Finite checks corroborate, but do not replace, the proof.
"""
from fractions import Fraction as F
from math import sqrt
import random

checks = 0

def check(cond, context):
    global checks
    checks += 1
    if not cond: raise AssertionError(context)


def laplacian(m, a, b):
    n=2*m
    out=[[F(0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            w=a if i//2==j//2 else b
            out[i][i]+=w;out[j][j]+=w
            out[i][j]-=w;out[j][i]-=w
    return out


def inverse(A):
    n=len(A)
    v=[[F(z) for z in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for p in range(n):
        k=next((k for k in range(p,n) if v[k][p]),None)
        if k is None:raise ZeroDivisionError('singular')
        v[p],v[k]=v[k],v[p]
        s=v[p][p]
        v[p]=[z/s for z in v[p]]
        for j in range(n):
            if j==p:continue
            s=v[j][p]
            if s: v[j]=[v[j][k]-s*v[p][k] for k in range(2*n)]
    return [row[n:] for row in v]


def determinant(A):
    v=[[F(z) for z in row] for row in A];n=len(A);d=F(1)
    for i in range(n):
        p=next((j for j in range(i,n) if v[j][i]),None)
        if p is None:return F(0)
        if p!=i:v[i],v[p]=v[p],v[i];d=-d
        v0=v[i][i];d*=v0
        for j in range(i+1,n):
            q=v[j][i]/v0
            for k in range(i+1,n):v[j][k]-=q*v[i][k]
    return d


def matrix_values(m, a, b):
    n=2*m
    L=laplacian(m,a,b)
    H=[[L[i][j]+F(1,n) for j in range(n)] for i in range(n)]
    Hinv=inverse(H)
    R=n*(sum(Hinv[i][i] for i in range(n))-1)
    T=determinant([row[:-1] for row in L[:-1]])
    return R,T


def spectral_values(m,a,b):
    n=2*m;k=m-1
    K=n*(F(k,n*b)+F(m,2*(k*b+a)))
    T=(n*b)**k *(2*(k*b+a))**m/n
    return K,T

for m in range(2,7):
    for a in [F(0),F(1,3),F(2),F(7,3)]:
        for b in [F(1,5),F(3,2)]:
            K1,T1=matrix_values(m,a,b)
            K2,T2=spectral_values(m,a,b)
            check(K1==K2,('resistance spectrum',m,a,b,K1,K2))
            check(T1==T2,('spanning-tree spectrum',m,a,b,T1,T2))
    k=m-1
    rD=F(2*m,2*m-1)
    rA=F(2*m*m,2*m*m-2*m+1)
    check(F(1)<rD<rA<F(2),('threshold order',m))
    check(rA-rD==F(2*m*(m-1),(2*m*m-2*m+1)*(2*m-1)),('gap',m))
    for r in [F(1,4),F(1,2),F(1),rD,F(11,10),rA,F(3,2),F(2),F(3)]:
        td=max(0.,float(F(2*m,1)/r-(2*m-1)))
        ta=max(0.,m*sqrt(float(F(2,1)/r-1))-k) if r<2 else 0.
        if r>=rD:check(td==0.,('tree pruning',m,r))
        if r>=rA:check(ta==0.,('resistance pruning',m,r))
        if rD<=r<rA:check(td==0 and ta>0,('disagreement',m,r))
        def kval(t): return (float(r)*t+2*k)*(k+m*m/(k+t))
        def dval(t): return (k+t)**m/(float(r)*t+2*k)**(2*m-1)
        for t in [0.,0.1,0.5,1.,2.,5.,10.,20.,40.]:
            check(kval(ta)<=kval(t)+1e-9,('A-opt',m,r,t,ta))
            check(dval(td)+1e-12>=dval(t),('D-opt',m,r,t,td))
        # Independent direct KKT derivative identity at rational trial points.
        for t in [F(0),F(1,3),F(2)]:
            U=r*t+2*k
            V=k+m*m/(k+t)
            direct=r*V-U*m*m/(k+t)**2
            formula=k*(r-F(m*m,1)*(2-r)/(k+t)**2)
            check(direct==formula,('KKT identity',m,r,t))

for gamma in [0.,.25,.75,1.,2.]:
    for m in [1000,10000]:
        r=1+gamma/m
        ta=max(0,m*sqrt(2/r-1)-(m-1))
        td=max(0,2*m/r-(2*m-1))
        check(abs(ta-max(0.,1-gamma))<.006,('A scaling',gamma,m,ta))
        check(abs(td-max(0.,1-2*gamma))<.006,('D scaling',gamma,m,td))

# Strict two-orbit uniqueness survives random independent nonuniform perturbations:
# midpoint strict convexity of trace-inverse and logdet objectives in a graph of six vertices.
rng=random.Random(18317)
m=3;n=2*m
for s in range(12):
    W=[]
    for z in range(2):
        L=[[F(0) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                c=F(1+rng.randrange(9),10)
                L[i][i]+=c;L[j][j]+=c;L[i][j]-=c;L[j][i]-=c
        W.append(L)
    def obj(L):
        H=[[L[i][j]+F(1,n) for j in range(n)] for i in range(n)]
        X=inverse(H)
        return n*(sum(X[i][i] for i in range(n))-1),determinant([row[:-1] for row in L[:-1]])
    v1=obj(W[0]);v2=obj(W[1]);mid=obj([[(W[0][i][j]+W[1][i][j])/2 for j in range(n)] for i in range(n)])
    check(mid[0]<(v1[0]+v2[0])/2,('strict trace inverse',s))
    check(mid[1]*mid[1]>v1[1]*v2[1],('strict determinant log concavity',s))

print('VERIFICATION_OK',checks,'checks')
