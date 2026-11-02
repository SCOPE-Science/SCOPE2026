#!/usr/bin/env python3
"""Exact standard-library census for membership shattering of maximal stable sets.
Run: python verify.py . No external package is required.
"""
from itertools import combinations, permutations
from functools import lru_cache
from collections import Counter


def graph_edges(n, code):
    return tuple(e for bit, e in enumerate(combinations(range(n), 2)) if code & (1 << bit))


def maximal_stable_sets(n, edges):
    nbr = [0]*n
    for u,v in edges:
        nbr[u] |= (1 << v)
        nbr[v] |= (1 << u)
    sets=[]
    for s in range(1 << n):
        if any(((s>>u)&1) and ((s>>v)&1) for u,v in edges):
            continue
        if all((s>>v)&1 or (nbr[v] & s) for v in range(n)):
            sets.append(s)
    return tuple(sets)


def vc_dimension(n, concepts):
    for k in range(n,-1,-1):
        for support in combinations(range(n),k):
            mask=sum(1<<v for v in support)
            if len({s & mask for s in concepts}) == 1<<k:
                return k
    assert False


def littlestone_dimension(n, concepts):
    @lru_cache(None)
    def dim(support):
        if len(support)<2:
            return 0
        best=0
        for v in range(n):
            pos=tuple(s for s in support if s & (1<<v))
            neg=tuple(s for s in support if not s & (1<<v))
            if pos and neg:
                best=max(best, 1+min(dim(pos),dim(neg)))
        return best
    return dim(tuple(concepts))


def canonical_code(n, edges):
    e=set(tuple(sorted(x)) for x in edges)
    pairs=list(combinations(range(n),2))
    return min(sum((1<<i) for i,(u,v) in enumerate(pairs)
                   if tuple(sorted((perm[u],perm[v]))) in e)
               for perm in permutations(range(n)))


def has_induced_p4(n, edges):
    e=set(edges)
    for sub in combinations(range(n),4):
        deg=[sum((min(u,v),max(u,v)) in e for v in sub if v!=u) for u in sub]
        if sorted(deg)==[1,1,2,2]:return True
    return False


def main():
    tables={}
    gap_types=Counter()
    is_cograph=Counter()
    for n in range(1,6):
        count=1 << (n*(n-1)//2)
        table=Counter()
        for code in range(count):
            edges=graph_edges(n,code)
            concepts=maximal_stable_sets(n,edges)
            vc=vc_dimension(n,concepts)
            ld=littlestone_dimension(n,concepts)
            table[(vc,ld)]+=1
            if n<=4: assert vc==ld
            if n==5 and ld>vc:
                assert (vc,ld)==(1,2)
                can=canonical_code(n,edges)
                gap_types[can]+=1
                is_cograph[not has_induced_p4(n,edges)]+=1
        tables[n]=dict(sorted(table.items()))
        print('ORDER',n,'LABELLED',count,'DIMENSION_COUNTS',tables[n])
    assert len(gap_types)==2
    assert sorted(gap_types.values())==[30,60]
    assert is_cograph[True]==30 and is_cograph[False]==60
    print('FIVE_VERTEX_GAP_TYPES',[(hex(i),c) for i,c in sorted(gap_types.items())])
    print('COGRAPH_GAP',is_cograph[True],'NONCOGRAPH_GAP',is_cograph[False])
    F_edges=((0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3))
    F=maximal_stable_sets(5,F_edges)
    assert F==(1,2,20,24)
    assert vc_dimension(5,F)==1 and littlestone_dimension(5,F)==2
    assert not has_induced_p4(5,F_edges)
    print('WITNESS_F',F,'VC',vc_dimension(5,F),'LD',littlestone_dimension(5,F))
    print('COMPLETE_GRAPH_CENSUS_PASS')

if __name__=='__main__':main()
