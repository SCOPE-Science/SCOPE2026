#!/usr/bin/env python3
"""Finite diagnostics for exact two-vector numerical annuli; not a proof."""
import cmath
import math
import random


def ip(x, y):
    return sum(v * w.conjugate() for v, w in zip(x, y))


def apply(a, b, x):
    return (a * x[0].conjugate() + b * x[1].conjugate(),
            -b * x[0].conjugate() + a * x[1].conjugate())


def bounds(a, b, q):
    c = math.hypot(a, b)
    t = abs(q)
    s = math.sqrt(max(0.0, 1.0 - t*t))
    return max(0.0, b*s-a*t), c if c*t <= a else a*t+b*s


def witness(a, b, q, which):
    c = math.hypot(a, b)
    t = abs(q)
    s = math.sqrt(max(0., 1.-t*t))
    if which == 'outer':
        m = min(a, c*t)
    else:
        m = min(a, c*s)
    theta = .5*math.acos(max(-1., min(1., m/a))) if a > 0 else 0.
    x = (complex(math.cos(theta)), 1j*math.sin(theta))
    v = (1j*math.sin(theta), complex(math.cos(theta)))
    z0 = q*ip(apply(a,b,x),x)
    z1 = ip(apply(a,b,x),v)
    phase = cmath.phase(z1)-cmath.phase(z0) if abs(z0)*abs(z1)>1e-14 else 0.
    if which == 'inner':
        phase -= math.pi
    unit = cmath.exp(1j*phase)
    y = tuple(q.conjugate()*u+s*unit*w for u,w in zip(x,v))
    return x,y


def main():
    random.seed(71512)
    cases = ((1.,0.), (0.,1.), (1.,1.), (2.,1.), (.4,1.5), (2.5,4.0))
    qvalues=(0j, .1+0j, .4+.2j, .4-.6j, .8+0j, 1j, 1+0j)
    checks = 0
    for a,b in cases:
        c=math.hypot(a,b)
        for q in qvalues:
            lower,upper=bounds(a,b,q)
            for which,expected in (('inner',lower),('outer',upper)):
                x,y=witness(a,b,q,which)
                assert abs(ip(x,x)-1)<1e-12
                assert abs(ip(y,y)-1)<1e-12
                assert abs(ip(x,y)-q)<1e-12
                assert abs(abs(ip(apply(a,b,x),y))-expected)<1e-11, (a,b,q,which,expected)
                checks += 4
            for _ in range(200):
                p=random.random()*math.pi/2
                u=random.random()*2*math.pi
                x=(math.cos(p), cmath.exp(1j*u)*math.sin(p))
                v=(-x[1].conjugate(), x[0].conjugate())
                phase=random.random()*2*math.pi
                s=math.sqrt(max(0,1-abs(q)**2))
                y=tuple(q.conjugate()*xx+s*cmath.exp(1j*phase)*vv for xx,vv in zip(x,v))
                # Correct orthogonal vector: <x,v> = 0 for this construction.
                assert abs(ip(x,y)-q)<1e-12
                z=abs(ip(apply(a,b,x),y))
                assert lower-1e-10 <= z <= upper+1e-10, (a,b,q,z,lower,upper)
                checks += 2
    print('PASS:',checks,'finite numerical assertions')


if __name__=='__main__':
    main()
