"""Reproduce the exact rational benchmark and independent geometric/numerical diagnostics.
Python 3 standard library only. This is supplementary to the analytical proof.
"""
import math
from fractions import Fraction


def integrate_simpson(func, a, b, intervals=4096):
    assert intervals % 2 == 0
    h = (b-a)/intervals
    total = func(a) + func(b)
    for k in range(1, intervals):
        total += (4 if k % 2 else 2) * func(a+k*h)
    return total*h/3


def ball_volume(d):
    return math.exp(d/2*math.log(math.pi)-math.lgamma(1+d/2))


def I(d, t):
    return integrate_simpson(lambda z: max(0.0, 1-z*z)**((d-1)/2), 0.0, t)


def J(d, t):
    if t == 1:
        return 0.0
    return math.exp((d+1)/2*math.log1p(-t*t))/(d*t)


def volume_product(d, t):
    c = ball_volume(d-1)
    q = I(d, t)
    return 4*c*c*q*(q+J(d,t))


def planar_hull_area(a, n=8192):
    # Independent polygonal approximation to conv(circle union {(-a,0),(a,0)}).
    pts = [(math.cos(2*math.pi*k/n), math.sin(2*math.pi*k/n))
           for k in range(n)] + [(-a,0.0),(a,0.0)]
    pts.sort()
    def cross(o,p,q): return (p[0]-o[0])*(q[1]-o[1])-(p[1]-o[1])*(q[0]-o[0])
    lo=[]
    for p in pts:
        while len(lo)>1 and cross(lo[-2],lo[-1],p)<=0: lo.pop()
        lo.append(p)
    hi=[]
    for p in reversed(pts):
        while len(hi)>1 and cross(hi[-2],hi[-1],p)<=0: hi.pop()
        hi.append(p)
    poly=lo[:-1]+hi[:-1]
    return abs(math.fsum(poly[k][0]*poly[(k+1)%len(poly)][1] -
                         poly[(k+1)%len(poly)][0]*poly[k][1]
                         for k in range(len(poly)))/2)


def test():
    # An independent exact-arithmetic three-dimensional sample.
    d=3; t=Fraction(1,2)
    I3=t-t**3/Fraction(3,1)
    J3=(1-t*t)**2/(d*t)
    assert I3==Fraction(11,24)
    assert J3==Fraction(3,8)
    assert 4*I3*(I3+J3)==Fraction(55,36)
    print('EXACT_RATIONAL_THREE_DIMENSIONAL_BENCHMARK_PASSED')

    for d in (2,3,4,5,8,12):
        ts=[.005,.03,.1,.2,.5,.8,.95,1.0]
        vals=[volume_product(d,t) for t in ts]
        assert all(vals[i]<vals[i+1] for i in range(len(vals)-1)),(d,vals)
        assert abs(vals[-1]/ball_volume(d)**2-1)<2e-6
        low=4*ball_volume(d-1)**2/d
        assert vals[0]>low
    print('MONOTONE_PROFILE_AND_BALL_ENDPOINT_DIAGNOSTICS_PASSED')

    # A separate planar primal convex-hull computation and polar-strip integral.
    for a in (1.15, 1.5, 2.0, 4.0):
        t=1/a
        primal=planar_hull_area(a)
        polar=2*(math.asin(t)+t*math.sqrt(1-t*t))
        independent_product=primal*polar
        assert abs(independent_product/volume_product(2,t)-1)<2.5e-6, (a,independent_product/volume_product(2,t))
    print('INDEPENDENT_PLANAR_CONVEX_HULL_AND_POLAR_STRIP_PASSED')

    # Sharp Taylor coefficients at both geometric ends, with benign dimensions.
    for d in (2,3,4,5):
        k=ball_volume(d-1)
        low=4*k*k/d
        coef_low=4*k*k*(d-1)/(3*d)
        t=.01
        assert abs((volume_product(d,t)-low)/(coef_low*t*t)-1)<.0008
        coef_high=(4*k*k)*(ball_volume(d)/(2*k))*2**((d+1)/2)*(d-1)/(d*(d+1))
        h=.01
        assert abs((ball_volume(d)**2-volume_product(d,1-h)) /
                   (coef_high*h**((d+1)/2))-1)<.03
    print('BOTH_SHARP_ENDPOINT_EXPANSIONS_PASSED')

    # Gaussian crossover using direct beta-profile quadrature, no special-function package.
    for tau in (.2,.5,1.0,2.0,3.0):
        H=integrate_simpson(lambda u: math.exp(-u*u/2),0,tau)
        limit=2/math.pi*H*(H+math.exp(-tau*tau/2)/tau)
        for d in (500,1000):
            t=tau/math.sqrt(d)
            # Use gamma logs to normalize without overflowing ball volumes.
            log_r=2*(math.lgamma(d/2+1)-math.lgamma((d-1)/2+1))-math.log(math.pi)
            ratio=4*math.exp(log_r)*I(d,t)*(I(d,t)+J(d,t))
            assert abs(ratio-limit)<.0012,(tau,d,ratio,limit)
    print('INDEPENDENT_GAUSSIAN_CROSSOVER_QUADRATURE_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':test()
