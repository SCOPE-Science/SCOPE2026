#!/usr/bin/env python3
"""Direct simple-graph 1-WL and predicted pointed Mobius-ladder wavefronts."""
from collections import Counter

def colors(parts):
    c={}
    for k,p in enumerate(parts):
        for x in p:
            assert x not in c
            c[x]=k
    return c

def predicted(m,r):
    if r==0:return [{0},set(range(1,m+1))]
    if r==1:return [{0},{1,m},set(range(2,m))]
    if r==2:return [{0},{1,m},{2},{m-1},set(range(3,m-1))]
    v=[{i} for i in range(0,min(r,m)+1)]
    v +=[{i} for i in range(max(m-r+1,r+1),m+1)]
    interior=set(range(r+1,m-r+1))
    if interior:v.append(interior)
    return v

def refine(c,adj):
    sig={u:(c[u],tuple(sorted(Counter(c[v] for v in adj[u]).items()))) for u in range(len(adj))}
    labels={a:k for k,a in enumerate(sorted(set(sig.values())))}
    return {u:labels[sig[u]] for u in sig}

def split_equal(c,pred,m):
    # all 2m vertices are grouped by their predicted reflection-shell class
    bypred={}
    for i in range(2*m):
        p=pred[min(i,2*m-i)]
        bypred.setdefault(p,set()).add(c[i])
    if any(len(colors)!=1 for colors in bypred.values()):return False,'predicted class split'
    val=[next(iter(colors)) for colors in bypred.values()]
    if len(val)!=len(set(val)):return False,'predicted classes merged'
    return True,None

def run(m):
    n=2*m
    adj=[{(i-1)%n,(i+1)%n,(i+m)%n} for i in range(n)]
    c={i:int(i!=0) for i in range(n)}
    steps=max(3,m//2)
    for r in range(steps+1):
        p=colors(predicted(m,r))
        assert len(p)==m+1,(m,r)
        ok,ex=split_equal(c,p,m)
        assert ok,(m,r,ex)
        if r<steps:
            nc=refine(c,adj)
            assert len(set(nc.values()))>=len(set(c.values()))
            c=nc
    assert len(set(refine(c,adj).values()))==len(set(c.values())), (m, "unexpected late split")
    assert len(set(c.values()))==m+1
    if steps>0:
        r=steps-1
        assert len(set(colors(predicted(m,r)).values()))<m+1
    return steps

for m in range(4,121):
    assert run(m)==max(3,m//2)
print('DIRECT PASS: all m=4..120, exact round-by-round predicted partitions and stabilization depths')
