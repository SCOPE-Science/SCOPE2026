#!/usr/bin/env python3
"""Finite local-rule certificate for 3-color cyclic dynamics on a clique with one leaf.
All possible nonhub clique-color supports and leaf-relative colors are covered.
"""
from itertools import combinations
from collections import Counter
from math import comb

def evolve(hub,leaf,nonhub):
    support=set(nonhub)
    step_hub=int(1 in support or leaf==1)
    step_leaf=int(leaf==2)
    y=tuple((a+int((a+1)%3==0 or (a+1)%3 in support)-step_hub)%3 for a in nonhub)
    return (hub+step_hub)%3, (leaf+step_leaf-step_hub)%3, y

def expected(S,L):
    if 1 in S and 2 in S:
        return {2:(0,3), 0:(1,3), 1:(2,3)}[L]
    if S=={0}:
        return {0:(0,1), 1:(2,1), 2:(1,1)}[L]
    if S <= {0,1}:
        return (1,1) if L==1 else (2,1)
    if S <= {0,2}:
        return (2,1) if L==1 else (1,1)
    raise ValueError(S)

support_hist=Counter()
for mask in range(1,8):
    S={i for i in range(3) if (mask>>i)&1}
    word=tuple(sorted(S))
    for L in range(3):
        x=(0,L,word); seen={}; seq=[]
        while x not in seen:
            seen[x]=len(seq);seq.append(x);x=evolve(*x)
            assert len(seq)<=6, (S,L)
        t,p=seen[x],len(seq)-seen[x]
        assert (t,p)==expected(S,L), (S,L,(t,p),expected(S,L))
        support_hist[(t,p,len(S))]+=1
assert sum(support_hist.values())==21
for r in range(1,16):
    counts=Counter()
    for (t,p,k),multiple in support_hist.items():
        onto=sum((-1)**(k-i)*comb(k,i)*i**r for i in range(k+1))
        counts[t,p]+=3*multiple*onto
    q=3**r-2**(r+1)+1
    expected_counts={(0,1):3,(1,1):3*(3*2**r-2), (2,1):3*(3*2**r-2),
                     (0,3):3*q,(1,3):3*q,(2,3):3*q}
    assert all(counts[t,p]==v for (t,p),v in expected_counts.items()),r
    assert sum(counts.values())==3**(r+2)
    print(f'r={r} classes:'+str(dict(sorted(counts.items()))))
print('SUPPORT_VERIFIED all=21 admissible support/leaf classes; symbolic first-entry counts r=1..15')
