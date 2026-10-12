#!/usr/bin/env python3
"""Exact reproducible census of Kempe reconfiguration for GP(8,3).
Requires Python 3 standard library only. Run: python3 verify.py certificate.json
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
import json, sys

E = sorted({tuple(sorted(z)) for i in range(8) for z in ((i,(i+1)%8),(i,i+8),(i+8,8+(i+3)%8))})
assert len(E)==24
index = {e:k for k,e in enumerate(E)}
incident = [[k for k,(u,v) in enumerate(E) if x in (u,v)] for x in range(16)]
assert all(len(s)==3 for s in incident)
FULL=(1<<24)-1

# A perfect matching is a disjoint edge set meeting every vertex.
@lru_cache(None)
def matchings(uncovered):
    if uncovered==0:return (0,)
    u=(uncovered & -uncovered).bit_length()-1
    out=[]
    for e in incident[u]:
        x,y=E[e];v=y if x==u else x
        if uncovered>>v & 1:
            out.extend(s|(1<<e) for s in matchings(uncovered ^ (1<<u) ^ (1<<v)))
    return tuple(out)
M=sorted(matchings((1<<16)-1)); assert len(M)==len(set(M))
ms=set(M); mid={m:i for i,m in enumerate(M)}
assert all(m.bit_count()==8 for m in M)

def comps_on_edge_mask(mask):
    unvisited=set(range(16));res=[]
    while unvisited:
        start=min(unvisited);unvisited.remove(start);todo=[start];vs={start}
        while todo:
            u=todo.pop()
            for k in incident[u]:
                if mask>>k & 1:
                    x,y=E[k];v=x^y^u
                    if v in unvisited:unvisited.remove(v);vs.add(v);todo.append(v)
        res.append(vs)
    return res

def typ(m):
    return tuple(sorted(map(len,comps_on_edge_mask(FULL^m))))
assert Counter(map(typ,M))==Counter({(6,10):24,(16,):6,(8,8):3})

Fset=set()
for a in M:
    for b in M:
        if a&b:continue
        c=FULL^a^b
        if c in ms:Fset.add(tuple(sorted((mid[a],mid[b],mid[c]))))
Fs=sorted(Fset); fidx={f:i for i,f in enumerate(Fs)}
assert len(Fs)==20
profiles=Counter(tuple(sorted(typ(M[k]) for k in f)) for f in Fs)
assert profiles==Counter({((6,10),(6,10),(6,10)):16,((8,8),(16,),(16,)):3,((8,8),(8,8),(8,8)):1})

# Kempe swaps: in a bichromatic union each component is a cycle.
A=set()
for i,f in enumerate(Fs):
    for ia,ib in combinations(f,2):
        a,b=M[ia],M[ib]
        for comp in comps_on_edge_mask(a|b):
            compmask=sum(1<<k for k,(u,v) in enumerate(E) if u in comp and v in comp)
            ax=a&compmask;bx=b&compmask
            na=a^ax^bx;nb=b^ax^bx
            # Empty or whole-color swaps induce no new unordered factorization.
            other=next(iter(set(f)-{ia,ib}))
            nf=tuple(sorted((mid[na],mid[nb],other)))
            j=fidx[nf]
            if i!=j:A.add(tuple(sorted((i,j))))
A=sorted(A)
assert len(A)==27
adj=[set() for _ in Fs]
for i,j in A:adj[i].add(j);adj[j].add(i)
U=set(range(20)); CC=[]
while U:
    root=min(U);U.remove(root);todo=[root];part={root}
    while todo:
        for w in adj[todo.pop()]&U:
            U.remove(w);part.add(w);todo.append(w)
    CC.append(sorted(part))
CC.sort(key=lambda x:-len(x))
assert list(map(len,CC))==[16,4]
assert sorted(Counter(map(len, [adj[i] for i in range(20)])).items())==[(1,3),(3,17)]
assert len([z for z in A if z[0] in CC[0] and z[1] in CC[0]])==24
assert len([z for z in A if z[0] in CC[1] and z[1] in CC[1]])==3
assert sorted(len(adj[i]) for i in CC[1])==[1,1,1,3]

if len(sys.argv)>1:
    cert=json.load(open(sys.argv[1],encoding='utf-8'))
    assert cert['graph_edges']==[list(x) for x in E]
    assert cert['matching_masks']==M
    assert cert['factorizations_as_matching_indices']==[list(f) for f in Fs]
    assert cert['kempe_edges_as_factorization_indices']==[list(e) for e in A]
    phi={int(k):v for k,v in cert['self_isomorphism_factorization_to_graph'].items()}
    assert set(phi)==set(CC[0]) and set(phi.values())==set(range(16))
    assert {tuple(sorted((phi[i],phi[j]))) for i,j in A if i in CC[0] and j in CC[0]}==set(E)
    assert sorted(cert['claw_component'])==CC[1]
    print('VERIFY_CERTIFICATE_OK 20_factorizations 27_switch_edges explicit_self_isomorphism=true')

print('VERIFY_OK GP(8,3) vertices=16 edges=24 perfect_matchings=33')
print('VERIFY_OK matchings_two_factor_types=6+10:24,16:6,8+8:3')
print('VERIFY_OK unordered_one_factorizations=20 profiles=16+3+1')
print('VERIFY_OK Kempe_graph_components=16+4 edges=24+3')
print('VERIFY_OK component_4=K_1,3 component_16=GP(8,3) via_certificate')
