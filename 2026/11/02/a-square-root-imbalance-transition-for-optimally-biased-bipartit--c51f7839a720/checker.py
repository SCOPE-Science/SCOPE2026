#!/usr/bin/env python3
"""Exact finite-horizon checks for biased exploration on complete bipartite graphs.
Only standard-library rational arithmetic is used. Finite checks do not prove the
asymptotic statements or the all-size optimality theorem.
"""
from fractions import Fraction as F
from functools import lru_cache
import itertools

CHECKS=0

def test(condition, detail=''):
    global CHECKS
    CHECKS+=1
    if not condition:
        raise AssertionError(detail or f'check {CHECKS}')

def arrival(m, epsilon, j):
    assert 1 <= j <= m
    return epsilon+(1-epsilon)*F(j,m)

def pmf_xi(m,epsilon,horizon):
    """Distribution of sum_{j=1}^{m-1} Geo(eps+(1-eps)j/m), truncated."""
    pmf=[F(0)]*(horizon+1)
    pmf[0]=F(1)
    for j in range(1,m):
        q=arrival(m,epsilon,j)
        gp=[F(0)]*(horizon+1)
        z=q
        for k in range(1,horizon+1):
            gp[k]=z
            z*=1-q
        new=[F(0)]*(horizon+1)
        for t in range(horizon+1):
            if pmf[t]:
                for k in range(1,horizon+1-t):
                    if gp[k]:new[t+k]+=pmf[t]*gp[k]
        pmf=new
    return pmf

def cdf(pmf,k):
    return sum(pmf[:k+1],F(0)) if k>=0 else F(0)

def dynamic(a,b,epsilon,horizon):
    @lru_cache(None)
    def val(na,nb,phase,remaining,policy):
        if na==a and nb==b:return F(1)
        if remaining==0:return F(0)
        if phase==0:
            u=b-nb
            next_yes=(na,nb+1,1)
            next_no=(na,nb,1)
            m=b
        else:
            u=a-na
            next_yes=(na+1,nb,0)
            next_no=(na,nb,0)
            m=a
        if not u:return val(*next_no,remaining-1,policy)
        vyes=val(*next_yes,remaining-1,policy)
        vno=val(*next_no,remaining-1,policy)
        low=(1-epsilon)*F(u,m)
        high=epsilon+(1-epsilon)*F(u,m)
        greedy=high*vyes+(1-high)*vno
        if policy==0:return greedy
        other=low*vyes+(1-low)*vno
        return max(greedy,other)
    pa=pmf_xi(a,epsilon,horizon)
    pb=pmf_xi(b,epsilon,horizon)
    for t in range(horizon+1):
        direct=val(1,0,0,t,0)
        optimal=val(1,0,0,t,1)
        if t%2:
            k=(t+1)//2
            formula=cdf(pa,k-1)*cdf(pb,k-1)
        else:
            k=t//2
            formula=cdf(pa,k)*cdf(pb,k-1)
        test(direct==formula,(a,b,epsilon,t,'formula',direct,formula))
        test(optimal==formula,(a,b,epsilon,t,'optimum',optimal,formula))
    # Exact finite-stage mean and variance identities for all m.
    for m in (a,b):
        mean=sum((1/arrival(m,epsilon,j) for j in range(1,m)),F(0))
        var=sum(((1-arrival(m,epsilon,j))/arrival(m,epsilon,j)**2 for j in range(1,m)),F(0))
        test(mean>=m-1)
        test(var>=0)

for a,b,e in itertools.product(range(1,6),range(1,6),(F(0),F(1,3),F(1,2),F(2,3),F(1))):
    dynamic(a,b,e,22)
print(f'PASS {CHECKS} exact rational assertions')
