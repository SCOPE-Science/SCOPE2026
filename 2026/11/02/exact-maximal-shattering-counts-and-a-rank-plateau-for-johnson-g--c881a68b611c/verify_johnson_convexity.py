#!/usr/bin/env python3
"""Finite independent checks for convex vertex-set shattering in Johnson graphs.
No third-party packages needed. All results are derived from generated vertices.
"""
from itertools import combinations
from math import comb, factorial
import random

def vertices(n,k):
    return [sum(1<<i for i in xs) for xs in combinations(range(n),k)]

def johnson_distance(a,b):
    return (a ^ b).bit_count()//2

def convex_by_geodesics(idx,n,V):
    for a in idx:
        for b in idx:
            d = johnson_distance(V[a],V[b])
            for z in range(len(V)):
                if z not in idx and johnson_distance(V[a],V[z])+johnson_distance(V[z],V[b]) == d:
                    return False
    return True

def generated_convex_sets(n,k,V):
    out={frozenset()}
    for lo in range(1<<n):
        for hi in range(1<<n):
            if lo & ~hi: continue
            c=frozenset(i for i,v in enumerate(V) if v&lo==lo and not(v&~hi))
            out.add(c)
    return out

def private_criterion(ids,n,V):
    ids=list(ids)
    if not ids: return True
    for pos,xid in enumerate(ids):
        others=ids[:pos]+ids[pos+1:]
        shared=(1<<n)-1
        covered=0
        for j in others:
            shared &= V[j]
            covered |= V[j]
        if not ((V[xid]&~covered) or (shared&~V[xid])):
            return False
    return True

def directly_shattered(ids,concepts):
    ids=list(ids)
    targets=set(range(1<<len(ids)))
    actual=set()
    for C in concepts:
        trace=sum(1<<j for j,x in enumerate(ids) if x in C)
        actual.add(trace)
        if len(actual)==len(targets):return True
    return False

def theoretical_vc(n,k):
    return n-min(2,k-1,n-k-1)

def theoretical_max_count(n,k):
    a=min(k,n-k)
    if a==1:return 1
    if a==2:return (8 if n==4 else n)
    return (factorial(n)//(2*factorial(k-1)*factorial(n-k-1))
            + (comb(n,2) if k==3 else 0)
            + (comb(n,2) if n-k==3 else 0))

def census_max(n,k):
    V=vertices(n,k)
    d=theoretical_vc(n,k)
    ct=0
    for ids in combinations(range(len(V)),d):
        ct += private_criterion(ids,n,V)
    return ct

def main():
    for n,k in [(3,1),(4,2),(5,2)]:
        V=vertices(n,k)
        generated=generated_convex_sets(n,k,V)
        allconvex={frozenset(i for i in range(len(V)) if mask>>i&1)
                   for mask in range(1<<len(V))
                   if convex_by_geodesics(frozenset(i for i in range(len(V)) if mask>>i&1),n,V)}
        assert allconvex==generated,(n,k,len(allconvex),len(generated))
        print(f'GEODESIC_VS_INTERVAL_EXHAUSTIVE_PASS n={n} k={k} convex={len(generated)}')
    n,k=6,3
    V=vertices(n,k)
    concepts=generated_convex_sets(n,k,V)
    tested=0
    for depth in range(0,6):
        for ids in combinations(range(len(V)),depth):
            criterion=private_criterion(ids,n,V)
            direct=directly_shattered(ids,concepts)
            assert criterion==direct,(ids,criterion,direct)
            tested+=1
    print(f'FULL_TRACE_VS_PRIVATE_CRITERION_PASS n=6 k=3 supports={tested} convex={len(concepts)}')
    for n in range(3,8):
        for k in range(1,n):
            actual=census_max(n,k)
            want=theoretical_max_count(n,k)
            assert actual==want,(n,k,actual,want)
            print(f'MAX_SUPPORT_CENSUS_PASS n={n} k={k} vc={theoretical_vc(n,k)} count={actual}')
    # Cross-check central construction, distinctness and witness criterion.
    for n,k in [(8,4),(8,3),(9,4),(10,5)]:
        p=n-k-1; q=k-1
        masks=set()
        for PP in combinations(range(n),p):
            rem1=set(range(n))-set(PP)
            for QQ in combinations(sorted(rem1),q):
                RR=rem1-set(QQ)
                maskQ=sum(1<<i for i in QQ)
                maskR=sum(1<<i for i in RR)
                points=tuple(sorted([maskQ|(1<<i) for i in PP]
                                    +[(maskQ&~(1<<j))|maskR for j in QQ]))
                assert len(points)==n-2
                assert all(x.bit_count()==k for x in points)
                assert private_criterion(list(range(len(points))),n,points)
                masks.add(points)
        expected=factorial(n)//(2*factorial(p)*factorial(q))
        assert len(masks)==expected,(n,k,len(masks),expected)
        print(f'MIXED_MAXIMAL_SUPPORT_CONSTRUCTION_PASS n={n} k={k} unique={len(masks)}')
    print('ALL_JOHNSON_GEODESIC_CONVEX_SHATTERING_CHECKS_PASS')

if __name__=='__main__':main()
