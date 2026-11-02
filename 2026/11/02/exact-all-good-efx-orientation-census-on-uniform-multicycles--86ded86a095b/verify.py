#!/usr/bin/env python3
"""Exact EFX multicycle census verifier; Python 3 standard library only."""
from itertools import product
from math import comb
from collections import Counter

def is_efx_direct(n,q,mask):
    # Good (edge i, copy t) is valued by vertex i and vertex (i+1) mod n.
    bundles=[[] for _ in range(n)]
    for i in range(n):
        for t in range(q):
            owner=(i+((mask>>(q*i+t))&1))%n
            bundles[owner].append(i)
    for a in range(n):
        own=sum(e==a or e==(a-1)%n for e in bundles[a])
        for b in range(n):
            if a==b: continue
            others=bundles[b]
            other_value=sum(e==a or e==(a-1)%n for e in others)
            for e in others:
                if own < other_value-int(e==a or e==(a-1)%n):
                    return False
    return True

def matrix(q):
    states=list(product(range(q+1),repeat=2))
    at={s:i for i,s in enumerate(states)}
    T=[[0]*len(states) for _ in states]
    for a,b in states:
        for c in range(q+1):
            if c <= 2*b + int(a==0) and 2*b <= a + q + int(c==q):
                T[at[(a,b)]][at[(b,c)]]=comb(q,c)
    return T

def mul(A,B):
    m=len(A)
    BT=list(zip(*B))
    return [[sum(a*b for a,b in zip(row,col)) for col in BT] for row in A]

def matpow(T,n):
    m=len(T)
    R=[[int(i==j) for j in range(m)] for i in range(m)]
    while n:
        if n&1:R=mul(R,T)
        T=mul(T,T)
        n//=2
    return R

def trace(T):
    return sum(T[i][i] for i in range(len(T)))

def charpoly(T):
    # Newton identities, returning det(I-zT) coefficient list.
    n=len(T)
    power=T
    traces=[]
    for _ in range(n):
        traces.append(trace(power))
        power=mul(power,T)
    c=[1]
    for k in range(1,n+1):
        x=-sum(c[k-j]*traces[j-1] for j in range(1,k+1))
        assert x%k==0
        c.append(x//k)
    return c

def poly_mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]+=v*w
    return z

def weighted_transfer_census(n,q):
    return trace(matpow(matrix(q),n))

def direct_census(n,q):
    return sum(is_efx_direct(n,q,mask) for mask in range(1<<(n*q)))

def main():
    checks=0; profiles=0
    for q,n_max in [(1,10),(2,8),(3,6),(4,4),(5,3)]:
        for n in range(3,n_max+1):
            d=direct_census(n,q)
            t=weighted_transfer_census(n,q)
            assert d==t,(n,q,d,t)
            profiles+=1<<(n*q)
            checks+=1
    for q,expected in [(1,poly_mul([1,-1,-1],[1,-1,1])),
                       (2,poly_mul([1,0,1],[1,-4,4,-2])+[0]*4),
                       (3,poly_mul([1,-1],[1,-7,6,-6])+[0]*12)]:
        assert charpoly(matrix(q))==expected,(q,charpoly(matrix(q)),expected)
    assert [weighted_transfer_census(n,2) for n in range(3,9)]==[22,66,184,522,1488,4226]
    assert [weighted_transfer_census(n,3) for n in range(3,7)]==[236,1466,9068,56090]
    print('VERIFY_OK direct_cases=%d exhaustive_orientations=%d charpoly_cases=3' %(checks,profiles))
    for q in [2,3]:
        print('q=%d n=3..8 counts='%q,[weighted_transfer_census(n,q) for n in range(3,9)])

if __name__=='__main__':main()
