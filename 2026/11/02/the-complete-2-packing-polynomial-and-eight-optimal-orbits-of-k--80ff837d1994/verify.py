#!/usr/bin/env python3
"""Exact finite cross-checks for a Kneser 2-packing cardinality enumerator.

Uses an anchored-pair count and direct exhaustive subset checks; no extra modules.
"""
from itertools import combinations
from math import comb, factorial
from collections import Counter


def choose(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0


def by_venn(r):
    n=3*r-3
    types={}
    for k in range(4):
        p12,p13,p23=[2]*k+[1]*(3-k)
        for t in range(min(p12,p13,p23)+1):
            h=p12+p13+p23-t-3
            a=r-p12-p13+t
            b=r-p12-p23+t
            c=r-p13-p23+t
            if min(h,a,b,c,p12-t,p13-t,p23-t)<0:
                continue
            den=(factorial(t)*factorial(p12-t)*factorial(p13-t)*factorial(p23-t)
                 *factorial(a)*factorial(b)*factorial(c)*factorial(h))
            num=comb(3,k)*factorial(n)
            assert (num//den)%6==0 and num%den==0
            types[(k,t)]=num//den//6
    singles=comb(n,r)
    pairs=singles*sum(comb(r,j)*comb(n-r,r-j) for j in (1,2))//2
    return (1,singles,pairs,sum(types.values())),types


def anchored(r):
    n=3*r-3
    singles=comb(n,r)
    triple_ordered=0
    for h in (1,2):
        copies=choose(r,h)*choose(n-r,r-h)
        count_third=0
        for w in range(h+1):
            for a in range(3):
                for b in range(3):
                    if 1<=w+a<=2 and 1<=w+b<=2:
                        c=r-w-a-b
                        count_third+=(choose(h,w)*choose(r-h,a)*choose(r-h,b)
                                      *choose(r-3+h,c))
        triple_ordered+=copies*count_third
    assert (singles*triple_ordered)%6==0
    return singles*triple_ordered//6


def exhaustive_small(r):
    n=3*r-3
    blocks=[sum(1<<i for i in c) for c in combinations(range(n),r)]
    edge=lambda x,y: (x&y).bit_count() in (1,2)
    pair_lists=[[j for j in range(i+1,len(blocks)) if edge(blocks[i],blocks[j])]
                for i in range(len(blocks))]
    pair_count=sum(map(len,pair_lists));triples=0;types=Counter()
    for i,L in enumerate(pair_lists):
        for j in L:
            for k in pair_lists[j]:
                if edge(blocks[i],blocks[k]):
                    triples+=1
                    p=[(blocks[x]&blocks[y]).bit_count()
                       for x,y in ((i,j),(i,k),(j,k))]
                    t=(blocks[i]&blocks[j]&blocks[k]).bit_count()
                    types[(p.count(2),t)]+=1
    return pair_count,triples,types

if __name__=='__main__':
    for r in range(4,26):
        coeff,types=by_venn(r)
        assert len(types)==8, (r,types)
        assert coeff[3]==anchored(r),r
        print('r',r,'n',3*r-3,'triples',coeff[3]) if r in (4,10,11,25) else None
    coeff,types=by_venn(4)
    P,T,TYPES=exhaustive_small(4)
    assert (P,T)==coeff[2:]
    assert dict(TYPES)==types
    print('VERIFY_OK: direct exhaustive K(9,4) pairs/triples, eight orbits; anchored formulas for r=4..25')
