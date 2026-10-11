#!/usr/bin/env python3
"""Exact finite-level spectral and translation-stabilizer checks."""
from itertools import combinations,product
from collections import Counter


def E_set(base,level):
    return tuple(sorted(sum((base//2)*bit*(base**j) for j,bit in enumerate(bits)) for bits in product((0,1),repeat=level)))

def zero(base,level,k):
    k%=base**level
    if k==0: return False
    for j in range(level):
        bj=base**j
        if k%bj==0 and (k//bj)%2==1:
            return True
    return False

def build(base,level):
    choices=list(product(range(0,base,2),range(1,base,2)))
    # canonical as nested b-adic tree: at first digit choose even/odd;
    # attach independent subtrees of length level-1, scaled by b.
    def rec(depth):
        if depth==0:
            yield (0,)
            return
        for ea,oa in choices:
            for ea_tail in rec(depth-1):
                for oa_tail in rec(depth-1):
                    yield tuple(sorted([ea+base*t for t in ea_tail]+[oa+base*t for t in oa_tail]))
    return rec(level)

def F(base,level,s):
    b=base; n=level
    if s==0:return (b*b//4)**(2**n-1)
    if b%4==0:return 0
    return (b*b//4)**(2**(n-s)-1) * (b//2)**(s*(2**(n-s)))

def check(base,level,brute=False):
    N=base**level; count=0;by_stabilizer=Counter();reps=set();
    for L in build(base,level):
        assert len(L)==2**level and len(set(L))==len(L)
        assert all(zero(base,level,y-x) for x,y in combinations(L,2)),(base,level,L)
        H=frozenset(L); stable=sum(frozenset((x+t)%N for x in H)==H for t in range(N))
        assert stable in {2**s for s in range(level+1)}
        by_stabilizer[stable]+=1
        reps.add(min(tuple(sorted((x+t)%N for x in L)) for t in range(N)))
        count+=1
    assert count==F(base,level,0),(count,F(base,level,0))
    for s in range(level+1):
        want=F(base,level,s)
        got=sum(cnt for h,cnt in by_stabilizer.items() if h>=2**s)
        assert got==want,(base,level,s,got,want)
    orbit_predict=sum((1 if s==0 else 2**(s-1))*F(base,level,s) for s in range(level+1))//N
    assert len(reps)==orbit_predict,(base,level,len(reps),orbit_predict)
    if brute:
        clique=0
        for C in combinations(range(N),2**level):
            if all(zero(base,level,y-x) for x,y in combinations(C,2)):
                clique+=1
        assert clique==count,(base,level,clique,count)
    print(f'EXACT_OK b={base} n={level} spectra={count} orbits={len(reps)} stabilizer_counts={dict(sorted(by_stabilizer.items()))} brute={brute}')

if __name__=='__main__':
    for b,n,brute in [(2,1,True),(2,2,True),(2,3,True),(4,1,True),(4,2,True),(4,3,False),(6,1,True),(6,2,True),(8,1,True),(8,2,True),(10,1,True),(12,1,True)]:
        check(b,n,brute)
