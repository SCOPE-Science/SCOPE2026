#!/usr/bin/env python3
"""Independent finite checks of grouped rooted-comb path-concept dimensions.

Run: python3 verify_comb.py
Only Python's standard library is required. Small finite checks are not an
infinite proof; the accompanying mathematical argument covers all parameters.
"""
from functools import lru_cache
from itertools import product


def all_compositions(n):
    for bits in product((0, 1), repeat=n-1):
        groups=[]; size=1
        for bit in bits:
            if bit: groups.append(size); size=1
            else: size += 1
        groups.append(size)
        yield tuple(groups)


def expected(groups):
    total=sum(groups)
    if total == 1: return (0, 0)
    k=0; current=0
    for weight in groups:
        current += weight
        if current >= 2:
            k+=1; current=0
    return (1, 1+k.bit_length()-1)


def direct_dimensions(groups):
    # Build the actual rooted tree: spine vertices 0,...,m-1;
    # a_i leaf children at spine vertex i.
    m=len(groups); parent=[-1]+list(range(m-1))
    for i,w in enumerate(groups): parent += [i]*w
    leaves=tuple(range(m,len(parent)))
    N=len(leaves)
    concepts=[]
    for leaf in leaves:
        path=set(); v=leaf
        while v>=0:
            path.add(v); v=parent[v]
        concepts.append(path)
    queries=[]
    for v in range(len(parent)):
        mask=sum(1<<j for j,p in enumerate(concepts) if v in p)
        if mask and mask!=(1<<N)-1: queries.append(mask)
    queries=tuple(sorted(set(queries)))
    full=(1<<N)-1
    @lru_cache(None)
    def rank(state):
        if state.bit_count()<2: return 0
        val=0
        for q in queries:
            pos=state&q; neg=state&~q
            if pos and neg:
                val=max(val, 1+min(rank(pos),rank(neg)))
        return val
    vc=0
    if N>1:
        vc=1
        for i,x in enumerate(queries):
            for y in queries[i+1:]:
                if all((full & ((x if a else ~x)&(y if b else ~y))) for a in (0,1) for b in (0,1)):
                    vc=2
                    break
            if vc>1: break
    return (vc,rank(full))


def main():
    cases=0
    for n in range(1,11):
        for profile in all_compositions(n):
            predicted=expected(profile)
            observed=direct_dimensions(profile)
            assert predicted==observed,(profile,predicted,observed)
            cases+=1
        print('TOTAL_LEAVES_CHECKED',n,'compositions',2**(n-1))
    special=((2,)*8,(1,)*8,(1,2,1,2,1,2),(100,),(1,100,1),(2,1,1,2,1,1,2,1,1))
    for profile in special:
        print('PROFILE',profile,'PREDICTION',expected(profile))
    assert expected((1,)*8)==(1,3)
    assert expected((2,)*8)==(1,4)
    assert expected((100,))==(1,1)
    assert expected((1,))==(0,0)
    print('ALL_ROOTED_COMB_PATH_SHATTERING_CHECKS_PASS', 'profiles',cases)

if __name__=='__main__': main()
