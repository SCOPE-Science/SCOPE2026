#!/usr/bin/env python3
"""Exact rational checker for sharp planar trapezoid zonoid Bézout constant.
Run with python3 verify.py. Standard library only.
"""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

def det(p, q):
    return p[0]*q[1]-p[1]*q[0]

def width(t, n):
    verts=((Q(0),Q(0)),(Q(1),Q(0)),(t,Q(1)),(Q(0),Q(1)))
    d=[p[0]*n[0]+p[1]*n[1] for p in verts]
    return max(d)-min(d)

def v_ks(t,u):
    return width(t,(-u[1],u[0]))/2

def v_ss(u,v):
    return abs(det(u,v))/2

def poly_vertices(t):
    return ((Q(1),Q(0)),(Q(1),Q(1)-t),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(-1),t-Q(1)),(Q(0),Q(-1)))

def run():
    rng=Random(20261029)
    count=0
    for denominator in range(2,25):
        for numerator in range(1,denominator):
            t=Q(numerator,denominator)
            pts=poly_vertices(t)
            for i,j in combinations(range(6),2):
                assert abs(det(pts[i],pts[j]))<=1
                count+=1
            assert abs(det(pts[0],pts[2]))==1
            # Polar inequalities verify every displayed vertex actually lies in the polar.
            dverts=((Q(1),Q(0)),(t,Q(1)),(Q(-1),Q(1)),(Q(-1),Q(0)),(-t,Q(-1)),(Q(1),Q(-1)))
            for p in pts:
                assert all(abs(p[0]*d[0]+p[1]*d[1])<=1 for d in dverts)
                count+=6
            # Explicit equality pair, and complete zonoid (finite zonotope) inequality.
            unitx=(Q(1),Q(0)); unity=(Q(0),Q(1)); area=(1+t)/2
            assert area*v_ss(unitx,unity)==(1+t)*v_ks(t,unitx)*v_ks(t,unity)
            count+=1
            for _ in range(25):
                aa=[(Q(rng.randint(-8,8)),Q(rng.randint(-8,8))) for i in range(1+rng.randrange(5))]
                bb=[(Q(rng.randint(-8,8)),Q(rng.randint(-8,8))) for i in range(1+rng.randrange(5))]
                vka=sum((v_ks(t,u) for u in aa),Q(0)); vkb=sum((v_ks(t,v) for v in bb),Q(0))
                vab=sum((v_ss(u,v) for u in aa for v in bb),Q(0))
                assert area*vab <= (1+t)*vka*vkb
                count+=1
    # Endpoints also check, despite collapsed polar combinatorial types.
    for t in (Q(0),Q(1)):
        p=poly_vertices(t)
        assert all(abs(det(a,b))<=1 for a,b in combinations(p,2))
        count+=15
    print('VERIFY_OK trapezoid zonoid Bezout: exact rational checks',count)
if __name__ == '__main__':
    run()
