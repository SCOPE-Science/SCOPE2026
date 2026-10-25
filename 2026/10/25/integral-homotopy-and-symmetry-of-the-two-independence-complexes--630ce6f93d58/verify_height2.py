#!/usr/bin/env python3
"""Exact finite mod-2 checks of the depth-two tree 2-independence theorem."""
from itertools import product
from collections import defaultdict
from math import prod

def graph(branch_sizes):
    k=len(branch_sizes)
    edges=[(0,i+1) for i in range(k)]
    v=k+1
    for i,b in enumerate(branch_sizes):
        for j in range(b):
            edges.append((i+1,v));v+=1
    return v,edges

def faces_by_size(branch_sizes):
    n,edges=graph(branch_sizes)
    adjacency=[0]*n
    for u,v in edges:
        adjacency[u]|=1<<v;adjacency[v]|=1<<u
    faces=defaultdict(list)
    for mask in range(1<<n):
        rest=mask;ok=True
        while rest:
            seed=rest & -rest; wave=seed;comp=0
            while wave:
                bit=wave & -wave;wave-=bit
                comp|=bit
                if comp.bit_count()>2: ok=False;break
                v=bit.bit_length()-1
                wave|=(adjacency[v] & mask & ~comp & ~wave)
            if not ok:break
            rest &=~comp
        if ok:faces[mask.bit_count()].append(mask)
    return faces

def rank_mod2(columns):
    basis={}
    for col in columns:
        while col:
            bit=col.bit_length()-1
            if bit in basis:col^=basis[bit]
            else:basis[bit]=col;break
    return len(basis)

def bettis_mod2(faces):
    nmax=max(faces)
    ranks={0:1 if faces[1] else 0}
    for size in range(2,nmax+1):
        low={face:i for i,face in enumerate(faces[size-1])}
        columns=[]
        for face in faces[size]:
            col=0;v=face
            while v:
                bit=v & -v;v^=bit
                col^=1<<low[face^bit]
            columns.append(col)
        ranks[size-1]=rank_mod2(columns)
    ranks[nmax]=0
    return {d:len(faces[d+1])-ranks[d]-ranks[d+1] for d in range(nmax) if len(faces[d+1])-ranks[d]-ranks[d+1]}

def expected(bs):
    k=len(bs);p=sum(bool(b) for b in bs)
    if k==1:return {1:bs[0]} if bs[0] else {}
    if p==0:return {1:k-1}
    if p==1:return {1:1}
    if any(b==0 or b==1 for b in bs):return {}
    mult=prod(b-1 for b in bs)
    return {2*k-1:mult} if mult else {}

def check(bs):
    f=faces_by_size(bs)
    got=bettis_mod2(f);want=expected(bs)
    assert got==want, (bs,got,want)
    return sum(map(len,f.values()))

def permutation_trace(bs,perm):
    f=faces_by_size(bs)
    n=sum(bs)+len(bs)+1
    assert len(perm)==n
    L=-1
    for size,fs in f.items():
        if size==0:continue
        for face in fs:
            transformed=0;pts=[]
            for j in range(n):
                if face>>j&1:transformed|=1<<perm[j];pts.append(perm[j])
            if transformed!=face:continue
            swaps=sum(pts[i]>pts[j] for i in range(len(pts)) for j in range(i+1,len(pts)))
            L+=(-1)**(size-1+swaps)
    dim=max(expected(bs)) if expected(bs) else None
    return (-1)**dim*L if dim is not None else 0

def symmetry_checks():
    checks=0
    def test(bs, perm, trace):
        nonlocal checks
        got=permutation_trace(bs,perm)
        assert got==trace, (bs, perm, got, trace)
        checks+=1
    # k=2, b=(2,2): signed leaf augmentation on each arm, even join factor swaps.
    test((2,2), [0,1,2,4,3,5,6], -1)
    test((2,2), [0,2,1,5,6,3,4], +1)
    test((2,2), [0,1,2,4,3,6,5], +1)
    # k=2, b=(3,3): the augmentation lattice has rank two on each branch.
    test((3,3),list(range(9)),4)
    test((3,3), [0,1,2,4,3,5,6,7,8],0)
    test((3,3), [0,1,2,4,5,3,6,7,8],-2)
    test((3,3), [0,2,1,6,7,8,3,4,5],2)
    # A bare star on three leaves: S_3 acts by its augmentation character.
    test((0,0,0), [0,2,1,3],0)
    test((0,0,0), [0,2,3,1],-1)
    # Exactly one positive branch has a canonical S^1 with trivial rooted-action.
    test((0,0,2),[0,2,1,3,4,5],1)
    test((0,0,2),[0,1,2,3,5,4],1)
    return checks

def main():
    cases=[]
    for k in range(1,5):
        for bs in product(range(3),repeat=k):
            if sum(bs)+k+1<=12:cases.append(bs)
    counts=[check(bs) for bs in cases]
    print('PASS: %d exact face-enumeration/mod-2 homology cases; total faces %d'%(len(cases),sum(counts)))
    for bs in [(2,2,2),(2,2,2,2),(3,3),(2,3,2),(0,0,2),(0,2,2),(0,0,0)]:
        print('case',bs,'faces',check(bs),'expected',expected(bs))
    print('PASS: %d symmetry Lefschetz-trace checks'%(symmetry_checks()))
if __name__=='__main__':main()
