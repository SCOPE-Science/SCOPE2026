#!/usr/bin/env python3
"""Exhaustive direct-composition checks for commuting Catalan-monoid idempotents."""
from itertools import product
from math import isqrt

M0=((1,0,1),(0,1,0),(0,0,2))
M1=((1,1,0),(1,1,0),(1,0,0))

def predecessor(n, mask):
    s=[1]+[i+1 for i in range(1,n) if mask & (1<<(i-1))]
    return tuple(max(j for j in s if j<=i) for i in range(1,n+1))

def compose(a,b):
    return tuple(a[i-1] for i in b)

def predicted_gap(n,s_mask,t_mask):
    seen=0
    for i in range(2,n+1):
        s=bool(s_mask & (1<<(i-2)))
        t=bool(t_mask & (1<<(i-2)))
        if s and t:
            seen=0
        elif s and not t:
            if seen==2: return False
            seen=1
        elif t and not s:
            if seen==1: return False
            seen=2
    return True

def transfer_centralizer(n,s_mask):
    vec=(1,0,0)
    for i in range(2,n+1):
        m=M1 if (s_mask & (1<<(i-2))) else M0
        vec=tuple(sum(vec[j]*m[j][k] for j in range(3)) for k in range(3))
    return sum(vec)

def check():
    expected_previous=(1,4)
    total_checks=0
    prevprev=0
    prev=0
    for n in range(1,11):
        maps=[predecessor(n,k) for k in range(1<<(n-1))]
        direct_total=0
        for s,a in enumerate(maps):
            comm_s=0
            for t,b in enumerate(maps):
                commutes=(compose(a,b)==compose(b,a))
                assert commutes==predicted_gap(n,s,t),(n,s,t)
                comm_s+=commutes
                direct_total+=commutes
                total_checks+=1
            assert comm_s==transfer_centralizer(n,s),(n,s,comm_s,transfer_centralizer(n,s))
        if n==1: assert direct_total==1
        elif n==2: assert direct_total==4
        else: assert direct_total==4*prev-2*prevprev,(n,direct_total,prev,prevprev)
        prevprev,prev=prev,direct_total
        print('n',n,'commuting ordered pairs',direct_total)
    assert total_checks==349525,total_checks
    print('ALL_CATALAN_IDEMPOTENT_COMMUTATION_TESTS_PASSED',total_checks)

if __name__=='__main__': check()
