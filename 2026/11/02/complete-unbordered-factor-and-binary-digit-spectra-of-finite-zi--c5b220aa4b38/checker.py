#!/usr/bin/env python3
"""Reproducibility check for unbordered contiguous factors of literal finite Zimin words.

Checks finite ranks only. Infinite-rank conclusion requires the accompanying proof.
"""
from collections import Counter

def zimin(n):
    z=''
    for i in range(n): z=z+chr(97+i)+z
    return z

def unbordered(s):
    return not any(s[:k]==s[-k:] for k in range(1,len(s)))

def popcount(k): return k.bit_count()

def predicted(n):
    z=[]
    for r in range(1,n+1):
        p=zimin(r-1)
        m=2**(r-1)
        for i in range(m):
            for j in range(m):
                if i&j==0:
                    z.append(p[-i:] if i else '')
                    z[-1] += chr(96+r) + p[:j]
    return set(z)

def brute(n):
    w=zimin(n)
    return {w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1) if unbordered(w[i:j])}

for n in range(1,9):
    w=zimin(n)
    actual=brute(n)
    expected=predicted(n)
    assert actual==expected, (n, (actual-expected), (expected-actual))
    hist=Counter(map(len,actual))
    assert len(actual)==(3**n-1)//2
    for ell in range(1,len(w)+1):
        count=(n-(ell-1).bit_length())*(2**popcount(ell-1)) if ell<=2**(n-1) else 0
        # ceil(log2 ell) == (ell-1).bit_length()
        assert hist[ell]==count, (n,ell,hist[ell],count)
    print(f'rank={n}, length={len(w)}, factors={len(actual)}, range=1..{2**(n-1)}: PASS')

# Independently verify boundary bit-condition as an entire boolean matrix.
for m in range(0,8):
    z=zimin(m)
    for i in range(2**m):
        left=z[-i:] if i else ''
        for j in range(2**m):
            f=left+'~'+z[:j]
            assert unbordered(f)==(i&j==0),(m,i,j)
    print(f'bit-boundary rank={m}, pair_count={4**m}: PASS')
print('ALL CHECKS PASS')
