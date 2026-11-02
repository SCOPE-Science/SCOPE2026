#!/usr/bin/env python3
"""Rebuild the four-erasure local normalizer spaces from independent Pauli tests."""
from collections import Counter
from itertools import combinations,product
from math import comb
P=[
'YZIIZZIZIXZXZXZYZXXX',
'IYZIIIIZIZYIZYYZZZZI',
'ZIXZZZZZIXXIZYYIZIXI',
'ZIIYZIIIIZIZYIZYYZZZ',
'ZZZIYIZIZYZIYXIIXXYX',
'ZZZIIYZIIIIZIZYIZYYZ',
'IIIZIZYIZYYZZZZIIYZI',
'IIZZIZIXZXZXZYZXXXYZ',
'ZIIIIZIZYIZYYZZZZIIY']
n=20; r=9
assert all(len(p)==20 for p in P)
X=[sum((p[j] in 'XY')<<j for j in range(n)) for p in P]
Z=[sum((p[j] in 'YZ')<<j for j in range(n)) for p in P]
assert all(((X[i]&Z[j]).bit_count()+(Z[i]&X[j]).bit_count())%2==0 for i in range(r) for j in range(r))
S=[]
for coeff in range(1<<r):
    a=b=0
    for i in range(r):
        if coeff & (1<<i):
            a^=X[i];b^=Z[i]
    S.append((a,b))
assert len(set(S))==512
weights=Counter((a|b).bit_count() for a,b in S)
assert weights==Counter({0:1,12:50,14:220,16:195,18:20,20:26})
# Independent method: enumerate the 4^4 local Pauli operators, not just matrix ranks.
hist=Counter()
pair_comm=Counter()
weight4=0
support_to_count={}
special=[]
for E in combinations(range(n),4):
    local=[]
    for terms in product(range(4), repeat=4):
        if terms==(0,0,0,0):continue
        x=z=0
        for j,t in zip(E,terms):
            if t in (1,3):x|=1<<j
            if t in (2,3):z|=1<<j
        if all(((x&Z[i]).bit_count()+(z&X[i]).bit_count())%2==0 for i in range(r)):
            local.append((x,z))
    d=(len(local)+1).bit_length()-1
    assert 2**d-1==len(local)
    hist[d]+=1
    # d=2: three nonzero vectors; all pairs have the same symplectic commutator.
    if d==2:
        special.append(E)
        a,b=local[:2]
        k=((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
        pair_comm[k]+=1
    for x,z in local:
        if (x|z).bit_count()==4:weight4+=1
print('SPECIAL_FOUR_SETS',special)
print('FOUR_SUPPORT_DIMENSIONS',dict(sorted(hist.items())))
print('DOUBLE_LOGICAL_COMMUTATOR',dict(sorted(pair_comm.items())))
print('WEIGHT_FOUR_LOGICAL_OPERATORS',weight4)
assert hist==Counter({0:3840,1:970,2:35})
assert weight4==1075
print('LOCAL_ENUMERATION_OK')
