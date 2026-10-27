"""Reproducibility checks for the edge-midpoint tree mixing theorem.

Requires Python 3 and numpy; sympy is used only for exact Taylor checks.
Numerical tests illustrate, but do not replace, the all-tree proof.
"""
from fractions import Fraction
from itertools import permutations
import math
import random
import numpy as np
import sympy as sp

checks=0

def check(ok, name):
    global checks
    checks+=1
    if not ok: raise AssertionError(name)

def mat_identity(n, zero=0, one=1):
    return [[one if i==j else zero for j in range(n)] for i in range(n)]

def prod(A,B):
    n=len(A)
    return [[sum((A[i][k]*B[k][j] for k in range(n)),0) for j in range(n)] for i in range(n)]

def perm_matrix(n, u,v):
    out=mat_identity(n)
    out[u],out[v]=out[v],out[u]
    return out

def edge_step(n,u,v,a,h):
    c=h*a/(1+h*a)
    M=mat_identity(n)
    for i in (u,v):
        M[i][i]-=c
    M[u][v]+=c; M[v][u]+=c
    return M

def edge_factors(tree, rates, n, h):
    M=mat_identity(n)
    for (u,v),a in zip(tree,rates):
        M=prod(edge_step(n,u,v,a,h),M)
    return M

def signature(tree,n):
    P=mat_identity(n)
    active=[]
    for u,v in tree:
        active.append((P[u].index(1),P[v].index(1)))
        P=prod(perm_matrix(n,u,v),P)
    cyc=[0];x=0
    for _ in range(n-1):
        x=next(i for i in range(n) if P[i][x]==1)
        cyc.append(x)
    check(len(set(cyc))==n,'limiting permutation is single cycle')
    pos={v:i for i,v in enumerate(cyc)}
    distances=[abs(pos[u]-pos[v]) for u,v in active]
    return P,active,distances,cyc

def predicted_gammas(dists,rates,n):
    return [4/n*sum(math.sin(math.pi*k*d/n)**2/a for d,a in zip(dists,rates)) for k in range(1,n)]

def spectral_nonunit(M):
    e=np.linalg.eigvals(np.asarray(M,dtype=float))
    ordered=sorted(e,key=lambda z:abs(z-1))
    check(abs(ordered[0]-1)<1e-7,'conservation eigenvalue')
    return max(abs(z) for z in ordered[1:])

for n in range(2,9):
    for shape in ('path','star'):
        tree=[(i,i+1) for i in range(n-1)] if shape=='path' else [(0,i) for i in range(1,n)]
        rates=[1]*len(tree)
        P,active,ds,cyc=signature(tree,n)
        if shape=='path':
            check(sorted(ds)==list(range(1,n)),'path transformed chord distances')
        else:
            check(all(d==1 or d==n-1 for d in ds),'star transformed chords adjacent')
        gammas=predicted_gammas(ds,rates,n)
        expected=2.0 if shape=='path' else 4*(n-1)/n*math.sin(math.pi/n)**2
        check(abs(min(gammas)-expected)<1e-12,'leading spectral coefficient')
        for h in (Fraction(1,4),Fraction(1,1),Fraction(11,3)):
            M=edge_factors(tree,[Fraction(a) for a in rates],n,h)
            for i in range(n):
                check(sum(M[i])==1,'exact row stochasticity')
                check(sum(M[j][i] for j in range(n))==1,'exact column stochasticity')
                check(all(M[i][j]>=0 for j in range(n)),'exact entrywise positivity')
            rho=spectral_nonunit(M)
            check(rho<1-1e-10,'strict finite-step mixing')
        for h in (10000.,100000.):
            rho=spectral_nonunit(edge_factors(tree,rates,n,h))
            check(abs(h*(1-rho)-expected)<0.008,'large step spectral asymptotic')
        if n>=4:
            h=0.0001
            mu=2*(1-math.cos(math.pi/n)) if shape=='path' else 1
            rho=spectral_nonunit(edge_factors(tree,rates,n,h))
            check(abs((1-rho)/h-mu)<0.01,'small step spectral asymptotic')

# Exact first-order matrix derivative with reciprocal step t=1/h.
t=sp.symbols('t')
for n in (3,4,5):
    for tree in ([ (i,i+1) for i in range(n-1)], [(0,i) for i in range(1,n)]):
        rates=[sp.Rational(i+2,2) for i in range(n-1)]
        M=sp.eye(n);P=sp.eye(n);V=sp.zeros(n)
        for (u,v),a in zip(tree,rates):
            vct=sp.eye(n)[:,u]-sp.eye(n)[:,v]
            pe=sp.eye(n)-vct*vct.T
            M=(pe+t/(t+a)*vct*vct.T)*M
            w=P.T*vct
            V+=w*w.T/a
            P=pe*P
        D=M.applyfunc(lambda x:sp.diff(x,t).subs(t,0))
        check(D==-P*V,'exact first derivative of ordered product')

# Random-tree checks on weighted instances, including unusual edge orders.
rng=random.Random(13819)
for n in range(3,9):
    for trial in range(15):
        tree=[(j,rng.randrange(j)) for j in range(1,n)]
        rng.shuffle(tree)
        rates=[Fraction(rng.randrange(1,7),rng.randrange(1,5)) for _ in tree]
        P,active,ds,cyc=signature(tree,n)
        gammas=predicted_gammas(ds,[float(a) for a in rates],n)
        check(min(gammas)>0,'positive Fourier attenuation for nonconstant modes')
        h=100000.
        rho=spectral_nonunit(edge_factors(tree,[float(a) for a in rates],n,h))
        check(abs(h*(1-rho)-min(gammas))<0.07,'random weighted tree perturbation rate')

print('VERIFY_OK',checks)
