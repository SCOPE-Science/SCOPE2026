#!/usr/bin/env python3
import networkx as nx

def same_partition(c, d):
    vs=list(c)
    return all((c[u]==c[v])==(d[u]==d[v]) for i,u in enumerate(vs) for v in vs[i+1:])

def stab(G):
    c={v:0 for v in G}
    s=0
    while True:
        sig={v:(c[v], tuple(sorted(c[w] for w in G[v]))) for v in G}
        names={}
        nc={v:names.setdefault(sig[v], len(names)) for v in G}
        if same_partition(c,nc):
            return s
        c=nc
        s+=1

count=0
extremal=0
for n in range(2,18):
    mx=-1
    atmax=0
    for G in nx.nonisomorphic_trees(n):
        count+=1
        s=stab(G)
        assert s <= (n-1)//2, (n,s)
        if s>mx:
            mx=s; atmax=1
        elif s==mx:
            atmax+=1
    assert mx==(n-1)//2, (n,mx)
    extremal += atmax
print(f"VERIFY_OK trees={count} n=2..17 extremal_instances={extremal} bound_and_sharpness=PASS")
