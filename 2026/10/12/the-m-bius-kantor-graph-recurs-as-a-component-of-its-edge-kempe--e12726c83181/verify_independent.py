#!/usr/bin/env python3
"""Independent edge-by-edge exact 3-edge-coloring/Kempe verifier for GP(8,3).
Requires only Python 3 standard library. Run: python3 verify_independent.py certificate.json
"""
from collections import Counter,deque
from itertools import combinations
import json,sys

# Independently build the edges via three edge-families and deduplicate.
E=sorted({tuple(sorted((i,(i+1)%8))) for i in range(8)}|
         {(i,i+8) for i in range(8)}|
         {tuple(sorted((8+i,8+(i+3)%8))) for i in range(8)})
assert len(E)==24
inc=[[e for e,(u,v) in enumerate(E) if x==u or x==v] for x in range(16)]
assert all(len(x)==3 for x in inc)
colors=[-1]*len(E);used=[0]*16;results=[]

def dfs(left):
    if left==0:
        assert all(x==7 for x in used)
        results.append(tuple(colors));return
    best=None; options=0;num=4
    for k,(u,v) in enumerate(E):
        if colors[k]>=0:continue
        possible=7&~(used[u]|used[v]); n=possible.bit_count()
        if n==0:return
        if n<num:
            num=n;best=k; options=possible
            if num==1:break
    u,v=E[best]
    for color in range(3):
        bit=1<<color
        if options&bit:
            colors[best]=color;used[u]|=bit;used[v]|=bit
            dfs(left-1)
            used[u]^=bit;used[v]^=bit;colors[best]=-1

# Remove six global color permutations by labeling the three edges at vertex 0.
for k,c in zip(sorted(inc[0]),range(3)):
    u,v=E[k];colors[k]=c;used[u]|=1<<c;used[v]|=1<<c
dfs(21)
assert len(results)==20
assert len(set(results))==20

def triple_from_coloring(C):
    masks=tuple(sum(1<<e for e,x in enumerate(C) if x==c) for c in range(3))
    return tuple(sorted(masks))
trips={triple_from_coloring(C) for C in results};assert len(trips)==20

# Complete Kempe graph from direct colors, not from matching enumeration.
T=sorted(trips);idx={t:i for i,t in enumerate(T)}
alladj=set()
for C in results:
    i=idx[triple_from_coloring(C)]
    for a,b in combinations(range(3),2):
        available={k for k in range(24) if C[k] in (a,b)}
        while available:
            first=min(available);Q=[first];component=set([first]);available.remove(first)
            while Q:
                e=Q.pop()
                for v in E[e]:
                    for j in inc[v]:
                        if j in available:
                            available.remove(j);component.add(j);Q.append(j)
            D=list(C)
            for k in component:D[k]=b if C[k]==a else a
            j=idx[triple_from_coloring(D)]
            if i!=j:alladj.add(tuple(sorted((i,j))))
assert len(alladj)==27
neighbors=[set() for _ in T]
for i,j in alladj:neighbors[i].add(j);neighbors[j].add(i)
remaining=set(range(20));componentsets=[]
while remaining:
    v=min(remaining);remaining.remove(v);Q=[v];group={v}
    while Q:
        for w in neighbors[Q.pop()]&remaining:
            remaining.remove(w);group.add(w);Q.append(w)
    componentsets.append(group)
assert sorted(map(len,componentsets))==[4,16]
assert sorted(Counter(map(len,neighbors)).items())==[(1,3),(3,17)]

if len(sys.argv)>1:
    cert=json.load(open(sys.argv[1],encoding='utf-8'))
    Ms=cert['matching_masks'];F=cert['factorizations_as_matching_indices']
    from_certificate={tuple(sorted(Ms[k] for k in f)) for f in F}
    assert from_certificate==trips
    c_order=[tuple(sorted(Ms[k] for k in f)) for f in F]
    cert_K={tuple(sorted((c_order[i],c_order[j]))) for i,j in cert['kempe_edges_as_factorization_indices']}
    direct_K={tuple(sorted((T[i],T[j]))) for i,j in alladj}
    assert cert_K==direct_K
    print('VERIFY_INDEPENDENT_CERTIFICATE_OK exact_colorings_and_Kempe_edges')
print('VERIFY_INDEPENDENT_OK assigned_edges=24 fixed_color_names_at_root=3 full_colorings=120 unordered=20')
print('VERIFY_INDEPENDENT_OK Kempe_edges=27 components=4+16 claw_degrees=1,1,1,3')
