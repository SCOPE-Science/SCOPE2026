#!/usr/bin/env python3
"""Supplementary finite calculations for anisotropic disk-noise attractor geometry.
These checks supplement, but do not replace, the infinite-series proof.
"""
import math

def radius(a, b, eps, t, count=500):
    total = 0.0
    for n in range(count):
        an, bn = a**n, b**n
        if an == 0.0 or bn == 0.0:
            break
        sn = math.sin(t)
        d = an*an*sn*sn + bn*bn*(1-sn*sn)
        if d == 0.0:
            break
        total += eps * (an*an*bn*bn) / (d**1.5)
    return total

def ellipse_radius(a, b, eps, n, t):
    u, v = a**n, b**n
    d = u*u*math.sin(t)**2 + v*v*math.cos(t)**2
    return eps*u*u*v*v/d**1.5


def check():
    eps=1.0
    for a, b in ((0.8, 0.4), (0.8, 0.6), (0.8, 0.68), (0.8, 0.75)):
        assert 0 < b < a < 1
        for t in (0.2, 0.35, 0.8):
            # two independent finite calculations of h+h'' for the first ellipse:
            rad=ellipse_radius(a,b,eps,1,t)
            d=1e-3
            def h(v):
                return math.sqrt(a*a*math.sin(v)**2+b*b*math.cos(v)**2)
            approx=h(t)+(h(t+d)-2*h(t)+h(t-d))/(d*d)
            assert abs(rad-approx)<2e-5, (a,b,t,rad,approx)
        r=a/b; q=a*a/b
        expected=("C3" if (b<a**3 or b>a**1.5) else "not_C3")
        assert expected in ('C3','not_C3')
        if q < 1:
            at_axis=1/(1-q)
            for t in (0.01,0.003):
                assert 0 < radius(a,b,eps,t) < at_axis
        else:
            assert radius(a,b,eps,0.001) < radius(a,b,eps,0.0001)
        print(f'a={a}, b={b}, predicted={expected}, q={q:.6g}, qr={q*r:.6g}, rho(0.01)={radius(a,b,eps,.01):.8g}')
    # For every n, the perimeter of an image disk is bounded by 2*pi*eps*a**n.
    for a,b in ((.8,.4),(.8,.75)):
        for n in range(7):
            approx=sum(ellipse_radius(a,b,1,n,2*math.pi*(j+.5)/8192) for j in range(8192))*(2*math.pi/8192)
            assert 0 < approx <= 2*math.pi*a**n*(1+1e-11)
    print('PASS: finite ellipse identities, endpoint monotonicity, perimeter bounds')

if __name__=='__main__':
    check()
