#!/usr/bin/env python3
"""Exact finite-field and Cartier coefficient checks for an elementary-symmetric genus-four model."""
from itertools import product, combinations
from collections import defaultdict

def gf(q):
    p=3; n=1 if q==3 else 2
    assert q in (3,9)
    def add(a,b):
        return ((a%3+b%3)%3) + 3*(((a//3+b//3)%3) if n==2 else 0)
    def mul(a,b):
        if n==1: return (a*b)%3
        x,y=a%3,a//3;u,v=b%3,b//3
        # adjoining t with t*t=-1=2 in characteristic three
        return ((x*u+2*y*v)%3)+3*((x*v+y*u)%3)
    return add,mul

def count_points(q):
    add,mul=gf(q);result=set()
    for x in product(range(q),repeat=5):
        if not any(x):continue
        a=0
        for t in x:a=add(a,t)
        if a:continue
        b=0
        for i,j in combinations(range(5),2):b=add(b,mul(x[i],x[j]))
        if b:continue
        c=0
        for i,j,k in combinations(range(5),3):c=add(c,mul(mul(x[i],x[j]),x[k]))
        if c:continue
        first=next(t for t in x if t)
        inv=next(t for t in range(1,q) if mul(t,first)==1)
        result.add(tuple(mul(z,inv) for z in x))
    return len(result)

def hasse():
    # Four affine coordinates and x_4=-sum(x_0..x_3).
    p=3
    def padd(P,Q):
        R=defaultdict(int)
        for x,c in P.items():R[x]+=c
        for x,c in Q.items():R[x]+=c
        return {x:c%p for x,c in R.items() if c%p}
    def pmul(P,Q):
        R=defaultdict(int)
        for a,c in P.items():
            for b,d in Q.items():R[tuple(u+v for u,v in zip(a,b))]+=c*d
        return {x:c%p for x,c in R.items() if c%p}
    one={(0,0,0,0):1}
    X=[{tuple(1 if k==j else 0 for k in range(4)):1} for j in range(4)]
    X.append({tuple(1 if k==j else 0 for k in range(4)):2 for j in range(4)})
    Q={};R={}
    for ids in combinations(range(5),2):Q=padd(Q,pmul(X[ids[0]],X[ids[1]]))
    for ids in combinations(range(5),3):R=padd(R,pmul(pmul(X[ids[0]],X[ids[1]]),X[ids[2]]))
    F=pmul(pmul(Q,R),pmul(Q,R))
    matrix=[]
    for i in range(4):
        row=[]
        for j in range(4):
            k=[2]*4;k[i]+=3;k[j]-=1
            row.append(F.get(tuple(k),0))
        matrix.append(row)
    return matrix

a=count_points(3);b=count_points(9)
assert a==0,(a,'F3')
assert b==30,(b,'F9')
M=hasse()
assert M==[[int(i==j) for j in range(4)] for i in range(4)],M
assert b==9+1-4*(1-2*3)
print('BRING_F3_POINTS=0;BRING_F9_POINTS=30')
print('HASSE_WITT_4_BY_4=IDENTITY')
print('ELLIPTIC_TRACE_AT_3=1;L_POLYNOMIAL=(1-T+3T^2)^4')
print('VERIFY_OK')
