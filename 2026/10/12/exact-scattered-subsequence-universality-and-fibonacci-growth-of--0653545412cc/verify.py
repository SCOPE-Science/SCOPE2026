#!/usr/bin/env python3
"""Consistency checks for an exact Baum-Sweet subsequence theorem."""
from itertools import groupby, product

def bs(n):
    if n == 0:
        return 1
    return int(all(len(list(g)) % 2 == 0 for k,g in groupby(bin(n)[2:]) if k == '0'))

def arch(w):
    cnt, flags = 0, 0
    for x in w:
        flags |= 1 << x
        if flags == 3:
            cnt += 1
            flags = 0
    return cnt

def contains_subsequence(w,u):
    i = 0
    for ch in w:
        if i < len(u) and ch == u[i]:
            i += 1
    return i == len(u)

def all_universal(w,k):
    return all(contains_subsequence(w,u) for u in product((0,1),repeat=k))

def predicted(N,bcount):
    if N <= 3:
        return (0,0,0,1)[N]
    is_end_doublet = False
    q=N-1
    if q>=4 and q & (q-1) == 0 and q.bit_length()%2==1:  # q=4^t, t>=1
        is_end_doublet=True
    return bcount-2-int(is_end_doublet)

NMAX = 1<<20
count=0;flags=0;u=0
fib0,fib1=0,1
fibs=[0,1]
for _ in range(30): fibs.append(fibs[-1]+fibs[-2])
prev=0; prevprev=0
for n in range(NMAX):
    bit=bs(n)
    if n>=1 and bit and prev:
        assert n == 4**((n.bit_length()-1)//2) and n.bit_length()%2==1, (n,prevprev,prev)
    if n>=2 and prev==1 and prevprev==1:
        assert bit==0
    flags|=1<<bit
    if flags==3:u+=1;flags=0
    count+=bit
    N=n+1
    assert u==predicted(N,count), (n,u,count,predicted(N,count))
    if N.bit_count()==1:
        m=N.bit_length()-1
        assert count==fibs[m+2]
        if m>=2:assert u==fibs[m+2]-2
    prevprev,prev=prev,bit
print(f'PREFIX_OK N=1..{NMAX} exact_formula=all adjacency_and_triples=all fibonacci_levels=0..20')

for N in range(0,30):
    w=tuple(bs(i) for i in range(N))
    k=arch(w)
    assert all_universal(w,k)
    assert not all_universal(w,k+1)
print('BRUTE_OK all_binary_subsequences_N=0..29')
