#!/usr/bin/env python3
"""Independent polygon-clipping checks for a regular triangle/diamond intersection profile."""
import math
import random

ROOT3 = math.sqrt(3.0)
T = [(1.0, 0.0), (-0.5, ROOT3/2), (-0.5, -ROOT3/2)]


def cross(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])


def cut(poly, a, b):
    if not poly:
        return []
    new = []
    for i, p in enumerate(poly):
        q = poly[(i+1) % len(poly)]
        vp = cross(a,b,p)
        vq = cross(a,b,q)
        if vp >= -1e-14:
            new.append(p)
        if (vp < -1e-14 and vq > 1e-14) or (vp > 1e-14 and vq < -1e-14):
            w = vp/(vp-vq)
            new.append((p[0]+w*(q[0]-p[0]), p[1]+w*(q[1]-p[1])))
    return new


def area(poly):
    if len(poly) < 3:
        return 0.0
    return abs(sum(poly[i][0]*poly[(i+1)%len(poly)][1]-poly[(i+1)%len(poly)][0]*poly[i][1] for i in range(len(poly)))/2)


def overlap(r,t=0.0,u=0.0):
    q = [(t+r,u),(t,u+r),(t-r,u),(t,u-r)]
    poly = T[:]
    for j in range(4):
        poly=cut(poly,q[j],q[(j+1)%4])
    return area(poly)


def formula(r):
    lo=3*(ROOT3-1)/4
    hi=(3+ROOT3)/4
    if r<=lo:
        return 2*r*r
    if r<hi:
        return 3*ROOT3/4-ROOT3*(hi-r)**2
    return 3*ROOT3/4


def translation(r):
    lo=3*(ROOT3-1)/4
    hi=(3+ROOT3)/4
    if r<=lo:
        return max(0.0,r-0.5)
    if r>=hi:
        return (1-ROOT3)/4
    return (1+2*r*(1-ROOT3))/4


def check():
    rng=random.Random(24853)
    rad=[.05,.2,3*(ROOT3-1)/4,.55,.7,.9,1.,1.1,(3+ROOT3)/4,1.2,1.8]
    for r in rad:
        t=translation(r)
        val=overlap(r,t,0)
        assert abs(val-formula(r))<2e-11,(r,val,formula(r))
        for j in range(180):
            dx=(rng.random()-.5)*2.8
            dy=(rng.random()-.5)*2.8
            v=overlap(r,t+dx,dy)
            assert v<=formula(r)+2e-10,(r,dx,dy,v,formula(r))
    at_center=overlap(1,0,0)
    assert abs(at_center-(2*ROOT3-9/4))<2e-11
    assert overlap(1,translation(1),0)>at_center+0.025
    # Analytic strict local decrease verified against independently clipped areas.
    for r in [.6,.8,1.,1.15]:
        t=translation(r)
        for dx in [-.001,-.0001,.0001,.001]:
            v=overlap(r,t+dx,0)
            assert abs(v-(formula(r)-2*dx*dx))<1e-10,(r,dx,v)
    print('TRIANGLE_DIAMOND_PROFILE_OK radii=11 translations=1980 strict_local=16')


if __name__=='__main__':
    check()
