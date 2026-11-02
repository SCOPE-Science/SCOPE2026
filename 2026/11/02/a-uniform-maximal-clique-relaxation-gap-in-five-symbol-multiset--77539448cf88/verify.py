#!/usr/bin/env python3
"""Exact finite and symbolic checks for five-symbol simplex clique gaps."""
from fractions import Fraction as F
from math import comb,ceil
from itertools import combinations_with_replacement

Q=5
OFFSETS={0:F(4,5),1:F(-1,5),2:F(1,15),3:F(-1,30)}

def compositions(n,k=Q):
    if k==1:
        yield (n,)
    else:
        for a in range(n+1):
            for tail in compositions(n-a,k-1):yield (a,)+tail

def bump(x,i,d):
    v=list(x);v[i]+=d
    return tuple(v)

def change(x,i,n):
    outside=[x[j] for j in range(Q) if j!=i]
    t=sum(outside)
    if x[i]<n-3 or t>3:return F(0)
    if any(a>1 for a in outside):return F(0)
    return OFFSETS.get(t,F(0))

def weight(x,n):
    return F(1,5)+sum((change(x,i,n) for i in range(Q)),F(0))

def verify_local_patterns():
    # Valid for all n >= 8: feasibility depends only on off-center total <= 4.
    n=13;i=0
    lower=set()
    upper=set()
    for x in compositions(3,4):
        for t in range(4):
            if sum(x)!=t:continue
            v=(n-t,)+x
            for j in range(Q):
                if v[j]>0:lower.add(bump(v,j,-1))
                upper.add(bump(v,j,+1))
    for y in lower:
        s=sum(change(bump(y,j,+1),i,n) for j in range(Q))
        assert s<=0,('lower',y,s)
    for z in upper:
        s=sum(change(bump(z,j,-1),i,n) for j in range(Q) if z[j]>0)
        slack=F(Q-sum(a>0 for a in z),Q)
        assert s<=slack,('upper',z,s,slack)
    # Exact total modification in one corner.
    patch=sum((change((n-sum(v),)+v,0,n) for v in compositions(0,4)),F(0))
    for t in range(1,4):
        patch+=sum((change((n-t,)+v,0,n) for v in compositions(t,4)),F(0))
    assert patch==F(4,15),patch


def verify_n(n):
    V=list(compositions(n))
    p={x:weight(x,n) for x in V}
    assert all(F(0)<=t<=F(1) for t in p.values())
    assert sum(p.values(),F(0))==F(len(V),5)+F(4,3)
    for y in compositions(n-1):
        assert sum((p[bump(y,j,+1)] for j in range(Q)),F(0))<=1,('lower',n,y)
    for z in compositions(n+1):
        assert sum((p[bump(z,j,-1)] for j in range(Q) if z[j]>0),F(0))<=1,('upper',n,z)
    assert F(len(V),5)+F(4,3)>ceil(F(len(V),5))
    print('CHECKED n=%d vertices=%d lower=%d upper=%d fractional_lower=%s' % (
        n,len(V),comb(n+3,4),comb(n+5,4),str(F(len(V),5)+F(4,3))))

if __name__=='__main__':
    verify_local_patterns()
    print('SYMBOLIC_PATTERN_CHECK_OK')
    for n in [8,9,10,11,12,15,20]:verify_n(n)
    print('VERIFY_OK')
