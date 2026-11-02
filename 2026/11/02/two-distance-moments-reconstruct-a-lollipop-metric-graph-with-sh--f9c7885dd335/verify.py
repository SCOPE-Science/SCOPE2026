"""Standalone numerical/exact checks for lollipop intrinsic-distance moment identities.
No external packages are needed.  The infinite-domain proof is in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from random import Random


def first_moment(t):
    return (Q(5)*t**3-Q(6)*t**2+4)/12


def second_moment(t):
    return (-t**4+6*t**3-6*t**2+2)/12


def contrast(t):
    return second_moment(t)-Q(4,5)*first_moment(t)


def case_moments(t):
    """An independent conditioning formula, without polynomial expansion."""
    a,b=t,1-t
    u=b**3/Q(3) + a**3/Q(4) + 2*a*b*(b/Q(2)+a/Q(4))
    v=b**4/Q(6) + a**4/Q(12) + 2*a*b*(b*b/Q(3)+a*b/Q(4)+a*a/Q(12))
    return u,v


def intrinsic_distance(x,y,a):
    if x<=a and y<=a:
        delta=abs(x-y)
        return min(delta,a-delta)
    if x>=a and y>=a:
        return abs(x-y)
    loop=x if x<a else y
    tail=(y-a) if x<a else (x-a)
    return tail+min(loop,a-loop)


def midpoint_integral(t,n=120):
    """Independent 2D Riemann midpoint integration over the entire length-1 graph."""
    a=float(t)
    one=two=0.0
    xs=[(i+0.5)/n for i in range(n)]
    for x in xs:
        for y in xs:
            z=intrinsic_distance(x,y,a)
            one+=z
            two+=z*z
    return one/n**2,two/n**2


def run():
    tests=0
    # Exact polynomial identities against an independent geometric conditioning.
    for k in range(1,200):
        t=Q(k,200)
        ma,mb=case_moments(t)
        assert ma==first_moment(t) and mb==second_moment(t)
        assert contrast(t)==-(5*t**4-10*t**3+6*t**2+6)/60
        assert Q(1,10)<-contrast(t)<Q(7,60)
        tests+=3

    # Exact pairwise injectivity and sharp inverse inequality.
    ts=[Q(i,120) for i in range(121)]
    for i,ti in enumerate(ts):
        for sj in ts[i+1:]:
            d=contrast(ti)-contrast(sj)
            assert d>0
            assert d>=(sj**2-ti**2)/160
            assert sj-ti <= sqrt(float(160*d))+1e-10
            tests+=3

    # Independent double quadrature, with conservative O(1/n) bound.
    for k in range(1,10):
        t=Q(k,10)
        m1,m2=midpoint_integral(t,150)
        assert abs(m1-float(first_moment(t)))<0.008
        assert abs(m2-float(second_moment(t)))<0.008
        tests+=2

    # Critical mean and an exact two-shape first-moment collision.
    tcrit=Q(4,5)
    assert first_moment(tcrit)==Q(17,75)
    a=Q(3,5)
    b=(3+3*sqrt(5))/10
    assert 0.6<b<1
    assert abs(float(first_moment(a))-float(first_moment(b)))<1e-13
    assert second_moment(a)>second_moment(b)
    tests+=4

    # Monte Carlo based on shortest paths rather than conditional formulas.
    rng=Random(20261031)
    n=75000
    for t in [0.17,0.53,0.82,0.96]:
        m1=m2=0.0
        for _ in range(n):
            z=intrinsic_distance(rng.random(),rng.random(),t)
            m1+=z
            m2+=z*z
        assert abs(m1/n-float(first_moment(t)))<0.008
        assert abs(m2/n-float(second_moment(t)))<0.008
        tests+=2

    # The square-root exponent cannot improve uniformly near the circle-vanishing boundary.
    for k in range(3,10):
        e=Q(1,10**k)
        diff=max(abs(first_moment(2*e)-first_moment(e)),
                 abs(second_moment(2*e)-second_moment(e)))
        assert e**2<diff<5*e**2
        tests+=1
    print(f'VERIFY_OK {tests} checks: exact identities, sharp inequalities, independent integration, seeded simulation')

if __name__=='__main__':
    run()
