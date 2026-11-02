#!/usr/bin/env python3
"""Reproduce spectral and optimization checks for the discrete-torus FMMC theorem.
Requires Python >=3.10, numpy>=1.24, scipy>=1.9.
Finite numerical checks supplement; they do not establish the all-size theorem.
"""
import itertools
import math
import numpy as np
from scipy.optimize import linprog

TOL=4e-9
checks=0

def ck(condition, message):
    global checks
    assert condition, message
    checks+=1

def constants(ns):
    c=[2-2*math.cos(2*math.pi/n) for n in ns]
    L=[2-2*math.cos(2*math.pi*(n//2)/n) for n in ns]
    H=sum(2/x for x in c)
    E=sum(y/x for x,y in zip(c,L))
    t=min(2/(E+1),1/H)
    a=[t/x for x in c]
    hold=1-2*sum(a)
    return c,L,H,E,t,a,hold

def parity_rule(ns):
    odds=[n for n in ns if n%2]
    return len(odds)<3 or (len(odds)==3 and any(n>3 for n in odds))

def ring_matrix(ns, aa):
    N=math.prod(ns)
    coords=list(itertools.product(*(range(n) for n in ns)))
    idx={x:i for i,x in enumerate(coords)}
    P=np.zeros((N,N), dtype=float)
    for x in coords:
        j=idx[x]
        for axis,n in enumerate(ns):
            for direction in [-1,1]:
                y=list(x);y[axis]=(y[axis]+direction)%n
                P[j,idx[tuple(y)]]+=aa[axis]
        P[j,j]+=1-2*sum(aa)
    return P,coords

def run(ns, do_full):
    c,L,H,E,t,a,hold=constants(ns)
    ck(t>0 and hold>=-TOL, f'feasibility: {ns}')
    ck((hold>1e-8)==parity_rule(ns),f'parity threshold: {ns} {hold}')
    ck(abs((1-H*t)-hold)<TOL, f'holding identity: {ns}')
    s=1-t
    eig=[]
    for k in itertools.product(*(range(n) for n in ns)):
        if all(ki==0 for ki in k):continue
        v=1-sum(ai*(2-2*math.cos(2*math.pi*ki/ni)) for ai,ki,ni in zip(a,k,ns))
        eig.append(v)
        ck(abs(v)<=s+TOL, f'spectrum bound: {ns} {k}')
    ck(abs(max(abs(v) for v in eig)-s)<TOL, f'exact SLEM: {ns}')
    # Independent LP using only the coordinate Fourier and lowest spectral inequalities.
    d=len(ns)
    obj=np.zeros(d+1);obj[-1]=1
    A=[]; b=[]
    for i in range(d):
        row=np.zeros(d+1);row[i]=-c[i];row[-1]=-1
        A.append(row);b.append(-1)
    row=np.array(L+[-1.0]);A.append(row);b.append(1)
    row=np.array([2.0]*d+[0.0]);A.append(row);b.append(1)
    sol=linprog(obj,A_ub=np.array(A),b_ub=np.array(b),bounds=[(0,None)]*d+[(0,None)],method='highs')
    ck(sol.success, f'linprog: {ns} {sol.message}')
    ck(abs(sol.x[-1]-s)<2e-8, f'linear optimality: {ns} {sol.x[-1]} {s}')
    ck(max(abs(sol.x[i]-a[i]) for i in range(d))<2e-8, f'LP uniqueness: {ns} {sol.x} {a}')
    if do_full:
        P,coords=ring_matrix(ns,a)
        ck(np.max(abs(P-P.T))<TOL, f'symmetry: {ns}')
        ck(np.min(P)>=-TOL, f'nonnegative: {ns}')
        ck(np.max(abs(P.sum(axis=1)-1))<TOL, f'stochastic: {ns}')
        spec=np.linalg.eigvalsh(P)
        ck(abs(max(abs(spec[:-1]))-s)<TOL, f'full matrix spectrum: {ns}')
        for i,ni in enumerate(ns):
            fi=np.array([np.exp(2j*np.pi*x[i]/ni) for x in coords])
            ck(np.max(abs(P@fi-s*fi))<TOL, f'contrast eigenvector: {ns} {i}')
        # Nonhomogeneous perturbations: preserve nonnegativity/stochasticity by reducing
        # all original edge weights and adding unequal positive redistributions, never
        # treating these finite draws as an unrestricted mathematical proof.
        rng=np.random.default_rng(1752+len(ns)+sum(ns))
        for _ in range(4):
            delta=np.zeros_like(P)
            for j,x in enumerate(coords):
                for axis,n in enumerate(ns):
                    y=list(x);y[axis]=(y[axis]+1)%n
                    k=coords.index(tuple(y))
                    shift=float(rng.uniform(-.04,.04))*a[axis]
                    delta[j,k]+=shift;delta[k,j]+=shift
                    delta[j,j]-=shift;delta[k,k]-=shift
            W=P+delta
            if np.min(W)<-1e-11:continue
            eigW=np.linalg.eigvalsh(W)
            ck(max(abs(eigW[:-1]))>=s-2e-9,f'unrestricted perturbation: {ns}')

shapes=[(3,), (4,), (5,), (6,), (7,), (8,), (3,3), (3,4), (3,5), (4,4), (4,5),
        (5,5), (3,3,3), (3,3,4), (3,3,5), (3,5,7), (3,4,5),
        (3,3,3,3), (3,3,3,4), (3,3,3,5), (3,3,5,5), (5,5,5,5),
        (4,4,4,4), (3,3,3,3,4), (4,5,6), (4,6,8), (5,6,7), (3,5,8)]
for ns in shapes:
    run(ns, math.prod(ns)<=105)
# Exact rational anchor cases.
ck(abs(constants((3,3,3))[4]-0.5)<1e-12,'three triangles boundary t')
ck(abs(constants((3,3,3))[6])<1e-12,'three triangles zero holding')
ck(abs(constants((3,3,3,3))[4]-3/8)<1e-12,'four triangles budget t')
ck(abs(constants((3,3,3,3))[6])<1e-12,'four triangles zero holding')
ck(constants((3,3,5))[6]>0,'two triangles plus C5 positive holding')
ck(constants((5,5,5,5))[6]<1e-11,'four odd cycles zero holding')
print(f'PASS: {checks} numerical and analytic consistency assertions across {len(shapes)} torus shapes.')
