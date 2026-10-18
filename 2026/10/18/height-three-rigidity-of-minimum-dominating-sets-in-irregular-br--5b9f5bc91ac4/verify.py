#!/usr/bin/env python3
"""Independent finite checks of a structural minimum-domination theorem.

Run: python3 verify.py
All tests use ordinary integer arithmetic and the Python standard library.
"""
from __future__ import annotations
from itertools import combinations, product
from random import Random

INF = 10**100


def make_tree(height, rng, max_children=4):
    """Return parent array for an irregular tree; each internal degree >=2."""
    parent = [-1]
    layers = [[0]]
    for _ in range(height):
        new = []
        for v in layers[-1]:
            for __ in range(rng.randint(2, max_children)):
                parent.append(v)
                new.append(len(parent) - 1)
        layers.append(new)
    return parent, layers


def expected_sets(layers):
    h = len(layers) - 1
    forced = set()
    for j in range(h - 1, -1, -3):
        if j >= 2:
            forced.update(layers[j])
    if h % 3 == 0:
        if h == 0:
            return {frozenset([0])}
        return {frozenset(forced | {x}) for x in layers[0] + layers[1]}
    elif h % 3 == 1:
        return {frozenset(forced | set(layers[0]))} if h > 1 else {frozenset([0])}
    else:
        # for h = 2 mod 3 the last required level is 1
        forced.update(layers[1])
        return {frozenset(forced)}


def formula(layers):
    h=len(layers)-1
    if h==0: return 1,1
    if h%3==0: return 1 + sum(len(layers[j]) for j in range(2,h,3)),1+len(layers[1])
    if h%3==1: return sum(len(layers[j]) for j in range(0,h,3)),1
    return sum(len(layers[j]) for j in range(1,h,3)),1


def brute(parent):
    n=len(parent)
    closed=[1<<i for i in range(n)]
    for v,p in enumerate(parent):
        if p>=0:
            closed[v]|=1<<p
            closed[p]|=1<<v
    allbits=(1<<n)-1
    for size in range(n+1):
        winners=[]
        for chosen in combinations(range(n),size):
            seen=0
            for v in chosen:seen|=closed[v]
            if seen==allbits:winners.append(frozenset(chosen))
        if winners:return size,set(winners)
    raise AssertionError('No dominating set')


def dp(parent):
    """Independent root-status DP: exact min costs and multiplicities."""
    children=[[] for _ in parent]
    for i,p in enumerate(parent):
        if p>=0: children[p].append(i)
    A=[(0,0)]*len(parent)
    B=[(0,0)]*len(parent)
    C=[(0,0)]*len(parent)
    for v in reversed(range(len(parent))):
        kids=children[v]
        if not kids:
            A[v]=(1,1)
            B[v]=(INF,0)
            C[v]=(0,1)
            continue
        score=1;count=1
        for u in kids:
            k=min(A[u][0],B[u][0],C[u][0])
            score+=k
            count*=sum(t[1] for t in (A[u],B[u],C[u]) if t[0]==k)
        A[v]=(score,count)
        # all child roots in A or B; at least one in A
        states=[(0,1,False)]
        for u in kids:
            new=[]
            for cost,cnt,hit in states:
                for typ,(w,num) in [(False,B[u]),(True,A[u])]:
                    if num:
                        new.append((cost+w,cnt*num,hit or typ))
            states=new
        mincost=min(cost for cost,cnt,hit in states if hit)
        B[v]=(mincost,sum(cnt for cost,cnt,hit in states if hit and cost==mincost))
        if any(B[u][1]==0 for u in kids):
            C[v]=(INF,0)
        else:
            cnt=1
            for u in kids:cnt*=B[u][1]
            C[v]=(sum(B[u][0] for u in kids),cnt)
    best=min(A[0][0],B[0][0])
    ways=(A[0][1] if A[0][0]==best else 0)+(B[0][1] if B[0][0]==best else 0)
    return best,ways


def verify():
    rng=Random(20261015)
    brute_cases=0
    for h in range(4):
        for _ in range(100):
            parent,layers=make_tree(h,rng,max_children=3)
            if len(parent)>18:continue
            want=formula(layers)
            actual,winning=brute(parent)
            assert (actual,len(winning))==want, (h,parent,want,actual,len(winning))
            assert winning==expected_sets(layers),(h,parent,winning,expected_sets(layers))
            assert dp(parent)==want
            brute_cases+=1
    # Include exhaustive branching-profile check through height 5
    # for spherically symmetric but nonconstant degrees.
    spherical_cases=0
    for h in range(1,6):
        for bs in product((2,3,4),repeat=h):
            parent=[-1];layers=[[0]]
            for d in bs:
                new=[]
                for p in layers[-1]:
                    for _ in range(d):
                        parent.append(p)
                        new.append(len(parent)-1)
                layers.append(new)
            assert dp(parent)==formula(layers),(h,bs,dp(parent),formula(layers))
            spherical_cases+=1
    # Irregular, nonconstant degrees including high-height trees.
    random_cases=0
    for h in range(2,7):
        for _ in range(85):
            parent,layers=make_tree(h,rng,max_children=3)
            assert dp(parent)==formula(layers),(h,dp(parent),formula(layers))
            random_cases+=1
    print('VERIFIED')
    print('brute_full_minimizer_classifications',brute_cases)
    print('all_spherical_branching_profiles',spherical_cases)
    print('irregular_branching_DP_instances',random_cases)
    print('total_instances',brute_cases+spherical_cases+random_cases)

if __name__=='__main__':verify()
