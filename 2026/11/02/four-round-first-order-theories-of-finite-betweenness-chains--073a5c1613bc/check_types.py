#!/usr/bin/env python3
"""Exhaustive, collision-free rank-four Hintikka types for finite strict betweenness.

The tuple type at zero remaining moves is its complete atomic diagram.
The one-move extension is the set of types of all one-element extensions.
All quantified choices, including repetitions, are enumerated.
"""
from itertools import product
from pathlib import Path

RANK = 4
interners = [{} for _ in range(RANK + 1)]

def atomic(t):
    equalities = tuple(t[i] == t[j] for i in range(len(t)) for j in range(i+1,len(t)))
    between = tuple((t[i] < t[j] < t[k] or t[k] < t[j] < t[i])
                    for i in range(len(t)) for j in range(len(t))
                    for k in range(len(t)) if len({i,j,k}) == 3)
    return (equalities,between)

def intern(depth, signature):
    d=interners[depth]
    if signature not in d: d[signature]=len(d)
    return d[signature]

def analyse(n):
    next_level={t: intern(RANK,atomic(t)) for t in product(range(n),repeat=RANK)}
    onepoint=None
    for j in range(RANK-1,-1,-1):
        curr={}
        for t in product(range(n),repeat=j):
            children=frozenset(next_level[t+(x,)] for x in range(n))
            curr[t]=intern(j,(atomic(t),children))
        if j==1: onepoint=[curr[(x,)] for x in range(n)]
        next_level=curr
    return next_level[()],onepoint

if __name__=='__main__':
    classes={}
    for n in range(1,18):
        t, onepoint=analyse(n)
        if t not in classes: classes[t]=len(classes)+1
        print('order=%d class=%d'%(n,classes[t]))
        if n in (13,14,15):
            print('onepoint_positions='+','.join(str(x) for x in onepoint))
    print('CLASS_COUNT=',len(classes))
