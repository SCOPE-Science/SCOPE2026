#!/usr/bin/env python3
"""Finite checks for rank/image-intersection strata of mutually annihilating square-zero matrices."""
from itertools import product
from collections import Counter

def add(a,b,q): return a^b if q==4 else (a+b)%q

def neg(a,q): return a if q==4 else (-a)%q

def mul(a,b,q):
    if q!=4:return a*b%q
    # Polynomial reduction modulo t²+t+1 over F_2.
    r=0
    for k in range(2):
        if (b>>k)&1:r^=a<<k
    if r&8:r^=0b1110 # x^3 + (x+1)x = x^3 + x^2 + x
    if r&4:r^=0b111 # x²+x+1
    return r

def rank(A,q):
    A=[list(row) for row in A];rows=len(A);cols=len(A[0]) if rows else 0
    r=0
    for j in range(cols):
        pivot=next((i for i in range(r,rows) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=next(x for x in range(1,q) if mul(x,A[r][j],q)==1)
        A[r]=[mul(v,inv,q) for v in A[r]]
        for i in range(rows):
            if i==r:continue
            factor=A[i][j]
            if factor:A[i]=[add(A[i][k],neg(mul(factor,A[r][k],q),q),q) for k in range(cols)]
        r+=1
        if r==rows:break
    return r

def matprod(A,B,q):
    n=len(A)
    return tuple(tuple(sum_prod([mul(A[i][k],B[k][j],q) for k in range(n)],q) for j in range(n)) for i in range(n))

def sum_prod(nums,q):
    x=0
    for v in nums:x=add(x,v,q)
    return x

def gaussian(n,k,q):
    if k<0 or k>n:return 0
    out=1
    num=1;den=1
    for i in range(k):num*=q**(n-i)-1;den*=q**(k-i)-1
    return num//den

def surj(d,r,q):
    if r>d:return 0
    v=1
    for j in range(r):v*=q**d-q**j
    return v

def formula(n,q,r,s,u):
    if min(r,s,u)<0 or u>min(r,s):return 0
    t=r+s-u; d=n-t
    if t>n:return 0
    return gaussian(n,r,q)*gaussian(r,u,q)*gaussian(n-r,s-u,q)*q**((r-u)*(s-u))*surj(d,r,q)*surj(d,s,q)

def check(n,q):
    z=tuple(tuple(0 for _ in range(n)) for _ in range(n))
    sq=[]
    for vec in product(range(q),repeat=n*n):
        A=tuple(vec[i*n:(i+1)*n] for i in range(n))
        if matprod(A,A,q)==z:sq.append((A,rank(A,q)))
    actual=Counter()
    for A,r in sq:
        for B,s in sq:
            if matprod(A,B,q)==z and matprod(B,A,q)==z:
                both=tuple(A[i]+B[i] for i in range(n))
                u=r+s-rank(both,q)
                actual[(r,s,u)]+=1
    expected={(r,s,u):formula(n,q,r,s,u) for r in range(n+1) for s in range(n+1) for u in range(min(r,s)+1) if formula(n,q,r,s,u)}
    assert dict(actual)==expected,(n,q,actual,expected)
    print('CHECK_OK n=%s q=%s square_zero=%s mutually_annihilating_pairs=%s strata=%s'%(n,q,len(sq),sum(actual.values()),len(actual)))

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]:check(n,q)
    print('VERIFY_OK')
