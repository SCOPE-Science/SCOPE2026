#!/usr/bin/env python3
"""Reproduce algebraic derivative identity and independent numerical diagnostics.
The infinite statement is proved in RESULT.md; finite diagnostics are not its proof.
Python standard library only.
"""
from fractions import Fraction as F
from math import sin, cos, pi, sqrt, isclose
from random import Random

# Polynomial arithmetic in independent indeterminates u,q.
def poly(*terms):
    return {k:F(v) for k,v in terms if v}
def C(v):return {(0,0):F(v)} if v else {}
def U():return {(1,0):F(1)}
def Q():return {(0,1):F(1)}
def add(a,b):
    c=a.copy()
    for k,v in b.items():
        c[k]=c.get(k,F(0))+v
        if not c[k]: del c[k]
    return c
def neg(a):return {k:-v for k,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    c={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():c[(i+k,j+l)]=c.get((i+k,j+l),F(0))+v*w
    return {k:v for k,v in c.items() if v}
def power(a,n):
    r=C(1)
    for _ in range(n):r=mul(r,a)
    return r
def deriv_q(a):return {(i,j-1):F(j)*v for (i,j),v in a.items() if j}

def ratio(x,y,z):
    sx,sy,sz=sin(x),sin(y),sin(z)
    S=sx+sy+sz
    return S*cos(x)*cos(y)*cos(z)/((sx+sy)*(sy+sz)*(sz+sx))

def main():
    u,q=U(),Q()
    c=sub(C(1),mul(C(2),power(u,2)))
    v2=sub(C(1),power(u,2))
    N=mul(add(mul(C(2),mul(u,q)),c),sub(power(q,2),power(u,2)))
    h=add(add(sub(power(q,2),v2),mul(C(2),mul(c,mul(u,q)))),power(c,2))
    D=mul(q,h)
    numerator=sub(mul(deriv_q(N),D),mul(N,deriv_q(D)))
    B=add(sub(mul(sub(mul(C(4),power(u,2)),C(1)),power(q,2)),mul(C(2),mul(u,q))),sub(mul(C(4),power(u,4)),mul(C(3),power(u,2))))
    asserted=mul(mul(c,power(sub(q,u),2)),B)
    assert numerator == asserted, 'exact polynomial derivative factorization failed'
    count=1
    for i in range(1,71):
        uu=F(i,100)
        if 2*uu*uu>=1:continue
        for j in range(1,101):
            qq=F(j,100)
            if qq*qq < 1-uu*uu:continue
            BB=(4*uu*uu-1)*qq*qq-2*uu*qq+4*uu**4-3*uu*uu
            assert BB<0,('sign',uu,qq,BB)
            count+=1
    rng=Random(20261028)
    for _ in range(1200):
        x,y,z=[rng.random() for k in range(3)]
        scale=(pi/2)/(x+y+z)
        x*=scale;y*=scale;z*=scale
        val=ratio(x,y,z)
        low=9*sqrt(3)/16
        assert low-3e-12 <= val < 1+3e-12,(x,y,z,val)
        sm=ratio((x+y)/2,(x+y)/2,z)
        assert sm <= val+3e-12,(x,y,z,val,sm)
        R=1.0
        th=[0,2*x,2*(x+y),pi,pi+2*x,pi+2*(x+y)]
        pts=[(cos(t),sin(t)) for t in th]
        area=0.5*sum(pts[i][0]*pts[(i+1)%6][1]-pts[(i+1)%6][0]*pts[i][1] for i in range(6))
        sides=[sqrt((pts[i][0]-pts[(i+1)%6][0])**2+(pts[i][1]-pts[(i+1)%6][1])**2) for i in range(6)]
        P=sum(sides)**2/4
        for a in sides:P*=sqrt(1-2*a/sum(sides))
        assert isclose(area/P,val,rel_tol=2e-11,abs_tol=2e-11),(val,area/P)
        count+=3
    print(f'PASS: polynomial identity; {count-1} exact sign and numerical diagnostics')

if __name__=='__main__':main()
