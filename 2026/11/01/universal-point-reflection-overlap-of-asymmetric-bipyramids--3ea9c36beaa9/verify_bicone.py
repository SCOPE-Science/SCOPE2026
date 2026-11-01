"""Independent exact slice integrals and numerical full-dimensional checks.

All universal conclusions are proved analytically in RESULT.md. This script
checks selected rational cases exactly and independently integrates cubical
cross-sections with displaced reflection centers.
"""
from fractions import Fraction as F
from math import isclose


def radius(y, t):
    if y < -t or y > 1:
        return F(0)
    return 1-y if y >= 0 else 1+y/t


def overlap_exact(m, t, c):
    """Integral of min(r(y), r(2c-y))**m with exact rational data."""
    low, high = max(-t, 2*c-1), min(F(1), 2*c+t)
    if low >= high:
        return F(0)
    pts = sorted({low, high} | {z for z in [F(0), 2*c] if low < z < high})
    # On these cells both radius functions are affine. Insert crossings.
    refined = set(pts)
    for a,b in zip(pts,pts[1:]):
        d1=radius(a,t)-radius(2*c-a,t)
        d2=radius(b,t)-radius(2*c-b,t)
        if d1*d2 < 0:
            refined.add(a+(b-a)*d1/(d1-d2))
    pts=sorted(refined)
    value=F(0)
    for a,b in zip(pts,pts[1:]):
        u=min(radius(a,t), radius(2*c-a,t))
        v=min(radius(b,t), radius(2*c-b,t))
        assert min(u,v) >= 0
        value+=(b-a)*sum(u**(m-k)*v**k for k in range(m+1))/(m+1)
    return value


def closed_overlap(m,t,c):
    z=F(1-t,2)
    if c <= 0:
        if t==0: return F(0)
        return F(2,m+1)*(t+c)**(m+1)/t**m
    if c < z:
        return F(2,m+1)*((1-c)**(m+1)-(1-t)*(1-2*c/(1-t))**(m+1))
    return F(2,m+1)*(1-c)**(m+1)

cases=0
for m in range(1,7):
    for t in [F(0),F(1,6),F(1,3),F(2,3),F(1)]:
        for i in range(1,20):
            c= -t+(1+t)*F(i,20)
            exact=overlap_exact(m,t,c)
            closed=closed_overlap(m,t,c)
            assert exact==closed,(m,t,c,exact,closed)
            cases+=1
print('EXACT_RATIONAL_PIECEWISE_SLICE_INTEGRALS_PASSED',cases)


def factor(y,t):
    if 0 <= y <= 1: return 1-y
    if t and -t <= y < 0:return 1+y/t
    return 0.


def numeric_cube_overlap(m,t,c,u,steps=5000):
    lo=max(-t,2*c-1);hi=min(1,2*c+t)
    if lo>=hi: return 0.
    def integrand(y):
        p,q=factor(y,t),factor(2*c-y,t)
        w=max(0.,min(p,2*u+q)-max(-p,2*u-q))
        return w*min(2*p,2*q)**(m-1) if m>1 else w
    h=(hi-lo)/steps
    return h*(integrand(lo)+integrand(hi)
       +sum((4 if i%2 else 2)*integrand(lo+i*h) for i in range(1,steps)))/3

checks=0
for m in range(1,6):
    alpha=2**(1/m)
    for t in [0.,.125,.35,.7,1.]:
        den=t+2*alpha-1
        center=(1-t)*(alpha-1)/den
        maximum=2*((1+t)/den)**m
        # The cubical B has volume 2**m.
        observed=numeric_cube_overlap(m,t,center,0.)/((2**m)*(1+t)/(m+1))
        assert abs(observed-maximum)<2e-7,(m,t,observed,maximum)
        for dc in [-.018,.018]:
            shifted=numeric_cube_overlap(m,t,center+dc,0.)/((2**m)*(1+t)/(m+1))
            assert shifted < maximum-1e-7,(m,t,center,shifted,maximum)
        sideways=numeric_cube_overlap(m,t,center,.037)/((2**m)*(1+t)/(m+1))
        assert sideways < maximum-1e-7,(m,t,sideways,maximum)
        checks+=1
print('INDEPENDENT_CUBE_INTEGRAL_AND_SHIFT_CHECKS_PASSED',checks)

# The explicit inversion is checked at all endpoints and interior samples.
for m in range(1,10):
    alpha=2**(1/m)
    for t in [0.,.1,.4,.8,1.]:
        r=2*((1+t)/(t+2*alpha-1))**m
        q=(r/2)**(1/m)
        t_recovered=(q*(2*alpha-1)-1)/(1-q)
        assert isclose(t,t_recovered,abs_tol=3e-13,rel_tol=3e-13)
print('SHAPE_INVERSION_ENDPOINTS_AND_INTERIOR_PASSED')
print('ALL_CHECKS_PASSED')
