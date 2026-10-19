#!/usr/bin/env python3
"""Self-contained direct comparison for distinct palindromic scattered subsequences.
Not a substitute for the all-parameter combinatorial proof.
"""
from collections import Counter
from itertools import permutations, product
from math import comb


def raw_palette(q, k, order=None):
    if order is None:
        order=tuple(range(q))
    w=order*k
    subs={()}
    for x in w:
        subs |= {s+(x,) for s in tuple(subs)}
    result=Counter()
    for s in subs:
        if s and s==s[::-1]:
            result[len(s)] += 1
    return result


def predicted(q, k):
    result=Counter()
    # every palindrome is determined by its half-word
    for m in range(k):
        for e in range(m+1):
            if 1+m+e<=k:
                result[2*m+1] += q*comb(m,e)*(q-1)**(m-e)
    for m in range(1,k):
        for e in range(m):
            if 1+m+e<=k:
                result[2*m] += q*comb(m-1,e)*(q-1)**(m-1-e)
    return result


def independent_greedy(q,k,limits=None):
    # This is independent of the closed-form coefficient derivation:
    # list all possible palindromes up to longest theoretical candidate,
    # and directly embed each into the actual host.
    W=tuple(range(q))*k
    tally=Counter()
    for length in range(1, min(2*k+2, len(W)+1)):
        m=(length+1)//2
        for half in product(range(q),repeat=m):
            cand=half+half[-2::-1] if length%2 else half+half[::-1]
            pos=0
            for z in cand:
                while pos<len(W) and W[pos]!=z: pos+=1
                if pos==len(W): break
                pos+=1
            else: tally[length]+=1
    return tally


def main():
    trials=[(2,k) for k in range(1,8)]+[(3,k) for k in range(1,6)]+[(4,k) for k in range(1,5)]+[(5,k) for k in range(1,4)]+[(6,k) for k in range(1,3)]
    for q,k in trials:
        expect=predicted(q,k)
        direct=raw_palette(q,k)
        if direct != expect:
            raise AssertionError((q,k,'direct',direct,expect))
        if q**k<=10000:
            third=independent_greedy(q,k)
            if third != expect:
                raise AssertionError((q,k,'greedy',third,expect))
    perm_checks=0
    for q,k in [(3,4),(4,3),(5,2)]:
        for order in permutations(range(q)):
            direct=raw_palette(q,k,order)
            if direct!=predicted(q,k): raise AssertionError((q,k,order,direct,predicted(q,k)))
            perm_checks+=1
    for q in range(2,11):
        last=Counter()
        for k in range(1,13):
            curr=predicted(q,k)
            assert sum(curr.values())>sum(last.values())
            assert max(curr)==2*k-1
            last=curr
    print('ALL_REPEATED_PERMUTATION_PALINDROME_CHECKS_PASSED', 'main_pairs',len(trials),'permutations',perm_checks,'q_range', '2..10', 'k_range','1..12')

if __name__=='__main__': main()
