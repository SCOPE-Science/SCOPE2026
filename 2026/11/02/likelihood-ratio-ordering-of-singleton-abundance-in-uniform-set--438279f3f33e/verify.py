#!/usr/bin/env python3
"""Exact finite checks for singleton/block-count total positivity in set partitions.

The infinite theorem follows from the analytic proof, not these checks.
"""
from collections import defaultdict
from math import comb

CHECKS=0

def check(condition, context):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(context)

def tables(M):
    a=[[0]*(M+1) for _ in range(M+1)]
    t=[[0]*(M+1) for _ in range(M+1)]
    a[0][0]=1
    t[0][0]=1
    for n in range(1,M+1):
        for k in range(1,n+1):
            t[n][k]=k*t[n-1][k]+t[n-1][k-1]
            # The first term is automatically zero when n=1.
            a[n][k]=k*a[n-1][k]+(n-1)*a[n-2][k-1] if n>=2 else 0
    return a,t

A,T=tables(75)

def weight(n,k,s):
    if not (0<=s<=k<=n):return 0
    return comb(n,s)*A[n-s][k-s]

# Independent generation via restricted-growth strings (unlabeled block partitions).
def brute(n):
    ans=defaultdict(int)
    def walk(blocks,next_label):
        if next_label==n:
            ans[(len(blocks),sum(len(b)==1 for b in blocks))]+=1
            return
        for b in blocks:
            b.append(next_label)
            walk(blocks,next_label+1)
            b.pop()
        blocks.append([next_label]);walk(blocks,next_label+1);blocks.pop()
    if n:walk([[0]],1)
    else:ans[(0,0)]=1
    return ans

for n in range(0,9):
    actual=brute(n)
    for k in range(n+1):
        for s in range(n+1):
            check(actual[(k,s)]==weight(n,k,s),('brute',n,k,s))

for n in range(0,76):
    for k in range(n+1):
        check(sum(weight(n,k,s) for s in range(n+1))==T[n][k],('marginal',n,k))

# Each adjacent-k and adjacent-s 2x2 minor, all accessible n.
for n in range(2,76):
    for k in range(n):
        for s in range(n):
            det=weight(n,k,s)*weight(n,k+1,s+1)-weight(n,k,s+1)*weight(n,k+1,s)
            check(det>=0,('adjacent-TP2',n,k,s,det))

# All minors including zero cells and nonadjacent strata.
for n in range(2,23):
    for k in range(n):
        for kk in range(k+1,n+1):
            for s in range(n):
                for ss in range(s+1,n+1):
                    det=weight(n,k,s)*weight(n,kk,ss)-weight(n,k,ss)*weight(n,kk,s)
                    check(det>=0,('full-TP2',n,k,kk,s,ss,det))

print('PASS: '+str(CHECKS)+' exact integer assertions (n<=75 adjacent, n<=22 all minors, n<=8 independent enumeration)')
