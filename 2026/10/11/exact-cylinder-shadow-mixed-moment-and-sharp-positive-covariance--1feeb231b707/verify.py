#!/usr/bin/env python3
"""Reproduce exact rational positivity bounds and independent projection checks."""
from fractions import Fraction as Q
import math


def arctan_series(x, count):
    return sum(((-1) ** k * x ** (2 * k + 1)) / Q(2 * k + 1)
               for k in range(count))


def rigorous_bounds():
    # Alternating arctangent series, with Machin's identity for pi.
    l5, u5 = arctan_series(Q(1, 5), 16), arctan_series(Q(1, 5), 17)
    l239, u239 = arctan_series(Q(1, 239), 16), arctan_series(Q(1, 239), 17)
    pl, pu = 16 * l5 - 4 * u239, 16 * u5 - 4 * l239
    assert Q(314159, 100000) < pl < pu < Q(314160, 100000)

    # Hypergeometric terms of I=(pi*pi/8)*sum t_n, n>=0.
    # t_0=1, t_(n+1)/t_n=((n-1/2)(n+1/2)(n+3/2))/((n+1)^2(n+2)).
    term = Q(1)
    total = Q(1)
    nmax = 144
    for n in range(nmax):
        term *= Q((2*n-1)*(2*n+1)*(2*n+3),
                  8*(n+1)**2*(n+2))
        total += term
    assert total > 0 and term < 0
    # For n>=1, |t_n|<=2/n**(5/2); tail after n=144 <= 1/1296.
    il = (pl*pl/8) * (total-Q(1, 1296))
    iu = (pu*pu/8) * total
    assert Q(930, 1000) < il < iu < Q(933, 1000)

    # Q(t)=4*C*t^2+B*t+4*pi*C, with t=h/r.
    cl = Q(2, 3)-pu*pu/16
    cu = Q(2, 3)-pl*pl/16
    bl = 2*pu*(Q(1, 3)-pu/8)+8*(il-pu**3/32)
    bu = 2*pl*(Q(1, 3)-pl/8)+8*(iu-pl**3/32)
    assert cl > Q(498, 10000)
    assert Q(-69, 100) < bl < bu < Q(-65, 100)
    # Consequently B^2 < 0.69^2 < 64*pi*C^2 = 4*(4*C)*(4*pi*C).
    assert Q(69, 100)**2 < 64*Q(314, 100)*Q(498, 10000)**2
    assert bu < 0 < cl
    return (pl, pu, il, iu, cl, cu, bl, bu)


def simpson(values, step):
    return step/3 * (values[0]+values[-1]+4*sum(values[1:-1:2])
                      +2*sum(values[2:-1:2]))


def quarter_elliptic(x, steps=240):
    vals = [math.sqrt(1-(1-x*x)*math.sin(j*math.pi/(2*steps))**2)
            for j in range(steps+1)]
    return simpson(vals, math.pi/(2*steps))


def numerical_moments(t, steps=480):
    area, perim, mixed = [], [], []
    for i in range(steps+1):
        theta = (math.pi/2)*i/steps
        x = math.sin(theta)
        y = math.cos(theta)
        j = quarter_elliptic(x)
        a = math.pi*x+2*t*y
        p = 4*j+2*t*y
        area.append(a*y)
        perim.append(p*y)
        mixed.append(a*p*y)
    ea = simpson(area, math.pi/(2*steps))
    ep = simpson(perim, math.pi/(2*steps))
    eap = simpson(mixed, math.pi/(2*steps))
    return ea, ep, eap, eap-ea*ep


def numerical_I(steps=1200):
    # x=sin(theta), y=cos(theta), dx=y*dtheta.
    vals=[]
    for i in range(steps+1):
        theta=math.pi*i/(2*steps)
        y=math.cos(theta)
        vals.append(y*y*quarter_elliptic(math.sin(theta)))
    return simpson(vals, math.pi/(2*steps))


def convex_hull(points):
    points = sorted(set(points))
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lower = []
    for p in points:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:
            upper.pop()
        upper.append(p)
    return lower[:-1]+upper[:-1]


def hull_area_perimeter(hull):
    area=0.0
    perimeter=0.0
    for p,q in zip(hull, hull[1:]+hull[:1]):
        area+=p[0]*q[1]-p[1]*q[0]
        perimeter+=math.hypot(q[0]-p[0],q[1]-p[1])
    return area/2,perimeter


def polygonal_projection_checks():
    # Project actual boundary vertices of polyhedral approximations of cylinders.
    cases=0
    for height in (0.4,1.7,5.0):
        for x in (0.06,0.23,0.57,0.81,0.97):
            y=math.sqrt(1-x*x)
            # Orthogonal plane basis: (0,1,0), (-x,0,y).
            pts=[(math.sin(2*math.pi*k/512),
                  -x*math.cos(2*math.pi*k/512)+z*height*y/2)
                 for z in (-1,1) for k in range(512)]
            ah,ph=hull_area_perimeter(convex_hull(pts))
            aa=math.pi*x+2*height*y
            pp=4*quarter_elliptic(x,400)+2*height*y
            assert abs(ah-aa)<0.0002,(height,x,ah,aa)
            assert abs(ph-pp)<0.0002,(height,x,ph,pp)
            cases+=1
    return cases


def main():
    pl,pu,il,iu,cl,cu,bl,bu=rigorous_bounds()
    pi=math.pi
    c=2/3-pi*pi/16
    ii=numerical_I()
    assert abs(ii-0.9318171570247627)<0.00000001,ii
    b=2*pi*(1/3-pi/8)+8*(ii-pi**3/32)
    tstar=-b/(8*c)
    minimum=4*pi*c-b*b/(16*c)
    assert 1.68<tstar<1.69 and 0.062<minimum<0.064
    for t in (0.3,tstar,2.0,5.0):
        ea,ep,eap,cov=numerical_moments(t)
        target_ea=pi*(1+t)/2
        target_ep=(pi*pi+pi*t)/2
        target_eap=8*pi/3+t*(2*pi/3+8*ii)+8*t*t/3
        target_cov=4*c*t*t+b*t+4*pi*c
        assert abs(ea-target_ea)<0.00004,(t,ea,target_ea)
        assert abs(ep-target_ep)<0.00004,(t,ep,target_ep)
        assert abs(eap-target_eap)<0.00012,(t,eap,target_eap)
        assert abs(cov-target_cov)<0.00012,(t,cov,target_cov)
    cases=polygonal_projection_checks()
    print('VERIFY_OK rational_interval=PASS analytic_quadrature=PASS hull_cases=%d' % cases)
    print('rigorous_I_interval=(%.12f, %.12f)'%(float(il),float(iu)))
    print('rigorous_B_interval=(%.12f, %.12f)'%(float(bl),float(bu)))
    print('sharp_ratio=%.12f minimum_normalized_covariance=%.12f'%(tstar, minimum))


if __name__=='__main__':
    main()
