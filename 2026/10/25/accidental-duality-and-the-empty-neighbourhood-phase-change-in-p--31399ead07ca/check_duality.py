#!/usr/bin/env python3
"""Exact finite checks for coupled zero-instance instantial neighbourhoods.
All candidate neighbourhoods are nonempty subsets of {0,...,n-1}.
"""
from collections import Counter
from fractions import Fraction
from math import comb

def universe(n):
    return list(range(1,1<<n))

def results(n):
    subsets = universe(n)
    nsets=len(subsets)
    superbits=[]
    for A in subsets:
        superbits.append(sum(1<<i for i,B in enumerate(subsets) if A&B==A))
    closures=[0]*(1<<nsets)
    for family in range(1,1<<nsets):
        low=family&(-family)
        closures[family]=closures[family^low]|superbits[low.bit_length()-1]
    count=Counter(closures)
    collision=sum(t*t for t in count.values())
    # Independently enumerate upset-family signatures; verify exact fiber weights.
    antichain_count=0
    upset_count=0
    for upper in range(1<<nsets):
        minima=0
        okay=True
        for i,A in enumerate(subsets):
            if (upper>>i)&1:
                if (superbits[i]&upper)!=superbits[i]:
                    okay=False;break
                if not any(((upper>>j)&1) and B!=A and B&A==B for j,B in enumerate(subsets)):
                    minima+=1
        if okay:
            antichain_count+=4**(upper.bit_count()-minima)
            upset_count+=1
    assert collision==antichain_count
    expected=Fraction(collision,(1<<nsets)**2)
    print('n=',n,'upsets=',upset_count,'collisions=',collision,'total_pairs=',(1<<nsets)**2,
          'probability=',str(expected),'unrestricted_probability=',str(Fraction(1,4)+expected/4))
    return subsets,closures,collision

def direct_truth(N,A,n):
    # 0-ary PINL box and diamond (N stores selected nonempty subsets)
    box=any((U&A)==U for U in N)
    diamond=all((U&A)!=0 for U in N)
    return box,diamond

for n in (1,2,3,4):
    subs,signatures,C=results(n)
    if n<=3:
        for f in range(1<<len(subs)):
            A=[u for i,u in enumerate(subs) if (f>>i)&1]
            for g in range(1<<len(subs)):
                B=[u for i,u in enumerate(subs) if (g>>i)&1]
                same=signatures[f]==signatures[g]
                dual=all(direct_truth(A,x,n)[0] != direct_truth(B,((1<<n)-1)^x,n)[1]
                         for x in range(1<<n))
                assert same==dual,(n,f,g,same,dual)
        print('DIRECT_MODAL_DUALITY_OK',n)
print('FINITE_ZERO_INSTANCE_COUPLING_OK')
