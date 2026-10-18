#!/usr/bin/env python3
"""Literal exhaustive checks of the one-long-gap circular-attractor theorem.
All indices zero based; no external modules or randomness.
"""
from itertools import combinations
from collections import defaultdict


def word(m, q, s):
    return ('1' + '0' * (q-1)) * m + '0' * s


def factors_and_coverage(w):
    n = len(w)
    ww = w + w
    masks = defaultdict(int)
    for length in range(1, n+1):
        for start in range(n):
            fac = ww[start:start+length]
            # literal circular occurrence; all crossed positions
            for offset in range(length):
                masks[fac] |= 1 << ((start+offset) % n)
    return masks


def predicted(m,q,s):
    L=(m-1)*q
    return {(j*q,L+t) for j in range(m) for t in range(1,q+s)
            if (j == m-1 or t<=q) and (j == 0 or t>=s)}


def run():
    cases=0
    total_pairs=0
    total_factors=0
    extremal=[]
    for m in range(2,8):
        for q in range(1,7):
            for s in range(1,8):
                w=word(m,q,s)
                n=len(w)
                masks=factors_and_coverage(w)
                needles=('1','0'*q, '1'+'0'*q, '0'*q+'1')
                assert all(u in masks for u in needles)
                # Every factor's coverage mask contains a witness mask.
                witness=[masks[u] for u in needles]
                assert all(any(v & x == x for x in witness) for v in masks.values()), (m,q,s)
                actual={(a,b) for a,b in combinations(range(n),2)
                        if all((bits & ((1<<a)|(1<<b))) !=0 for bits in witness)}
                expected=predicted(m,q,s)
                assert actual == expected, (m,q,s,actual^expected)
                count=2*q+(m-2)*max(q-s+1,0)
                assert len(actual)==count,(m,q,s,len(actual),count)
                # nonexistence of singleton from distinct one-letter factors.
                assert masks['0'] & masks['1']==0
                if (m,q,s)==(5,4,3):
                    assert len(actual)==14
                    extremal=sorted(actual)
                cases+=1
                total_pairs+=len(actual)
                total_factors+=len(masks)
    print('EXACT LITERAL CHECK: PASS')
    print(f'parameter triples: {cases}; total distinct circular factors: {total_factors}; total optimal pairs: {total_pairs}')
    print('all factors dominated by one of four witness coverage masks: PASS')
    print('all two-position subsets exactly equal to theorem classification: PASS')
    print('all singleton attractors impossible: PASS')
    print('sample (m,q,s)=(5,4,3), optimal pairs:', extremal)

if __name__=='__main__':
    run()
