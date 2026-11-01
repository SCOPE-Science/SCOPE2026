#!/usr/bin/env python3
"""Independent finite diagnostics for a geometric interpoint-moment theorem.

The general proof is in RESULT.md. These checks do not certify all shapes.
Python 3 standard library only.
"""
from fractions import Fraction as F
from math import cos, sin, pi
from random import Random


def radius_constant(d):
    return F((d + 2) * (d + 3), d * (d + 4))


def radial_coefficient(d):
    return F((d + 2)**2, 2 * d * (d + 4))


def moments_of_box(sides):
    # Each coordinate is independently uniform on [-a_i,a_i].
    squares = [F(a)**2 for a in sides]
    s1 = sum(squares, F(0))
    s2 = sum((a*a for a in squares), F(0))
    m2 = s1 / 3
    m4 = s2 / 5 + (s1*s1-s2) / 9
    trc2 = s2 / 9
    ed2 = 2*m2
    ed4 = 2*m4+2*m2*m2+4*trc2
    # Independent difference-coordinate calculation: E(X_i-Y_i)^4
    # =16a_i^4/15; E(X_i-Y_i)^2=2a_i^2/3.
    direct = 16*s2/15 + 4*(s1*s1-s2)/9
    assert direct == ed4
    ratio = ed4/(ed2*ed2)
    cov_defect = trc2/(m2*m2)-F(1,len(sides))
    # In a star-shaped body, the following equals Var_nu(rho^2)/E_nu(rho^2)^2.
    rvar = (m4/(m2*m2))*F(len(sides)*(len(sides)+4),(len(sides)+2)**2)-1
    assert rvar >= 0 and cov_defect >= 0
    assert ratio-radius_constant(len(sides)) == radial_coefficient(len(sides))*rvar+cov_defect
    return ed2,ed4,ratio,m2,m4


def test_ball():
    for d in range(2,41):
        m2=F(d,d+2)
        m4=F(d,d+4)
        trc2=F(d,(d+2)**2)
        lhs=(2*m4+2*m2*m2+4*trc2)/(4*m2*m2)
        assert lhs==radius_constant(d)
        assert radial_coefficient(d)>0
    assert radius_constant(2)==F(5,3)
    print('EXACT_BALL_CONSTANTS_D2_TO_D40_PASSED')


def test_boxes():
    for d in range(2,13):
        for a in ([1]*d,[2]+[1]*(d-1),[F(3,2),F(1,3)]+[1]*(d-2)):
            ed2,ed4,rat,*_=moments_of_box(a)
            assert rat>=radius_constant(d)
            assert ed2>0 and ed4>0
    assert moments_of_box([1,1])[2] == F(17,10)
    assert moments_of_box([1,1,1])[2] == F(22,15)
    # At cubes the covariance defect vanishes but the radial defect is positive.
    print('RECTANGULAR_BOX_INDEPENDENT_MOMENTS_PASSED')


def test_2d_polar():
    a,b=2.0,1.0
    N=120000
    integrals=[0.0,0.0,0.0]
    for j in range(N):
        t=2*pi*(j+0.5)/N
        co,si=abs(cos(t)),abs(sin(t))
        r=min(a/co if co>0 else float('inf'), b/si if si>0 else float('inf'))
        integrals[0]+=r*r
        integrals[1]+=r**4
        integrals[2]+=r**6
    m2_polar=0.5*integrals[1]/integrals[0]
    m4_polar=(1.0/3.0)*integrals[2]/integrals[0]
    *_,m2_box,m4_box=moments_of_box([2,1])
    assert abs(m2_polar-float(m2_box))<1e-6
    assert abs(m4_polar-float(m4_box))<5e-6
    print('RECTANGULAR_POLAR_INTEGRAL_PASSED')


def test_annulus():
    # A punctured disk is not star-shaped about its centroid.
    for q in (F(1,100), F(1,4), F(3,4), F(99,100)):
        # squared inner/outer radius ratio = q, normalized outer radius = 1
        m2=(1+q)/2
        m4=(1+q+q*q)/3
        rat=1+m4/(2*m2*m2)
        assert F(3,2)<rat<F(5,3)
    print('ANNULUS_CONVEXITY_BOUNDARY_PASSED')


def test_sampling():
    rng=Random(20261027)
    sides=(2.0,1.0,0.5)
    expected2,expected4,*_=moments_of_box([2,1,F(1,2)])
    N=150000
    s2=s4=0.0
    for _ in range(N):
        q=sum((rng.uniform(-a,a)-rng.uniform(-a,a))**2 for a in sides)
        s2+=q
        s4+=q*q
    assert abs(s2/N-float(expected2))/float(expected2)<0.013
    assert abs(s4/N-float(expected4))/float(expected4)<0.027
    print('SEEDED_PAIR_SAMPLING_SANITY_PASSED')


if __name__=='__main__':
    test_ball()
    test_boxes()
    test_2d_polar()
    test_annulus()
    test_sampling()
    print('ALL_CHECKS_PASSED')
