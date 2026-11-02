#!/usr/bin/env python3
"""Exact finite-size checks for deterministic chirp-coded binary diffraction."""
from collections import defaultdict
from itertools import combinations

def keys_prime(p,a):
    seen={}
    collisions=[]
    for m in range(1<<p):
        S=[j for j in range(p) if (m>>j)&1]
        # canonical autocorrelation cyclotomic coefficients for nonzero lags
        K=[len(S)]
        for h in range(1,p):
            v=[0]*p
            for j in S:
                if ((m>>((j-h)%p))&1):
                    v[(a*(2*h*j-h*h))%p]+=1
            K.extend(v[i]-v[p-1] for i in range(p-1))
        key=tuple(K)
        if key in seen:
            collisions.append((seen[key],m))
        else:
            seen[key]=m
    expected=[(1,1<<j) for j in range(1,p)]
    assert collisions==expected,(p,a,collisions[:10],expected)
    print(f'p={p}, a={a}, signals={1<<p}, unique_power_spectra={(1<<p)-p+1}, nontrivial_collisions={len(collisions)}')

def composite_pair(N,a,b,d,s):
    S={0,d%N}
    T={s%N,(s+d)%N}
    assert S!=T and len(S)==len(T)==2
    # An equality of exact chirp-encoded correlations for all h,
    # verified by root-of-unity exponent-count arrays (stronger than evaluation equality).
    def corr(S,h):
        v=[0]*N
        for j in S:
            if (j-h)%N in S:
                v[(a*(2*h*j-h*h)+b*h)%N]+=1
        return tuple(v)
    for h in range(N):
        assert corr(S,h)==corr(T,h),(N,a,b,d,s,h,corr(S,h),corr(T,h))
    print(f'N={N}, a={a}, support_A={sorted(S)}, support_B={sorted(T)}: identical coded power spectra')

if __name__=='__main__':
    for p in (3,5,7,11):
        for a in (1,2) if p>3 else (1,):
            keys_prime(p,a)
    for N,d,s in [(4,2,1),(6,3,1),(8,4,1),(9,3,3),(10,5,1),(15,3,5),(21,3,7),(25,5,5)]:
        composite_pair(N,1,3,d,s)
    print('All exact finite checks passed.')
