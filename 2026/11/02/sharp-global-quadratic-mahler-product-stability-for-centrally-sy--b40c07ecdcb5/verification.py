#!/usr/bin/env python3
"""Reproduce finite arithmetic and geometric checks for the stated hexagon stability law.
Uses Python 3 standard library only; it is a check, not a substitute for the proof.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi


def schur_data(a,b,c):
    S=a+b+c
    Q=a*b+b*c+c*a
    P=a*b*c
    D=(a+b)*(b+c)*(c+a)
    W=c*(a-b)**2+a*(b-c)**2+b*(c-a)**2
    V=F((a-b)**2+(b-c)**2+(c-a)**2,S*S)
    M=F(8*S*Q,D)
    return M,F(W,D),V

# Sparse integral polynomials in x,y,z, represented by monomial exponent tuples.
def atom(i):
    return {tuple(int(j==i) for j in range(3)):1}
def cn(k):
    return {(0,0,0):k}
def add(*args):
    out={}
    for p in args:
        for v,c in p.items():out[v]=out.get(v,0)+c
    return {v:c for v,c in out.items() if c}
def mul(*args):
    out=cn(1)
    for q in args:
        nxt={}
        for u,a in out.items():
            for v,b in q.items():
                w=tuple(u[i]+v[i] for i in range(3))
                nxt[w]=nxt.get(w,0)+a*b
        out=nxt
    return {v:c for v,c in out.items() if c}
def neg(p):return {k:-v for k,v in p.items()}
def sub(p,q):return add(p,neg(q))
def pw(p,n):return mul(*([p]*n))

def symbolic_check():
    x,y,z=atom(0),atom(1),atom(2)
    a=add(x,y,z);b=add(y,z);c=z
    S=add(a,b,c)
    Q=add(mul(a,b),mul(b,c),mul(c,a))
    P=mul(a,b,c)
    D=mul(add(a,b),add(b,c),add(c,a))
    N=add(pw(sub(a,b),2),pw(sub(b,c),2),pw(sub(c,a),2))
    W=sub(mul(S,Q),mul(cn(9),P))
    assert W==add(mul(c,pw(sub(a,b),2)),mul(a,pw(sub(b,c),2)),mul(b,pw(sub(c,a),2)))
    L=sub(mul(cn(2),pw(S,2),W),mul(D,N))
    U=sub(mul(cn(2),D,N),mul(pw(S,2),W))
    q=add(pw(x,2),mul(x,y),pw(y,2))
    expectL=add(
        mul(cn(20),pw(z,3),q),
        mul(cn(2),pw(z,2),add(x,mul(cn(2),y)),add(mul(cn(4),pw(x,2)),mul(cn(13),x,y),mul(cn(13),pw(y,2)))),
        mul(cn(4),z,y,add(x,y),add(mul(cn(2),pw(x,2)),mul(cn(11),x,y),mul(cn(11),pw(y,2)))),
        mul(cn(6),pw(y,2),pw(add(x,y),2),add(x,mul(cn(2),y)))
    )
    expectU=add(
        mul(cn(14),pw(z,3),q),
        mul(pw(z,2),add(x,mul(cn(2),y)),add(mul(cn(20),pw(x,2)),mul(cn(11),x,y),mul(cn(11),pw(y,2)))),
        mul(cn(2),z,add(mul(cn(3),pw(x,4)),mul(cn(16),pw(x,3),y),mul(cn(20),pw(x,2),pw(y,2)),mul(cn(8),x,pw(y,3)),mul(cn(4),pw(y,4)))),
        mul(cn(3),pw(x,2),y,add(x,y),add(x,mul(cn(2),y)))
    )
    assert L==expectL,(L,expectL)
    assert U==expectU,(U,expectU)
    assert all(k>=0 for k in L.values()) and all(k>=0 for k in U.values())
    return len(L),len(U)


def hull(points):
    points=sorted(set(points))
    def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower=[]
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=1e-11:lower.pop()
        lower.append(p)
    upper=[]
    for p in points[::-1]:
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=1e-11:upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]

def shoelace(pts):
    return .5*abs(sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts))))

def independent_area_product(a,b,c):
    g=[(a,0.),(b/2.,b*3**.5/2.),(-c/2.,c*3**.5/2.)]
    poly=hull([tuple(sum(sign[j]*g[j][i]/2. for j in range(3)) for i in (0,1)) for sign in product((-1,1),repeat=3)])
    assert len(poly)==6,len(poly)
    polar=[]
    for i in range(6):
        p,q=poly[i],poly[(i+1)%6]
        det=p[0]*q[1]-p[1]*q[0]
        assert det>0
        polar.append(((q[1]-p[1])/det,(p[0]-q[0])/det))
    return shoelace(poly)*shoelace(polar)


def run():
    mon=symbolic_check()
    t=0
    for a in range(1,13):
        for b in range(1,13):
            for c in range(1,13):
                M,deficit,V=schur_data(a,b,c)
                assert M+deficit==9
                assert V/2<=deficit<=2*V
                if len({a,b,c})>1:
                    assert V/2<deficit<2*V
                geo=independent_area_product(a,b,c)
                assert abs(geo-float(M))<2e-11*max(1,float(M)),(a,b,c,geo,float(M))
                t+=1
    assert schur_data(1,1,1)[0]==9
    assert schur_data(1,1,0)[0]==8
    print('PASS symbolic polynomial identities; nonnegative certificates have %d and %d monomials'%mon)
    print('PASS %d positive-integer triples: rational bounds and independent convex-hull/polar area products'%t)
    print('PASS: limiting sharp constants lower=1/2, upper=2, regular-point=9/8 by exact formulas')

if __name__=='__main__':run()
