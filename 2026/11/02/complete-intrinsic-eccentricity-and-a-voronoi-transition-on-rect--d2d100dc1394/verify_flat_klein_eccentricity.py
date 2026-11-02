#!/usr/bin/env python3
"""Exact rational tests for an intrinsic flat-Klein-bottle eccentricity formula.

No numerical optimization or external packages are required. This file is
supplementary finite testing; the universal statement has an analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations
import random


def inequalities(L, w, b):
    c = 2*w-b
    # All inequalities are A*x+B*y <= C for the lifted source's
    # Euclidean Voronoi cell around (0,0).
    return [
        (F(1), F(0), L), (-F(1), F(0), L),
        (F(0), F(1), w), (F(0), -F(1), w),
        (L, -b, (L*L+b*b)/2),
        (-L, -b, (L*L+b*b)/2),
        (L, c, (L*L+c*c)/2),
        (-L, c, (L*L+c*c)/2),
    ]


def rational_voronoi_vertices(L,w,b):
    cons=inequalities(L,w,b)
    out=set()
    for (a,d,e),(A,D,E) in combinations(cons,2):
        det=a*D-A*d
        if det==0: continue
        x=(e*D-E*d)/det
        y=(a*E-A*e)/det
        if all(aa*x+dd*y<=ee for aa,dd,ee in cons): out.add((x,y))
    return out


def theoretical_radius_squared(L,w,b):
    c=2*w-b
    T=b*c
    if T<=L*L:
        return w*w+((L*L-T)/(2*L))**2
    return ((c*c+L*L)/(2*c))**2


def test_exact():
    n=0
    for L in [F(1,5), F(1,3), F(1,2),F(1),F(3,2),F(2),F(3),F(5)]:
        for w in [F(1,5),F(1,3),F(1,2),F(1),F(3,2),F(2),F(3),F(5)]:
            for q in range(0,11):
                b=w*F(q,10)
                vs=rational_voronoi_vertices(L,w,b)
                assert 4 <= len(vs) <= 8,(L,w,b,len(vs))
                exact=max(x*x+y*y for x,y in vs)
                wanted=theoretical_radius_squared(L,w,b)
                assert exact==wanted,(L,w,b,exact,wanted,vs)
                n+=1
    # A nonendpoint critical case with T = L^2 exactly.
    L,w,b=F(3),F(5),F(1)
    vs=rational_voronoi_vertices(L,w,b)
    assert b*(2*w-b)==L*L and len(vs)==4 and theoretical_radius_squared(L,w,b)==w*w
    return n


def test_random_point_bound():
    rand=random.Random(771301)
    tested=0
    for _ in range(50):
        L=rand.uniform(.3,4)
        w=rand.uniform(.3,4)
        b=rand.uniform(0,w)
        R2=float(theoretical_radius_squared(F(L),F(w),F(b)))
        for _ in range(500):
            x=rand.uniform(0,2*L)
            y=rand.uniform(-w,w)
            # Nearest orbit points; extending by more periods cannot
            # decrease the distance below the global bound established
            # analytically from the Voronoi cell.
            closest=min((x-j*L)**2+(y-(2*k*w-(b if j%2 else 0)))**2
                        for j in range(-2,5) for k in range(-2,3))
            assert closest <= R2+1e-10,(L,w,b,x,y,closest,R2)
            tested+=1
    return tested


if __name__=='__main__':
    print('Exact rational covering-radius cases:',test_exact())
    print('Seeded direct orbit-distance tests:',test_random_point_bound())
    print('PASS: all finite checks; the general theorem is proved separately.')
