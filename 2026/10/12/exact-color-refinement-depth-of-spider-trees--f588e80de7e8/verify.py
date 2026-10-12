#!/usr/bin/env python3
from collections import defaultdict
import itertools

def spider(lengths):
    adj=[set()]
    meta={0:("center",None,None)}
    for L in lengths:
        verts=list(range(len(adj),len(adj)+L))
        adj.extend(set() for _ in verts)
        prev=0
        for x,v in enumerate(verts,1):
            adj[prev].add(v); adj[v].add(prev); prev=v
            meta[v]=("leaf" if x==L else "internal",x,L)
    return adj,meta

def part(labels):
    d=defaultdict(set)
    for v,c in enumerate(labels): d[c].add(v)
    return frozenset(frozenset(s) for s in d.values())

def refine(adj):
    colors=[0]*len(adj); parts=[part(colors)]
    for _ in range(len(adj)+3):
        sig=[(colors[v],tuple(sorted(colors[w] for w in adj[v]))) for v in range(len(adj))]
        names={}; new=[names.setdefault(s,len(names)) for s in sig]
        p=part(new); parts.append(p)
        if p==parts[-2]: return parts
        colors=new
    raise RuntimeError

def desc(meta,r):
    labels=[]
    for v in range(len(meta)):
        k,x,L=meta[v]
        if k=="center": labels.append(("c",))
        elif k=="leaf": labels.append(("l",min(L,r)))
        else: labels.append(("i",min(x,r),min(L-x,r)))
    return part(labels)

def formula(lengths):
    ds=sorted(set(lengths)); L=ds[-1]
    return (L+1)//2 if len(ds)==1 else max((L+1)//2,ds[-2]+1)

depth_checks=descriptor_checks=0
for d in range(3,7):
    for lengths in itertools.combinations_with_replacement(range(1,11),d):
        adj,meta=spider(lengths)
        parts=refine(adj); depth=len(parts)-2
        assert depth==formula(lengths),(lengths,depth,formula(lengths))
        for r in range(1,depth+1):
            assert parts[r]==desc(meta,r),(lengths,r)
            descriptor_checks+=1
        depth_checks+=1

extremal_checks=0
for d in range(3,6):
    for N in range(d+1,23):
        T=N-1; best=-1
        for ls in itertools.combinations_with_replacement(range(1,T+1),d):
            if sum(ls)==T: best=max(best,formula(ls))
        assert best==(N-d)//2+1,(d,N,best)
        extremal_checks+=1

print(f"VERIFY_OK depth_checks={depth_checks} descriptor_round_checks={descriptor_checks} extremal_checks={extremal_checks}")
