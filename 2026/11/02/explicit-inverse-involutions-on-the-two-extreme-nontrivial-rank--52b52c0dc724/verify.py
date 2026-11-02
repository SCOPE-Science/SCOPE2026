#!/usr/bin/env python3
"""Standalone exact checker for inverse involutions on extreme ranks of isotone maps.
Python 3.9+; no third-party dependencies.
"""
from math import comb

def rank2(a,b,c):
    assert 1 <= a < N and 1 <= b < c <= N
    return tuple(b if x <= a else c for x in range(1,N+1))

def tau2(a,b,c):
    if b <= a < c:
        return a,b,c
    if a < b:
        return c-1,a,b
    assert c <= a
    return b,c,a+1

def rank_high(a,b):
    assert 1 <= a < N and 1 <= b <= N
    im=[v for v in range(1,N+1) if v!=b]
    return tuple(im[x-1 if x<=a else x-2] for x in range(1,N+1))

def tau_high(a,b):
    if a <= b <= a+1:
        return a,b
    if b<a:
        return b,a+1
    assert b>a+1
    return b-1,a

def compose(f,g):
    return tuple(g[x-1] for x in f)

def is_inverse(f,g):
    return compose(compose(f,g),f)==f and compose(compose(g,f),g)==g

for N in range(2,19):
    C2=[(a,b,c) for a in range(1,N) for b in range(1,N+1) for c in range(b+1,N+1)]
    H=[(a,b) for a in range(1,N) for b in range(1,N+1)]
    assert len(C2)==(N-1)*comb(N,2)
    assert len(H)==N*(N-1)
    assert len(set(rank2(*x) for x in C2))==len(C2)
    assert len(set(rank_high(*x) for x in H))==len(H)
    fix2,fixh=0,0
    for x in C2:
        y=tau2(*x)
        assert y in C2 and tau2(*y)==x, ('involution rank2',N,x,y)
        f,g=rank2(*x),rank2(*y)
        assert is_inverse(f,g), ('inverse rank2',N,x,y)
        assert (x==y)==(compose(f,f)==f),('fixed iff idempotent rank2',N,x)
        fix2+=(x==y)
    for x in H:
        y=tau_high(*x)
        assert y in H and tau_high(*y)==x, ('involution upper',N,x,y)
        f,g=rank_high(*x),rank_high(*y)
        assert is_inverse(f,g), ('inverse upper',N,x,y)
        assert (x==y)==(compose(f,f)==f),('fixed iff idempotent upper',N,x)
        fixh+=(x==y)
    assert fix2==comb(N+1,3)
    assert fixh==2*(N-1)
    assert (len(C2)-fix2)//2==comb(N,3)
    assert (len(H)-fixh)//2==comb(N-1,2)
    print(f'N={N:2} rank2_size={len(C2):5} rank2_fixed={fix2:5} rank2_swaps={comb(N,3):5} upper_size={len(H):4} upper_fixed={fixh:3} upper_swaps={comb(N-1,2):4}')
print('VERIFY_OK')
