#!/usr/bin/env python3
"""Exact three-round first-order fingerprints of finite Cartesian products of cliques.
Input is a tuple of alphabet cardinalities. No external packages required.
"""
from itertools import product, combinations_with_replacement
from math import prod
from collections import defaultdict

CASES = ((2,), (3,), (2,2), (2,3), (2,2,2), (3,3), (2,2,3), (2,2,2,2), (3,3,3))

def class_id(q):
    d=len(q)
    b=sum(t==2 for t in q)
    if d==1: return 1 if b else 2
    if d==2: return 3 if b==2 else (4 if b==1 else 6)
    if b==d: return 5 if d==3 else 8
    if b==0: return 9
    return 7

def analytic_pair_fingerprint(q):
    N=prod(q); degree=sum(t-1 for t in q)
    ans=set()
    diagonal={(1,1,0,0),(0,0,1,1)}
    if N>1+degree: diagonal.add((0,0,0,0))
    ans.add((1,0,tuple(sorted(diagonal))))
    def pair(edge,both,one,neither):
        patterns={(1,0,0,edge),(0,1,edge,0)}
        if both:patterns.add((0,0,1,1))
        if one:patterns.update(((0,0,1,0),(0,0,0,1)))
        if neither:patterns.add((0,0,0,0))
        return (0,edge,tuple(sorted(patterns)))
    for t in q:
        common=t-2
        ans.add(pair(1,common>0,degree-1-common>0,N-2*degree+common>0))
    if len(q)>=2:
        ans.add(pair(0,True,degree-2>0,N-2*degree>0))
    if len(q)>=3:
        ans.add(pair(0,False,True,N-2-2*degree>0))
    return tuple(sorted(ans))

def direct_vertex_game(q):
    vertices=list(product(*(range(s) for s in q)))
    x=vertices[0]; ans=set()
    def adj(a,b):
        return sum(i!=j for i,j in zip(a,b))==1
    for y in vertices:
        xy=int(adj(x,y)); code=set()
        for z in vertices:
            code.add((int(z==x),int(z==y),int(adj(x,z)),int(adj(y,z))))
        ans.add((int(x==y),xy,tuple(sorted(code))))
    return tuple(sorted(ans))

def run():
    reps=defaultdict(list)
    enum=0
    for d in range(1,9):
        for q in combinations_with_replacement(range(2,9),d):
            enum+=1
            cid=class_id(q)
            reps[cid].append(q)
            assert analytic_pair_fingerprint(q)==analytic_pair_fingerprint(CASES[cid-1]), ('ANALYTIC',q,cid)
    print('SYMBOLIC_ALL_PARAMETERS_REDUCED_OK', 'instances='+str(enum),'dimensions=1..8','alphabets=2..8')
    assert len(set(map(analytic_pair_fingerprint,CASES)))==9
    print('NINE_SEPARATE_RANK_THREE_FINGERPRINTS_OK')
    assert [prod(q) for q in CASES]==[2,3,4,6,8,9,12,16,27]
    assert all(not any(prod(q)<prod(CASES[i-1]) for q in reps[i]) for i in range(1,10))
    print('NINE_SHARP_MINIMAL_REPRESENTATIVES_OK', 'sizes=2,3,4,6,8,9,12,16,27')
    full=0
    for d in range(1,6):
        for q in combinations_with_replacement(range(2,7),d):
            if prod(q)>150:continue
            assert direct_vertex_game(q)==analytic_pair_fingerprint(q), ('DIRECT',q)
            full+=1
    print('INDEPENDENT_DIRECT_TRIPLE_ATOMIC_TYPES_OK', 'instances='+str(full),'max_graph_size=150')
    for i,q in enumerate(CASES,1):
        direct=direct_vertex_game(q)
        assert direct==analytic_pair_fingerprint(q)
        print('REPRESENTATIVE_OK', 'class='+str(i),'factors='+str(q),'vertices='+str(prod(q)),'pairtypes='+str(len(direct)))
    print('VERIFY_OK')
if __name__=='__main__':run()
