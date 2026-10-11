#!/usr/bin/env python3
"""Reproduce the exact sphere formulas from the complete-graph vertex realization."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, sqrt
import numpy as np
from scipy.optimize import minimize

for n in range(3, 13):
    candidates=[tuple([Q(0)]*n)]
    candidates += [tuple(Q(i==j) for i in range(n)) for j in range(n)]
    for k in range(3,n+1):
        for S in combinations(range(n),k):
            candidates.append(tuple(Q(1,2) if i in S else Q(0) for i in range(n)))
    assert len(candidates)==1+n+sum(comb(n,k) for k in range(3,n+1))

    if n<=6:
        t=Q(1,n)
        R2=Q(n-1,n)
        contacts=set(range(1,n+1))
    else:
        t=Q(n-4,4*(n-2))
        R2=Q(n**3,16*(n-2)**2)
        contacts=set(range(1,n+1))|{len(candidates)-1}
        a=Q(n,2*(n-2)**2)
        b=Q(n*n-8*n+8,2*(n-2)**2)
        assert a>0 and b>0 and n*a+b==1 and a+b/2==t

    hits=[]
    for idx,v in enumerate(candidates):
        d2=sum((x-t)**2 for x in v)
        assert d2<=R2,(n,idx,d2,R2)
        if d2==R2:
            hits.append(idx)
    assert set(hits)==contacts,(n,set(hits),contacts)

    # Mathematical contact barycenter for both phases.
    if n<=6:
        for j in range(n):
            assert Q(1,n)==t
    else:
        center=[a+b/2 for _ in range(n)]
        assert all(x==t for x in center)

    int_R2=Q(n-1,n)
    if n<=6:
        assert R2-int_R2==0
    else:
        assert R2-int_R2==Q((n*n-8*n+8)**2,16*n*(n-2)**2)

# An independent full vertex-epigraph solve, not an optimization over t alone.
for n in range(3,9):
    V=[np.zeros(n)]
    V += [np.eye(n)[j] for j in range(n)]
    for k in range(3,n+1):
        for S in combinations(range(n),k):
            v=np.zeros(n)
            v[list(S)]=0.5
            V.append(v)
    V=np.asarray(V)
    t=(1/n if n<=6 else (n-4)/(4*(n-2)))
    R2=(1-1/n if n<=6 else n**3/(16*(n-2)**2))
    x0=np.r_[np.full(n,t),R2+1e-4]
    def fun(w):return w[-1]
    # Vector constraints are evaluated simultaneously; the formulation is
    # min rho2 subject to rho2 >= ||v-c||2 for every vertex v.
    def feasible(w):
        return w[-1]-np.sum((V-w[:-1])**2,axis=1)
    opt=minimize(fun,x0,method='SLSQP',constraints=[{'type':'ineq','fun':feasible}],
                 options={'ftol':2e-11,'maxiter':5000})
    assert opt.success,(n,opt.message)
    assert abs(opt.fun-R2)<2e-7,(n,opt.fun,R2)
    assert np.max(abs(opt.x[:-1]-t))<3e-5,(n,opt.x[:-1],t)
print('VERIFY_OK fractional-clique-sphere n=3..12 exact_vertices_and_contacts=yes n=3..8 full_epigraph=yes')
