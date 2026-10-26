#!/usr/bin/env python3
"""Independent graph-DAG enumeration, dimension recurrence, and certificate replay."""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

HERE=Path(__file__).resolve().parent
cert=json.loads((HERE/'certificate.json').read_text(encoding='utf-8'))
assert cert['edges_in_bit_order']==[['a','u'],['a','v'],['a','w'],['b','u'],['b','v'],['b','w']]
verts=['a','b','u','v','w']; edge_idx=[(verts.index(a),verts.index(b)) for a,b in cert['edges_in_bit_order']]

def acyclic(word,edges=edge_idx,n=5):
    adj=[[] for _ in range(n)];indeg=[0]*n
    for j,(a,b) in enumerate(edges):
        if word>>j&1:a,b=b,a
        adj[a].append(b);indeg[b]+=1
    Q=[v for v in range(n) if indeg[v]==0]
    for a in Q:
        for b in adj[a]:
            indeg[b]-=1
            if indeg[b]==0:Q.append(b)
    return len(Q)==n

hyp=[w for w in range(64) if acyclic(w)]
assert len(hyp)==46
assert all(acyclic(w)==(not ({(0,1),(1,0)} <= {((w>>i)&1,(w>>(i+3))&1) for i in range(3)})) for w in range(64))

# The orientation bitsets below represent version spaces over the 46 hypotheses.
Q=[sum(1<<i for i,w in enumerate(hyp) if w>>q&1) for q in range(6)]
@lru_cache(None)
def ldim(S):
    if S.bit_count()<=1:return 0
    best=0
    for B in Q:
        left=S&~B;right=S&B
        if not left or not right:continue
        best=max(best,1+min(ldim(left),ldim(right)))
    return best
assert ldim((1<<len(hyp))-1)==5

# All pair-query VC traces; 4 is also proved symbolically via the forest criterion.
vc=0
for r in range(1,7):
    for sub in combinations(range(6),r):
        traces={sum(((w>>q)&1)<<i for i,q in enumerate(sub)) for w in hyp}
        if len(traces)==(1<<r):vc=max(vc,r)
assert vc==4

node=cert['node_queries'];witness=cert['leaf_orientation_words']
assert len(node)==31 and len(witness)==32
assert all(isinstance(q,int) and 0<=q<6 for q in node)
assert len(set(witness))==32 and all(w in hyp for w in witness)
for leaf,w in enumerate(witness):
    prefix=0
    for t in range(5):
        q=node[(1<<t)-1+prefix]
        expected=(leaf>>(4-t))&1
        assert (w>>q)&1==expected,(leaf,t,q,w)
        prefix=2*prefix+expected

# C_4 has 14 acyclic orientations, so Ldim=VC=3 by the forest shattering criterion.
cycle_edges=[(0,1),(1,2),(2,3),(3,0)]
assert sum(acyclic(w,cycle_edges,4) for w in range(16))==14
print('ALL_ACYCLIC_ORIENTATION_CHECKS_PASS')
print(f'K23_acyclic_orientations={len(hyp)};K23_VCdim={vc};K23_Ldim={ldim((1<<len(hyp))-1)}')
print(f'certificate_depth=5;distinct_path_witnesses={len(set(witness))};C4_acyclic_orientations=14')
print(f'version_spaces_visited={ldim.cache_info().currsize}')
