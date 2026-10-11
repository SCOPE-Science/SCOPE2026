#!/usr/bin/env python3
import itertools
import math
import numpy as np
from scipy.spatial import HalfspaceIntersection
from scipy.optimize import minimize

def stable_sets(n):
    out=[]
    for mask in range(1<<n):
        if all(not (((mask>>i)&1) and ((mask>>((i+1)%n))&1)) for i in range(n)):
            v=np.array([(mask>>i)&1 for i in range(n)],dtype=float)
            out.append(v)
    return out

def halfspace_vertices(n):
    hs=[]
    # -x_i <= 0
    for i in range(n):
        a=np.zeros(n); a[i]=-1.0
        hs.append(np.r_[a,0.0])
    # x_i+x_{i+1}-1 <= 0
    for i in range(n):
        a=np.zeros(n); a[i]=1.0; a[(i+1)%n]=1.0
        hs.append(np.r_[a,-1.0])
    interior=np.full(n,0.25)
    pts=HalfspaceIntersection(np.array(hs),interior).intersections
    # Deduplicate numerical copies.
    uniq=[]
    for p in pts:
        if not any(np.linalg.norm(p-q)<1e-7 for q in uniq):
            uniq.append(p)
    return uniq

def expected_vertices(n):
    out=stable_sets(n)
    if n%2==1:
        out.append(np.full(n,0.5))
    return out

def same_set(A,B,tol=1e-7):
    return len(A)==len(B) and all(any(np.linalg.norm(a-b)<tol for b in B) for a in A)

for n in range(3,13):
    got=halfspace_vertices(n)
    exp=expected_vertices(n)
    assert same_set(got,exp), (n,len(got),len(exp))

    if n%2==0:
        c=np.full(n,0.5)
        R2=n/4.0
        d2=np.array([np.sum((v-c)**2) for v in exp])
        assert np.max(np.abs(d2-R2))<2e-8
    else:
        alpha=(n-1)//2
        c=np.full(n,alpha/n)
        R2=(n*n-1)/(4*n)
        ss=stable_sets(n)
        for v in ss:
            k=int(round(float(v.sum())))
            gotd=float(np.sum((v-c)**2))
            want=(alpha*alpha+k)/n
            assert abs(gotd-want)<2e-9
        h=np.full(n,0.5)
        assert abs(float(np.sum((h-c)**2))-1/(4*n))<2e-9
        contacts=[v for v in ss if abs(float(np.sum((v-c)**2))-R2)<2e-9]
        assert len(contacts)==n
        assert all(abs(v.sum()-alpha)<1e-9 for v in contacts)
        assert np.max(np.abs(np.mean(contacts,axis=0)-c))<2e-9

for n in range(3,10):
    V=np.array(expected_vertices(n))
    if n%2==0:
        c0=np.full(n,0.5); R20=n/4.0
    else:
        alpha=(n-1)//2
        c0=np.full(n,alpha/n); R20=(n*n-1)/(4*n)
    x0=np.r_[c0,R20*1.01+1e-6]
    def obj(w): return w[-1]
    cons=[]
    for v in V:
        cons.append({'type':'ineq','fun':lambda w,v=v: w[-1]-np.sum((v-w[:-1])**2)})
    res=minimize(obj,x0,method='SLSQP',constraints=cons,options={'ftol':1e-12,'maxiter':5000})
    assert res.success,(n,res.message)
    assert abs(res.fun-R20)<5e-7,(n,res.fun,R20)
    assert np.max(np.abs(res.x[:-1]-c0))<2e-5,(n,res.x[:-1],c0)

print('VERIFY_OK frac-cycle-MEB n=3..12 vertices=yes formulas=yes n=3..9 full_epigraph=yes')
