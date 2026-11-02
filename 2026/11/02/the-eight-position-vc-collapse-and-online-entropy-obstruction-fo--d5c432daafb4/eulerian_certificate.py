#!/usr/bin/env python3
"""Exact pair-comparison shattering for permutations with at most two descents.

Usage: python eulerian_certificate.py build [certificate.json]
       python eulerian_certificate.py verify [certificate.json]

No external packages required. All arithmetic and searches are exhaustive.
"""
import itertools
import json
import sys
from functools import lru_cache
from pathlib import Path


def descents(p):
    return sum(p[j] > p[j+1] for j in range(len(p)-1))


def brute_perms(n):
    return tuple(p for p in itertools.permutations(range(n)) if descents(p) <= 2)


def insertion_perms(n):
    level = {(0,)}
    for size in range(2, n+1):
        newer = set()
        for p in level:
            for j in range(size):
                q = p[:j] + (size-1,) + p[j:]
                if descents(q) <= 2:
                    newer.add(q)
        level = newer
    return tuple(sorted(level))


def concepts(n):
    ps = brute_perms(n)
    assert ps == insertion_perms(n), ('independent_enumerators_disagree', n)
    queries = tuple(itertools.combinations(range(n), 2))
    ones = []
    for a,b in queries:
        z=0
        for j,p in enumerate(ps):
            if p[a] > p[b]: z |= 1 << j
        ones.append(z)
    return ps, queries, tuple(ones)


def vc_dimension(ones, num_concepts):
    allmask=(1<<num_concepts)-1
    maximum=0
    witness=()
    visited=0
    def dfs(index, masks, selected):
        nonlocal maximum,witness,visited
        visited+=1
        if len(selected)>maximum:
            maximum=len(selected); witness=selected
        for j in range(index,len(ones)):
            b=ones[j]
            children=[]
            for mask in masks:
                pos=mask&b;neg=mask^pos
                if not pos or not neg:break
                children.extend((neg,pos))
            else:
                dfs(j+1,children,selected+(j,))
    dfs(0,[allmask],())
    return maximum,witness,visited


def adaptive_dimension(ones,num_concepts):
    allmask=(1<<num_concepts)-1
    @lru_cache(maxsize=None)
    def possible(mask,depth):
        if depth==0:return True
        if mask.bit_count()<(1<<depth):return False
        for one in ones:
            yes=mask&one;no=mask^yes
            if min(yes.bit_count(),no.bit_count())<1<<(depth-1):continue
            if possible(no,depth-1) and possible(yes,depth-1):return True
        return False
    D=0
    for d in range(1,num_concepts.bit_length()):
        if not possible(allmask,d):break
        D=d
    return D, possible


def build_tree(mask, depth, ones, possible):
    if depth==0:return (mask & -mask).bit_length()-1
    for j,one in enumerate(ones):
        yes=mask&one;no=mask^yes
        if no and yes and possible(no,depth-1) and possible(yes,depth-1):
            return [j,build_tree(no,depth-1,ones,possible),build_tree(yes,depth-1,ones,possible)]
    raise AssertionError('missing_child')


def check_tree(tree,mask,depth,ones):
    if depth==0:
        assert isinstance(tree,int) and (mask>>tree)&1
        return [tree],0
    assert isinstance(tree,list) and len(tree)==3
    q=int(tree[0]); assert 0<=q<len(ones)
    yes=mask&ones[q];no=mask^yes
    assert yes and no
    leaves0,node0=check_tree(tree[1],no,depth-1,ones)
    leaves1,node1=check_tree(tree[2],yes,depth-1,ones)
    assert set(leaves0).isdisjoint(leaves1)
    return leaves0+leaves1,1+node0+node1


def run(mode,path):
    expected_counts=(1,2,6,23,93,360,1312,4541)
    expected_vc=(0,1,2,3,4,5,6,6)
    expected_ld=(0,1,2,4,6,8,10,11)
    rows=[]
    for n in range(1,9):
        ps,qs,one=concepts(n)
        assert len(ps)==expected_counts[n-1]
        vc,wit,visited=vc_dimension(one,len(ps))
        depth,possible=adaptive_dimension(one,len(ps))
        assert (vc,depth)==(expected_vc[n-1],expected_ld[n-1]),(n,vc,depth)
        row={'n':n,'concept_count':len(ps),'vc':vc,'littlestone':depth,
             'cardinality_ceiling':len(ps).bit_length()-1,
             'vc_support':[list(qs[i]) for i in wit],
             'vc_search_nodes':visited,
             'adaptive_subsets':possible.cache_info().currsize}
        if n==8:
            assert not possible((1<<len(ps))-1,12)
            if mode=='build':
                tree=build_tree((1<<len(ps))-1,11,one,possible)
            else:
                tree=json.loads(path.read_text('utf-8'))['adaptive_witness_tree']
            leaves,nodes=check_tree(tree,(1<<len(ps))-1,11,one)
            assert nodes==2047 and len(leaves)==len(set(leaves))==2048
        rows.append(row)
        print('DIMENSION_PASS',n,'concepts',len(ps),'VC',vc,'Ldim',depth,'VC-search-nodes',visited,'adaptive-memo-subsets',row['adaptive_subsets'], flush=True)
    if mode=='build':
        payload={'schema':1,'definition':'At most two adjacent descents; query (a,b) with a<b is pi[a]>pi[b], zero-indexed.',
                 'n':8,'depth':11,'adaptive_witness_tree':tree,'dimension_rows':rows}
        path.write_text(json.dumps(payload,separators=(',',':'),ensure_ascii=False)+'\n',encoding='utf-8')
        print('CERTIFICATE_WRITTEN',str(path))
    else:
        cert=json.loads(path.read_text('utf-8'))
        assert cert['n']==8 and cert['depth']==11 and cert['dimension_rows']==rows
        print('CERTIFICATE_VERIFIED',str(path))
    print('EULERIAN_TWO_DESCENTS_ALL_CHECKS_PASS')

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'verify'
    assert mode in ('build','verify')
    path=Path(sys.argv[2]) if len(sys.argv)>2 else Path('certificate.json')
    run(mode,path)
