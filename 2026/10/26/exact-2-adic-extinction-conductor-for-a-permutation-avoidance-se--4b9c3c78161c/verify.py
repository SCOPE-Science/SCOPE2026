#!/usr/bin/env python3
"""Exact arithmetic replay for the dyadic cutoff theorem."""
from math import comb

def catalan(k):
    return comb(2*k, k)//(k+1)

def coeff(n):
    return sum(((-1)**(n-k))* (1<<k)*catalan(k)*comb(2*k+1,n-k)
               for k in range((n+1)//3,n+1) if 0 <= n-k <= 2*k+1)

def valuations(v):
    return (v & -v).bit_length()-1

N=230
arr=[1,1]
for n in range(2,N):
    u=sum(arr[j]*arr[n-1-j] for j in range(n))
    v=sum(arr[j]*arr[n-2-j] for j in range(n-1))
    arr.append(2*(u-v))
for n in range(N):
    assert arr[n] == coeff(n), ('coefficient',n)
    lower=(n+1)//3
    assert valuations(arr[n]) >= lower
    attained = (n in (0,1) or any(n in (3*((1<<r)-1)-1,
           3*((1<<r)-1),3*((1<<r)-1)+1) for r in range(1,12)))
    assert (valuations(arr[n]) == lower) == attained, ('valuation boundary', n)
for alpha in range(1,65):
    max_k=max(k for k in range(alpha) if k+(k+1).bit_count()-1 < alpha)
    cutoff=3*max_k+2
    assert all(arr[n]%(1<<alpha)==0 for n in range(cutoff,N)), ('tail',alpha)
    assert arr[cutoff-1]%(1<<alpha) !=0, ('minimality',alpha)
assert arr[:5]==[1,1,2,6,22]
for alpha in range(6,65):
    m=1<<alpha
    forbidden={(m//2+c)%m for c in (1,2,6,22)}
    assert not any(v%m in forbidden for v in arr[:3*alpha]), alpha
print('VERIFY_OK: coefficients n=0..229; equality indices; sharp cutoffs alpha=1..64; four residue families')
