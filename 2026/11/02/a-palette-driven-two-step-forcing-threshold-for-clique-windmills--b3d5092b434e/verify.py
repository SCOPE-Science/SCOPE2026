#!/usr/bin/env python3
"""Independent exact checks of nonchromatic palette windmill forced completion.

Usage: python3 verify.py
No external packages. This explicitly examines original graph neighbourhoods.
"""
from itertools import product
from collections import Counter
from math import comb, factorial


def falling(n, k):
    if n < k:
        return 0
    z = 1
    for a in range(k): z *= n-a
    return z


def graph(r, m):
    n=1+r*m
    adj=[set() for _ in range(n)]
    for i in range(m):
        block=[0]+list(range(1+i*r,1+(i+1)*r))
        for u in block:
            for v in block:
                if u!=v:adj[u].add(v)
    return [tuple(sorted(x)) for x in adj]


def succeeds(assign, adj, q):
    a=list(assign)
    for v, nb in enumerate(adj):
        if a[v] != q and any(a[w]==a[v] for w in nb):
            return False
    while True:
        news={}
        for v,nb in enumerate(adj):
            if a[v]!=q: continue
            allowed=set(range(q))-set(a[w] for w in nb if a[w]!=q)
            if len(allowed)==1:news[v]=next(iter(allowed))
        if not news:break
        for v,c in news.items():a[v]=c
    return all(c!=q for c in a) and all(a[v]!=a[w] for v,nb in enumerate(adj) for w in nb)


def coeff_formula(r,m,q):
    t=q-1
    cover=sum((-1)**j*comb(t,j)*falling(t-j,r)**m for j in range(t+1))
    return Counter({r*m:q*cover, r*m+1:q*falling(t,r)**m})


def run():
    cases=[(2,1,4),(2,2,4),(2,3,4),(2,2,5),(2,3,5),(2,2,6),(3,1,5),(3,2,5)]
    summary=[]
    for r,m,q in cases:
        adj=graph(r,m); n=len(adj)
        d=Counter()
        for seq in product(range(q+1),repeat=n):
            if succeeds(seq,adj,q):d[n-seq.count(q)]+=1
        expected=coeff_formula(r,m,q)
        assert +d==+expected,(r,m,q,sorted(d.items()),sorted(expected.items()))
        cover=expected[r*m]//q
        assert (cover>0)==(r+1<q<=r*m+1)
        summary.append((r,m,q,dict(sorted(d.items()))))
    print('VERIFY_OK nonchromatic_palettes',summary)

if __name__=='__main__':run()
