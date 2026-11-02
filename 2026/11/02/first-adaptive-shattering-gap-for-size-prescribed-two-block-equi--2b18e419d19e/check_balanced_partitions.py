#!/usr/bin/env python3
"""Exact small-order certificates for pair-membership questions about two-block partitions.
Only Python standard-library modules are used.
"""
import itertools
import json
from functools import lru_cache
from pathlib import Path

def concepts(n, a):
    if not (1 <= a <= n//2):
        raise ValueError((n,a))
    edges = list(itertools.combinations(range(n),2))
    blocks=[]
    for subset in itertools.combinations(range(n),a):
        if n==2*a and 0 not in subset:
            continue
        S=set(subset)
        blocks.append(tuple(subset))
    values = [sum((1<<i) for i,(x,y) in enumerate(edges) if (x in subset)==(y in subset)) for subset in map(set,blocks)]
    return edges, blocks, values

def vc_dimension(values, m):
    for size in range(min(m,(len(values)).bit_length()-1),-1,-1):
        for chosen in itertools.combinations(range(m),size):
            patterns={sum(((v>>i)&1)<<j for j,i in enumerate(chosen)) for v in values}
            if len(patterns)==(1<<size):
                return size, list(chosen)
    raise AssertionError('empty finite class')

def littlestone_dimension(values, m):
    N=len(values); full=(1<<N)-1
    positive=[sum(1<<i for i,val in enumerate(values) if (val>>j)&1) for j in range(m)]
    @lru_cache(maxsize=None)
    def dim(mask):
        best=0
        for p in positive:
            yes=mask & p; no=mask & (full^p)
            if yes and no:
                best=max(best,1+min(dim(yes),dim(no)))
        return best
    return dim(full),dim,positive,full

def witness_tree(values, m, depth):
    d, dim, positive, full=littlestone_dimension(values,m)
    if d<depth:raise AssertionError((d,depth))
    def descend(mask, rem):
        if rem==0:
            i=(mask&(-mask)).bit_length()-1
            return {'hypothesis_index':i}
        for q,p in enumerate(positive):
            yes=mask&p; no=mask&(full^p)
            if yes and no and dim(yes)>=rem-1 and dim(no)>=rem-1:
                return {'query_index':q,'0':descend(no,rem-1),'1':descend(yes,rem-1)}
        raise AssertionError((mask,rem))
    return descend(full,depth)

def verify_tree(tree,values,m,depth,mask=None):
    if mask is None:mask=(1<<len(values))-1
    if depth==0:
        i=tree['hypothesis_index']; assert (mask>>i)&1
        assert set(tree)=={'hypothesis_index'}
        return 1
    assert set(tree)=={'query_index','0','1'}
    q=tree['query_index']; assert 0<=q<m
    masks=[sum(1<<i for i,v in enumerate(values) if ((v>>q)&1)==a) for a in (0,1)]
    lhs=mask&masks[0];rhs=mask&masks[1]
    assert lhs and rhs
    return verify_tree(tree['0'],values,m,depth-1,lhs)+verify_tree(tree['1'],values,m,depth-1,rhs)

def classify_three_edge_orbits(edges):
    # Exhaustive direct triples and four structural types independent of VC dimension routine.
    orbit_count={}
    for triple in itertools.combinations(range(len(edges)),3):
        graph=[edges[i] for i in triple]
        degree=[sum(v in e for e in graph) for v in range(5)]
        if sorted(degree,reverse=True)==[3,1,1,1,0]:kind='star plus isolate'
        elif sorted(degree,reverse=True)==[2,2,2,0,0]:kind='triangle plus isolates'
        elif sorted(degree,reverse=True)==[2,2,1,1,0]:kind='four-vertex path plus isolate'
        elif sorted(degree,reverse=True)==[2,1,1,1,1]:kind='three-vertex path and disjoint edge'
        else:raise AssertionError((graph,degree))
        orbit_count[kind]=orbit_count.get(kind,0)+1
    return orbit_count

def main():
    results=[]
    for n in range(2,6):
        for a in range(1,n//2+1):
            E,H,C=concepts(n,a)
            vc,w=vc_dimension(C,len(E))
            ld,_,_,_=littlestone_dimension(C,len(E))
            results.append({'n':n,'smaller_block':a,'hypotheses':len(H),'vc':vc,'littlestone':ld})
    assert results==[
        {'n':2,'smaller_block':1,'hypotheses':1,'vc':0,'littlestone':0},
        {'n':3,'smaller_block':1,'hypotheses':3,'vc':1,'littlestone':1},
        {'n':4,'smaller_block':1,'hypotheses':4,'vc':2,'littlestone':2},
        {'n':4,'smaller_block':2,'hypotheses':3,'vc':1,'littlestone':1},
        {'n':5,'smaller_block':1,'hypotheses':5,'vc':2,'littlestone':2},
        {'n':5,'smaller_block':2,'hypotheses':10,'vc':2,'littlestone':3}]
    E,H,C=concepts(5,2)
    forbidden=classify_three_edge_orbits(E)
    assert sum(forbidden.values())==120
    # Check all three-query supports, not just representatives.
    for triple in itertools.combinations(range(10),3):
        labels={sum(((v>>i)&1)<<j for j,i in enumerate(triple)) for v in C}
        assert len(labels)<8
    tree=witness_tree(C,len(E),3)
    assert verify_tree(tree,C,len(E),3)==8
    certificate={'query_edges_zero_indexed':[list(e) for e in E],
                 'smaller_blocks_zero_indexed':[list(s) for s in H],
                 'depth_three_tree':tree,
                 'three_edge_support_orbits':forbidden}
    output=Path(__file__).resolve().parent/'balanced_five_certificate.json'
    output.write_text(json.dumps(certificate,sort_keys=True,indent=2)+'\n',encoding='utf-8')
    print('SMALL_TWO_BLOCK_PROFILES',json.dumps(results,separators=(',',':')))
    print('THREE_EDGE_ORBITS',json.dumps(forbidden,sort_keys=True))
    print('EXHAUSTIVE_THREE_EDGE_SUPPORTS',120,'ALL_FAIL')
    print('ADAPTIVE_TREE_DEPTH',3,'LEAVES',8)
    print('CERTIFICATE_SHA256',__import__('hashlib').sha256(output.read_bytes()).hexdigest())
    print('ALL_BALANCED_PARTITION_CHECKS_PASS')
if __name__=='__main__':main()
