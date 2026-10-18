#!/usr/bin/env python3
"""Weighted reflection-orbit quotient, independently iterating 1-WL.
Checks the claimed interior wavefront and four penultimate boundary patterns.
Finite sample tests support but do not constitute the parametric induction.
"""
from collections import defaultdict

def fold(n,i):
    j=i%n
    return min(j,n-j)

def refine_quotient(n):
    h=n//2
    types=[('U',j) for j in range(h+1)]+[('V',j) for j in range(h+1)]
    idx={x:k for k,x in enumerate(types)}
    neighbor=[]
    for kind,j in types:
        if kind=='U':adj=[('U',fold(n,j-1)),('U',fold(n,j+1)),('V',j)]
        else:adj=[('V',fold(n,j-2)),('V',fold(n,j+2)),('U',j)]
        neighbor.append([idx[x] for x in adj])
    C=[int(x==('U',0)) for x in types]
    states=[C]
    while True:
        labels=[(C[t],tuple(sorted(C[y] for y in neighbor[t]))) for t in range(len(types))]
        lut={x:i for i,x in enumerate(sorted(set(labels)))}
        new=[lut[x] for x in labels]
        if len(set(new))==len(set(C)):return types,states
        states.append(new);C=new

def equality_classes(labels,typ):
    res=defaultdict(set)
    for c,v in zip(labels,typ):res[c].add(v)
    return frozenset(frozenset(v) for v in res.values())

def predicted_interior(n,r,types):
    a=2*r-4
    out=[]
    for k,j in types:
        if k=='U' and j<=a-1:label=(k,j)
        elif k=='V' and j<=a:label=(k,j)
        elif k=='U' and j==a or k=='V' and j in (a+1,a+2):label=('C',)
        else:label=('T',)
        out.append(label)
    return equality_classes(out,types)

def penultimate(n):
    h=n//2
    if n%4==0:
        return [frozenset((('U',h-3),('V',h))),
                frozenset((('U',h-2),('V',h-1))),
                frozenset((('U',h-1),('U',h)))]
    if n%4==1:
        return [frozenset((('U',h-2),('V',h-1),('V',h))),
                frozenset((('U',h-1),('U',h)))]
    return [frozenset((('U',h-2),('V',h)))]

checks=0;cycles=0
for n in range(14,501):
    types,states=refine_quotient(n)
    R=(n+10)//4
    assert len(states)-1==R,(n,len(states)-1,R)
    assert len(set(states[R]))==len(types)
    if n>=26:
        for r in range(6,R-1):
            assert equality_classes(states[r],types)==predicted_interior(n,r,types),(n,r)
            checks+=1
        d=defaultdict(set)
        for t,c in zip(types,states[R-1]):d[c].add(t)
        observed=frozenset(frozenset(v) for v in d.values() if len(v)>1)
        assert observed==frozenset(penultimate(n)),(n,observed)
    cycles+=1
print('PASS reflection-orbit weighted quotient: n=14..500,',cycles,'instances;',checks,'interior-wavefront partitions and all penultimate seam patterns')
