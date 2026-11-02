#!/usr/bin/env python3
"""Finite reproducibility checks for three-point packing stability.

Run with Python 3, no external dependencies. All arithmetic is exact.
"""
from itertools import combinations, product
from collections import defaultdict

D2 = ((0,0),(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))

def diff(A, mod):
    return {(a-b)%mod for a in A for b in A}

def max_packings_cycle(p,A):
    D=diff(A,p)
    sizes=set()
    for mask in range(1,1<<p):
        B=[j for j in range(p) if (mask>>j)&1]
        if any((b-c)%p in D for b,c in combinations(B,2)):continue
        if {((b+d)%p) for b in B for d in D}!=set(range(p)):continue
        sizes.add(len(B))
    return sizes

def valid_torus(p,B):
    vs=set(product(range(p),repeat=2))
    Bs=set(B)
    D={(a%p,b%p) for a,b in D2}
    independent=(len(Bs)==len(B) and all(((u[0]-v[0])%p,(u[1]-v[1])%p) not in D for u,v in combinations(B,2)))
    dominated={((u[0]+d[0])%p,(u[1]+d[1])%p) for u in B for d in D}==vs
    return independent and dominated

def witnesses(p):
    S={0} if p in (5,7) else {0,5}
    first=sorted((x,y) for x in range(p) for y in range(p) if (y-2*x)%p in S)
    # Greedy maximal packing; every vertex gets considered in lexicographic order.
    occupied=set();second=[]
    for u in product(range(p),repeat=2):
        if u not in occupied:
            second.append(u)
            occupied.update((((u[0]+dx)%p,(u[1]+dy)%p) for dx,dy in D2))
    assert valid_torus(p,first) and valid_torus(p,second)
    return first,second

def maximal_sets_small_field(p,d,A):
    X=list(product(range(p), repeat=d)); n=len(X)
    D={tuple((a[i]-b[i])%p for i in range(d)) for a in A for b in A}
    allmax=[]
    for mask in range(1,1<<n):
        B=[X[i] for i in range(n) if mask>>i&1]
        if any(tuple((a[i]-b[i])%p for i in range(d)) in D for a,b in combinations(B,2)):
            continue
        if {tuple((a[i]+delta[i])%p for i in range(d)) for a in B for delta in D}!=set(X):
            continue
        allmax.append(B)
    return allmax

def gaps(p,k):
    assert 4*k<=p<=7*k
    res=[4]*k;extra=p-4*k
    for i in range(k):
        add=min(3,extra);res[i]+=add;extra-=add
    assert extra==0
    return res

def positions(gs,p):
    s=0;B=[]
    for gap in gs:
        B.append(s);s=(s+gap)%p
    assert s==0 and len(set(B))==len(B)
    return B

def main():
    # All affine/translation classes are covered by anchored triples {0,a,b}.
    for p in (5,7,11):
        tally=defaultdict(set)
        for a,b in combinations(range(1,p),2):
            D=diff([0,a,b],p)
            tally[len(D)].add(tuple(max_packings_cycle(p,[0,a,b])))
        print('CYCLIC',p,{d:sorted(s) for d,s in sorted(tally.items())})
        assert all(len(s)==1 and len(next(iter(s)))==1 for s in tally.values())
        B0,B1=witnesses(p)
        expect={5:(5,7),7:(7,13),11:(22,31)}[p]
        assert (len(B0),len(B1))==expect
        print('TORUS',p,'sizes',len(B0),len(B1),'GREEDY',B1)
    for p,d,A,expected_count,expected_size in [
        (2,2,[(0,0),(1,0),(0,1)],4,1),
        (2,3,[(0,0,0),(1,0,0),(0,1,0)],16,2),
        (3,2,[(0,0),(1,0),(0,1)],3,3),
        (3,2,[(0,0),(1,0),(2,0)],27,3)]:
        fs=maximal_sets_small_field(p,d,A)
        assert len(fs)==expected_count and {len(x) for x in fs}=={expected_size}
        print('SMALL_FIELD',p,d,'number',len(fs),'size',expected_size)
    for p in (13,17,19,23,29,31,37,41,43,47,53):
        if p==13: k=2
        elif p<20: k=3
        else: k=p//5
        for j in (k,k+1):
            B=positions(gaps(p,j),p)
            D=diff((0,1,3),p)
            assert len(B)==j
            assert all((a-b)%p not in D for a,b in combinations(B,2))
            assert {(b+d)%p for b in B for d in D}==set(range(p))
        print('LARGE_PRIME',p,'different sizes',k,k+1)
    print('VERIFY_OK')

if __name__=='__main__': main()
