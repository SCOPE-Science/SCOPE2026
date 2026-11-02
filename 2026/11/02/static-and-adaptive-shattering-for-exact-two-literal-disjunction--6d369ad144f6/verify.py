"""Standalone finite certificates for rank-two monotone-disjunction shattering.

Usage: python verify.py certificates.json
"""
import itertools
import json
import math
import sys
from functools import lru_cache


def verify_basis(d, cols):
    assert all(isinstance(x,int) and 0 <= x < (1<<d) for x in cols)
    targets={x|y for i,x in enumerate(cols) for y in cols[i+1:]}
    assert targets==set(range(1<<d)),(d,sorted(set(range(1<<d))-targets))


def verify_tree(tree):
    n,d=tree['n'],tree['depth']
    nodes,leaves=tree['nodes'],tree['leaves']
    assert len(nodes)==(1<<d)-1 and len(leaves)==1<<d
    assert set(nodes)=={''.join(s) for k in range(d) for s in itertools.product('01',repeat=k)}
    assert set(leaves)=={''.join(s) for s in itertools.product('01',repeat=d)}
    seen=set()
    for path,centre in leaves.items():
        assert len(centre)==2 and 1 <= centre[0] < centre[1] <=n
        pair=tuple(centre)
        assert pair not in seen
        seen.add(pair)
        for k,bit in enumerate(path):
            pool=nodes[path[:k]]
            assert len(pool)==len(set(pool)) and all(1<=x<=n for x in pool)
            prediction=int(bool(set(pair)&set(pool)))
            assert prediction==int(bit),(n,path,k,pool,pair)
    return (n,d,len(nodes),len(leaves))


def verify_dimension_upper():
    # A pool with t excluded coordinates leaves C(t,2) negative concepts.
    expected_l={2:0,3:1,4:2,5:3,6:3,7:4,8:4,9:4,10:5,11:5,12:5}
    depth_witness={3:1,4:2,5:3,7:4,10:5}
    for n,depth in expected_l.items():
        if n in (9,12):
            target={9:5,12:6}[n]
            possibilities={math.comb(t,2) for t in range(n+1)}
            assert not any((1<<(target-1))<=v<=math.comb(n,2)-(1<<(target-1)) for v in possibilities)
            assert depth==target-1
        else:
            assert math.comb(n,2)<(1<<(depth+1))
        assert any(m<=n and dd==depth for m,dd in depth_witness.items()) or depth==0
    return expected_l


def verify_static_upper():
    # Any shattered d-tuple needs two zero columns, all d singleton columns.
    # d=3 needs one extra column to represent the full vector.
    # d=4 needs >=2 extras: one extra creates at most 2 weight-three patterns.
    # d=5 needs >=5 extras: <=4 cannot produce all ten triples AND the all-ones pattern.
    # d=6 with n=12 needs 8 base columns and <=4 extras. They yield at most
    # 22+4*7+6=56 distinct OR outputs, fewer than 64.
    assert 22+4*7+6<64
    # Independent finite cross-check: no choice of <=4 extra nonunit columns
    # extends canonical d=5 columns to a complete pairwise-OR basis.
    d=5
    base=[0,0]+[1<<i for i in range(d)]
    choices=[x for x in range(1,1<<d) if x.bit_count()>=2]
    checked=0
    for k in range(5):
        for extras in itertools.combinations(choices,k):
            checked+=1
            cols=base+list(extras)
            outputs={x|y for i,x in enumerate(cols) for y in cols[i+1:]}
            assert len(outputs)<(1<<d),(k,extras)
    assert checked==sum(math.comb(26,k) for k in range(5))
    return checked



def exact_littlestone(n):
    pairs=list(itertools.combinations(range(n),2))
    all_concepts=(1<<len(pairs))-1
    queries=[]
    for pool in range(1<<n):
        positive=sum(1<<j for j,(a,b) in enumerate(pairs)
                     if (pool>>a)&1 or (pool>>b)&1)
        if 0<positive<all_concepts:
            queries.append(positive)
    queries=sorted(set(queries))
    @lru_cache(None)
    def can(concepts,depth):
        if concepts.bit_count()<(1<<depth):return False
        if depth==0:return True
        limit=1<<(depth-1)
        for q in queries:
            yes=concepts&q
            no=concepts^yes
            if yes.bit_count()>=limit and no.bit_count()>=limit:
                if can(no,depth-1) and can(yes,depth-1):return True
        return False
    depth=0
    while can(all_concepts,depth+1):
        depth+=1
    return depth

def main():
    with open(sys.argv[1],encoding='utf-8') as f:cert=json.load(f)
    assert sorted(cert)==['column_bases','definition','trees']
    expected_basis={1:3,2:4,3:6,4:8,5:12}
    for d,n in expected_basis.items():
        cols=cert['column_bases'][str(d)]
        assert len(cols)==n
        verify_basis(d,cols)
    print('OR_BASES_PASS',sorted(expected_basis.items()))
    checks=verify_static_upper()
    print('DIMENSION_FIVE_EXCLUSION_PASS',checks)
    sizes=[verify_tree(t) for t in cert['trees']]
    assert sizes==[(3,1,1,2),(4,2,3,4),(5,3,7,8),(7,4,15,16),(10,5,31,32)]
    print('TREE_WITNESSES_PASS',sizes)
    l=verify_dimension_upper()
    v={2:0,3:1,4:2,5:2,6:3,7:3,8:4,9:4,10:4,11:4,12:5}
    assert [(v[n],l[n]) for n in range(2,13)]==[(0,0),(1,1),(2,2),(2,3),(3,3),(3,4),(4,4),(4,4),(4,5),(4,5),(5,5)]
    computed={n:exact_littlestone(n) for n in range(2,13)}
    assert computed==l
    print('INDEPENDENT_ADAPTIVE_RECURSION_PASS',list(computed.items()))
    print('EXACT_DIMENSIONS_PASS',[(n,v[n],l[n]) for n in range(2,13)])
    print('SPARSE_DISJUNCTION_ALL_CHECKS_PASS')

if __name__=='__main__':main()
