"""Exact independent verification for component-type cross-covariance in G(n,p).

All enumerations are finite checks, not a proof for unrestricted n.
"""
from fractions import Fraction
from math import comb, factorial, log, exp
from itertools import combinations
from collections import defaultdict


def falls(n,k):
    v=1
    for j in range(k): v*=n-j
    return v


def graph_component_profiles(n,mask):
    adj=[[] for _ in range(n)]
    edges=list(combinations(range(n),2))
    for t,(u,v) in enumerate(edges):
        if mask>>t&1:
            adj[u].append(v);adj[v].append(u)
    seen=set(); comps=[]
    for i in range(n):
        if i in seen:continue
        stack=[i];seen.add(i); verts=[]
        while stack:
            v=stack.pop();verts.append(v)
            for j in adj[v]:
                if j not in seen:seen.add(j);stack.append(j)
        e=sum(len(adj[j]) for j in verts)//2
        degrees=tuple(sorted((len(adj[j]) for j in verts)))
        comps.append((len(verts),e,degrees))
    return comps


def enumerate_exact(n,p):
    q=1-p
    pairs=list(combinations(range(n),2))
    M=len(pairs)
    expect=defaultdict(Fraction); mixed=defaultdict(Fraction)
    shapes=set()
    for mask in range(1<<M):
        e=mask.bit_count(); weight=p**e*q**(M-e)
        comps=graph_component_profiles(n,mask)
        counts=defaultdict(int)
        for k,edges,degs in comps:
            counts[k,edges,degs]+=1
            counts[k,None,None]+=1
        expect.update({x:expect[x]+weight*a for x,a in counts.items()})
        keys=list(counts)
        for i,a in enumerate(keys):
            for b in keys[i+1:]:
                if a[0]!=b[0]:
                    mixed[tuple(sorted((a,b),key=repr))]+=weight*counts[a]*counts[b]
        shapes.update(keys)
    checks=0
    for (a,b),both in mixed.items():
        h,k=a[0],b[0]
        ratio=Fraction(falls(n-h,k),falls(n,k))*q**(-h*k)
        assert both==expect[a]*expect[b]*ratio, (n,p,a,b,both,expect[a]*expect[b]*ratio)
        checks+=1
    return checks


def verify():
    checks=0
    for n in range(3,7):
        for p in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
            checks+=enumerate_exact(n,p)
    for n in range(4,28):
        d={}
        for h in range(1,n):
            for k in range(1,n-h+1):
                if h==k: continue
                rho=Fraction(falls(n-h,k),falls(n,k))
                pstar=1-float(rho)**(1/(h*k))
                assert pstar>1/n-1.e-12,(n,h,k)
                d[(h,k)]=pstar; checks+=1
        for (h,k),v in d.items():
            if (h+1,k) in d:
                assert d[(h+1,k)]>v-1.e-13,(n,h,k)
                checks+=1
            if (h,k+1) in d:
                assert d[(h,k+1)]>v-1.e-13,(n,h,k)
                checks+=1
    print('PASS',checks,'exact pair-moment and numeric threshold checks')


if __name__=='__main__':
    verify()
