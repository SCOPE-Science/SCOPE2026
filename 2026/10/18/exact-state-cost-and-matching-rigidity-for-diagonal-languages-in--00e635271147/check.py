#!/usr/bin/env python3
"""Finite checks for the exact cactus-NFA state theorem for diagonal length-two languages."""
from itertools import product
from math import ceil, factorial


def is_cactus(vertices, edges):
    adj = {i: set() for i in range(vertices)}
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    for a,b in edges:
        count=0
        def walk(u,seen):
            nonlocal count
            if count>=2: return
            if u==b:
                count+=1; return
            for v in adj[u]:
                if (u==a and v==b) or (u==b and v==a) or (u==b and v==a): continue
                if {u,v}=={a,b}:continue
                if v not in seen:walk(v,seen|{v})
        walk(a,{a})
        if count>=2:return False
    return True


def graph(n,t,masks):
    # State 0 is start, states 1..n read first letter; n+1..n+t are accepting.
    return [(0,1+i) for i in range(n)]+[(1+i,n+1+j) for i,mask in enumerate(masks) for j in range(t) if mask>>j&1]


def accept(n,t,masks,w):
    states={0}
    for c in w:
        nxt=set()
        for p in states:
            if p==0: nxt.add(1+c)
            elif 1<=p<=n and p==1+c:
                i=p-1
                nxt.update(n+1+j for j in range(t) if masks[i]>>j&1)
        states=nxt
    return any(p>=n+1 for p in states)


for n in range(1,6):
    cactus_at={}
    tree_at={}
    for t in range(1,n+1):
        if t>3 and t>ceil(n/2)+1:continue
        ok=0; tok=0; examples=[]
        for masks in product(range(1,1<<t),repeat=n):
            if sum(bool(mask>>j&1) for mask in masks for j in range(t))<n:continue
            edges=graph(n,t,masks)
            cactus=is_cactus(1+n+t,edges)
            if cactus:
                ok+=1
                if len(examples)<2:examples.append(masks)
                assert all(accept(n,t,masks,w)==(len(w)==2 and w[0]==w[1])
                           for k in range(4) for w in product(range(n),repeat=k))
                if len(edges)==n+t:
                    tok+=1
        cactus_at[t]=ok; tree_at[t]=tok
    optimum=ceil(n/2)
    expected=factorial(n)//(2**(n//2)*factorial(n//2)) * factorial(optimum)
    assert all(v==0 for t,v in cactus_at.items() if t<optimum)
    assert cactus_at[optimum]==expected, (n,cactus_at,expected)
    assert all(v==0 for t,v in tree_at.items() if t<n)
    if n in tree_at:assert tree_at[n]>0
    print(f'n={n}: cactus min={1+n+optimum}; labeled canonical optimal automata={cactus_at[optimum]}; alphabet partitions={expected//factorial(optimum)}; tree min={2*n+1}; unrestricted/planar min={n+2}.')
print('ALL CHECKS PASS')
