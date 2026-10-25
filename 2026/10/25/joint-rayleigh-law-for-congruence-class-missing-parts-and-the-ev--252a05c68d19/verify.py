#!/usr/bin/env python3
"""Exact finite checks of a periodic minimum-excludant identity."""
from math import comb

def partitions(N):
    p=[0]*(N+1)
    p[0]=1
    for k in range(1,N+1):
        for i in range(k,N+1): p[i]+=p[i-k]
    return p

def min_missing_counts(N,h,R,p):
    out={r:[0]*(N+1) for r in R}
    S=0
    for m in range(1,N+2):
        if m%h not in R: continue
        if S>N: break
        for n in range(S,N+1):
            out[m%h][n]+=p[n-S]-(p[n-S-m] if n-S>=m else 0)
        S+=m
    return out

def overpartition_even_counts(N):
    B=[0]*(N+1)
    for r in range(1,N//2+1):
        w=[1]+[0]*N
        for j in range(1,r+1):
            step=2*j-1
            for i in range(N,step-1,-1): w[i]+=w[i-step]
        for j in range(1,r):
            step=2*j
            for i in range(step,N+1): w[i]+=w[i-step]
            for i in range(N,step-1,-1): w[i]+=w[i-step]
        step=2*r
        for i in range(step,N+1): w[i]+=w[i-step]
        for i in range(step,N+1): B[i]+=w[i-step]
    return B

def main():
    N=2400
    p=partitions(N)
    A=min_missing_counts(N,4,{0,2,3},p)
    assert all(sum(A[r][n] for r in A)==p[n] for n in range(N+1))
    B=overpartition_even_counts(85)
    assert all(A[3][n]==B[n] for n in range(1,86))
    for h,R in [(2,{0}), (3,{0,1,2}), (5,{1,3}), (7,{0,2,5})]:
        K=180
        a=min_missing_counts(K,h,R,p)
        assert all(sum(a[r][n] for r in a)==p[n] for n in range(K+1))
    print('a_e/p samples:',[(n, round(A[3][n]/p[n],8)) for n in (100,300,800,1600,2400)])
    print('sample a_e,b_e:', [(n,A[3][n],B[n]) for n in (2,3,6,12,24,48,80)])
    print('VERIFY_OK')
if __name__=='__main__':main()
