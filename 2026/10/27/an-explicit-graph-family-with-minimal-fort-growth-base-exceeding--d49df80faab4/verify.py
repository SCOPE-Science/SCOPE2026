#!/usr/bin/env python3
"""Exact local gadget enumeration and independent small-order tests."""
from itertools import combinations
from collections import Counter
E=((0,1),(0,3),(0,5),(1,2),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(4,5))
N=6

def is_fort(vertices, edges, mask):
    if not mask:return False
    adj=[0]*vertices
    for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
    return all(((mask>>i)&1) or (adj[i]&mask).bit_count()!=1 for i in range(vertices))

def minforts(v,edges):
    selected=[]
    for k in range(1,v+1):
        for ss in combinations(range(v),k):
            mask=sum(1<<u for u in ss)
            if any((mask & sub)==sub for sub in selected):continue
            if is_fort(v,edges,mask):selected.append(mask)
    return selected
local=minforts(6,E)
rooted=[m for m in local if m&1];notrooted=[m for m in local if not (m&1)]
assert len(rooted)==8 and len(notrooted)==6
assert all(m.bit_count()==3 for m in rooted)
expected_rooted=[{0,1,2},{0,1,3},{0,2,3},{0,1,4},{0,3,4},{0,2,5},{0,3,5},{0,4,5}]
expected_notrooted=[{2,4},{1,5},{1,2,3},{1,3,4},{2,3,5},{3,4,5}]
as_sets=lambda vals:{frozenset(i for i in range(6) if m>>i&1) for m in vals}
assert as_sets(rooted)==set(map(frozenset,expected_rooted))
assert as_sets(notrooted)==set(map(frozenset,expected_notrooted))

# Establish the needed local lemma by exhausting every peripheral subset.
local_admissible={}
for mask in range(1<<5):
    ss={i+1 for i in range(5) if mask>>i&1}
    if all(i in ss or sum((min(i,j),max(i,j)) in E for j in ss)!=1 for i in range(1,6)):
        local_admissible[frozenset(ss)]=len(ss&{1,3,5})
assert len(local_admissible)==17
assert all({2,4}.issubset(s) for s,t in local_admissible.items() if t==1)
assert all(any(z.issubset(s) for z in expected_notrooted) for s,t in local_admissible.items() if s and t!=1)
for s in expected_rooted:
    per=s-{0}
    assert not any(z.issubset(per) for z in expected_notrooted)
    assert frozenset(per) not in local_admissible

def bouquet(k):
    def vertex(p,v):return 0 if v==0 else 1+5*p+v-1
    edges={tuple(sorted((vertex(p,u),vertex(p,v)))) for p in range(k) for u,v in E}
    return 5*k+1, tuple(sorted(edges))
for k in (1,2,3):
    v,edges=bouquet(k)
    forts=minforts(v,edges)
    expected=8**k+6*k
    assert len(forts)==expected,(k,len(forts),expected)
    counts=Counter(bool(m&1) for m in forts)
    assert counts[True]==8**k and counts[False]==6*k
    print(f'k={k} vertices={v} minimal_forts={len(forts)} rooted={counts[True]} rootless={counts[False]}')
print('LOCAL_ADMISSIBLE=17 ROOTED=8 ROOTLESS=6')
print('VERIFY_OK')
