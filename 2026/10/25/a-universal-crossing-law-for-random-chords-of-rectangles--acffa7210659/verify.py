"""Deterministic numerical checks for the arclength-endpoint rectangle chord law."""
import math
import random


def opposite(t):
    return t*(3-t)/(1+t)


def adjacent(t):
    return t - 0.5*(1-t)**2*math.log((1+t)/(1-t))


def atom(a,b):
    return (a*a+b*b)/(2*(a+b)**2)


def cdf(t,a,b):
    p=atom(a,b)
    return p*opposite(t)+(1-2*p)*adjacent(t)


def h(t):
    return 2*adjacent(t)-opposite(t)


def bisect_zero(f, low, high, steps=100):
    assert f(low)<0 and f(high)>0
    for _ in range(steps):
        mid=(low+high)/2
        if f(mid)<0:
            low=mid
        else:
            high=mid
    return (low+high)/2


def penetration(P,Q):
    # The maximum of two absolute affine coordinates is convex piecewise linear.
    # A minimum occurs at an endpoint, coordinate zero, or an equality of the
    # signed normalized coordinate expressions.
    x0,y0=P; x1,y1=Q
    dx=x1-x0;dy=y1-y0
    candidates=[0.,1.]
    for alpha,beta in ((dx,x0),(dy,y0),(dx-dy,x0-y0),(dx+dy,x0+y0)):
        if abs(alpha)>1e-14:
            t=-beta/alpha
            if 0<=t<=1:
                candidates.append(t)
    return min(max(abs(x0+t*dx),abs(y0+t*dy)) for t in candidates)


def boundary_point(rng,a,b):
    z=rng.random()*4*(a+b)
    if z<2*a:
        return (-a+z,b)
    z-=2*a
    if z<2*b:
        return (a,b-z)
    z-=2*b
    if z<2*a:
        return (a-z,-b)
    z-=2*a
    return (-a,-b+z)


def run():
    t_star=bisect_zero(h,0.4,0.8)
    assert abs(t_star-0.5604879233027861)<1e-13
    assert abs(h(t_star))<1e-14
    for r in (1.,1.5,3.,7.,100.):
        p=atom(r,1.)
        recovered=(2*p+math.sqrt(4*p-1))/(1-2*p)
        assert abs(recovered-r)<1e-9*max(1,r)
        assert abs(cdf(t_star,r,1.)-cdf(t_star,1.,1.))<2e-14
    assert h(.01)<0 and h(.99)>0
    # Independently sample the actual two-endpoint geometry, without conditioning
    # on side labels or using the derived closed forms.
    rng=random.Random(115020)
    for a,b in ((1.,1.),(3.,1.),(7.,2.)):
        m=160000
        samples=[]
        for _ in range(m):
            P=boundary_point(rng,a,b)
            Q=boundary_point(rng,a,b)
            samples.append(penetration((P[0]/a,P[1]/b),(Q[0]/a,Q[1]/b)))
        for t in (.15,.35,.56,.8):
            obs=sum(s<=t for s in samples)/m
            expected=cdf(t,a,b)
            assert abs(obs-expected)<0.008,(a,b,t,obs,expected)
    print('RECTANGLE_PENETRATION_CHECKS_OK')
    print('universal_crossing',format(t_star,'.16g'))


if __name__=='__main__':
    run()
