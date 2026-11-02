"""Numerical consistency tests for the unit cube's intrinsic vertex-distance law.

This program uses Python's standard library, requires no network access, and
implements the stated mathematical formulas independently of source unfoldings.
"""
import math
import random

PI = math.pi
ROOT2 = math.sqrt(2.0)
ROOT5 = math.sqrt(5.0)
C = 1.0 / ROOT2


def phi(a, r):
    return (r*r*math.asin(a/r)+a*math.sqrt(max(0.0, r*r-a*a)))/2.0


def cdf(r):
    if r <= 0:
        return 0.0
    if r <= 1:
        return PI*r*r/8
    if r <= ROOT2:
        return phi(C,r)-0.25
    if r < ROOT5:
        return phi(1,r)+phi(C,r)-PI*r*r/8-0.75
    return 1.0


def density(r):
    if r <= 0 or r >= ROOT5:
        return 0.0
    if r <= 1:
        return PI*r/4
    if r <= ROOT2:
        return r*math.asin(1/(ROOT2*r))
    return r*(math.asin(1/r)+math.asin(1/(ROOT2*r))-PI/4)


def simpson(f,a,b,n=10000):
    assert n % 2 == 0
    h=(b-a)/n
    t=f(a)+f(b)
    for j in range(1,n):
        t+=(4 if j%2 else 2)*f(a+j*h)
    return t*h/3


def planar_integral_cdf(r):
    # Numerically integrate over square and triangle in Cartesian coordinates.
    # For each horizontal y, intersect x>=0 with the circle of radius r.
    if r <= 0:return 0.0
    def sq(y):
        return min(1.0,math.sqrt(max(0.0,r*r-y*y))) if y<r else 0.0
    def tri(y):
        if y > r:return 0.0
        xhi=math.sqrt(max(0.0,r*r-y*y))
        return max(0.0,min(1+y,xhi)-1.0)
    # Break at all circle-line intersections to control square-root corners.
    sq_area=simpson(sq,0,min(1,r),5000)
    tr_area=simpson(tri,0,min(1,r),5000)
    return sq_area/2+tr_area


def test():
    assert abs(cdf(ROOT5)-1)<1e-14
    assert abs(cdf(1)-PI/8)<1e-14
    assert abs(cdf(ROOT2)-(PI/6+(math.sqrt(3)-1)/4))<1e-12
    full=simpson(density,0,1,6000)+simpson(density,1,ROOT2,6000)+simpson(density,ROOT2,ROOT5,6000)
    moment=(simpson(lambda r:r*r*density(r),0,1,6000)
            +simpson(lambda r:r*r*density(r),1,ROOT2,6000)
            +simpson(lambda r:r*r*density(r),ROOT2,ROOT5,6000))
    assert abs(full-1)<1e-8,full
    assert abs(moment-1.5)<1e-8,moment
    radii=[0.2,0.5,0.8,1.0,1.13,1.3,ROOT2,1.6,1.87,2.0,2.17,ROOT5]
    for r in radii:
        # Cartesian planar integration uses independent midpoint partitioning.
        # At exact thresholds its corner singularities limit convergence order.
        diff=abs(cdf(r)-planar_integral_cdf(r))
        assert diff<1e-5,(r,diff)
    rng=random.Random(237416)
    N=300000
    samples=[]
    for _ in range(N):
        face=rng.randrange(6)
        a,b=rng.random(),rng.random()
        dsq=a*a+b*b if face<3 else 1+a*a+b*b+2*min(a,b)
        samples.append(math.sqrt(dsq))
    e2=sum(x*x for x in samples)/N
    assert abs(e2-1.5)<0.015,e2
    for r in [0.5,0.9,1.0,1.2,ROOT2,1.6,1.9,2.1]:
        observed=sum(x<=r for x in samples)/N
        assert abs(observed-cdf(r))<0.006,(r,observed,cdf(r))
    for eps in [0.05,0.02,0.01]:
        ratio=(1-cdf(ROOT5-eps))/(eps*eps)
        assert abs(ratio-5/12)<0.001,(eps,ratio)
    print('PASS: CDF normalization, planar quadratures, E[D²]=3/2,')
    print('300000 sampled points, and upper-tail coefficient 5/12')
    print('max intrinsic distance =',ROOT5)

if __name__=='__main__':
    test()
