#!/usr/bin/env python3
"""Independent finite checks for weighted restricted-partition congruences.

Only standard-library arithmetic is used. Finite checks corroborate an analytic proof.
"""
from math import isqrt
from functools import lru_cache

N = 2400

# Two independent generating-function constructions: unrestricted odd and
# at-most-once even parts for weighted coefficients; 4-regular partitions.
b = [0]*(N+1)
w = [0]*(N+1)
b[0] = 1
for m in range(1,N+1):
    if m % 2:
        for n in range(m,N+1):
            old=b[n-m]
            w[n] += w[n-m] + m*old
            b[n] += old
    else:
        for n in range(N,m-1,-1):
            old=b[n-m]
            w[n] += w[n-m] - m*old
            b[n] += old
    for n in range(N+1):
        b[n] &= 15
        w[n] &= 15

b4 = [0]*(N+1)
b4[0]=1
for m in range(1,N+1):
    if m%4:
        for n in range(m,N+1):
            b4[n] = (b4[n]+b4[n-m])%16
assert b == b4, ('Glaisher b4 identity', next(i for i in range(N+1) if b[i]!=b4[i]))

def r1r2(n):
    M=8*n+1
    cnt=[0,0]
    for y in range(4,isqrt(M)+1,4):
        z=M-y*y
        if z>0 and isqrt(z)**2==z and isqrt(z)%2==1:
            cnt[0]+=1
        z=M-2*y*y
        if z>0 and isqrt(z)**2==z and isqrt(z)%2==1:
            cnt[1]+=1
    return cnt

def char_sum_four(m):
    total=0
    for d in range(1,isqrt(m)+1):
        if m%d:
            continue
        for z in (d,m//d) if d*d!=m else (d,):
            total += 1 if z%4==1 else (-1 if z%4==3 else 0)
    return total

for n in range(N+1):
    M=8*n+1
    R1,R2=r1r2(n)
    assert char_sum_four(M)==2*R1+int(isqrt(M)**2==M), ('Jacobi normalization',n)
    c=R1+R2
    assert (w[n]-n*b4[n]+4*c)%8==0, ('quadratic form identity',n,w[n],b4[n],r1r2(n))

# Independent prime-factor test of the inert-prime transfer condition.
def factor_odd(m):
    out=[]
    d=3
    while d*d<=m:
        if m%d==0:
            k=0
            while m%d==0:
                k+=1
                m//=d
            out.append((d,k))
        d+=2
    if m>1:
        out.append((m,1))
    return out

transfer_count=0
for n in range(N+1):
    if any(p%8 in (5,7) and e%2 for p,e in factor_odd(8*n+1)):
        transfer_count+=1
        assert (w[n]-n*b4[n])%8==0, ('prime transfer',n,8*n+1)

progressions25=(8,13,18,23)
progressions49=(13,20,27,34,41,48)
checks=0
for mod,residues in ((25,progressions25),(49,progressions49)):
    for r in residues:
        for n in range(r,N+1,mod):
            assert w[n]%8==0, ('progression',mod,r,n,w[n])
            checks+=1

@lru_cache(None)
def partitions(n,max_part):
    if n==0:
        return ((),)
    return tuple((m,)+p for m in range(min(max_part,n),0,-1)
         for p in partitions(n-m,m))
for n in range(26):
    direct=0
    for part in partitions(n,n):
        if len([m for m in part if m%2==0])!=len(set(m for m in part if m%2==0)):
            continue
        direct+=sum(m if m%2 else -m for m in part)
    assert direct%16==w[n], ('independent enumeration',n,direct,w[n])

print('VERIFY_OK coefficients=2401 form_identical=2401 weighted_partition_direct=26 progressions_checks='+str(checks)+' b4_checks=2401 two_square_normalization=2401 transfer_checks='+str(transfer_count))
