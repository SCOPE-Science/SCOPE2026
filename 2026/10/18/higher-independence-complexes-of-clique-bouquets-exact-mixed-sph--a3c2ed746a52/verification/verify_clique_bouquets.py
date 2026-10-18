#!/usr/bin/env python3
"""Finite independent cross-checks of higher-independence clique bouquet theorem.

Unconditional enumeration of the induced-component definition, independent
enumeration from proposed decomposition, and exact F_2 boundary elimination.
This is finite corroboration only; the general theorem is proved separately.
"""
from collections import Counter, defaultdict
from itertools import combinations
from math import comb


def rank_gf2(columns):
    pivots={}
    for column in columns:
        x=column
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x
                break
            x^=pivots[p]
    return len(pivots)


def check(r, sizes):
    n=len(sizes)
    N=sum(sizes)
    assert n>=2 and r>=2
    blocks=[]
    current=1
    for m in sizes:
        blocks.append(tuple(range(current,current+m)))
        current+=m
    edges={frozenset((0,x)) for x in range(1,N+1)}
    for block in blocks:
        edges.update(frozenset((x,y)) for x,y in combinations(block,2))
    adjacency=[0]*(N+1)
    for pair in edges:
        a,b=tuple(pair)
        adjacency[a]|=1<<b
        adjacency[b]|=1<<a
    all_faces=[]
    independently_constructed=[]
    for S in range(1<<(N+1)):
        left=S
        valid=True
        while left:
            initial=left&-left
            component=initial
            fringe=initial
            while fringe:
                bit=fringe&-fringe
                fringe^=bit
                vertex=bit.bit_length()-1
                new=(adjacency[vertex]&S)&~component
                component|=new
                fringe|=new
            if component.bit_count()>r:
                valid=False
                break
            left&=~component
        if valid:
            all_faces.append(S)
        if S&1:
            structural=(S.bit_count()-1<=r-1)
        else:
            structural=all((S&sum(1<<v for v in B)).bit_count()<=r for B in blocks)
        if structural:
            independently_constructed.append(S)
    assert all_faces==independently_constructed
    bysize=defaultdict(list)
    for S in all_faces:
        if S: bysize[S.bit_count()].append(S)
    ranks={}
    boundary=[]
    for k in range(1,max(bysize)+1):
        down= bysize.get(k-1,[])
        up= bysize.get(k,[])
        row={s:i for i,s in enumerate(down)}
        cols=[]
        if k==1:
            # reduced complex: C0 -> Z via augmentation
            cols=[1 for s in up]
        else:
            for s in up:
                x=0
                for bit in (1<<v for v in range(N+1) if s&(1<<v)):
                    x^=1<<row[s^bit]
                cols.append(x)
        boundary.append(rank_gf2(cols))
    reduced_betti={}
    for k in range(1,max(bysize)+1):
        d=k-1
        b=len(bysize[k])-boundary[k-1]-(boundary[k] if k<len(boundary) else 0)
        if b:reduced_betti[d]=b
    expected={}
    low=comb(N-1,r-1) if N-1>=r-1 else 0
    high=1
    for m in sizes:
        high*=comb(m-1,r) if m-1>=r else 0
    if low: expected[r-1]=low
    if high: expected[n*r-1]=high
    assert reduced_betti==expected, (r,sizes,reduced_betti,expected)
    print(f'r={r} sizes={sizes} vertices={N+1} faces={len(all_faces)-1} F2_reduced_betti={dict(sorted(reduced_betti.items()))} PASS')


if __name__=='__main__':
    for r,s in [(2,[2,2]),(2,[3,3]),(2,[3,4]),(2,[1,4]),
                (2,[3,3,3]),(3,[4,4]),(3,[3,4]),(3,[2,2]),
                (4,[5,5]),(5,[1,2])]:
        check(r,s)
    print('ALL TEN FINITE CHECKS PASSED')
