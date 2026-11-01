#!/usr/bin/env python3
"""Exact-rational verification of boundary radial moment identities on parallelograms.

Supplementary finite tests, not a proof for all real shapes or convex weights.
"""
from fractions import Fraction as F
from random import Random
from math import isclose


def add(p, q):
    out=[F(0)]*max(len(p), len(q))
    for i,v in enumerate(p): out[i]+=v
    for i,v in enumerate(q): out[i]+=v
    return out


def mul(p, q):
    out=[F(0)]*(len(p)+len(q)-1)
    for i,u in enumerate(p):
        for j,v in enumerate(q): out[i+j]+=u*v
    return out


def poly_power(p,k):
    out=[F(1)]
    for _ in range(k): out=mul(out,p)
    return out


def radial_moment(a,b,t,k):
    r"""\int_boundary |x|^(2k) ds; u=(a,0), v=b((1-t^2),(2t))/(1+t^2)."""
    cs=(1-t*t)/(1+t*t)
    sn=2*t/(1+t*t)
    u=(a,F(0));v=(b*cs,b*sn)
    # Four edges, two parallel to u (length 2a), two to v (length 2b).
    vs=[(u[0]+v[0],u[1]+v[1]), (-u[0]+v[0],-u[1]+v[1]),
        (-u[0]-v[0],-u[1]-v[1]), (u[0]-v[0],u[1]-v[1])]
    total=F(0)
    for i in range(4):
        x,y=vs[i];xx,yy=vs[(i+1)%4]
        dx=xx-x;dy=yy-y
        length=2*a if i%2==0 else 2*b
        r2=[x*x+y*y,2*(x*dx+y*dy),dx*dx+dy*dy]
        p=poly_power(r2,k)
        total+=length*sum((v/F(j+1) for j,v in enumerate(p)),F(0))
    return total


def run():
    rng=Random(20261029)
    count=0
    eq=0
    for _ in range(300):
        a=F(rng.randint(1,15),rng.randint(1,8))
        b=F(rng.randint(1,15),rng.randint(1,8))
        t=F(rng.randint(1,20),rng.randint(1,20))
        s=a+b;L=4*s
        sn=2*t/(1+t*t)
        A=4*a*b*sn
        E0=radial_moment(a,b,t,0)
        E2=radial_moment(a,b,t,1)
        E4=radial_moment(a,b,t,2)
        E6=radial_moment(a,b,t,3)
        Es4=radial_moment(s/2,s/2,F(1),2)
        Es6=radial_moment(s/2,s/2,F(1),3)
        assert E0==L
        assert E2==L**3/48
        assert E4==L**5/1280-L*A*A/12
        assert E4-Es4==L*(L**4/256-A*A)/12
        assert E4>=Es4
        assert E6>=Es6
        is_square=(a==b and t==1)
        assert (E4==Es4)==is_square
        if is_square:eq+=1
        count+=1
    for a,b,t in [(F(1),F(1),F(1)),(F(2),F(2),F(1)),(F(3),F(3),F(1)),(F(1),F(2),F(1)),(F(1),F(1),F(2))]:
        s=a+b; L=4*s; sn=2*t/(1+t*t); A=4*a*b*sn
        assert radial_moment(a,b,t,2)==L**5/1280-L*A*A/12
        assert (radial_moment(a,b,t,2)==radial_moment(s/2,s/2,F(1),2))==(a==b and t==1)
        count+=1
    print(f'EXACT_CHECK_OK systems={count} E0 E2 E4 area-deficit E6 convex-power equality; square_cases={eq+3}')


if __name__=='__main__': run()
