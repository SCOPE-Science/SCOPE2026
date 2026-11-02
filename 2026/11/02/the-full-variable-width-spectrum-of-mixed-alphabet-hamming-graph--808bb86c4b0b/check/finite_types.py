#!/usr/bin/env python3
"""Independent count-free finite-variable type refinement for small Hamming graphs.
Scientific reproduction script; usage: python finite_types.py.
"""
from itertools import product, combinations
from collections import Counter


def graph(alph):
    v = list(product(*(range(q) for q in alph)))
    edge = [[sum(a != b for a,b in zip(u,w)) == 1 for w in v] for u in v]
    return v, edge


def compare(a,b,k,limit=20):
    graphs = [graph(a),graph(b)]
    atom = []
    specs = []
    for v, E in graphs:
        n=len(v); tuples=list(product(range(n), repeat=k))
        specs.append((n, tuples, E))
        for x in tuples:
            atom.append(tuple((0 if x[i]==x[j] else 1 if E[x[i]][x[j]] else 2) for i in range(k) for j in range(i+1,k)))
    ids={x:i for i,x in enumerate(sorted(set(atom)))}
    colors=[ids[x] for x in atom]
    cuts=[0, len(specs[0][1]),len(atom)]
    rounds=0
    while rounds<limit:
        sigs=[]
        for gi,(n, tuples,E) in enumerate(specs):
            start=cuts[gi]
            powers=[n**(k-1-i) for i in range(k)]
            for t,tup in enumerate(tuples):
                old=colors[start+t]
                bands=[]
                for i in range(k):
                    ii=tup[i]; p=powers[i]
                    inds=(t+(val-ii)*p for val in range(n))
                    bands.append(tuple(sorted({colors[start+z] for z in inds})))
                sigs.append((old,tuple(bands)))
        newIDs={}
        new=[]
        for s in sigs:
            if s not in newIDs: newIDs[s]=len(newIDs)
            new.append(newIDs[s])
        rounds+=1
        if len(newIDs)==len(set(colors)):
            colors=new
            break
        colors=new
    support1=set(colors[:cuts[1]]);support2=set(colors[cuts[1]:]);
    assert rounds<limit, (a,b,k,'no stabilization')
    return (support1==support2, rounds, len(support1),len(support2),len(set(colors)))

cases=[
 ((2,4),(2,5),4,True),
 ((2,3),(2,4),4,False),
 ((3,3),(3,4),4,False),
 ((4,),(5,),4,True),
 ((4,),(5,),5,False),
 ((2,2),(2,3),3,False),
 ((2,3),(2,4),3,True),
 ((2,3),(3,3),3,False),
 ((3,),(4,),3,True),
 ((3,),(4,),4,False),
]
for a,b,k,expect in cases:
    result=compare(a,b,k)
    assert result[0]==expect,(a,b,k,expect,result)
    print(f'PASS k={k} G={a} H={b} equivalent={result[0]} refinement_rounds={result[1]} support_sizes={result[2:4]}')
print(f'PASS all {len(cases)} independent logical-refinement comparisons')
