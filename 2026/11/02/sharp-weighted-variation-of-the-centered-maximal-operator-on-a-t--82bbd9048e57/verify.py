#!/usr/bin/env python3
"""Exact-rational checks for a weighted three-vertex centered maximal operator."""
from fractions import Fraction as F
from itertools import product

def row_gain(h,u,v,x,y):
    W=h+u+v
    H=(u*x+v*y)/W
    a=u/(h+u); b=v/(h+v)
    Mc=max(F(0),H)
    Ma=max(x,a*x,H)
    Mb=max(y,b*y,H)
    return abs(Ma-Mc)+abs(Mb-Mc)

def boundary_rays(h,u,v):
    W=h+u+v
    a=u/(h+u); b=v/(h+v)
    lines=[(F(1),F(0)),(F(0),F(1)),(u,v),
           (u-W,v),(u,v-W),(u-W*a,v),(u,v-W*b)]
    for p,q in lines:
        if not (p or q): continue
        for sign in (-1,1):
            yield (sign*q/(abs(p)+abs(q)),
                   -sign*p/(abs(p)+abs(q)))

def claimed(h,u,v):
    U=max(u,v); L=min(u,v)
    positive=1-L/(h+u+v)
    negative=U*(h+2*L)/((h+2*U)*(h+L))
    return max(positive,negative)

def run():
    amounts=[F(1,10),F(1,3),F(1),F(2),F(5),F(13)]
    checks=0
    for h,u,v in product(amounts,repeat=3):
        best=max(row_gain(h,u,v,x,y) for x,y in boundary_rays(h,u,v))
        assert best==claimed(h,u,v),(h,u,v,best,claimed(h,u,v))
        checks+=1
        # Explicit positive-leaf and negative two-leaf extremizers.
        U=max(u,v);L=min(u,v)
        a=U/(h+U)
        s=1/(1+a); t=a/(1+a)
        xp,yp=(F(1),F(0)) if u==L else (F(0),F(1))
        assert row_gain(h,u,v,xp,yp)==1-L/(h+u+v)
        xn,yn=(-s,-t) if u==U else (-t,-s)
        assert row_gain(h,u,v,xn,yn)==U*(h+2*L)/((h+2*U)*(h+L))
        checks+=2
    assert claimed(F(1),F(1),F(1))==F(2,3)
    assert claimed(F(1,100),F(1),F(1))==F(100,101)
    print('PASS:',checks+2,'exact-rational formula, extremizer, and benchmark checks')
if __name__=='__main__':run()
