#!/usr/bin/env python3
"""Exact finite census for semi-induced red-red-blue stars in three-class graphs.
No external dependencies. Exhaustive integer enumeration is the finite proof certificate.
"""
from math import comb

def score_from_degrees(n, ds):
    return sum(d*(d-1)*(n-1-d) for d in ds)

def clique_degrees(n,m):
    # Largest clique followed by one partial vertex and isolates.
    t=0
    while t<n and comb(t+1,2)<=m:
        t+=1
    s=m-comb(t,2)
    ans=[0]*n
    for i in range(t): ans[i]=t-1
    for i in range(s):
        ans[i]+=1
        ans[t]+=1
    assert sum(ans)==2*m
    return ans

def endpoint_scores(n,m):
    E=comb(n,2)
    qc=clique_degrees(n,m)
    qs=[n-1-d for d in clique_degrees(n,E-m)]
    return score_from_degrees(n,qc),score_from_degrees(n,qs)

def profile(n,a,b,c):
    assert min(a,b,c)>=0 and a+b+c==n
    m=comb(a+b,2)+a*c
    ds=[n-1]*a+[a+b-1]*b+[a]*c
    assert sum(ds)==2*m
    return m,score_from_degrees(n,ds)

def adj(n,a,b,c):
    edges=set()
    for u in range(n):
        for v in range(u+1,n):
            if (u<a+b and v<a+b) or (u<a and v>=a+b):
                edges.add((u,v))
    return edges

def raw_direct(n,edges):
    e=set(edges)
    output=0
    for center in range(n):
        nbrs=[v for v in range(n) if v!=center and (min(v,center),max(v,center)) in e]
        non=[v for v in range(n) if v!=center and (min(v,center),max(v,center)) not in e]
        for r1 in nbrs:
            for r2 in nbrs:
                if r1==r2:continue
                for blue in non:
                    if blue not in (r1,r2):output+=1
    return output

allprofiles=0
for n in range(2,21):
    exceptions=[]
    for a in range(n+1):
        for b in range(n-a+1):
            c=n-a-b
            m,val=profile(n,a,b,c)
            qc,qs=endpoint_scores(n,m)
            allprofiles+=1
            if val<min(qc,qs):exceptions.append((m,a,b,c,val,qc,qs))
            if n<=8:
                ed=adj(n,a,b,c)
                assert len(ed)==m
                assert raw_direct(n,ed)==val
    if n<20:
        assert not exceptions, (n,exceptions)
    else:
        assert exceptions==[(165,6,12,2,7308,7860,7344),(167,7,11,2,6992,7370,7072)], exceptions
    print('n=%d profiles=%d strict_end_point_improvements=%d%s' %
          (n, comb(n+2,2), len(exceptions), (' values='+str(exceptions)) if exceptions else ''))
assert allprofiles==comb(23,3)-1-3  # n=2 through 20: C(23,3)-C(4,3)=1771-4
for a,b,c in [(6,12,2),(7,11,2)]:
    n=20
    edges=adj(n,a,b,c)
    m,val=profile(n,a,b,c)
    assert len(edges)==m
    assert raw_direct(n,edges)==val
print('ALL CHECKS PASSED; profiles=%d; direct_raw_checks=2, plus all n<=8; first_order=20; unique_triples_at_each_improving_m=yes'%allprofiles)
