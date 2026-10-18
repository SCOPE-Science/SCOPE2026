#!/usr/bin/env python3
"""Exact finite checks for S-legal-index-difference representation-growth theorem.
Uses only Python standard library. The proof of all infinite claims is symbolic.
"""
from math import log

def legal(mask, n, k, c):
    return all(not (mask >> (n-1-gap)) & 1
               for gap in range(1,k+1) if gap != k-c and n-1-gap >= 0)

def enumerate_sum_decompositions(k,c,N):
    # Distinct subsets remain separate, even when their sums coincide.
    subsets=[(0,0)]
    a=[];d=[1];averages=[]
    for n in range(1,N+1):
        old_representable={z for _,z in subsets}
        x=1
        while x in old_representable:
            x+=1
        a.append(x)
        if n>=18:
            averages.append((n, sum(z<x for _,z in subsets),x))
        new=[]
        for mask,s in subsets:
            if legal(mask,n,k,c):
                new.append((mask|(1<<(n-1)),s+x))
        subsets.extend(new)
        d.append(len(subsets))
        if n>k+1:
            expect=d[n-1]+d[n-k+c]-d[n-k+c-1]+d[n-k-1]
            assert d[n]==expect,('d recurrence',k,c,n,d[n],expect)
        if c==1 and k>=11 and n>k+2:
            assert a[n-1]==a[n-2]+a[n-k-2],('a recurrence',k,n,a)
    return a,d,averages

def root_bisect(f):
    lo,hi=1.0,1.5
    assert f(lo)<0 and f(hi)>0
    for _ in range(90):
        mid=(lo+hi)*.5
        if f(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)*.5

def spectral_checks():
    count=0
    for k,c in ((11,1),(12,1),(15,1),(20,1),(30,1),(50,1),
                (11,2),(17,3),(23,2),(50,5)):
        lam=root_bisect(lambda x:(x-1)*x**k-1)
        rho=root_bisect(lambda x:(x-1)*(x**k-x**c)-1)
        assert 1<lam<rho<1.5
        gap=(rho-lam)/lam
        assert gap>0
        print('spectral k=%d c=%d lambda=%.12f rho=%.12f ratio=%.12f' %
             (k,c,lam,rho,rho/lam))
        count+=1
    return count

def verify_count_dp(k,c,N):
    # Finite automaton: all legal previous k-bit suffixes, counted exactly.
    dp={0:1};d=[1]
    for n in range(1,N+1):
        nxt={}
        for mask,w in dp.items():
            tail=(mask<<1)&((1<<k)-1)
            nxt[tail]=nxt.get(tail,0)+w
            if all(not (mask>>(j-1))&1 for j in range(1,k+1) if j!=k-c):
                nxt[tail|1]=nxt.get(tail|1,0)+w
        dp=nxt;d.append(sum(dp.values()))
        if n>k+1:
            expect=d[n-1]+d[n-k+c]-d[n-k+c-1]+d[n-k-1]
            assert d[n]==expect,('DP recurrence',k,c,n)
    return d

if __name__=='__main__':
    count=0
    for k,c,N in ((11,1,44),(12,1,40),(14,1,39),(11,2,32)):
        a,d,averages=enumerate_sum_decompositions(k,c,N)
        assert d==verify_count_dp(k,c,N)
        print('exact subset/mex k=%d c=%d n=%d a_n=%d legal_subsets=%d' %
              (k,c,N,a[-1],d[-1]))
        if k==11 and c==1:
            print('mean counts n, numerator, a_n:', [x for x in averages if x[0] in (20,30,40)])
        count+=1
    for k,c,N in ((17,3,115),(19,2,115),(29,1,130),(23,5,120)):
        d=verify_count_dp(k,c,N)
        print('transfer recurrence k=%d c=%d n=%d count=%d' % (k,c,N,d[-1]))
        count+=1
    count+=spectral_checks()
    print('PASS all %d parameter tests; finite checks not an infinite proof' % count)
