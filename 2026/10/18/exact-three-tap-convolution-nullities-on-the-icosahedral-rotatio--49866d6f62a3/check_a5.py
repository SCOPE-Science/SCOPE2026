#!/usr/bin/env python3
"""Exact-arithmetic exhaustive verification of the A5 three-tap nullity theorem.

Requires only Python 3 standard library. There is no randomized or floating-point step.
Running this file constructs and checks all 1,711 identity-normalized three-element
supports, equivalent to all 34,220 supports by left translation.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, combinations

N = 5
identity = tuple(range(N))

def compose(a, b):
    return tuple(a[b[i]] for i in range(N))

def parity(p):
    return sum(p[i] > p[j] for i in range(N) for j in range(i+1,N)) % 2

G = tuple(p for p in permutations(range(N)) if parity(p) == 0)
assert len(G) == 60 and G[0] == identity
index = {p:i for i,p in enumerate(G)}
mult = [[index[compose(a,b)] for b in G] for a in G]
inv = [index[tuple(p.index(j) for j in range(N))] for p in G]

def order(g):
    z = 0
    for k in range(1,61):
        z = mult[z][g]
        if z == 0: return k
    raise ArithmeticError('order failure')
orders = list(map(order, range(60)))
assert Counter(orders) == {1:1,2:15,3:20,5:24}

# An A5 conjugacy class of twelve five-cycles; the other twelve form its complement.
five = next(g for g in range(60) if orders[g] == 5)
class_a = {mult[mult[c][five]][inv[c]] for c in range(60)}
assert len(class_a) == 12
assert all(inv[g] in class_a for g in class_a)  # Orientation of quotients does not change the five-cycle class.
assert sum(orders[g] == 5 and g not in class_a for g in range(60)) == 12

def subgroup_order(a,b):
    generated={0}
    frontier=[0]
    while frontier:
        g=frontier.pop()
        for h in (a,b):
            t=mult[g][h]
            if t not in generated:
                generated.add(t)
                frontier.append(t)
    return len(generated)

def invariant(a,b):
    diff=mult[inv[a]][b]
    signature=tuple(sorted((orders[a],orders[b],orders[diff])))
    h=subgroup_order(a,b)
    both_same=None
    if signature == (3,5,5):
        fives=[z for z in (a,b,diff) if orders[z]==5]
        assert len(fives)==2
        both_same = (fives[0] in class_a)==(fives[1] in class_a)
    return signature,h,both_same

EXPECTED = {
    ((2,2,2),4,None):(0,15),
    ((2,2,3),6,None):(20,90),
    ((2,2,5),10,None):(0,180),
    ((2,3,3),12,None):(0,180),
    ((2,3,5),60,None):(0,360),
    ((2,5,5),60,None):(5,180),
    ((3,3,3),3,None):(40,10),
    ((3,3,3),12,None):(10,60),
    ((3,3,5),60,None):(0,180),
    ((3,5,5),60,False):(4,180),
    ((3,5,5),60,True):(10,180),
    ((5,5,5),5,None):(0,36),
    ((5,5,5),60,None):(4,60),
}

def rank_over_Q(support):
    # Column j is sum_{s in support} e_{sj}. Every elimination is over Q.
    A=[[0]*60 for _ in range(60)]
    for j in range(60):
        for g in support:
            A[mult[g][j]][j] += 1
    rank=0
    for col in range(60):
        pivot=next((r for r in range(rank,60) if A[r][col]),None)
        if pivot is None:
            continue
        A[rank],A[pivot] = A[pivot],A[rank]
        d=A[rank][col]
        if d!=1:
            A[rank][col:]=[Fraction(x,d) for x in A[rank][col:]]
        for r in range(rank+1,60):
            q=A[r][col]
            if q:
                A[r][col:]=[x-q*y for x,y in zip(A[r][col:],A[rank][col:])]
        rank+=1
        if rank==60:break
    return rank

def verify():
    census=Counter()
    examples={}
    for a,b in combinations(range(1,60),2):
        key=invariant(a,b)
        # Verify that choice of the anchored vertex does not alter the intrinsic type.
        assert key == invariant(inv[a], mult[inv[a]][b])
        assert key == invariant(inv[b], mult[inv[b]][a])
        assert key in EXPECTED, ('unclassified',a,b,key)
        nullity=60-rank_over_Q((0,a,b))
        assert nullity==EXPECTED[key][0], (a,b,key,nullity)
        census[key]+=1
        examples.setdefault(key,(a,b))
    assert len(census)==13
    assert all(census[k]==n for k,(_,n) in EXPECTED.items())
    distribution=Counter()
    for key,count in census.items():
        distribution[EXPECTED[key][0]]+=20*count
    assert distribution=={0:19020,4:4800,5:3600,10:4800,20:1800,40:200}
    assert sum(distribution.values())==34220
    assert sum(v for k,v in distribution.items() if k) == 15200

if __name__ == '__main__':
    verify()
    print('PASS: all 1,711 normalized supports checked over Q; 13 types; 34,220 total.')
