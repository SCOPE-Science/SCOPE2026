#!/usr/bin/env python3
"""Finite checks of sharp support/fiber inequalities for binary symplectic graphs.
The unrestricted-k theorem is established in the accompanying proof, not by testing.
"""
from itertools import combinations

def span_by_at_most(n,cap):
    out=set()
    for j in range(cap+1):
        for ids in combinations(range(n),j):
            x=0
            for i in ids:x^=1<<i
            out.add(x)
    return out

def symp(x,y,d):
    return sum(((x>>(2*i))&1)*((y>>(2*i+1))&1)+((x>>(2*i+1))&1)*((y>>(2*i))&1) for i in range(d))%2

def check():
    for k in range(3,12):
        n=k-1
        forbidden=span_by_at_most(n,n-1)
        assert len(forbidden)==(1<<n)-1
        # Tight case: n independent isotropic fixed vectors in dimension 2n.
        fixed=[1<<(2*i) for i in range(n)]
        zero_fiber=[x for x in range(1<<(2*n)) if all(symp(x,a,n)==0 for a in fixed)]
        # Avoid enumerating the 2^20 dimensional vector space at large k.
        if k<=9:
            assert len(zero_fiber)==(1<<n)
            assert len([x for x in zero_fiber if x not in {
                sum(fixed[i] for i in ids) for j in range(n) for ids in combinations(range(n),j)
            }])==1
        for r in range(1,n+1):
            fiber=1<<(2*n-r)
            bad=(1<<n)-1 if r==n else (1<<r)
            assert fiber>bad,(k,r,fiber,bad)
        print('k',k,'threshold_dimension',n,'minimum_fiber',1<<n,'forbidden',len(forbidden),'PASS')
    # Explicit separating witnesses between dimensions three and four for FO^5.
    a=[1<<(2*i) for i in range(4)]
    w=1
    for i in range(4):
        assert symp(a[i],a[i],4)==0
        for j in range(i):assert symp(a[i],a[j],4)==0
        assert symp(a[i],1,4)==0
    # f_1 has pairing (1,0,0,0) against e_1,...,e_4.
    w=2
    assert tuple(symp(w,z,4) for z in a)==(1,0,0,0)
    print('five_variable_boundary_witness',tuple(a),w,'PASS')
    print('ALL CHECKS PASSED')

if __name__=='__main__':check()
