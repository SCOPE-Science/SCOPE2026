#!/usr/bin/env python3
"""Independent mod-prime H_1 checks via quotient barycentric 2-skeleton."""
from itertools import combinations
from collections import defaultdict
from math import comb

def quot(d):
    n=2*d; full=(1<<n)-1
    parity=[sum(1<<i for i in range(p,n,2)) for p in [0,1]]
    def rot(x,k):return (((x<<k)|(x>>(n-k))) & full) if k else x
    def canon(t):return min(tuple(rot(x,k) for x in t) for k in range(n))
    faces=sorted(x for x in range(1,1<<n) if not any((x&p)==p for p in parity))
    index={x:i for i,x in enumerate(faces)}
    vertids=sorted({canon((x,)) for x in faces}); vi={x:i for i,x in enumerate(vertids)}
    v_for={x:vi[canon((x,))] for x in faces}
    edges=set()
    for y in faces:
        x=(y-1)&y
        while x:
            edges.add(canon((x,y)))
            x=(x-1)&y
    edges=sorted(edges); ei={x:i for i,x in enumerate(edges)}
    e_for=lambda x,y:ei[canon((x,y))]
    par=list(range(len(vertids)))
    def find(x):
        while x!=par[x]:par[x]=par[par[x]];x=par[x]
        return x
    tree=set()
    for e,(x,y) in enumerate(edges):
        u,v=find(v_for[x]),find(v_for[y])
        if u!=v:par[u]=v;tree.add(e)
    assert len(tree)==len(vertids)-1
    others=[e for e in range(len(edges)) if e not in tree]
    cols={e:i for i,e in enumerate(others)}
    relations={}
    for z in faces:
        y=(z-1)&z
        while y:
            x=(y-1)&y
            while x:
                t=canon((x,y,z))
                if t not in relations:
                    r=defaultdict(int)
                    for i,e in [(1,e_for(x,y)),(-1,e_for(x,z)),(1,e_for(y,z))]:
                        if e in cols:r[cols[e]]+=i
                    relations[t]={c:v for c,v in r.items() if v}
                x=(x-1)&y
            y=(y-1)&z
    return (len(vertids),len(edges),len(relations),len(others),list(relations.values()))

def rank_mod(rows,p):
    pivots={}
    for row in rows:
        a={c:v%p for c,v in row.items() if v%p}
        while a:
            c=min(a)
            if c not in pivots:
                s=pow(a[c],-1,p)
                pivots[c]={k:(v*s)%p for k,v in a.items() if v}
                break
            f=a[c]
            for j,v in pivots[c].items():
                a[j]=(a.get(j,0)-f*v)%p
                if not a[j]:del a[j]
    return len(pivots)

if __name__=='__main__':
 for d in [3,4,5]:
    nvs,nes,ntris,nfree,rels=quot(d)
    ranks={p:nfree-rank_mod(rels,p) for p in [2,3,5,7,101]}
    print('d=',d,'quotient_cells_v_e_tri=',(nvs,nes,ntris),'free_generators=',nfree,'H1_dimensions_over_Fp=',ranks,flush=True)
    assert ranks[101]==0
    expected={3:{2:0,3:1,5:0,7:0},4:{2:1,3:0,5:0,7:0},5:{2:0,3:0,5:1,7:0}}[d]
    assert all(ranks[p]==v for p,v in expected.items())
 print('QUOTIENT MOD-PRIME H1 VALIDATED')
