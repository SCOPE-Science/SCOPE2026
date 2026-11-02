#!/usr/bin/env python3
"""Exact finite tests for Chebyshev radii of maximum-norm hyperplanes."""
from fractions import Fraction as F
from itertools import product
import random


def fixed_radius(weights, points):
    """Compute exact Chebyshev radius through the interval-feasibility test."""
    assert points and all(len(p) == len(weights) for p in points)
    n = len(weights)
    assert all(sum(weights[i]*p[i] for i in range(n)) == 0 for p in points)
    W = sum(weights)
    assert W > 0 and all(w >= 0 for w in weights)
    hi = [max(p[i] for p in points) for i in range(n)]
    lo = [min(p[i] for p in points) for i in range(n)]
    diameter = max(hi[i]-lo[i] for i in range(n))
    return (max(diameter/F(2), sum(weights[i]*hi[i] for i in range(n))/W,
                -sum(weights[i]*lo[i] for i in range(n))/W), diameter)


def center_feasible(weights, points, radius):
    """Independent exact weighted-interval intersection test."""
    n=len(weights)
    lower=[]; upper=[]
    for i in range(n):
        m=max(p[i] for p in points)
        M=min(p[i] for p in points)
        lower.append(m-radius)
        upper.append(M+radius)
    return (all(l<=u for l,u in zip(lower,upper)) and
            sum(w*l for w,l in zip(weights,lower)) <= 0 <=
            sum(w*u for w,u in zip(weights,upper)))


def witness(weights):
    j=max(range(len(weights)), key=lambda i: weights[i])
    pts=[[F(0)]*len(weights)]
    for i in range(len(weights)):
        if i==j: continue
        z=[F(0)]*len(weights)
        z[i]=F(1)
        z[j]=-weights[i]/weights[j]
        pts.append(z)
    return pts


def exercise():
    rng=random.Random(479106)
    checks=0
    for n in range(2,10):
        for case in range(300):
            weights=[F(rng.randint(0,12)) for _ in range(n)]
            if not any(weights): weights[0]=F(1)
            j=max(range(n),key=lambda i: weights[i])
            W=sum(weights)
            expected=max(F(1,2), F(1)-weights[j]/W)
            wpts=witness(weights)
            r,d=fixed_radius(weights,wpts)
            assert d==1 and r==expected,(weights,r,expected)
            checks+=1
            for t in range(7):
                points=[]
                for k in range(1+rng.randrange(5)):
                    vec=[F(rng.randint(-10,10),rng.randint(1,7)) for _ in range(n)]
                    vec[j]=-sum(weights[i]*vec[i] for i in range(n) if i!=j)/weights[j]
                    points.append(vec)
                exact,D=fixed_radius(weights,points)
                if D:
                    assert exact<=expected*D,(n,weights,exact,D,expected)
                assert center_feasible(weights,points,exact)
                assert not center_feasible(weights,points,exact-F(1,100000))
                checks+=3
    print('PASS:',checks,'exact rational tests with all coefficient-degenerate cases')

if __name__=='__main__': exercise()
