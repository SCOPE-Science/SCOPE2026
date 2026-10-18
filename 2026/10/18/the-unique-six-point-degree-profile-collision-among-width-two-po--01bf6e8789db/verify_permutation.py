#!/usr/bin/env python3
"""Independent finite-width-two poset census via 321-avoiding permutations.
For a permutation p, the relation i<j and p[i]<p[j] is a width<=2 poset
exactly when p has no decreasing subsequence of length 3. Every width<=2
poset has such a representation (two linear extensions).
"""
from collections import defaultdict
from itertools import permutations


def relation(p):
    n=len(p)
    return frozenset((i,j) for i in range(n) for j in range(i+1,n) if p[i]<p[j])

def profile(E,n):
    return [(sum((j,i) in E for j in range(n)),sum((i,j) in E for j in range(n))) for i in range(n)]

def iso(E,F,n):
    a=profile(E,n);b=profile(F,n)
    choices=[[j for j in range(n) if b[j]==a[i]] for i in range(n)]
    order=sorted(range(n),key=lambda i:(len(choices[i]),a[i]))
    f={};used=set()
    def extend(t):
        if t==n:return True
        i=order[t]
        for j in choices[i]:
            if j in used:continue
            if any(((i,k) in E)!=((j,f[k]) in F) or ((k,i) in E)!=((f[k],j) in F) for k in f):continue
            f[i]=j;used.add(j)
            if extend(t+1):return True
            used.remove(j);del f[i]
        return False
    return extend(0)

for n in range(1,7):
    buckets=defaultdict(list);avoid=0
    for p in permutations(range(n)):
        if any(p[i]>p[j]>p[k] for i in range(n) for j in range(i+1,n) for k in range(j+1,n)):continue
        avoid+=1
        E=relation(p);k=tuple(sorted(profile(E,n)))
        if not any(iso(E,F,n) for F in buckets[k]):buckets[k].append(E)
    total=sum(len(v) for v in buckets.values())
    collision=sorted(len(v) for v in buckets.values() if len(v)>1)
    print(f'n={n} 321_avoiders={avoid} classes={total} profiles={len(buckets)} collision_multiplicities={collision}')
    assert total==[1,2,4,10,26,75][n-1]
    assert collision==([2] if n==6 else [])
print('PASS: independent permutation enumeration agrees')
