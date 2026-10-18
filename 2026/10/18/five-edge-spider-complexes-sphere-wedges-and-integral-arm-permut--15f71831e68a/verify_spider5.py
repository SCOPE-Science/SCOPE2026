#!/usr/bin/env python3
"""Finite reproducibility checks for the 3-path-free complexes of five-edge spiders.
Only finite tests; the unbounded theorem follows from the written homotopy proof.
Python 3, standard library only.
"""
from collections import defaultdict
from itertools import combinations, permutations


def ind2_faces(n, edges):
    adj=[set() for _ in range(n)]
    for a,b in edges:
        adj[a].add(b);adj[b].add(a)
    bad=set()
    for v in range(n):
        for a,b in combinations(sorted(adj[v]),2):
            bad.add((1<<a)|(1<<b)|(1<<v))
    return {mask for mask in range(1<<n) if all(mask&trip!=trip for trip in bad)}


def path_faces(n):
    return ind2_faces(n,[(i,i+1) for i in range(n-1)])


def collapse_to(F, target):
    F=set(F); target=set(target); steps=[]
    while F != target:
        options=[]
        for face in F-target:
            if not face: continue
            uppers=[g for g in F if g.bit_count()==face.bit_count()+1 and (g&face)==face]
            if len(uppers)!=1: continue
            coface=uppers[0]
            if not any(g!=coface and g&coface==coface for g in F):
                options.append((face,coface))
        if not options:
            raise AssertionError('no elementary free-face collapse to target')
        a,b=min(options,key=lambda t:(-t[0].bit_count(),t))
        F.remove(a);F.remove(b);steps.append((a,b))
    return steps


def spider(k):
    n=1+5*k
    edges=[]
    for arm in range(k):
        a=1+5*arm
        edges.extend([(0,a)]+[(a+j,a+j+1) for j in range(4)])
    return n, edges


def bit_ranks(F):
    by_dim=defaultdict(list)
    for f in F-{0}: by_dim[f.bit_count()-1].append(f)
    rank={}
    for d in range(1,max(by_dim)+1):
        idx={f:i for i,f in enumerate(by_dim[d-1])}
        piv={};r=0
        for face in by_dim[d]:
            bits=face;v=0
            while bits:
                b=bits&-bits;bits-=b
                v^=1<<idx[face^b]
            while v:
                b=v&-v
                if b in piv:v^=piv[b]
                else:piv[b]=v;r+=1;break
        rank[d]=r
    betti={d:len(fs)-rank.get(d,0)-rank.get(d+1,0) for d,fs in by_dim.items()}
    betti[0]-=1
    return {d:x for d,x in betti.items() if x}


def fixed_lefschetz(F,k,p):
    # p[i] is image of arm i; the center is fixed, positions within arms fixed.
    perm=[0]*(5*k+1)
    for i in range(k):
        for j in range(5):perm[1+5*i+j]=1+5*p[i]+j
    total=0
    for f in F:
        if f==0: continue
        vertices=[i for i in range(len(perm)) if f>>i&1]
        moved=[perm[i] for i in vertices]
        if sorted(moved)!=vertices:continue
        inversions=sum(moved[a]>moved[b] for a in range(len(vertices)) for b in range(a+1,len(vertices)))
        total+=(-1)**(len(vertices)-1+inversions)
    return total


if __name__=='__main__':
    C4=path_faces(4)
    C3={f for f in C4 if not f&1}
    assert len(C3)==7
    assert len(collapse_to(C4,C3))==3
    C5=path_faces(5)
    assert len(C5)==24
    assert len(collapse_to(C5,{0,1<<4}))==11
    print('P4 -> P3: 3 elementary collapses; P5 -> point: 11 elementary collapses')

    for k in (2,3):
        n,edges=spider(k)
        F=ind2_faces(n,edges)
        b=bit_ranks(F)
        assert b=={2*k+1:k-1},(k,b)
        print('spider',k,'vertices',n,'nonempty faces',len(F)-1,'mod-2 reduced Betti',b)
        for p in permutations(range(k)):
            # Expected standard representation trace = fixed arms minus one.
            tr=sum(i==p[i] for i in range(k))-1
            expected=1+(-1)**(2*k+1)*tr
            computed=fixed_lefschetz(F,k,p)
            assert computed==expected,(k,p,expected,computed)
        print('spider',k,'signed simplex Lefschetz traces: all',len(list(permutations(range(k)))),'arm permutations agree with augmentation character')
    print('SUCCESS: finite checks complete; no infinite-range computation claimed')
