#!/usr/bin/env python3
"""Exact rank-three EF types for unions of undirected cycles; independent of classification formulas."""
from functools import lru_cache
from collections import defaultdict

def partitions(n,minp=3):
    if n==0:
        yield ()
    else:
        for x in range(minp,n+1):
            for y in partitions(n-x,x):
                yield (x,)+y

def build(parts):
    adj=[]; shift=0
    for m in parts:
        for j in range(m):
            adj.append({shift+(j-1)%m, shift+(j+1)%m})
        shift+=m
    return adj

def type3(adj):
    n=len(adj)
    # atomic 3-type encoded by 3 equalities and 3 edges in fixed order
    def ty0(t):
        return tuple(int(t[i]==t[j]) for i,j in ((0,1),(0,2),(1,2)))+tuple(int(t[j] in adj[t[i]]) for i,j in ((0,1),(0,2),(1,2)))
    t1_cache={}
    def t1(i,j):
        if (i,j) not in t1_cache:
            t1_cache[(i,j)]=frozenset(ty0((i,j,k)) for k in range(n))
        return t1_cache[(i,j)]
    t2_cache={}
    def t2(i):
        if i not in t2_cache:
            t2_cache[i]=frozenset(t1(i,j) for j in range(n))
        return t2_cache[i]
    return frozenset(t2(i) for i in range(n))

def key(parts):
    n=sum(parts)
    if n<=6:
        return ('small',parts)
    return ('large',)+tuple(int(any((m==3 if i==0 else m==4 if i==1 else m>=5) for m in parts)) for i in range(3))

def run(maxn=29):
    from hashlib import sha256
    type_ids={}; types_by_key=defaultdict(set); key_by_type=defaultdict(set); minreps={}
    cases=0
    for n in range(3,maxn+1):
        for parts in partitions(n):
            cases+=1
            t=type3(build(parts)); ky=key(parts)
            if t not in type_ids: type_ids[t]=len(type_ids)
            types_by_key[ky].add(type_ids[t]);key_by_type[type_ids[t]].add(ky)
            if ky not in minreps:minreps[ky]=(n,parts)
    assert all(len(s)==1 for s in types_by_key.values()),[(k,v) for k,v in types_by_key.items() if len(v)>1]
    assert all(len(s)==1 for s in key_by_type.values()),[(k,v) for k,v in key_by_type.items() if len(v)>1]
    assert len(types_by_key)==12,(len(types_by_key),len(type_ids))
    print('EXACT_RANK3_TYPES_OK', 'max_n',maxn,'partition_instances',cases,'classes',len(type_ids))
    for k in sorted(minreps,key=lambda z:(minreps[z][0],z)):
        print('CLASS',k,'MIN',minreps[k], 'TYPE',next(iter(types_by_key[k])))
    digest=sha256('\n'.join(repr((k,minreps[k])) for k in sorted(minreps,key=str)).encode()).hexdigest()
    print('MIN_REP_LIST_SHA256',digest)
    print('MAX_REPRESENTATIVE_VERTICES',max(n for n,_ in minreps.values()))

if __name__=='__main__':
    import sys
    run(int(sys.argv[1]) if len(sys.argv)>1 else 24)
