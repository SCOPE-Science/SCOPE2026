#!/usr/bin/env python3
"""Exact finite checks for bounded cycle-multiplicity partitions.
Each partition, not each labelled permutation, has unit weight.
This file checks finite counts only; it is not an infinite-limit proof.
"""
from itertools import product
from fractions import Fraction


def counts(cap, nmax, omitted=()):
    """Counts of partitions with each positive part used at most `cap` times."""
    omit=set(omitted)
    p=[0]*(nmax+1); p[0]=1
    for j in range(1,nmax+1):
        if j in omit: continue
        nxt=[0]*(nmax+1)
        for total,v in enumerate(p):
            if not v: continue
            for a in range(cap+1):
                x=total+a*j
                if x>nmax: break
                nxt[x]+=v
        p=nxt
    return p


def partitions(n,maxpart=None):
    if n==0:
        yield ()
        return
    if maxpart is None or maxpart>n: maxpart=n
    for j in range(maxpart,0,-1):
        for tail in partitions(n-j,j):
            yield (j,)+tail

checks=0
for r in (1,2,3):
    N=120
    q=counts(r,N)
    for n in range(1,15):
        b=0
        for p in partitions(n):
            if all(p.count(j)<=r for j in set(p)):
                b+=1
        assert b==q[n], (r,n,b,q[n])
        checks+=1
    for k in (1,2,3):
        rest=counts(r,N,range(1,k+1))
        for n in range(N+1):
            total=sum(rest[n-sum(j*a for j,a in enumerate(vec,1))]
                      for vec in product(range(r+1),repeat=k)
                      if sum(j*a for j,a in enumerate(vec,1))<=n)
            assert total==q[n],(r,k,n,total,q[n])
            checks+=1

# Exact marginal laws at finite sizes and bounded sup-norm deviations.
report=[]
for r in (1,2,3):
    N=480
    allq=counts(r,N)
    rest=counts(r,N,(1,2))
    n=480
    probs=[Fraction(rest[n-a-2*b],allq[n]) for a,b in product(range(r+1),repeat=2)]
    err=max(abs(z-Fraction(1,(r+1)**2)) for z in probs)
    report.append((r,allq[n].bit_length(),float(err)))
    assert sum(probs)==1
    checks+=1
print('BOUNDED_CYCLE_PARTITIONS_EXACT_OK',checks,'finite_checks',report)
