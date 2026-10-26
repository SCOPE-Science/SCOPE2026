#!/usr/bin/env python3
"""Reproduce the complete small-prime restricted quintic sumset census.

All computations use Python integers. No external packages or datasets are needed.
"""
from math import gcd, isqrt

EXCEPTIONAL_MISSING = {
    11: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    31: [2, 3, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 28, 29],
    41: [1, 3, 7, 9, 14, 16, 19, 20, 21, 22, 25, 27, 32, 34, 38, 40],
    61: [4, 5, 6, 9, 17, 23, 38, 44, 52, 55, 56, 57],
    71: [1, 20, 23, 26, 30, 32, 34, 37, 39, 41, 45, 48, 51, 70],
    101: [1, 6, 10, 14, 17, 32, 36, 39, 41, 44, 57, 60, 62, 65, 69, 84, 87, 91, 95, 100],
}

def primes_through(n):
    out=[]
    for q in range(2,n+1):
        if all(q%d for d in range(2,isqrt(q)+1)):
            out.append(q)
    return out

def prime_factors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: out.append(n)
    return out

def fifth_power_set_by_direct_powers(p):
    return {pow(x,5,p) for x in range(1,p)}

def fifth_power_set_by_primitive_root(p):
    if p==2: return {1}
    factors=prime_factors(p-1)
    gen=next(g for g in range(2,p) if all(pow(g,(p-1)//q,p)!=1 for q in factors))
    d=gcd(5,p-1)
    return {pow(gen,d*j,p) for j in range((p-1)//d)}

def pair_sums_direct(h,p):
    return {(u+v)%p for u in h for v in h if u!=v}

def pair_sums_complement(h,p):
    # Independent O(p * |H|) representation test, not pair enumeration.
    return {a for a in range(p) if any((a-u)%p in h and (a-u)%p!=u for u in h)}

def verify():
    ps=primes_through(240)
    relevant=[]
    for p in ps:
        a=fifth_power_set_by_direct_powers(p)
        b=fifth_power_set_by_primitive_root(p)
        assert a==b, (p,'fifth-power values disagree')
        direct=pair_sums_direct(a,p)
        complement=pair_sums_complement(b,p)
        assert direct==complement, (p,'restricted sums disagree')
        missing=sorted(set(range(p))-direct)
        if p>=5 and p%5!=1:
            assert not missing, (p,'nonexceptional prime')
        if p%5==1:
            relevant.append(p)
            assert missing==EXCEPTIONAL_MISSING.get(p,[]), (p,'missing spectrum',missing)
            assert len(a)==(p-1)//5
    assert relevant==[11,31,41,61,71,101,131,151,181,191,211]
    assert (set(range(2))-pair_sums_direct(fifth_power_set_by_direct_powers(2),2))=={0,1}
    assert (set(range(3))-pair_sums_direct(fifth_power_set_by_direct_powers(3),3))=={1,2}
    # Algebraic sufficiency for all larger p≡1 (mod 5): p>39,
    # (p-39)**2 > 144*p implies p+1-12*sqrt(p)>40.
    assert (241-39)**2>144*241
    # (p-39)^2-144p has derivative 2p-222>0 for p>=241.
    assert 2*241-222>0
    print('VERIFIED: two exact algorithms, all primes <= 240; 11 finite fifth-power cases; genus-six large-prime bound')
    for p in relevant:
        print(f'p={p}; missing={len(EXCEPTIONAL_MISSING.get(p,[]))}')

if __name__=='__main__': verify()
