#!/usr/bin/env python3
"""Independent finite checks for ternary no-equal-adjacency 2-abelian quotient."""
from itertools import product
from math import comb

ARCS = ((0,1),(1,0),(1,2),(2,1),(2,0),(0,2))

def coefficient(e):
    # [z^e] 3/(1-z)^4(1+z)^2 - 3z^2/(1-z^2)
    return 3*sum((-1)**k*(k+1)*comb(e-k+3,3)
                 for k in range(e+1)) - (3 if e>=2 and e%2==0 else 0)

def word_observations(n):
    answer = set()
    for first in range(3):
        for choices in product((0,1), repeat=n-1):
            word=[first]
            for choice in choices:
                word.append(tuple(c for c in range(3) if c != word[-1])[choice])
            ones=tuple(word.count(i) for i in range(3))
            bigrams=tuple(sum((a,b)==edge for a,b in zip(word,word[1:]))
                          for edge in ARCS)
            answer.add((ones,bigrams))
    return len(answer)

def compositions(total,parts):
    if parts==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first, parts-1):
                yield (first,)+rest

def euler_profile_count(e):
    if e==0: return 3
    count=0
    for counts in compositions(e, 6):
        out=[0,0,0]; inn=[0,0,0]
        for (a,b),multiplicity in zip(ARCS,counts):
            out[a]+=multiplicity;inn[b]+=multiplicity
        imbalance=tuple(out[i]-inn[i] for i in range(3))
        active=sum(out[i]+inn[i]>0 for i in range(3))
        if imbalance==(0,0,0):count+=active
        elif sorted(imbalance)==[-1,0,1]:count+=1
    return count

def main():
    for n in range(1,14):
        assert word_observations(n)==coefficient(n-1),(n,'word')
    for e in range(13):
        assert euler_profile_count(e)==coefficient(e),(e,'euler')
    print('TERNARY_HOMOPOLYMER_FREE_2ABELIAN_PASS brute_lengths=1..13 euler_arc_totals=0..12')

if __name__=='__main__':main()
