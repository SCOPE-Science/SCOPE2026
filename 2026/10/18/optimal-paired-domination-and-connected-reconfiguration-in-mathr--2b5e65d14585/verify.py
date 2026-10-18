#!/usr/bin/env python3
"""Exhaustive verification of a paired-domination census on two-subset Kneser graphs."""
from itertools import combinations
from math import comb

def direct(n):
    edges=list(combinations(range(n),2))
    masks=[(1<<i)|(1<<j) for i,j in edges]
    adj=[sum(1<<j for j in range(len(edges)) if i!=j and masks[i]&masks[j]==0) for i in range(len(edges))]
    got=0; types={6:0,7:0,8:0}; mismatches=[]; subset_count=0
    for tup in combinations(range(len(edges)),4):
        subset_count+=1
        s=sum(1<<i for i in tup)
        dom=all((s & (adj[v] | (1<<v)))!=0 for v in range(len(edges)))
        pm=any(((adj[tup[a]]>>tup[b])&1) and ((adj[tup[c]]>>tup[d])&1) for a,b,c,d in ((0,1,2,3),(0,2,1,3),(0,3,1,2)))
        paired=dom and pm
        triples=any(not (masks[a]&masks[b] or masks[a]&masks[c] or masks[b]&masks[c]) for a,b,c in combinations(tup,3))
        if paired!=triples: mismatches.append((tup,paired,triples))
        if paired:
            got+=1
            supp=(0)
            for i in tup:supp|=masks[i]
            types[supp.bit_count()]+=1
    want=180*comb(n,6)+(315*comb(n,7) if n>=7 else 0)+(105*comb(n,8) if n>=8 else 0)
    expected={6:180*comb(n,6),7:315*comb(n,7) if n>=7 else 0,8:105*comb(n,8) if n>=8 else 0}
    assert not mismatches and got==want and types==expected,(n,mismatches[:2],got,want,types,expected)
    print(f'n={n} selected_4={subset_count} optimum={got} supports={types}')
    return subset_count

if __name__=='__main__':
    total=0
    for n in range(6,11):total+=direct(n)
    print('VERIFICATION_OK n=6..10 candidate_sets=',total)
