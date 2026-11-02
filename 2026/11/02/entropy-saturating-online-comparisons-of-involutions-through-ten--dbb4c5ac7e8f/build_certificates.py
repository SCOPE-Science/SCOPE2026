#!/usr/bin/env python3
"""Build exact adaptive comparison-shattering trees for finite involution permutations."""
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

def enumerate_involutions(n):
    values=[-1]*n
    def rec(remaining):
        if not remaining:
            yield tuple(values);return
        i=remaining[0]
        values[i]=i
        yield from rec(remaining[1:])
        for j,v in enumerate(remaining[1:]):
            values[i]=v;values[v]=i
            yield from rec(remaining[1:j+1]+remaining[j+2:])
            values[v]=-1
        values[i]=-1
    return sorted(rec(tuple(range(n))))

def calculate(n):
    concepts=enumerate_involutions(n)
    pairs=list(combinations(range(n),2))
    masks=[]
    for u,v in pairs:
        masks.append(sum(1<<i for i,p in enumerate(concepts) if p[u]<p[v]))
    root=(1<<len(concepts))-1
    queries=[];leaves=[];memo_states=[]
    @lru_cache(maxsize=None)
    def shatters(state,depth):
        if depth==0:return True
        if state.bit_count()<1<<depth:return False
        need=1<<(depth-1)
        for ma in masks:
            p=state&ma;q=state^p
            if p.bit_count()>=need and q.bit_count()>=need and shatters(p,depth-1) and shatters(q,depth-1):return True
        return False
    best=0
    for depth in range(1,len(concepts).bit_length()):
        if shatters(root,depth):best=depth
        else:break
    nodes=[-1]*(1<<best)
    witnesses=[-1]*(1<<best)
    def build(state,depth,index):
        if depth==0:
            witnesses[index-(1<<best)]=((state&-state).bit_length()-1)
            return
        need=1<<(depth-1)
        for i,ma in enumerate(masks):
            p=state&ma;q=state^p
            if p.bit_count()>=need and q.bit_count()>=need and shatters(p,depth-1) and shatters(q,depth-1):
                nodes[index]=i
                build(q,depth-1,index*2)
                build(p,depth-1,index*2+1)
                return
        raise AssertionError((state,depth))
    build(root,best,1)
    assert len(set(witnesses))==len(witnesses)
    return {'n':n,'concept_count':len(concepts),'depth':best,'node_query_indices':nodes[1:], 'leaf_witness_involution_indices':witnesses,'query_index_rule':'lexicographic unordered pairs (i,j), zero based; 0 left, 1 right','witness_index_rule':'lexicographically sorted involutions as zero-based tuples','memoized_states':shatters.cache_info().currsize}

if __name__=='__main__':
    d=[calculate(n) for n in range(2,11)]
    dest=Path(__file__).with_name('adaptive_certificates.json')
    dest.write_text(json.dumps({'schema_version':1,'domain':'all involutions on [n], queried by pi[i]<pi[j]','certificates':d},separators=(',',':'))+'\n',encoding='utf-8')
    print('BUILT',[(x['n'],x['concept_count'],x['depth'],x['memoized_states']) for x in d],dest.stat().st_size,flush=True)
