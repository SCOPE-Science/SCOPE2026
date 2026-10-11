#!/usr/bin/env python3
"""Independent numerical checks for the cube-width distribution laws.

No numerical sample in this file is used as a proof of the analytic theorems.
Only the Python standard library is required.
"""
import math
import random

PI = math.pi
ROOT2 = math.sqrt(2)
ROOT3 = math.sqrt(3)


def survival_3(s):
    """Analytically derived survival for a unit cube's directional width."""
    if s <= 1:
        return 1.0
    if s >= ROOT3:
        return 0.0
    cap = 4 * (1 - s / ROOT3)
    if s >= ROOT2:
        return cap
    a = math.acos(max(-1.0, min(1.0, s / math.sqrt(2 * (3 - s*s)))))
    g = math.acos(max(-1.0, min(1.0, 1 / math.sqrt(3 - s*s))))
    return cap - 12 / PI * (g - (s / ROOT3)*a)


def density_3(s):
    if not 1 < s < ROOT3:
        return 0.0
    if s >= ROOT2:
        return 4 / ROOT3
    a = math.acos(s / math.sqrt(2*(3-s*s)))
    return 4 / ROOT3 * (1 - 3*a / PI)


def independent_octant_quad(s, n=120000):
    """Integrate polar-coordinate arc lengths, independently of the cap formula.

    On x>=0, y>=0, z>=0 and S^2, x is uniform in [0,1]
    under normalized octant area, and the azimuth is uniform in [0,pi/2].
    """
    acc = 0.0
    for k in range(n):
        x = (k+0.5)/n
        t = (s-x) / (ROOT2*math.sqrt(1-x*x))
        if t <= 1/ROOT2:
            arc = PI/2
        elif t >= 1:
            arc = 0.0
        else:
            arc = 2*math.acos(t)
        acc += arc
    return 2*acc/(PI*n)


def sphere_area(m):
    return 2 * PI**((m+1)/2) / math.gamma((m+1)/2)


def simpson(f, a, b, n=400):
    assert n%2==0
    h = (b-a)/n
    val = f(a)+f(b)
    for j in range(1,n):
        val += (4 if j%2 else 2)*f(a+j*h)
    return val*h/3


def cap_tail(d,s):
    theta = math.acos(s/math.sqrt(d))
    return 2**d*sphere_area(d-2)/sphere_area(d-1)*simpson(
        lambda t: math.sin(t)**(d-2),0,theta,n=1000)


def forbidden_segment(d,s,steps=150):
    """Spherical cap area inside u_1<0 by a separate nested angular integral."""
    q=math.sqrt(d-1)
    eps=q-s
    if eps <=0:return 0.0
    def f(x):
        z=(s-x)/(q*math.sqrt(1-x*x))
        if z>=1:return 0.0
        phi=math.acos(max(-1.,min(1.,z)))
        return (1-x*x)**((d-3)/2)*sphere_area(d-3)*simpson(
            lambda t: math.sin(t)**(d-3),0,phi,n=steps)
    return simpson(f,-eps,0,n=steps)


def correction_constant(d):
    return 2**d/PI*(2/math.sqrt(d-1))**((d-2)/2)


def test():
    vals=[1.005,1.03,1.11,1.25,1.37,1.414,1.48,1.59,1.70,1.728]
    errs=[]
    for s in vals:
        v=survival_3(s)
        w=independent_octant_quad(s)
        errs.append(abs(v-w))
    assert max(errs)<2e-5, max(errs)
    assert abs(survival_3(1)-1)<1e-14
    assert abs(survival_3(ROOT3))<1e-14
    assert abs(survival_3(ROOT2)-4*(1-math.sqrt(2/3)))<1e-14
    assert abs(density_3(1.1)-4/ROOT3*(1-3/PI*math.acos(1.1/math.sqrt(2*(3-1.1**2)))))<1e-14
    for d in (3,4,5,7):
        r=math.sqrt(d-1)+0.1*(math.sqrt(d)-math.sqrt(d-1))
        assert 0<cap_tail(d,r)<1
    for d in (3,4,5):
        eps=0.002
        seg=forbidden_segment(d, math.sqrt(d-1)-eps)
        correction=2**d*d/sphere_area(d-1)*seg
        ratio=correction/(correction_constant(d)*eps**(d/2))
        assert abs(ratio-1)<0.06,(d,ratio)
    rng=random.Random(2026)
    for d in (3,4,5):
        n=60000
        threshold=math.sqrt(d-1)
        hit=0
        for _ in range(n):
            z=[rng.gauss(0,1) for _ in range(d)]
            score=sum(map(abs,z))/math.sqrt(sum(v*v for v in z))
            hit += (score >= threshold)
        p=cap_tail(d,threshold)
        empirical=hit/n
        assert abs(empirical-p)<0.018,(d,empirical,p)
    print('VERIFY_OK; 3D independent quadrature max error',max(errs),
          '; all-dimensional threshold constants and random-direction checks passed')

if __name__ == '__main__':
    test()
