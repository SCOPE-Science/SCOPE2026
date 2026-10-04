#!/usr/bin/env python3
from itertools import product


def weak_order(sizes):
    pts=[(i,j) for i,r in enumerate(sizes) for j in range(r)]
    def leq(a,b):
        return a==b or a[0] < b[0]
    return pts,leq


def enumerate_maps(src_sizes,tgt_sizes):
    S,_=weak_order(src_sizes)
    T,leq=weak_order(tgt_sizes)
    choices=[list(product(T, repeat=r)) for r in src_sizes]
    seqs=[(c,) for c in choices[0]]
    for i in range(1,len(src_sizes)):
        nxt=[]
        for seq in seqs:
            prev=seq[-1]
            for c in choices[i]:
                if all(leq(a,b) for a in prev for b in c):
                    nxt.append(seq+(c,))
        seqs=nxt
    maps=[tuple(x for block in seq for x in block) for seq in seqs]
    return S,T,leq,maps


def proof_dichotomy(src_sizes,tgt_sizes,f):
    assert all(r==2 for r in src_sizes)
    h,k=len(src_sizes),len(tgt_sizes)
    image_levels={j:set() for j in range(k)}
    pos=0
    blocks=[]
    for r in src_sizes:
        block=f[pos:pos+r]; pos+=r; blocks.append(block)
        for x in block: image_levels[x[0]].add(x)
    occupied={j:v for j,v in image_levels.items() if v}
    if any(len(v)==1 for v in occupied.values()):
        return 'singleton'
    # No singleton occupied level: verify the structural branch used in the proof.
    target_indices=[]
    for block in blocks:
        levels={x[0] for x in block}
        assert len(levels)==1
        assert len(set(block))==2
        target_indices.append(next(iter(levels)))
    assert all(target_indices[i] < target_indices[i+1] for i in range(len(target_indices)-1))
    assert len(set(target_indices))==h
    if h>k:
        raise AssertionError('No-singleton branch impossible when source height exceeds target height')
    assert h<k
    assert set(range(k)) - set(target_indices)
    return 'omitted'


def component_count(leq,maps):
    n=len(maps)
    parent=list(range(n))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a!=b: parent[b]=a
    for i in range(n):
        fi=maps[i]
        for j in range(i+1,n):
            fj=maps[j]
            if all(leq(a,b) for a,b in zip(fi,fj)) or all(leq(b,a) for a,b in zip(fi,fj)):
                union(i,j)
    return len({find(i) for i in range(n)})

cases=[
    ((2,2),(2,3,2)),
    ((2,2),(3,2,3)),
    ((2,2,2),(3,2)),
    ((2,2,2),(2,3)),
    ((2,2),(2,2,2,2)),
    ((2,2,2,2),(2,3)),
]
expected_counts=[303,533,71,71,648,89]
for (src,tgt),expected in zip(cases,expected_counts):
    _,_,leq,maps=enumerate_maps(src,tgt)
    assert len(maps)==expected
    branches={'singleton':0,'omitted':0}
    for f in maps:
        branches[proof_dichotomy(src,tgt,f)] += 1
    comps=component_count(leq,maps)
    assert comps==1
    print(f'{src}->{tgt}: maps={len(maps)} singleton={branches["singleton"]} omitted={branches["omitted"]} components={comps}')
print('VERIFY_OK')
