#!/usr/bin/env python3
"""Exact-rational verification of a three-person Shapley-fair merge-stability obstruction."""
from fractions import Fraction
from itertools import permutations
from math import factorial

N = frozenset((1,2,3))
V = {
 frozenset():0, frozenset((1,)):2, frozenset((2,)):2,
 frozenset((3,)):0, frozenset((1,2)):5,
 frozenset((1,3)):0, frozenset((2,3)):0,
 N:6
}

def shapley(S):
    out = {i:Fraction(0) for i in S}
    for order in permutations(sorted(S)):
        before = frozenset()
        for i in order:
            after=before|{i}
            out[i] += Fraction(V[after]-V[before],factorial(len(S)))
            before=after
    assert sum(out.values()) == V[S]
    return out

# The five partitions of {1,2,3}.
parts = [
 (N,),
 (frozenset((1,2)),frozenset((3,))),
 (frozenset((1,3)),frozenset((2,))),
 (frozenset((2,3)),frozenset((1,))),
 (frozenset((1,)),frozenset((2,)),frozenset((3,))),
]
def sfms(part):
    fair=all(x>=0 for S in part for x in shapley(S).values())
    merge_stable=all(V[A|B]<=V[A]+V[B]
                     for k,A in enumerate(part) for B in part[k+1:])
    return fair,merge_stable

for part in parts:
    print(tuple(''.join(map(str,sorted(S))) for S in part),
          'payoffs=',{''.join(map(str,sorted(S))):shapley(S) for S in part},
          'fair,merge_stable=',sfms(part))
    assert sfms(part) != (True,True)

assert shapley(N)=={1:Fraction(19,6),2:Fraction(19,6),3:Fraction(-1,3)}
assert shapley(frozenset((1,2)))=={1:Fraction(5,2),2:Fraction(5,2)}
assert V[N]-V[frozenset((1,2))]-V[frozenset((3,))] == 1

# Stable under one full split-then-exhaustive-merge step, but internally unfair.
def split(part):
    out=[]
    for S in part:
        shp=shapley(S)
        bad={i for i in S if shp[i]<0}
        if not bad:
            out.append(S)
            continue
        good=S-bad
        if good and all(x>=0 for x in shapley(good).values()):
            out.append(good)
            out.extend(frozenset((i,)) for i in sorted(bad))
        else:
            out.extend(frozenset((i,)) for i in sorted(S))
    return tuple(out)

def merge_to_exhaustion(part):
    part=list(part)
    while True:
        pair=next(((i,j) for i,A in enumerate(part) for j,B in enumerate(part)
                   if j>i and V[A|B]>V[A]+V[B]),None)
        if pair is None: break
        i,j=pair
        part=[S for k,S in enumerate(part) if k not in (i,j)]+[part[i]|part[j]]
    return tuple(part)

P=(frozenset((1,2)),frozenset((3,)))
assert split((N,))==P
assert merge_to_exhaustion(P)==(N,)
assert merge_to_exhaustion(split((N,)))==(N,)
assert merge_to_exhaustion(split(P))==(N,)
assert sfms((N,))==(False,True)

# Lyapunov drop in the full update from the fair pair partition.
def W(part):
    neg=sum(max(Fraction(0),-w) for S in part for w in shapley(S).values())
    return -neg,sum(V[S] for S in part)
assert W(P)==(0,5) and W((N,))==(Fraction(-1,3),6)
assert W((N,))<W(P)
print('PASS: exact Shapley values, all five partitions, strict profitable merge, split/merge loop, and Lyapunov violation')
