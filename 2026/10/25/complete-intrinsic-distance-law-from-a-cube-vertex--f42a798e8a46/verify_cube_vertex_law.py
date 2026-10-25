#!/usr/bin/env python3
"""Exact face-unfolding certificate and independent quadrature checks for cube vertex geodesic balls.

Python 3, standard library only. Run: python3 verify_cube_vertex_law.py
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import asin, pi, sqrt

FACES = [(axis, side) for axis in range(3) for side in (0, 1)]

def vertices(face):
    axis, side = face
    free = [j for j in range(3) if j != axis]
    return [tuple(side if j == axis else a[free.index(j)] for j in range(3))
            for a in product((0, 1), repeat=2)]

def initial_chart(face):
    free = [j for j in range(3) if j != face[0]]
    return {v: (v[free[0]], v[free[1]]) for v in vertices(face)}

def attach_chart(chart, old, new):
    common = sorted(set(vertices(old)).intersection(vertices(new)))
    assert len(common) == 2
    p, q = (chart[v] for v in common)
    dx, dy = q[0]-p[0], q[1]-p[1]
    assert dx*dx+dy*dy == 1
    center = (sum(x for x, _ in chart.values())/4,
              sum(y for _, y in chart.values())/4)
    inward = (center[0]-(p[0]+q[0])/2, center[1]-(p[1]+q[1])/2)
    outward = (-dy, dx)
    if sum(outward[k]*inward[k] for k in range(2)) > 0:
        outward = (-outward[0], -outward[1])
    ans = {v: chart[v] for v in common}
    for v in common:
        w = list(v)
        w[old[0]] = 1-old[1]
        ans[tuple(w)] = (chart[v][0]+outward[0], chart[v][1]+outward[1])
    assert set(ans) == set(vertices(new))
    return ans

def all_developments():
    def explore(chain, chart):
        f = chain[-1]
        if f == (0, 1):
            by = {(v[1],v[2]): pos for v,pos in chart.items()}
            p = by[0,0]
            ey = tuple(by[1,0][j]-p[j] for j in range(2))
            ez = tuple(by[0,1][j]-p[j] for j in range(2))
            assert sum(e*e for e in ey) == sum(e*e for e in ez) == 1
            assert sum(ey[j]*ez[j] for j in range(2)) == 0
            c = (sum(x*x for x in p),
                 2*sum(p[j]*ey[j] for j in range(2)),
                 2*sum(p[j]*ez[j] for j in range(2)))
            yield c
            return
        for g in FACES:
            if g[0] != f[0] and g not in chain:
                yield from explore(chain+[g], attach_chart(chart, f, g))
    for face in ((0,0),(1,0),(2,0)):
        yield from explore([face], initial_chart(face))

def polynomial_multiply(a,b):
    c = Counter()
    for (i,j),v in a.items():
        for (k,l),w in b.items(): c[(i+k,j+l)] += v*w
    return dict(c)

def polynomial_power(a,k):
    p={(0,0): 1}
    for _ in range(k): p=polynomial_multiply(p,a)
    return p

def exact_moments(k):
    near=polynomial_power({(2,0):1,(0,2):1},k)
    far=polynomial_power({(0,0):1,(2,0):1,(0,2):1,(1,0):2},k)
    en=sum((Fraction(val,(i+1)*(j+1)) for (i,j),val in near.items()),Fraction(0))
    ef=2*sum((Fraction(val,(i+1)*(i+j+2)) for (i,j),val in far.items()),Fraction(0))
    return (en,ef,(en+ef)/2)

def area_near(r):
    if r<=0:return 0.0
    if r<=1:return pi*r*r/4
    if r<sqrt(2):return sqrt(r*r-1)+r*r*(asin(1/r)-pi/4)
    return 1.0

def area_far(r):
    if r<=1:return 0.0
    if r>=sqrt(5):return 1.0
    a=max(0.0,sqrt(r*r-1)-1)
    b=(sqrt(2*r*r-1)-1)/2
    def J(t):
        w=1+t
        return (w*sqrt(max(0.0,r*r-w*w))+r*r*asin(min(1.0,w/r)))/2
    return 2*(J(b)-J(a)+a-b*b/2)

def cdf(r):
    if r<0:return 0.0
    if r>=sqrt(5):return 1.0
    return (area_near(r)+area_far(r))/2

def midpoint_cdf(r,n=350):
    # A separate, non-analytic Riemann-sum comparison on the two face types.
    near=far=0
    for i in range(n):
        u=(i+0.5)/n
        for j in range(n):
            v=(j+0.5)/n
            near += (u*u+v*v<=r*r)
            far += (1+u*u+v*v+2*min(u,v)<=r*r)
    return (near+far)/(2*n*n)

def main():
    records=list(all_developments())
    counts=Counter(records)
    assert len(records)==80 and len(counts)==24
    assert (1,0,2) in counts and (1,2,0) in counts
    # Each developed squared distance has the form
    # y^2+z^2+c0+cy*y+cz*z. The difference from the candidate
    # y^2+z^2+1+2*min(y,z) is affine on each of the two triangles
    # y<=z and z<=y. These triangles have four distinct vertices.
    for c0,cy,cz in counts:
        assert min(c0-1,c0+cy-1,c0+cz-1,c0+cy+cz-3)>=0
    assert exact_moments(1)==(Fraction(2,3),Fraction(7,3),Fraction(3,2))
    assert exact_moments(2)==(Fraction(28,45),Fraction(277,45),Fraction(61,18))
    for r in (0.5,0.95,1.1,1.35,sqrt(2),1.7,2.1):
        assert abs(cdf(r)-midpoint_cdf(r)) < 0.004, (r,cdf(r),midpoint_cdf(r))
    assert cdf(0)==0.0 and cdf(sqrt(5))==1.0
    print('PASS: 80 simple face walks, 24 exact developed distance classes')
    print('PASS: all four affine-region inequality vertices checked in each class')
    print('PASS: E[R^2]=3/2, E[R^4]=61/18 by rational polynomial integration')
    print('PASS: analytic CDF vs independently sampled surface-area quadrature')
    print('Exact coefficient multiplicities (c0,cy,cz,count):')
    for k,v in sorted(counts.items()):print(*k,v)

if __name__=='__main__':main()
