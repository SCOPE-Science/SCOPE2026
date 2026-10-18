"""Finite reproducibility tests for the radial weighted-perimeter theorem.

All universal conclusions are analytical; these are independent finite checks.
Only Python's standard library is required.
"""

import math
import random

PI = math.pi


def rectangle_p2(a, b):
    """Exact squared-radius weighted perimeter of [-a,a] x [-b,b]."""
    return 4.0 * (a**3 + b**3) / 3.0 + 4.0 * a * b * (a + b)


def rectangle_p2_parallel(a, b, t):
    """Exact formula by straight sides and four circular quarter-arcs."""
    return (rectangle_p2(a, b)
            + t * (16*a*b + 2*PI*(a*a+b*b))
            + 12*(a+b)*t*t + 2*PI*t**3)


def simpson(f, lo, hi, steps=800):
    assert steps % 2 == 0
    h = (hi-lo)/steps
    s = f(lo)+f(hi)
    for i in range(1, steps):
        s += (4 if i%2 else 2)*f(lo+i*h)
    return s*h/3


def independent_rectangle_p2_parallel(a, b, t):
    # Two shifted horizontal + two shifted vertical segments.
    straight = 4*a**3/3 + 4*a*(b+t)**2 + 4*b**3/3 + 4*b*(a+t)**2
    # Outer quarter-circle near (+a,+b), x=a+t cos theta, y=b+t sin theta.
    corner = 4*t*simpson(lambda th: (a+t*math.cos(th))**2+
                              (b+t*math.sin(th))**2, 0.0,PI/2)
    return straight + corner


def circle_p(n, p, r):
    return n*math.pi**(n/2)/math.gamma(n/2+1)*r**(n-1+p)


def sharp_coefficient(n, p, R):
    return n*math.pi**(n/2)/math.gamma(n/2+1)*(n-1+p)*R**(n-2+p)


def check():
    random.seed(20261014)
    count=0
    for n in range(2, 10):
        for p in (0.25, 0.7, 1, 2, 3.5):
            for R in (0.3,1.0,4.0):
                eps=1e-6*R
                ratio=(circle_p(n,p,R)-circle_p(n,p,R-eps))/eps
                C=sharp_coefficient(n,p,R)
                assert abs(ratio/C-1)<5e-5,(n,p,R)
                assert circle_p(n,p,R)-circle_p(n,p,R-eps)<=C*eps*(1+1e-10)
                count += 2
    for k in range(200):
        a=0.1+2.0*random.random()
        b=0.1+2.0*random.random()
        t=0.01+random.random()
        got=rectangle_p2_parallel(a,b,t)
        indep=independent_rectangle_p2_parallel(a,b,t)
        assert abs(got-indep)<1e-8*max(1.,abs(got)),(a,b,t,got,indep)
        R=math.hypot(a,b)
        bound=2*PI*((R+t)**3-R**3)
        assert got-rectangle_p2(a,b) < bound,(a,b,t)
        count += 2
    # Independently integrate two unequal convex diamonds with a common origin.
    # Pointwise matched vertex movements supply a certified upper bound for d_H.
    for p in (0.2, 0.7, 1.4, 3.0):
        for k in range(125):
            abcd = [0.25+1.2*random.random() for _ in range(4)]
            eps = 0.001+0.03*random.random()
            shifted = [v+eps*(2*random.random()-1) for v in abcd]
            def per(weights):
                a,b,c,d=weights
                verts=[(a,0.),(0.,b),(-c,0.),(0.,-d)]
                result=0.
                for i in range(4):
                    x0,y0=verts[i]; x1,y1=verts[(i+1)%4]
                    dx=x1-x0;dy=y1-y0
                    result+=math.hypot(dx,dy)*simpson(
                        lambda u:(math.hypot(x0+u*dx,y0+u*dy)**p),0.,1.,128)
                return result
            observed=abs(per(abcd)-per(shifted))
            # Matching vertices move by <=eps, so Hausdorff distance <=eps.
            upper=sharp_coefficient(2,p,2.)*eps
            assert observed < upper+1e-10,(p,abcd,shifted,observed,upper)
            count+=1
    for a in (0.1,0.4,1.0,2.1):
        # Degenerate rectangle -> twice the weighted line segment (p=2).
        line=4*a**3/3
        assert abs(rectangle_p2(a,1e-8)-line)<1e-5
        count+=1
    print('RADIAL_WEIGHTED_PERIMETER_SHARP_FINITE_CHECKS_OK',count)


if __name__=='__main__':
    check()
