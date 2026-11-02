#!/usr/bin/env python3
"""Reproduce weight-two circular covering construction and small exact checks."""
from itertools import product
from collections import Counter, deque
from math import comb

def cyc_windows(s,k):
    return [tuple(s[(i+j)%len(s)] for j in range(k)) for i in range(len(s))]

def construct(k):
    N=1<<(k-1); edges=[]
    for w in range(1<<k):
        if w.bit_count()==2: edges.append(w)
    p=[1]+[0]*(k-2)
    for a in cyc_windows(p,k):
        v=0
        for b in a:v=2*v+b
        edges.append(v)
    adj=[[] for _ in range(N)];deg=[0]*N;indeg=[0]*N
    for w in edges:
        u=w>>1;v=w&(N-1);adj[u].append((v,w&1));deg[u]+=1;indeg[v]+=1
    assert deg==indeg
    root=next(i for i in range(N) if deg[i])
    stack=[(root,None)];out=[]
    while stack:
        v=stack[-1][0]
        if adj[v]:
            t,b=adj[v].pop();stack.append((t,b))
        else:
            _,b=stack.pop()
            if b is not None:out.append(b)
    out=out[::-1]
    assert len(out)==len(edges), (k,len(out),len(edges))
    wins=cyc_windows(out,k)
    C=Counter(wins)
    required={tuple((v>>j)&1 for j in range(k-1,-1,-1)) for v in range(1<<k) if v.bit_count()==2}
    assert required.issubset(C)
    assert len(out)==comb(k,2)+k-1
    assert sum(C[w]-1 for w in required)+(sum(count for w,count in C.items() if w not in required))==k-1
    return out

def exhaustive_small(k,opt):
    req={tuple(v) for v in product((0,1),repeat=k) if sum(v)==2}
    for length in range(1,opt):
        # rotational symmetry fix first 1 at position 0 for each nonzero candidate
        for rest in product((0,1),repeat=length-1):
            s=(1,)+rest
            if req.issubset(cyc_windows(s,k)):
                raise AssertionError((k,length,s))

for k in range(4,20):
    result=construct(k)
    if k<=6:exhaustive_small(k,len(result))
    print('CHECK',k,len(result),comb(k,2),''.join(map(str,result)) if k<=8 else '',flush=True)
print('VERIFY_OK all k=4..19 and exact exhaustive k=4..6')
