#!/usr/bin/env python3
"""Independent geometric and numerical checks for a polygonal volume-product identity.

The proof is analytical. These tests verify independent coordinate reconstructions,
transfer comparisons, and the local stability expansion for finite configurations.
"""
from __future__ import annotations
import math
import random

TOL = 3.0e-11
checks = 0


def close(a: float, b: float, atol: float = TOL) -> None:
    global checks
    assert abs(a-b) <= atol*max(1.0, abs(a), abs(b)), (a,b)
    checks += 1


def polygon_area(pts):
    return .5*abs(sum(x*y2-y*x2 for (x,y),(x2,y2) in zip(pts,pts[1:]+pts[:1])))


def normal_angles(n, gaps):
    alpha=2*math.pi/n
    rotations=[0.0]
    for x in gaps[:-1]:
        rotations.append(rotations[-1]+x)
    angles=sorted(j*alpha+t for j in range(n) for t in rotations)
    return angles


def geometric_areas(n, gaps):
    angles=normal_angles(n,gaps)
    nn=len(angles)
    pol=[(math.cos(x),math.sin(x)) for x in angles]
    v=[]
    for i,x in enumerate(angles):
        y=angles[(i+1)%nn]+(2*math.pi if i+1==nn else 0)
        half=(y-x)/2
        rad=1/math.cos(half)
        v.append((rad*math.cos((x+y)/2),rad*math.sin((x+y)/2)))
    return polygon_area(v), polygon_area(pol)


def analytic_areas(n, gaps):
    return n*sum(math.tan(g/2) for g in gaps), n*.5*sum(math.sin(g) for g in gaps)


def mahler(n,g):
    a,b=analytic_areas(n,g)
    return a*b


def test():
    global checks
    rng=random.Random(20261029)
    for n in (3,4,5,7,12):
        alpha=2*math.pi/n
        for k in (2,3,4,6):
            for it in range(120):
                raw=[rng.uniform(.05,2) for _ in range(k)]
                scale=alpha/sum(raw)
                g=[v*scale for v in raw]
                aa,bb=analytic_areas(n,g)
                a2,b2=geometric_areas(n,g)
                close(aa,a2)
                close(bb,b2)
                # The shape depends on cyclic placement; the product depends only on gaps.
                gp=g[:]
                rng.shuffle(gp)
                close(mahler(n,g),mahler(n,gp))
                # Strict transfer toward equality from a larger to a smaller gap.
                inds=sorted(range(k),key=lambda t:g[t])
                low,high=inds[0],inds[-1]
                d=(g[high]-g[low])*rng.uniform(.01,.49)
                h=g[:]
                h[high]-=d
                h[low]+=d
                assert mahler(n,h)>mahler(n,g), (n,k,g,h)
                checks += 1
                # Simultaneous verification of the pairwise derivative sign.
                t=sum(math.tan(z/2) for z in g)
                s=sum(math.sin(z) for z in g)
                dx=.5*s/(math.cos(g[high]/2)**2)+t*math.cos(g[high])
                dy=.5*s/(math.cos(g[low]/2)**2)+t*math.cos(g[low])
                assert dx<dy, (n,k,g,dx,dy)
                checks += 1
            # Sharp equal-gap upper and coincident-rotation lower limits.
            equal=[alpha/k]*k
            close(mahler(n,equal),(n*k*math.sin(math.pi/(n*k)))**2)
            corner=[alpha]+[0.0]*(k-1)
            close(mahler(n,corner),(n*math.sin(math.pi/n))**2)
            # Hessian coefficient on zero-sum tangent plane (analytic second order).
            v=[1,-1]+[0]*(k-2)
            center=mahler(n,equal)
            coef=n*n*k/4*math.cos(alpha/k)*math.tan(alpha/(2*k))**2*sum(x*x for x in v)
            for scale in (0.005,0.003,0.002):
                eps=scale*alpha/k
                gm=[g+eps*z for g,z in zip(equal,v)]
                gp=[g-eps*z for g,z in zip(equal,v)]
                observed=(2*center-mahler(n,gp)-mahler(n,gm))/(2*eps**2)
                # center - 0.5*(P(g+eps*v)+P(g-eps*v)) = coef*eps^2 + O(eps^4)
                close(observed,coef,atol=0.00003)
    print('PASS',checks,'independent numerical comparisons')

if __name__=='__main__':
    test()
