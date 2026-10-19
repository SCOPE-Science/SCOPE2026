#!/usr/bin/env python3
"""Exact rational checks for a finite hyperedge unanimity update model.

This executable checks finite instances only. The all-size statements rely
on the analytical proof in RESULT.md, not on these checks.
"""
from fractions import Fraction as F
from itertools import combinations
from math import ceil

checks = 0

def check(ok, message='exact check failed'):
    global checks
    assert ok, message
    checks += 1

# One mixed hyperedge: all possible local compositions and several probabilities.
for a in range(1, 15):
    for b in range(1, 15):
        k = a+b
        for p in (F(0), F(1, 5), F(1, 2), F(4, 5), F(1)):
            plus = (1-p)*F(a, k)
            minus = (1-p)*F(b, k)
            check(plus*b-minus*a == 0)
            check(plus*b*b+minus*a*a == (1-p)*a*b)
            check(a*b >= k-1)

# Exact dense linear system solver, suitable for small finite-state checks.
def solve(M, rhs):
    n=len(rhs)
    A=[list(row)+[rhs[i]] for i,row in enumerate(M)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if A[i][j]),None)
        if pivot is None:
            raise ArithmeticError('singular transient system')
        A[j],A[pivot]=A[pivot],A[j]
        v=A[j][j]
        A[j]=[u/v for u in A[j]]
        for i in range(n):
            if i==j or not A[i][j]:
                continue
            v=A[i][j]
            A[i]=[A[i][t]-v*A[j][t] for t in range(n+1)]
    return [A[i][-1] for i in range(n)]

def is_active(mask,edge):
    s=sum(bool(mask & (1<<v)) for v in edge)
    return 0<s<len(edge)

def update(mask, edge, opinion):
    out=mask
    for v in edge:
        if opinion:
            out|=(1<<v)
        else:
            out&=~(1<<v)
    return out

def experiment(n, layouts, p):
    # Each active hyperedge is chosen uniformly; adaptation cycles topology.
    states=[(x,t) for x in range(1<<n) for t in range(len(layouts))]
    index={state:j for j,state in enumerate(states)}
    count=len(states)
    M=[[F(int(i==j)) for j in range(count)] for i in range(count)]
    rhs_time=[F(0)]*count
    rhs_weight=[F(0)]*count
    rhs_endpoint=[F(0)]*count
    stop=[False]*count
    ell=min(len(e) for H in layouts for e in H)
    for i,(mask,t) in enumerate(states):
        H=[e for e in layouts[t] if is_active(mask,e)]
        if not H:
            stop[i]=True
            x=mask.bit_count()
            rhs_endpoint[i]=F(x*(n-x))
            continue
        rhs_time[i]=F(1)
        rhs_weight[i]=sum((F(len([v for v in e if mask&(1<<v)])*len([v for v in e if not mask&(1<<v)]),len(H)) for e in H),F(0))
        for edge in H:
            a=sum(bool(mask&(1<<v)) for v in edge)
            b=len(edge)-a
            prop_factor=F(1-p,len(H))
            for next_mask,prob in ((update(mask,edge,1),F(a,len(edge))),
                                   (update(mask,edge,0),F(b,len(edge)))):
                M[i][index[(next_mask,t)]]-=prop_factor*prob
            if p:
                M[i][index[(mask,(t+1)%len(layouts))]]-=F(p,len(H))
    times=solve(M,rhs_time)
    weighted=solve(M,rhs_weight)
    endpoints=solve(M,rhs_endpoint)
    B=F(n*n,4*(1-p)*(ell-1))
    for i,(mask,t) in enumerate(states):
        x=mask.bit_count()
        phi=F(x*(n-x))
        check(phi==(1-p)*weighted[i]+endpoints[i])
        check(times[i] <= phi/((1-p)*(ell-1)))
        check(times[i] <= B)
        if stop[i]:
            check(times[i]==0 and weighted[i]==0 and endpoints[i]==phi)
    return states,times,weighted,endpoints

E=lambda *v: tuple(v)
for n,layouts in [
    (2,[[E(0,1)]]),
    (3,[[E(0,1),E(1,2)]]),
    (3,[[E(0,1,2)]]),
    (4,[[E(0,1),E(1,2),E(2,3)]]),
    (4,[[E(0,1,2),E(1,2,3)]]),
    (4,[[E(0,1),E(2,3)]]),
    (4,[[E(0,1),E(1,2),E(2,3),E(0,3)]]),
    (4,[[E(0,1,2,3)]]),
    (4,[[E(0,1),E(1,2)], [E(1,2),E(2,3)]]),
    (4,[[E(0,1,2),E(1,2,3)], [E(0,1),E(2,3)]]),
    (4,[[E(0,1),E(0,2),E(0,3)], [E(1,2),E(1,3),E(2,3)]]),
]:
    for p in (F(0),F(1,3),F(2,3)):
        states,times,weighted,endpoints=experiment(n,layouts,p)
        if len(layouts)==1 and p==0 and all(len(e)==2 for e in layouts[0]):
            vertices={v for e in layouts[0] for v in e}
            reach={min(vertices)}
            while True:
                grown=reach | {v for e in layouts[0] if set(e)&reach for v in e}
                if grown==reach: break
                reach=grown
            if reach==set(range(n)):
                for (mask,_),tm in zip(states,times):
                    check(tm==mask.bit_count()*(n-mask.bit_count()))
# Sharpness of the all-size active-edge factor: one N-vertex edge, 1 supporter.
for ell in range(2,15):
    a,b=1,ell-1
    phi=a*b
    check(phi==ell-1)
    check(F(phi,ell-1)==1)
print(f'PASS: {checks} exact rational assertions')
