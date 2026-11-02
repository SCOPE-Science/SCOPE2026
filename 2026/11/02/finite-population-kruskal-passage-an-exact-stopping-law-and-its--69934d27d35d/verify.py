#!/usr/bin/env python3
"""Independent finite-order checks for Kruskal-type random-deck passage laws."""
from collections import defaultdict
from itertools import permutations
from math import comb, e, factorial


def count_tail_by_subsets(m,n):
    L=m*n
    # Coefficients [x^t q^s] of product (1+x q^j)^m, restricted to s<L.
    dp={(0,0):1}
    for value in range(1,n+1):
        nxt=defaultdict(int)
        for (t,s),count in dp.items():
            for k in range(m+1):
                if s+k*value < L:
                    nxt[(t+k,s+k*value)] += count*comb(m,k)
        dp=nxt
    counts=[0]*(L+1)
    for (t,s),count in dp.items():
        counts[t]+=count
    return [counts[t]/comb(L,t) for t in range(L+1)], counts


def multiset_decks(m,n):
    counts=[m]*n
    L=m*n
    a=[0]*L
    def rec(p):
        if p==L:
            yield tuple(a)
            return
        for i in range(n):
            if counts[i]:
                counts[i]-=1; a[p]=i+1
                yield from rec(p+1)
                counts[i]+=1
    yield from rec(0)


def direct_t(deck):
    pos=0; taken=0
    while pos<len(deck):
        pos+=deck[pos]
        taken+=1
    return taken


def run():
    total_decks=0
    cases=0
    for m,n_max in [(1,7),(2,5),(3,4)]:
        for n in range(1,n_max+1):
            L=m*n
            tail,counts=count_tail_by_subsets(m,n)
            hist=[0]*(L+1)
            num=0
            for deck in multiset_decks(m,n):
                hist[direct_t(deck)]+=1
                num+=1
            expected=factorial(L)
            for i in range(1,n+1):
                expected//=factorial(m) if i==1 else 1 # workaround re-evaluate below
            expected=factorial(L)//(factorial(m)**n)
            assert num==expected, (m,n,num,expected)
            for t in range(L+1):
                direct=sum(hist[j] for j in range(t+1,L+1))/num
                assert abs(tail[t]-direct) < 1e-14, (m,n,t,tail[t],direct)
            assert tail[0]==1 and tail[L]==0
            assert all(tail[t]>=tail[t+1]-1e-14 for t in range(L))
            total_decks+=num
            cases+=1
    # Subset coefficients provide an independent finite-n expectation and tail sanity check.
    for n in (40,80,160):
        tail,_=count_tail_by_subsets(1,n)
        mean=sum(tail)
        assert 0 < mean < e
        target=7*e/4
        delta=n*(e-mean)
        assert abs(target-delta)<0.25, (n,mean,delta,target)
        for t in (1,2,3,4,5):
            asym=1/factorial(t)-t*(t*t-t+4)/(4*factorial(t)*n)
            assert abs(tail[t]-asym)<0.008, (n,t,tail[t],asym)
    print(f'VERIFY_OK multiset_parameter_cases={cases} direct_decks={total_decks} finite_n_bias_checked=40,80,160')

if __name__=='__main__': run()
