#!/usr/bin/env python3
"""Independent integer checks for a rank--depth census of interval-image order-decreasing maps.

Run: python checker.py
No external modules or network access required.
"""
from collections import Counter
from itertools import product, combinations_with_replacement
from math import comb


def binom(n,k):
    return comb(n,k) if n >= 0 and 0 <= k <= n else 0


def recurrence(N):
    # A(n,k,h): nonconstant-or-constant zero-root maps with image size k+1
    # and least positive zero power h.
    A = {}
    for n in range(2,N+1):
        A[n,0,1] = 1
        for k in range(1,n-1):
            for h in range(2,n):
                val=sum(A.get((k+1,j,h-1),0)*binom(n-k-1,k-j)
                        for j in range(k))
                if val:
                    A[n,k,h]=val
    return A


def direct(n):
    # Direct enumerate monotone one-Lipschitz maps with f(1)=f(2)=1.
    tally=Counter()
    for increments in product((0,1),repeat=n-2):
        f=[1,1]
        for b in increments:
            f.append(f[-1]+b)
        assert len(f)==n
        assert all(f[i]<=i+1 for i in range(n))
        assert all(f[i+1]-f[i] in (0,1) for i in range(n-1))
        # Evaluate actual powers from n, rather than the proposed recurrence.
        cur=n
        depth=0
        while cur!=1:
            cur=f[cur-1]
            depth+=1
            assert depth<n
        # A nondecreasing map has its largest orbit at n.
        for i in range(1,n+1):
            curr=i
            for _ in range(depth): curr=f[curr-1]
            assert curr==1
        tally[f[-1]-1,depth]+=1
    return tally


def fibonacci(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def check():
    A=recurrence(32)
    tested=0
    # Independently enumerate all monotone maps for the smallest chains.
    for n in range(2,9):
        structurally=set()
        for bits in product((0,1),repeat=n-2):
            vals=[1,1]
            for bit in bits: vals.append(vals[-1]+bit)
            structurally.add(tuple(vals))
        independently=set()
        for vals in combinations_with_replacement(range(1,n+1),n):
            if all(vals[i] <= i+1 for i in range(n)) and all(vals[i+1]-vals[i]<=1 for i in range(n-1)) and vals[1]==1:
                independently.add(vals)
        assert structurally==independently, n
    for n in range(2,17):
        actual=direct(n)
        expected=Counter({(k,h):num for (size,k,h),num in A.items()
                          if size==n})
        assert actual==expected, (n,actual-expected,expected-actual)
        assert sum(actual.values())==2**(n-2)
        tested+=len(actual)
    for n in range(2,33):
        c=Counter({(k+1,h):num for (size,k,h),num in A.items()
                   if size==n})
        assert sum(c.values())==2**(n-2)
        assert sum(num for (r,h),num in c.items() if h<=2)==fibonacci(n)
        for r in range(1,n):
            cells={h for (rr,h),num in c.items() if rr==r and num}
            m=n-r
            low=(n-1+m-1)//m
            assert cells==set(range(low,r+1)),(n,r,cells,low)
            if r>=2:
                assert c[r,r]==n-r
            if r==1:
                assert c[r,1]==1
            for h in range(1,n):
                if h==2 and r>=2:
                    assert c[r,h]==binom(n-r,r-1)
        tested+=len(c)
    print('ALL_EXACT_CHECKS_PASSED', 'verified_cells=',tested,
          'bruteforce_n=2..16', 'recurrence_n=2..32')
    for n in (5,8,12):
        c=Counter()
        for (size,k,h),num in A.items():
            if size==n: c[h]+=num
        print('n=',n,'depth_histogram=', sorted(c.items()))

if __name__=='__main__':check()
