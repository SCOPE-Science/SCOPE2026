#!/usr/bin/env python3
"""Reproduce finite checks for a regular octahedron's random section radius law.

The checks are numerical or finite exact arithmetic, not a substitute for the proof.
Requires only Python's standard library.
"""
import math
import random
from fractions import Fraction

PI = math.pi


def cone_denominator(t):
    w1 = math.sqrt(1 + 2*t*t)
    w2 = math.sqrt(2 + t*t)
    return (math.sqrt(3)*w1*w2 + (1+2*t)*w2
            + (1+t+t*t)*math.sqrt(3) + (2+t)*w1)


def tail(t):
    if t < 0 or t > 1:
        raise ValueError('t must lie in [0,1]')
    return 24/PI * math.atan2((1-t)**2, cone_denominator(t))


def section_radius(normal):
    v = sorted(map(abs, normal))
    return math.hypot(v[0], v[2])/(v[0] + v[2])


def independent_vertex_radius(normal):
    radii = []
    a = list(map(abs, normal))
    for i in range(3):
        for j in range(i+1, 3):
            if a[i] + a[j] > 0:
                radii.append(math.hypot(a[i],a[j])/(a[i]+a[j]))
    return max(radii)


def spherical_excess(t):
    # Independent spherical-triangle angle computation via the cosine law.
    v = [(1.,1.,1.), (t,t,1.), (t,1.,1.)]
    u = [tuple(q/math.sqrt(sum(p*p for p in x)) for q in x) for x in v]
    cs = [sum(u[(j+1)%3][k]*u[(j+2)%3][k] for k in range(3)) for j in range(3)]
    sides = [math.acos(max(-1.,min(1.,x))) for x in cs]
    ang = []
    for j in range(3):
        a, b, c = sides[j], sides[(j+1)%3], sides[(j+2)%3]
        cosine = (math.cos(a)-math.cos(b)*math.cos(c))/(math.sin(b)*math.sin(c))
        ang.append(math.acos(max(-1.,min(1.,cosine))))
    return sum(ang)-PI


def gaussian_integral_tail(t):
    # Half-normal order statistics: P(min/max >= t) =
    # 3 int_0^inf f(z) (F(z)-F(tz))**2 dz.
    N = 6000
    a, b = 0., 9.
    h = (b-a)/N
    total = 0.
    for i in range(N+1):
        z = a+i*h
        density = math.sqrt(2/PI)*math.exp(-z*z/2)
        p = math.erf(z/math.sqrt(2))-math.erf(t*z/math.sqrt(2))
        y = 3*density*p*p
        total += (1 if i in (0,N) else 4 if i%2 else 2)*y
    return h*total/3


def check():
    rng = random.Random(22026)
    assert abs(tail(0.)-1.) < 5e-15
    assert tail(1.) == 0.
    values = [tail(i/1000) for i in range(1001)]
    assert all(-1e-14 <= b <= a+1e-14 for a,b in zip(values,values[1:]))
    for t in [0., 0.1, 0.2, 0.35, 0.5, 0.7, 0.85]:
        g = gaussian_integral_tail(t)
        assert abs(tail(t)-g) < 2e-9, ('Gaussian integral',t,tail(t),g)
    for t in [0., 0.2, 0.5, 0.8]:
        omega = spherical_excess(t)
        assert abs(tail(t)-12*omega/PI) < 2e-12, ('spherical excess',t)
    for i in range(22000):
        n = [rng.gauss(0,1) for _ in range(3)]
        r1 = section_radius(n)
        r2 = independent_vertex_radius(n)
        assert abs(r1-r2) < 3e-15, (n,r1,r2)
        assert 1/math.sqrt(2)-1e-15 <= r1 <= 1+1e-15
    # Exact rational squared radii comparison, independent of floating point.
    for aa in range(6):
        for bb in range(6):
            for cc in range(6):
                if max(aa,bb,cc)==0:continue
                v=sorted((aa,bb,cc))
                best=Fraction(v[0]**2+v[2]**2,(v[0]+v[2])**2)
                pairs=[(aa,bb),(aa,cc),(bb,cc)]
                vals=[Fraction(x*x+y*y,(x+y)**2) for x,y in pairs if x+y]
                assert max(vals)==best, (aa,bb,cc)
    # Independent random sampling, fixed seed, loose statistical tolerance.
    trials=180000
    thresholds=[0.25,0.5,0.75]
    hits=[0,0,0]
    for _ in range(trials):
        v=sorted(abs(rng.gauss(0,1)) for _ in range(3))
        ratio=v[0]/v[2]
        for i,t in enumerate(thresholds):
            hits[i]+=(ratio>=t)
    for t,k in zip(thresholds,hits):
        assert abs(k/trials-tail(t))<0.006, (t,k/trials,tail(t))
    # Inversion of the diameter parametrization on the open support.
    for t in [0.,0.04,0.25,0.5,0.8,0.999]:
        r=math.sqrt(1+t*t)/(1+t)
        t2=(1-r*r)/(r*r+math.sqrt(max(0.,2*r*r-1)))
        assert abs(t-t2)<1e-9, (t,t2)
    print('VERIFY_OK:',
          '7 Gaussian-integral comparisons;',
          '4 spherical-excess comparisons;',
          '22000 radius checks;',
          '215 rational-coordinate tests;',
          '180000 sampled normals;',
          '6 inverse checks')

if __name__=='__main__':
    check()
