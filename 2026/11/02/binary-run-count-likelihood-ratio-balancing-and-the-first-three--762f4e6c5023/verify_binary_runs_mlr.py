#!/usr/bin/env python3
"""Exact arithmetic and exhaustive finite checks for run-count balancing laws.

Usage: python verify_binary_runs_mlr.py
This checker does not replace the all-length combinatorial proof.
"""
from functools import lru_cache
from itertools import product
from math import comb
from fractions import Fraction


def binom(n,k):
    return comb(n,k) if n>=0 and 0<=k<=n else 0


def binary_counts(n,k,r):
    if k in (0,n):return int(r==1)
    if r<2 or r>n:return 0
    s=r//2
    if r%2==0:
        return 2*binom(k-1,s-1)*binom(n-k-1,s-1)
    return (binom(k-1,s)*binom(n-k-1,s-1)
            +binom(k-1,s-1)*binom(n-k-1,s))


@lru_cache(None)
def color_counts(composition,previous=-1):
    if not any(composition):return (1,)
    out=[0]*(sum(composition)+2)
    for symbol,num in enumerate(composition):
        if not num:continue
        q=list(composition);q[symbol]-=1
        sub=color_counts(tuple(q),symbol)
        increase=int(previous==-1 or previous!=symbol)
        for r,v in enumerate(sub):out[r+increase]+=v
    return tuple(out)


def main():
    tests=0
    # Independent small-word construction (not the formula used in the proof).
    for n in range(1,12):
        seen={(k,r):0 for k in range(n+1) for r in range(1,n+1)}
        for word in product((0,1),repeat=n):
            k=sum(word)
            r=1+sum(a!=b for a,b in zip(word,word[1:]))
            seen[k,r]+=1
        for k in range(n+1):
            for r in range(1,n+1):
                assert seen[k,r]==binary_counts(n,k,r),(n,k,r)
                tests+=1
    # Check all exact binary total-positivity minors through n=40.
    for n in range(2,41):
        for k in range(n+1):
            assert sum(binary_counts(n,k,r) for r in range(1,n+1))==binom(n,k)
            tests+=1
        for k in range(1,n//2):
            old=[binary_counts(n,k,r) for r in range(1,n+1)]
            new=[binary_counts(n,k+1,r) for r in range(1,n+1)]
            for r in range(1,n+1):
                for s in range(r+1,n+1):
                    assert old[r-1]*new[s-1]>=old[s-1]*new[r-1],(n,k,r,s)
                    tests+=1
            # Verify the conditional right-tail stochastic envelope.
            for cut in range(1,n+2):
                assert sum(old[cut-1:])*binom(n,k+1)<=sum(new[cut-1:])*binom(n,k)
                tests+=1
    # Three-letter fixed-composition laws from independent suffix recurrence.
    # Prove minimality of the all-positive, three-letter counterexample by
    # exhaustive compositions and every one-unit balancing move for n<=7.
    for n in range(3,8):
        for a in range(1,n-1):
            for b in range(1,n-a):
                c=n-a-b
                if c<1:continue
                oldcomposition=(a,b,c)
                for i,j in ((0,1),(0,2),(1,2)):
                    if oldcomposition[i]-oldcomposition[j]<2:continue
                    newcomposition=list(oldcomposition)
                    newcomposition[i]-=1
                    newcomposition[j]+=1
                    old=color_counts(oldcomposition)
                    new=color_counts(tuple(newcomposition))
                    for r in range(1,n+1):
                        for s in range(r+1,n+1):
                            assert old[r]*new[s]>=old[s]*new[r],(n,oldcomposition,newcomposition,r,s)
                            tests+=1
    # Actual smallest strictly positive three-color counterexample.
    old=color_counts((3,1,4))
    new=color_counts((2,2,4))
    assert old[7]==60 and old[8]==14 and sum(old)==280
    assert new[7]==120 and new[8]==24 and sum(new)==420
    assert old[7]*new[8]<old[8]*new[7]
    tests+=3
    print(f'EXACT_ASSERTIONS={tests}')
    print('THREE_COLOR_COUNTS_OLD='+str(old))
    print('THREE_COLOR_COUNTS_NEW='+str(new))
    print('THREE_COLOR_MLR_COUNTEREXAMPLE=R7_vs_R8')


if __name__=='__main__':main()
