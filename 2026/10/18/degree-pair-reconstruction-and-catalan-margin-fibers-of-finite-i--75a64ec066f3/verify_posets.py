#!/usr/bin/env python3
"""Independent brute-force enumeration of strictly ordered finite posets."""
from math import comb
from collections import defaultdict

def census(n):
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    types=set();out_profs=set();valid=0
    for pattern in range(1<<len(edges)):
        successors=[0]*n
        for z,(i,j) in enumerate(edges):
            if (pattern>>z)&1: successors[i]|=1<<j
        if any((successors[i]>>j)&1 and (successors[j] & ~successors[i])
               for i,j in edges):continue
        # An interval order is exactly a poset with nested strict successor sets.
        if any((a & ~b) and (b & ~a) for a in successors for b in successors):continue
        valid+=1
        out=[a.bit_count() for a in successors]
        indeg=[sum((successors[i]>>j)&1 for i in range(n)) for j in range(n)]
        # Recover every predecessor set by sorting vertices by outdegree.
        rank=sorted(range(n),key=lambda i:(-out[i],indeg[i],i))
        for y in range(n):
            reconstructed=set(rank[:indeg[y]])
            actual={x for x in range(n) if (successors[x]>>y)&1}
            assert reconstructed==actual,(n,pattern,y)
        # Identical degree pairs are twins and can be interchanged freely.
        for x in range(n):
            for y in range(x+1,n):
                if (out[x],indeg[x])==(out[y],indeg[y]):
                    assert successors[x]==successors[y]
                    assert all(((successors[z]>>x)&1)==((successors[z]>>y)&1) for z in range(n))
        canon=tuple(tuple((successors[i]>>j)&1 for j in rank) for i in rank)
        types.add(canon)
        out_profs.add(tuple(sorted(out,reverse=True)))
    return valid,len(types),len(out_profs)

if __name__=='__main__':
    expected=[1,2,5,15,53,217]
    for n in range(1,7):
        labeled,types,profiles=census(n)
        assert types==expected[n-1],(n,types)
        assert profiles==comb(2*n,n)//(n+1)
        print(f'n={n} topological_labelings={labeled} interval_order_types={types} successor_profiles={profiles}')
    print('VERIFY_POSETS_PASS')
