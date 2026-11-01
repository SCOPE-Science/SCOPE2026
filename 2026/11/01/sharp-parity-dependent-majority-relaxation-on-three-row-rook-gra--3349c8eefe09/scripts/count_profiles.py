#!/usr/bin/env python3
"""Exact first-entry and least-period counts on K_3 Cartesian K_n.

The eight frequencies are for the binary columns 000,...,111.
All arithmetic is integer; the reduction is exact for every n>=2.
"""
from itertools import combinations
from collections import Counter
from math import factorial
import sys

def profiles(n):
    for cuts in combinations(range(n+7),7):
        last=-1; out=[]
        for c in cuts:
            out.append(c-last-1);last=c
        out.append(n+6-last)
        yield tuple(out)

def orbit(p,n):
    types=tuple(j for j,v in enumerate(p) if v)
    weights=tuple(p[j] for j in range(8) if p[j])
    seen={}; words=[]
    while types not in seen:
        seen[types]=len(words)
        words.append(types)
        sums=[sum(w for typ,w in zip(types,weights) if (typ>>i)&1) for i in range(3)]
        updated=[]
        for typ in types:
            value=0
            for i in range(3):
                old=(typ>>i)&1
                neighbors=sums[i]-old+sum((typ>>h)&1 for h in range(3) if h!=i)
                new=(1 if 2*neighbors>n+1 else (0 if 2*neighbors<n+1 else old))
                value|=new<<i
            updated.append(value)
        types=tuple(updated)
    return len(words)-seen[types],seen[types]

def census(n):
    counts=Counter();fac=factorial(n)
    for p in profiles(n):
        d,t=orbit(p,n)
        ways=fac
        for c in p:ways//=factorial(c)
        counts[d,t]+=ways
    assert sum(counts.values())==8**n
    assert max(t for d,t in counts)<= (3 if n&1 else 4)
    assert set(d for d,t in counts)<={1,2}
    return counts

def main():
    for n in map(int,sys.argv[1:]) if len(sys.argv)>1 else range(2,13):
        counts=census(n)
        print(n, sorted((d,t,counts[d,t]) for d,t in counts))

if __name__=='__main__': main()
