"""Reproducible numerical diagnostics for the maximum-area triangle of a symmetric circular lens.

The universal statement is proved analytically in RESULT.md. Sampling does not certify a continuum.
Run: python3 verify.py
"""
import math
import random


def double_area(points):
    (x1,y1),(x2,y2),(x3,y3)=points
    return abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1))


def optimal(h):
    theta=math.acos(h)
    z=math.sin(theta/3)
    H=math.sin(theta)
    r=math.cos(theta/3)-h
    return 2*math.sin(2*theta/3)**3, ((0,H),(-r,-z),(r,-z))


def checks():
    rng=random.Random(0x310C19)
    hs=[0.0001,0.01,0.06,0.1,0.2,0.3,0.5,0.7,0.83,0.95,0.99,0.9999]
    diag=0
    for h in hs:
        theta=math.acos(h)
        H=math.sqrt(1-h*h)
        exact,triangle=optimal(h)
        geo=double_area(triangle)/2
        assert abs(exact-geo)<2e-13, (h,exact,geo)
        a=math.sin(theta/3)
        residual=1-2*a*a-a*H-h*math.sqrt(1-a*a)
        assert abs(residual)<3e-13,(h,residual)
        diag+=2
        def pt():
            y=(rng.random()*2-1)*H
            f=math.sqrt(max(0,1-y*y))-h
            return ((rng.random()*2-1)*f,y)
        def boundary():
            y=(rng.random()*2-1)*H
            f=math.sqrt(max(0,1-y*y))-h
            return (f if rng.random()<.5 else -f,y)
        # Two independently seeded forms of triangle sampling,
        # including arbitrary interior vertices and arc-boundary vertices.
        for j in range(5000):
            triplet=[pt(),pt(),pt()] if j%2 else [boundary(),boundary(),boundary()]
            area=double_area(triplet)/2
            assert area <= exact+2e-11,(h,triplet,area,exact)
            diag+=1
        # At all-smooth stationary configuration its second variation is positive.
        u=(-(1-2*h)+math.sqrt((1-2*h)**2+8))/4
        if u>h:
            a2=math.sqrt(1-u*u)
            curvature=a2*(-1+6*u*u-4*u**3)/u**3
            assert u>max(h,.5) and curvature>0
            diag+=1
    # Previously published special case: equal circles with centers at distance equal to radius.
    v,_=optimal(.5)
    assert abs(v-2*math.sin(2*math.pi/9)**3)<1e-13
    print('VERIFY_OK lens cases=%d numerical_diagnostics=%d prior_special_case=matched' % (len(hs),diag))

if __name__=='__main__':
    checks()
