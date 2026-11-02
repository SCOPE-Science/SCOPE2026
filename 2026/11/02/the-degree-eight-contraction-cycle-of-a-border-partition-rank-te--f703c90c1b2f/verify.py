#!/usr/bin/env python3
"""Exact arithmetic checks for the displayed multilinear and cycle normalizations."""
from random import Random
from math import comb

def dot(u,v):
    return sum(x*y for x,y in zip(u,v))

def determinant(u,v,w):
    return (u[0]*(v[1]*w[2]-v[2]*w[1])
            -u[1]*(v[0]*w[2]-v[2]*w[0])
            +u[2]*(v[0]*w[1]-v[1]*w[0]))

def tensor(a,b,c,d):
    p=lambda u,v:dot(u,v)
    return (p(c,d)*(a[0]*b[1]-b[0]*a[1])
            +p(b,d)*(c[0]*a[1]-a[0]*c[1])
            +p(a,d)*(b[0]*c[1]-c[0]*b[1])
            +d[1]*(a[0]*p(b,c)+b[0]*p(a,c)+c[0]*p(a,b))
            +d[0]*(a[1]*p(b,c)+b[1]*p(a,c)+c[1]*p(a,b)))

def contracted(a,b,c,d):
    first=(a[0],b[0],c[0]); second=(a[1],b[1],c[1])
    q=(dot(b,c),dot(a,c),dot(a,b))
    ans=d[0]*dot(second,q)+d[1]*dot(first,q)
    for j in range(2,len(a)):
        ans+=d[j]*determinant(first,second,(a[j],b[j],c[j]))
    return ans

R=Random(20261020)
checks=0
for n in (5,6,7,9):
    for _ in range(60):
        a,b,c,d=([R.randint(-3,3) for j in range(n)] for k in range(4))
        assert tensor(a,b,c,d)==contracted(a,b,c,d)
        checks+=1
        s,t=R.randint(-3,3),R.randint(-3,3)
        v=[R.randint(-3,3) for j in range(3)]
        if s==t==0: t=1
        rows=[[R.randint(-3,3) for k in range(3)] for j in range(n-2)]
        aa=[s*v[0],t*v[0]]+[x[0] for x in rows]
        bb=[s*v[1],t*v[1]]+[x[1] for x in rows]
        cc=[s*v[2],t*v[2]]+[x[2] for x in rows]
        q=(dot(bb,cc),dot(aa,cc),dot(aa,bb))
        F=3*(s*s+t*t)*v[0]*v[1]*v[2]
        F+=sum(v[0]*x[1]*x[2]+v[1]*x[0]*x[2]+v[2]*x[0]*x[1] for x in rows)
        assert dot([s*x for x in v],q)==s*F
        assert dot([t*x for x in v],q)==t*F
        for x in rows: assert determinant([s*y for y in v],[t*y for y in v],x)==0
        checks+=1
# Projective cone over P1 x P2 has H(m)=(m+1)*C(m+2,2).
# Its leading coefficient is 1/2, hence projective degree 3.
assert (11+1)*comb(11+2,2)==936
assert 6*1//2==3
assert 3*3-1==8
print('VERIFY_OK',checks)
