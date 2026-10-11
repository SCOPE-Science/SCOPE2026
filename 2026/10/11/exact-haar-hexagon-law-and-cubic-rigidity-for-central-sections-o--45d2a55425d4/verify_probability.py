#!/usr/bin/env python3
"""Independent finite checks for the box central-section six-face probability law.
The finite checks supplement, and do not replace, the analytic proof.
"""
from math import acos, atan, pi, sqrt, asin
from random import Random


def dot(x, y):
    return sum(s*t for s, t in zip(x, y))

def norm(x):
    return sqrt(dot(x, x))

def unit(x):
    d=norm(x)
    return tuple(t/d for t in x)

def sub(x, y):
    return tuple(a-b for a,b in zip(x,y))

def scale(t, x):
    return tuple(t*v for v in x)

def angle_at(p, q, r):
    # Spherical interior angle at p: project q and r into tangent plane.
    v=unit(sub(q,scale(dot(p,q),p)))
    w=unit(sub(r,scale(dot(p,r),p)))
    return acos(max(-1.,min(1.,dot(v,w))))

def exact_formula(a,b,c):
    alpha=sqrt(a*a+b*b); beta=sqrt(a*a+c*c); gamma=sqrt(b*b+c*c)
    den=alpha*beta*gamma+b*c*gamma+a*c*beta+a*b*alpha
    return 4/pi * atan(2*a*b*c/den)

def spherical_excess_formula(a,b,c):
    p=unit((b,a,0.)); q=unit((c,0.,a)); r=unit((0.,c,b))
    area=angle_at(p,q,r)+angle_at(q,r,p)+angle_at(r,p,q)-pi
    return 2*area/pi

rng=Random(20261009)
# Two geometrically unrelated integrations: spherical triangle excess vs triple product.
for j in range(400):
    a,b,c=(10**rng.uniform(-0.6,0.6) for k in range(3))
    p=exact_formula(a,b,c); q=spherical_excess_formula(a,b,c)
    assert abs(p-q)<1e-11, (j,a,b,c,p,q)
    assert 0<p<=4/pi*atan(sqrt(2)/5)+1e-12

# The known closed expression for the cube provides a stringent normalization check.
peak=4/pi*atan(sqrt(2)/5)
assert abs(peak-(1-6/pi*asin(1/3)))<1e-13
assert abs(exact_formula(1,1,1)-peak)<1e-14

# Gaussian directions give Haar-spherical normals; compare random-face counts.
for a,b,c in [(1.,1.,1.), (2.,1.,1.), (1.,2.,3.), (10.,1.,1.)]:
    n=180000
    hit=0
    for _ in range(n):
        x,y,z=(abs(rng.gauss(0,1)) for k in range(3))
        x*=a; y*=b; z*=c
        if x<y+z and y<x+z and z<x+y:
            hit+=1
    observed=hit/n
    predicted=exact_formula(a,b,c)
    assert abs(observed-predicted)<0.008, (a,b,c,observed,predicted)
    print('box',a,b,c,'exact',round(predicted,9),'sample',round(observed,9))

# Two scale invariance and sharp upper bound sanity tests.
for j in range(200):
    a,b,c=(10**rng.uniform(-2,2) for k in range(3))
    l=10**rng.uniform(-2,2)
    assert abs(exact_formula(a,b,c)-exact_formula(l*a,l*b,l*c))<1e-13
    alpha=sqrt(a*a+b*b);beta=sqrt(a*a+c*c);gamma=sqrt(b*b+c*c)
    den=alpha*beta*gamma+b*c*gamma+a*c*beta+a*b*alpha
    assert den/(a*b*c)>=5*sqrt(2)-1e-12
print('VERIFY_OK: spherical excess 400; Haar Gaussian 720000; sharp bound 200; scale 200.')
