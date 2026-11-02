#!/usr/bin/env python3
"""Standalone exact checks for Boolean radius-two Hamming-ball shattering."""
from collections import Counter
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
CERT=json.loads((ROOT/'certificate.json').read_text('utf-8'))


def dist(u,v):
    return (u^v).bit_count()


def test_static(queries,centers,d):
    assert len(centers)==1<<len(queries)
    assert len(set(queries))==len(queries)
    assert len(set(centers))==len(centers)
    for pattern,c in enumerate(centers):
        assert 0<=c<(1<<d)
        actual=sum((dist(c,x)<=2)<<i for i,x in enumerate(queries))
        assert actual==pattern, (queries,pattern,c,actual)


def test_tree(node,d,labels=(),depth=0):
    if 'center' in node:
        assert depth==5
        c=node['center']
        assert 0<=c<(1<<d)
        for q,a in labels:
            assert (dist(c,q)<=2)==bool(a)
        return [c],0
    q=node['query']
    assert 0<=q<(1<<d)
    yes,iy=test_tree(node['yes'],d,labels+((q,1),),depth+1)
    no,ino=test_tree(node['no'],d,labels+((q,0),),depth+1)
    return yes+no,1+iy+ino


def verify_five_obstruction():
    # If five queries were shattered, one radius-two ball would contain all
    # five; translate its center to zero. Each query then has weight <=2.
    # Every occupied coordinate has a nonzero five-bit incidence column.
    # The coordinate multiplicities satisfy each row's total <=2.
    count=0
    best=0
    histogram=Counter()
    def examine(cols):
        nonlocal count,best
        queries=[sum((1<<j) for j,p in enumerate(cols) if p&(1<<i)) for i in range(5)]
        if len(set(queries))<5:
            return
        count+=1
        m=len(cols)
        # Centers giving at least one positive answer have total weight <=4;
        # at most two set bits can lie beyond the occupied coordinates.
        trace=set()
        for outside in range(3):
            for inside in range(1<<m):
                if inside.bit_count()+outside>4:
                    continue
                response=0
                for i,q in enumerate(queries):
                    if (inside^q).bit_count()+outside<=2:
                        response|=1<<i
                if response:
                    trace.add(response)
        best=max(best,len(trace))
        histogram[len(trace)]+=1
        assert len(trace)<31, ('shattered candidate',cols)
    def visit(p,cap,cols):
        if p==32:
            examine(cols)
            return
        limit=min(cap[i] for i in range(5) if p&(1<<i))
        for times in range(limit+1):
            nextcap=tuple(cap[i]-times*bool(p&(1<<i)) for i in range(5))
            visit(p+1,nextcap,cols+[p]*times)
    visit(1,(2,2,2,2,2),[])
    assert count==7260, count
    assert best==26, best
    print('UNIVERSAL_FIVE_QUERY_OBSTRUCTION_PASS',count,'normal_forms','max_nonzero_patterns',best)


def verify_symbolic_fiber_sanity():
    # Finite corroboration of each branch type invoked in the universal proof.
    # The universal proof remains the symbolic incidence-size case analysis.
    for d in (4,5,6,7,8):
        U=set(range(d))
        H1={frozenset()} | {frozenset((i,)) for i in U} | {frozenset((0,j)) for j in U-{0}}
        H2={frozenset(),frozenset((0,)),frozenset((1,))} | {frozenset((i,j)) for i in U for j in U if i<j and (i in (0,1) or j in (0,1))}
        def is_star_or_singletons(family):
            if all(len(c)==1 for c in family): return True
            return any(all(c==frozenset((b,)) or (len(c)==2 and b in c) for c in family) for b in U)
        for H in (H1,H2):
            for q in range(1<<d):
                support=frozenset(i for i in U if (q>>i)&1)
                yes={c for c in H if len(c^support)<=2}
                no=H-yes
                assert not yes or not no or len(yes)<=5 or is_star_or_singletons(no), (d,H is H2,q,len(yes),no)
        F={frozenset()} | {frozenset((i,)) for i in U} | {frozenset((i,j)) for i in U for j in U if i<j}
        for q in range(1<<d):
            s=frozenset(i for i in U if(q>>i)&1)
            yes={c for c in F if len(c^s)<=2}
            if 1<=len(s)<=2:
                assert len(yes)==2*d
            elif 3<=len(s)<=4:
                assert len(yes)<=6
            else:
                assert not yes or yes==F
    print('STRUCTURAL_BRANCH_TYPES_PASS ambient=4..8')


def check_small_dimensions():
    for d,target in ((1,0),(2,0),(3,1),(4,3),(5,4),(6,5)):
        n=1<<d
        masks=[sum(1<<c for c in range(n) if dist(c,x)<=2) for x in range(n)]
        allcenters=(1<<n)-1
        @lru_cache(None)
        def depth_possible(S,k):
            if k==0:
                return bool(S)
            if S.bit_count()<(1<<k):
                return False
            for mask in masks:
                pos=S&mask;neg=S&~mask
                if pos.bit_count()>=(1<<(k-1)) and neg.bit_count()>=(1<<(k-1)) and depth_possible(pos,k-1) and depth_possible(neg,k-1):
                    return True
            return False
        assert depth_possible(allcenters,target)
        assert not depth_possible(allcenters,target+1)
        print('EXACT_SMALL_ONLINE_PASS',d,target,depth_possible.cache_info().currsize)


def main():
    test_static(CERT['vc3_four_dimensional_witness']['queries'],CERT['vc3_four_dimensional_witness']['centers_by_binary_pattern'],4)
    print('THREE_QUERY_STATIC_SHATTER_PASS',8)
    verify_symbolic_fiber_sanity()
    test_static(CERT['vc4_witness_queries'],CERT['vc4_witness_centers_by_binary_pattern'],5)
    print('FOUR_QUERY_STATIC_SHATTER_PASS',len(CERT['vc4_witness_centers_by_binary_pattern']))
    leaves,nodes=test_tree(CERT['online_tree_depth5'],6)
    assert len(leaves)==32 and len(set(leaves))==32 and nodes==31
    print('DEPTH_FIVE_ONLINE_TREE_PASS',nodes,len(leaves))
    verify_five_obstruction()
    check_small_dimensions()
    print('RADIUS_TWO_ALL_CHECKS_PASS')

if __name__=='__main__':
    main()
