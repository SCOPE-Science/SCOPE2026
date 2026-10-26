#!/usr/bin/env python3
"""Independent verification of exact small 2-factor VC/Littlestone certificates."""
from itertools import combinations,permutations
from functools import lru_cache
import json,sys


def canon(t):return tuple(sorted(tuple(sorted(e)) for e in t))

def independent_factors(n):
    found=set()
    # All Hamiltonian cycles, with vertex zero fixed, up to reversal.
    for p in permutations(range(1,n)):
        if p[0]>p[-1]:continue
        cyc=(0,)+p
        found.add(canon((cyc[i],cyc[(i+1)%n]) for i in range(n)))
    # The only disconnected spanning 2-regular simple graphs of <=6 vertices
    # are two vertex-disjoint triangles, possible exactly for n=6.
    if n==6:
        for block in combinations(range(1,6),2):
            a=(0,)+block;b=tuple(x for x in range(6) if x not in a)
            found.add(canon(list(combinations(a,2))+list(combinations(b,2))))
    return found

def verify_tree(node,admissible,depth,answers,all_leaves):
    if depth==0:
        assert set(node)=={'witness_edges'}
        witness=canon(node['witness_edges'])
        assert witness in admissible
        for e,v in answers:
            assert (e in witness)==bool(v)
        all_leaves.append(witness)
        return
    assert set(node)=={'query','zero','one'}
    edge=tuple(sorted(node['query']))
    for v,key in ((0,'zero'),(1,'one')):
        verify_tree(node[key],admissible,depth-1,answers+[(edge,v)],all_leaves)


def verify(case):
    n=case['n'];edges=list(combinations(range(n),2));factors=independent_factors(n)
    assert len(factors)==case['number_of_factors']
    assert all(len(f)==n and all(sum(u in e for e in f)==2 for u in range(n)) for f in factors)
    qs=[tuple(q) for q in case['vc_queries']]
    assert len(qs)==case['vc_dimension']
    assert len(case['vc_witnesses'])==1<<len(qs)
    for bit,raw in enumerate(case['vc_witnesses']):
        f=canon(raw)
        assert f in factors
        assert sum((q in f)<<i for i,q in enumerate(qs))==bit
    leaf=[]
    d=case['littlestone_dimension']
    verify_tree(case['adaptive_tree'],factors,d,[],leaf)
    assert len(leaf)==2**d and len(set(leaf))==len(leaf)
    # Compute all lower- and upper-dimension claims independently, using
    # a different enumeration of objects and exhaustive query families.
    F=list(sorted(factors));N=len(F);allh=(1<<N)-1
    pos=[sum(1<<i for i,f in enumerate(F) if e in f) for e in edges]
    neg=[allh^x for x in pos]
    @lru_cache(None)
    def ld(U):
        if U.bit_count()<2:return 0
        v=0
        for p,q in zip(pos,neg):
            a,b=U&p,U&q
            if a and b:v=max(v,1+min(ld(a),ld(b)))
        return v
    assert ld(allh)==d
    # Every potential VC set of size exactly v+1 fails. If v+1 sets fail,
    # no larger set can be shattered by monotonicity. Full lower witness above.
    badsize=len(qs)+1
    witness_count=0
    for ix in combinations(range(len(edges)),badsize):
        seen=set()
        for f in F:
            seen.add(sum((edges[j] in f)<<h for h,j in enumerate(ix)))
            if len(seen)==2**badsize:
                witness_count+=1;break
    assert witness_count==0,(n,witness_count)
    print(f'n={n}: factors={N}, VC={len(qs)}, Ldim={d}, Ldim_states={ld.cache_info().currsize}, excluded_VC_{badsize}_sets={witness_count}, leaves={len(leaf)}')

if __name__=='__main__':
    with open(sys.argv[1]) as f:cert=json.load(f)
    assert cert['format']=='edge-query-two-factor-certificates-v1'
    for item in cert['cases']:verify(item)
    print('ALL_TWO_FACTOR_SHATTERING_CERTIFICATES_PASS')
