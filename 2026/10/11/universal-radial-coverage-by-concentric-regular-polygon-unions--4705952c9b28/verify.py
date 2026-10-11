#!/usr/bin/env python3
"""Reproduce geometric diagnostics for the concentric-regular-polygon union theorem.
Requires Python >= 3.9 and shapely >= 2; no network access needed.
"""
from math import pi, sin, cos, tan, acos, hypot
from random import Random
from shapely.geometry import Polygon
from shapely.ops import unary_union


def geometric_union(n, rotations, radius=1.0):
    parts=[]
    for a in rotations:
        pts=[(radius*cos(a+2*pi*j/n),radius*sin(a+2*pi*j/n)) for j in range(n)]
        parts.append(Polygon(pts))
    return unary_union(parts)


def formula(n, rotations, radius=1.0):
    alpha=pi/n; r=radius*cos(alpha); L=2*alpha
    phases=sorted(a % L for a in rotations)
    gaps=[phases[i+1]-phases[i] for i in range(len(phases)-1)]+[phases[0]+L-phases[-1]]
    area=n*r*r*sum(tan(alpha)-tan(alpha-g/2) for g in gaps)
    return area, (2/r)*area, gaps


def angular_coverage(n, gaps, t, radius=1.0):
    alpha=pi/n;r=radius*cos(alpha)
    if t<=r: return 2*pi
    if t>=radius:return 0.0
    eta=alpha-acos(r/t)
    return n*sum(min(g,2*eta) for g in gaps)


def direct_angular_measure(n, rotations, t, samples=20000, radius=1.0):
    alpha=pi/n;r=radius*cos(alpha)
    if t<=r:return 2*pi
    if t>=radius:return 0
    total=0
    for j in range(samples):
        phi=2*pi*(j+0.5)/samples
        covered=False
        for a in rotations:
            # Independent: test halfplanes defining the polygon.
            if all(t*cos(phi-(a+(2*k+1)*alpha)) <= r+1e-13 for k in range(n)):
                covered=True;break
        total+=covered
    return 2*pi*total/samples


def run():
    rng=Random(14159265)
    cases=0
    max_area_error=0.0
    max_perimeter_error=0.0
    for n in (3,4,5,6,7,9):
        for m in (1,2,3,4,5):
            alpha=pi/n;L=2*alpha
            configs=[[L*j/m for j in range(m)], [0.0]*m]
            configs += [[rng.random()*L for _ in range(m)] for _ in range(6)]
            for rotations in configs:
                geo=geometric_union(n,rotations)
                area,perimeter,gaps=formula(n,rotations)
                max_area_error=max(max_area_error,abs(geo.area-area))
                max_perimeter_error=max(max_perimeter_error,abs(geo.length-perimeter))
                assert abs(geo.area-area)<2e-11,(n,m,geo.area,area)
                assert abs(geo.length-perimeter)<2e-10,(n,m,geo.length,perimeter)
                max_area=n*m*cos(alpha)**2*(tan(alpha)-tan(alpha-alpha/m))
                min_area=n*cos(alpha)**2*tan(alpha)
                assert min_area-1e-11<=area<=max_area+1e-11
                if len(set(round((p%L),9) for p in rotations))==m:
                    assert len(geo.exterior.coords)-1 >=n*m
                cases+=1
    # A geometric circle-sampling test independent of the cyclic-gap algebra.
    coverage_error=0.0
    for n,m in ((3,3),(5,4),(8,3)):
        L=2*pi/n
        rotations=[rng.random()*L for _ in range(m)]
        _,_,gaps=formula(n,rotations)
        for x in (0.12,0.31,0.51,0.75,0.94):
            r=cos(pi/n);t=r+(1-r)*x
            exact=angular_coverage(n,gaps,t)
            approx=direct_angular_measure(n,rotations,t,12000)
            err=abs(exact-approx)
            coverage_error=max(coverage_error,err)
            assert err<0.002, (n,m,t,exact,approx)
    # Check the analytic disk-deficit asymptotic at increasing m.
    for n in (3,4,6,10):
        a=pi/n;r=cos(a)
        constant=pi*pi*tan(a)/n
        def ad(m):return n*m*r*r*(tan(a)-tan(a-a/m))
        assert abs((pi-ad(20000))*20000-constant)<2.5e-3
    print('VERIFY_OK', 'geometric_cases',cases,
          'max_area_error',format(max_area_error,'.3g'),
          'max_perimeter_error',format(max_perimeter_error,'.3g'),
          'max_coverage_error',format(coverage_error,'.3g'))

if __name__=='__main__': run()
