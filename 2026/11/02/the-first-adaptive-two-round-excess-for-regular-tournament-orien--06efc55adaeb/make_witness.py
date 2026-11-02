#!/usr/bin/env python3
"""Generate a complete binary prediction tree for regular tournaments on seven points."""
from itertools import combinations
from functools import lru_cache
import json
from pathlib import Path
n=7
edges=list(combinations(range(n),2))
H=[]
for h in range(1<<len(edges)):
    degree=[0]*n
    for i,(u,v) in enumerate(edges):
        degree[u if (h>>i)&1 else v]+=1
    if degree==[3]*n:
        H.append(h)
assert len(H)==2640
masks=[sum(1<<j for j,h in enumerate(H) if (h>>i)&1) for i in range(len(edges))]
whole=(1<<len(H))-1
@lru_cache(maxsize=None)
def viable(version,remaining):
    if remaining==0:return True
    if version.bit_count()<(1<<remaining):return False
    for m in masks:
        pos=version&m
        neg=version^pos
        if min(pos.bit_count(),neg.bit_count())<(1<<(remaining-1)):
            continue
        if viable(pos,remaining-1) and viable(neg,remaining-1):
            return True
    return False
assert viable(whole,11)
assert not viable(whole,12)

def construct(version,remaining):
    if remaining==0:
        return [H[(version & -version).bit_length()-1]]
    for i,m in enumerate(masks):
        pos=version&m
        neg=version^pos
        if min(pos.bit_count(),neg.bit_count())<(1<<(remaining-1)):
            continue
        if viable(pos,remaining-1) and viable(neg,remaining-1):
            return [i,construct(pos,remaining-1),construct(neg,remaining-1)]
    raise AssertionError((version.bit_count(),remaining))

T=construct(whole,11)
p={'n':n,'depth':11,'edge_order':edges,'tree':T}
path=Path(__file__).with_name('depth11_tree.json')
path.write_text(json.dumps(p,separators=(',',':'))+'\n',encoding='utf-8')

def inspect(t,level=0):
    if len(t)==1:return 0,1,{t[0]}
    assert len(t)==3
    a,b,ls=inspect(t[1],level+1); c,d,rs=inspect(t[2],level+1)
    return a+c+1,b+d,ls|rs
nodes,leaves,distinct=inspect(T)
print('regular tournaments',len(H),'nodes',nodes,'leaves',leaves,'distinct_leaf_witnesses',len(distinct),'file_bytes',path.stat().st_size,'cache',viable.cache_info())
