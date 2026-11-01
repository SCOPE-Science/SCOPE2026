#!/usr/bin/env python3
"""Reproduce exact and probabilistic checks for the centered tetrahedral section-radius law.

Python 3.10+ standard library only.  Assertions are not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product
from math import acos, atan2, pi, sqrt, isclose
from random import Random

VERTICES = ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))


def exact_radius2(normal):
    h = [sum(normal[j]*v[j] for j in range(3)) for v in VERTICES]
    pos = [i for i in range(4) if h[i] > 0]
    neg = [j for j in range(4) if h[j] < 0]
    if not pos or not neg:
        raise ValueError('Plane must meet all sides of origin-containing tetrahedron')
    vals = []
    for i in pos:
        for j in neg:
            p, q = h[i], -h[j]
            x = [F(q*VERTICES[i][k] + p*VERTICES[j][k], p+q) for k in range(3)]
            actual = sum(z*z for z in x)
            predicted = F(3) - F(8*p*q, (p+q)**2)
            assert actual == predicted
            vals.append(actual)
    return max(vals), len(pos)*len(neg), h


def law(r):
    """(quadrilateral, triangular) sub-CDFs for the standard tetrahedron."""
    if r <= 1.0:
        return (0.0, 0.0)
    if r >= sqrt(3):
        # Limit formula retained for normalization checks.
        r = sqrt(3)
    s = sqrt((r*r-1)/2)
    a, b = sqrt(2)*s/(1+s), s/sqrt(2)
    M, N = sqrt(1+a*a), sqrt(1+2*b*b)
    phi = atan2(a*b, M*N+M+N+1+a*b)
    q = 24*phi/pi
    t = 0.0 if s <= 0.5 else 2*(3*acos(max(-1,min(1,s*(2-s)/(1+2*s*s))))-pi)/pi
    return q, t


def exact_sign_threshold(normal, s):
    R2, vcount, h = exact_radius2(normal)
    k = F(1-s, 1+s) if isinstance(s, int) else (1-s)/(1+s)
    pairs = [(h[i], -h[j]) for i in range(4) if h[i]>0 for j in range(4) if h[j]<0]
    event = all(k*q <= p and k*p <= q for p,q in pairs)
    return event, R2<=1+2*s*s


def run():
    count = 0
    # Exact integer/rational comparisons of all geometric vertices and ratio cutoffs.
    for xyz in product(range(-5,6), repeat=3):
        if xyz == (0,0,0):
            continue
        if not all(sum(xyz[k]*v[k] for k in range(3)) != 0 for v in VERTICES):
            continue
        R2, nv, heights = exact_radius2(xyz)
        assert 1 <= R2 <= 3
        assert nv in (3,4)
        for s in (F(0), F(1,8),F(1,4), F(1,2),F(3,5),F(4,5), F(1)):
            A,B = exact_sign_threshold(xyz,s)
            assert A == B
            count += 1
    # Verify cone solid-angle identities directly from 4D ray Gram matrices.
    for s in (0.51,0.57,0.62,0.75,0.9,1.0):
        k = (1-s)/(1+s)
        A = 1-2*k
        w1=(1,-A,-k,-k)
        w2=(1,-k,-A,-k)
        d=sum(a*b for a,b in zip(w1,w2))
        n1=sqrt(sum(a*a for a in w1))
        cosedge=d/n1**2
        cosang=cosedge/(1+cosedge)
        target=s*(2-s)/(1+2*s*s)
        assert abs(cosang-target)<3e-14
        count += 1
    # Spherical-triangle area computed with independent normalized rays.
    for s in (0.05,0.2,0.5,0.7,0.85,1.0):
        a,b=sqrt(2)*s/(1+s),s/sqrt(2)
        c=(0.,0.,1.)
        v=(a,0.,1.)
        w=(b,b,1.)
        norms=[sqrt(sum(t*t for t in z)) for z in (c,v,w)]
        V=[tuple(x/n for x in z) for z,n in zip((c,v,w),norms)]
        dot=lambda u,z: sum(x*y for x,y in zip(u,z))
        omega=2*atan2(abs(V[1][0]*V[2][1]-V[1][1]*V[2][0]),1+dot(V[0],V[1])+dot(V[1],V[2])+dot(V[2],V[0]))
        formula=2*atan2(a*b,sqrt(1+a*a)*sqrt(1+2*b*b)+sqrt(1+a*a)+sqrt(1+2*b*b)+1+a*b)
        assert abs(omega-formula)<1e-13
        count += 1
    assert law(sqrt(3))[0]+law(sqrt(3))[1] > 1-1e-12
    assert abs(sum(law(sqrt(3)))-1)<1e-12
    assert law(sqrt(1.5))[1]==0
    assert abs(law(sqrt(1.5))[0]-0.275100171205)<2e-8
    # Unbiased sampling from sphere: independent Gaussian coordinate normals.
    rand=Random(20261031)
    thresholds=(1.02,1.1,1.2,sqrt(1.5),1.3,1.5,1.7)
    hits=[0]*len(thresholds)
    tri_hits=[0]*len(thresholds)
    N=150000
    for _ in range(N):
        u=[rand.gauss(0,1) for _ in range(3)]
        h=[sum(u[j]*v[j] for j in range(3)) for v in VERTICES]
        ps=[x for x in h if x>0]
        ns=[-x for x in h if x<0]
        r2=max(3-8*p*q/(p+q)**2 for p in ps for q in ns)
        for j,t in enumerate(thresholds):
            if r2<=t*t:
                hits[j]+=1
                if len(ps) != 2:
                    tri_hits[j]+=1
    for j,t in enumerate(thresholds):
        q,tr=law(t)
        assert abs(hits[j]/N-(q+tr)) < 0.009, (t,hits[j]/N,q+tr)
        assert abs(tri_hits[j]/N-tr) < 0.009, (t,tri_hits[j]/N,tr)
        count+=2
    print('PASS', count, 'exact and structural assertions plus',N,'Haar-random plane samples')
    for j,t in enumerate(thresholds):
        q,tr=law(t)
        print(f'  r={t:.9f} analytic_P={q+tr:.9f} observed_P={hits[j]/N:.9f} analytic_triangle={tr:.9f}')

if __name__=='__main__':
    run()
