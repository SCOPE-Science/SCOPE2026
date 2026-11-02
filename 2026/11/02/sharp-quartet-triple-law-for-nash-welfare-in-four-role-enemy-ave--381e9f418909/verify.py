#!/usr/bin/env python3
"""Exact checks for four-role aversion-to-enemies Nash welfare.

Run with Python 3 (standard library only): python verify.py
The finite checks supplement, and do not replace, the universal proof.
"""
from functools import lru_cache
from itertools import combinations
from math import factorial
from random import Random


def predicted(sizes):
    """Return (Nash product, (pairs, triples, quartets)), when positive."""
    a, b, c, d = sorted(sizes, reverse=True)
    n = a+b+c+d
    if n < 2 or a > n-a:
        return 0, None
    surplus = n-2*a
    q = min(d, surplus//2)
    upper = min(surplus-2*q, (n-4*q)//3)
    t = upper - ((upper-n) % 2)
    assert t >= 0
    p = (n-3*t-4*q)//2
    assert p >= 0 and a <= p+t+q and q <= d
    return 8**t * 81**q, (p,t,q)


@lru_cache(None)
def brute_color_product(sizes):
    """Exact optimization over all possible non-singleton color-transversal coalitions."""
    if not any(sizes):
        return 1
    i = next(i for i,z in enumerate(sizes) if z)
    others = [j for j in range(i+1,4) if sizes[j]]
    best = 0
    for r in range(1,len(others)+1):
        for J in combinations(others,r):
            s = list(sizes)
            for j in (i,*J):
                s[j] -= 1
            sz = 1+r
            best = max(best, (sz-1)**sz * brute_color_product(tuple(s)))
    return best


@lru_cache(None)
def ordered_slot_coefficient(sizes,p,t,q):
    """Coefficient of the elementary-symmetric polynomial product."""
    if not (p or t or q):
        return int(all(x==0 for x in sizes))
    if q:
        s=4
        qq=(p,t,q-1)
    elif t:
        s=3
        qq=(p,t-1,q)
    else:
        s=2
        qq=(p-1,t,q)
    ans=0
    for J in combinations([i for i,z in enumerate(sizes) if z],s):
        remain=list(sizes)
        for j in J:remain[j]-=1
        ans+=ordered_slot_coefficient(tuple(remain),*qq)
    return ans


def predicted_count(sizes):
    val, shape=predicted(sizes)
    if not val:return None
    p,t,q=shape
    coeff=ordered_slot_coefficient(tuple(sizes),p,t,q)
    numerator=coeff
    for a in sizes:numerator*=factorial(a)
    denominator=factorial(p)*factorial(t)*factorial(q)
    assert numerator%denominator==0
    return numerator//denominator


def brute_labeled(sizes):
    """Enumerate labeled coalitions; exclude singleton/zero-product partitions."""
    colors=tuple(i for i,c in enumerate(sizes) for _ in range(c))
    n=len(colors)
    @lru_cache(None)
    def rec(mask):
        if mask == 0:
            return 1,1
        lsb=mask & -mask
        i=lsb.bit_length()-1
        options=[j for j in range(i+1,n) if (mask>>j)&1 and colors[j]!=colors[i]]
        best=0;num=0
        for size in range(2, min(4,1+len(options))+1):
            for J in combinations(options,size-1):
                col=(colors[i],)+(tuple(colors[j] for j in J))
                if len(set(col))!=size:continue
                newmask=mask ^ (1<<i)
                for j in J:newmask ^= 1<<j
                smaller,cnt=rec(newmask)
                if not smaller:continue
                prod=smaller*(size-1)**size
                if prod>best:best,num=prod,cnt
                elif prod==best:num+=cnt
        return best,num
    return rec((1<<n)-1)


def construct(sizes):
    """Bipartite Havel-Hakimi construction of optimal role-transversal teams."""
    product,shape=predicted(sizes)
    if product==0:return None
    p,t,q=shape
    remaining=list(sizes)
    columns=[]
    for degree in [4]*q+[3]*t+[2]*p:
        order=sorted(range(4),key=lambda i:(-remaining[i],i))
        J=tuple(order[:degree])
        assert all(remaining[i]>0 for i in J)
        for i in J:remaining[i]-=1
        columns.append(J)
    assert remaining==[0,0,0,0]
    from_cols=1
    for J in columns:from_cols *= (len(J)-1)**len(J)
    assert from_cols==product
    return columns


def main():
    checked=0
    for a in range(1,11):
        for b in range(a+1):
            for c in range(b+1):
                for d in range(c+1):
                    sizes=(a,b,c,d)
                    if sum(sizes)>24:continue
                    expected,shape=predicted(sizes)
                    actual=brute_color_product(sizes)
                    assert expected==actual,(sizes,shape,expected,actual)
                    if expected:
                        construct(sizes)
                    checked+=1
    print('Optimal Nash products: PASS',checked,'ordered role-size profiles (n<=24)')

    count_cases=0
    for a in range(1,4):
        for b in range(a+1):
            for c in range(b+1):
                for d in range(c+1):
                    sizes=(a,b,c,d)
                    if sum(sizes)>9:continue
                    prod,count=brute_labeled(sizes)
                    expected,shape=predicted(sizes)
                    assert expected==prod,(sizes,expected,prod)
                    if prod:
                        expect_count=predicted_count(sizes)
                        assert count==expect_count,(sizes,count,expect_count)
                    count_cases+=1
    print('Labeled optimal-partition counts: PASS',count_cases,'role-size profiles (n<=9)')

    rng=Random(20260518)
    for _ in range(2000):
        sizes=tuple(rng.randrange(51) for _ in range(4))
        expected,shape=predicted(sizes)
        if expected:
            construct(sizes)
    print('Havel-Hakimi realizations: PASS 2000 seeded large profiles')

    assert predicted((5,4,4,1))==(8**2*81,(2,2,1))
    assert predicted((4,3,2,1))==(81,(3,0,1))
    assert predicted((3,3,3,3))==(81**3,(0,0,3))
    assert predicted((6,1,1,1))==(0,None)
    assert 81>64
    print('Boundary and strict-exchange checks: PASS')

if __name__=='__main__':main()
