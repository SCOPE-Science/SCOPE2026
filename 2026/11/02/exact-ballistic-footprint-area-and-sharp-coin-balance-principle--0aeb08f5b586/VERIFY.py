#!/usr/bin/env python3
"""Independent numerical checks of an exact planar quantum-walk velocity footprint.

Requires Python 3.9+ standard library only. This is corroboration, not the proof.
"""
import math
import random

PI = math.pi


def footprint_closed(a, b):
    if a <= 0 or b <= 0 or a + b > 1:
        raise ValueError('Require a>0, b>0, a+b<=1')
    s, t = a + b, a - b
    return 2 * (s * math.asin(s) * math.sqrt(1 - t*t)
                - t * math.asin(t) * math.sqrt(max(0.0, 1 - s*s)))


def ellipse_parameters(a, b):
    s, t = a + b, a - b
    delta = math.sqrt(max(0., (1 - s*s)*(1 - t*t)))
    p = 1 + a*a - b*b
    q = 2 - p
    return (p + delta, q - delta, p - delta, q + delta)


def integrate_midpoint(f, start, end, n=10000):
    h = (end-start)/n
    return h*sum(f(start+(i+.5)*h) for i in range(n))


def footprint_numeric(a, b, n=12000):
    """Area under min(two ellipses): direct quadrature, not closed-form integration."""
    Ar, Br, At, Bt = ellipse_parameters(a, b)
    cross = math.sqrt(2)*a
    r_end = math.sqrt(Ar)
    t_end = math.sqrt(At)
    assert 0 < cross <= min(r_end, t_end) + 1e-11
    return 4 * (
      integrate_midpoint(lambda u: math.sqrt(Br)*math.sqrt(max(0, 1-u*u/Ar)), 0, cross, n)
      + integrate_midpoint(lambda u: math.sqrt(Bt)*math.sqrt(max(0, 1-u*u/At)), cross, t_end, n))


def group_velocity(a, b, k1, k2):
    kp, km = k1+k2, k2-k1
    tau = a*math.cos(kp) - b*math.cos(km)
    den = math.sqrt(1-tau*tau)
    return ((a*math.sin(kp)+b*math.sin(km))/den,
            (a*math.sin(kp)-b*math.sin(km))/den)


def check():
    rng = random.Random(240809578)
    checks=0
    for s in (0.09, .25, .5, .72, .88, .99):
      for fraction in (.02, .1, .25, .4, .5, .6, .75, .9, .98):
        a, b=s*fraction, s*(1-fraction)
        direct=footprint_numeric(a,b,7000)
        closed=footprint_closed(a,b)
        assert abs(direct-closed)<2.e-7, (a,b,direct,closed)
        checks+=1
        assert 0 < closed <= 2*s*math.asin(s)+1.e-12
        checks+=1
        t=a-b
        sharp=(s*math.asin(s)+2*math.sqrt(1-s*s))*t*t
        assert 2*s*math.asin(s)-closed>=sharp-1.e-12
        checks+=1
        if abs(a-b)>1e-12:
            assert closed < 2*s*math.asin(s)
            checks+=1
        Ar,Br,At,Bt=ellipse_parameters(a,b)
        u,w=math.sqrt(2)*a,math.sqrt(2)*b
        assert abs(u*u/Ar+w*w/Br-1)<2e-8
        assert abs(u*u/At+w*w/Bt-1)<2e-8
        checks+=2
        for _ in range(40):
          k1=rng.uniform(-PI,PI)
          k2=rng.uniform(-PI,PI)
          v1,v2=group_velocity(a,b,k1,k2)
          u,w=(v1+v2)/math.sqrt(2),(v1-v2)/math.sqrt(2)
          assert u*u/Ar + w*w/Br <= 1+1.e-9
          assert u*u/At + w*w/Bt <= 1+1.e-9
          assert max(abs(v1),abs(v2))<=s+1.e-9
          checks+=3
    for a in (.05, .2, .5, .8, .95):
       b=1-a
       assert abs(footprint_closed(a,b)-PI*2*math.sqrt(a*b))<1e-12
       checks+=1
    for s in (.05,.35,.6,.85,.98,1.0):
       vals=[footprint_closed((s+t)/2,(s-t)/2) for t in (0,.1*s,.3*s,.5*s,.75*s,.95*s)]
       assert all(vals[i]>vals[i+1] for i in range(5)), (s,vals)
       checks+=5
    for eps in (1e-3,1e-4,1e-5,1e-6):
       s=1-eps
       ratio=(PI-2*s*math.asin(s))/(2*math.sqrt(2*eps))
       assert abs(ratio-1)<.05
       checks+=1
    print(f"PASS: {checks} independent geometric, dispersion, and optimization checks")


if __name__=='__main__':
    check()
