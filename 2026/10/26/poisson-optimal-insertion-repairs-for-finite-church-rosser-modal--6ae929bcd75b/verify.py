#!/usr/bin/env python3
"""Finite independent checks for a critical-window Church--Rosser insertion law."""
from itertools import combinations
from math import comb
from fractions import Fraction
import random


def pair_rows(rows):
    n=len(rows)
    return [(u,v) for u in range(n) for v in range(u+1,n) if not (rows[u] & rows[v])]

def direct_confluence(rows):
    n=len(rows)
    for x in range(n):
        for y in range(n):
            if not (rows[x] >> y) & 1: continue
            for z in range(n):
                if (rows[x] >> z) & 1 and not (rows[y] & rows[z]):
                    return False
    return True

def modal_valid(rows):
    n=len(rows)
    for valuation in range(1<<n):
        for x in range(n):
            ant=any(not (rows[y]&~valuation) for y in range(n) if (rows[x]>>y)&1)
            conseq=all(bool(rows[z]&valuation) for z in range(n) if (rows[x]>>z)&1)
            if ant and not conseq:
                return False
    return True

def active(rows,u,v):
    return any((rows[x]>>u)&1 and (rows[x]>>v)&1 for x in range(len(rows)))

def certificate(rows):
    n=len(rows)
    bad=pair_rows(rows)
    used=set()
    if min(x.bit_count() for x in rows)<2: return None
    for u,v in bad:
        if u in used or v in used or not active(rows,u,v):return None
        used.update((u,v))
    edit=list(rows)
    for u,v in bad:
        available=rows[v] & ~(1<<u)
        if not available: return None
        w=(available & -available).bit_length()-1
        assert not (edit[u]>>w)&1
        edit[u]|=1<<w
    assert direct_confluence(edit)
    # Every original activated bad pair needs an edge from one of its two endpoints;
    # the pairs are disjoint, so these are independent lower certificates.
    return len(bad)

def enumerate_small(n):
    edges=[(x,y) for x in range(n) for y in range(n) if x!=y]
    total=1<<len(edges)
    nvalid=0; certs=0; zsum=0; z2sum=0; overlaps=0
    for m in range(total):
        rows=[0]*n
        for bit,(x,y) in enumerate(edges):
            if (m>>bit)&1:rows[x]|=1<<y
        direct=direct_confluence(rows)
        assert direct == modal_valid(rows)
        nvalid+=direct
        z=len(pair_rows(rows)); zsum+=z; z2sum+=z*(z-1)
        if certificate(rows) is not None: certs+=1
        for (u,v),(x,y) in combinations(pair_rows(rows),2):
            if len({u,v,x,y})==3:overlaps+=1
    p=Fraction(1,2)
    ez=comb(n,2)*(1-p*p)**(n-2) if n>=2 else Fraction(0)
    assert Fraction(zsum,total)==ez
    paircount_disjoint=3*comb(n,4)
    paircount_shared=3*comb(n,3)
    joint_disjoint=(1-p*p)**(2*(n-2))
    joint_shared=(1-p*p)**2 * (1-2*p*p+p*p*p)**(n-3) if n>=3 else 0
    expected_second=2*(paircount_disjoint*joint_disjoint+paircount_shared*joint_shared)
    assert Fraction(z2sum,total)==expected_second
    assert Fraction(overlaps,total)==paircount_shared*joint_shared
    print('DIRECT_MODAL_AND_FACTORIAL_MOMENTS_OK',n,total,nvalid,certs,str(ez))


def test_small_minimum():
    n=3
    edges=[(x,y) for x in range(n) for y in range(n) if x!=y]
    total=1<<len(edges)
    for m in range(total):
        rows=[0]*n
        for bit,(x,y) in enumerate(edges):
            if (m>>bit)&1:rows[x]|=1<<y
        if direct_confluence(rows): continue
        mindist=None
        missing=((1<<len(edges))-1)^m
        sub=missing
        while True:
            new=m|sub
            e_rows=[0]*n
            for bit,(x,y) in enumerate(edges):
                if (new>>bit)&1:e_rows[x]|=1<<y
            if direct_confluence(e_rows):
                mindist=sub.bit_count() if mindist is None else min(mindist,sub.bit_count())
            if sub==0:break
            sub=(sub-1)&missing
        cert=certificate(rows)
        if cert is not None:assert mindist==cert,(rows,mindist,cert)
    print('EXHAUSTIVE_INSERTION_DISTANCE_OK',n,total)

def test_optimal_multiplicity():
    # Exhaustive optimal insertion choices on all four-world certificate frames.
    n=4
    edges=[(x,y) for x in range(n) for y in range(n) if x!=y]
    inspected=0
    for mask in range(1<<len(edges)):
        rows=[0]*n
        for bit,(x,y) in enumerate(edges):
            if mask>>bit & 1: rows[x]|=1<<y
        k=certificate(rows)
        if k is None:continue
        bad=pair_rows(rows)
        predicted=1
        for u,v in bad:
            predicted*=rows[u].bit_count()+rows[v].bit_count()-int((rows[u]>>v)&1)-int((rows[v]>>u)&1)
        actual=0
        missing=[e for b,e in enumerate(edges) if not mask>>b&1]
        for chosen in combinations(missing,k):
            altered=list(rows)
            for u,v in chosen: altered[u]|=1<<v
            if direct_confluence(altered): actual+=1
        assert actual==predicted,(rows,k,actual,predicted)
        inspected+=1
    print('FOUR_WORLD_OPTIMAL_REPAIR_MULTIPLICITY_OK',inspected)

def test_random():
    rng=random.Random(719483)
    good=0
    for n in (12,25,55,80):
        p=(2*__import__('math').log(n)/n)**0.5
        for rep in range(600):
            rows=[sum(1<<y for y in range(n) if y!=x and rng.random()<p) for x in range(n)]
            cert=certificate(rows)
            if cert is not None:
                good+=1
                if len(pair_rows(rows))==0:assert direct_confluence(rows)
    print('RANDOM_REPAIR_CERTIFICATES_OK',good)

if __name__=='__main__':
    for n in range(1,5):enumerate_small(n)
    test_small_minimum()
    test_optimal_multiplicity()
    test_random()
    print('CHURCH_ROSSER_POISSON_INSERTION_CHECK_OK')
