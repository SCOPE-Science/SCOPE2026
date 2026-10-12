#!/usr/bin/env python3
from math import isqrt

def is_binary_keith(N):
    bits=[int(c) for c in bin(N)[2:]]
    n=len(bits)
    if n==1:
        return True
    seq=bits[:]
    s=sum(seq)
    while s < N:
        seq.append(s)
        s=sum(seq[-n:])
    return s == N

def ceil_log2(w):
    return (w-1).bit_length()

def predicted(n):
    out={1<<(n-1)}
    for w in range(2,n+1):
        c=ceil_log2(w)
        L=1<<c
        A=(1<<(n-c))*w
        P,S=divmod(A,L+1)
        if S < L and P.bit_count()+S.bit_count()==w:
            N=P*L+S
            assert N.bit_length()==n
            assert N.bit_count()==w
            out.add(N)
    return out

all_nonpowers=[]
checked=0
for n in range(2,19):
    lo=1<<(n-1)
    hi=1<<n
    direct={N for N in range(lo,hi) if is_binary_keith(N)}
    pred=predicted(n)
    assert direct==pred,(n,sorted(direct^pred)[:20])
    for N in direct:
        checked += 1
        if N & (N-1):
            all_nonpowers.append(N)

known=[3,143,285,569,683,1138,1366,2276,154203,308405,616810,678491]
for N in known:
    if N < (1<<18):
        assert N in all_nonpowers

print("VERIFY_OK",
      "bit_lengths=2..18",
      f"keith_checked={checked}",
      f"nonpowers={sorted(all_nonpowers)}")
