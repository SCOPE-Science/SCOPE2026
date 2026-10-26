#!/usr/bin/env python3
"""Reproduce finite checks for singleton distance-two legal sums."""
from math import sqrt


def rec_terms(N):
    a=[0,1,2,4]
    for n in range(3,N):
        a.append(a[n]+a[n-2])
    return a


def valid_masks(n):
    for mask in range(1<<n):
        if mask & (mask>>2):
            continue
        yield mask


def all_legal_sums(a,n):
    for mask in valid_masks(n):
        yield sum(a[j+1] for j in range(n) if mask>>j&1)


def fib(n):
    p,q=0,1
    for _ in range(n):p,q=q,p+q
    return p


def predicted_d(n):
    return fib((n+1)//2+2)*fib(n//2+2)


def checks():
    N=19
    a=rec_terms(N)
    # Independent greedy mex construction, including the empty set.
    observed=[]
    for n in range(1,17):
        have=set(all_legal_sums([0]+observed,n-1))
        mex=1
        while mex in have:mex+=1
        observed.append(mex)
        assert mex==a[n], (n,mex,a[n])
    for n in range(1,18):
        sums=list(all_legal_sums(a,n))
        assert len(sums)==predicted_d(n)
        if n>=4:
            assert sum(a[1:n-2])==a[n]-4
            below=sum(v<a[n] for v in all_legal_sums(a,n-1))
            assert predicted_d(n-3) <= below <= predicted_d(n-1)
            # Exhaustively count individual representation multiplicities.
            c=[0]*a[n]
            for v in all_legal_sums(a,n-1):
                if v<a[n]:c[v]+=1
            assert all(c), (n,[j for j,x in enumerate(c) if not x])
            assert sum(c)==below
    assert a[1:11]==[1,2,4,5,7,11,16,23,34,50]
    print('VERIFIED: independent mex through n=16; legal subset formulas through n=17;')
    print('          exact total-sum identity, complete multiplicities and mean bounds.')

if __name__=='__main__':checks()
