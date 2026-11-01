#!/usr/bin/env python3
"""Reproducible mathematical checks for the Haar cube-shadow circumradius law.

Only Python 3 standard library is required. These checks supplement, rather
than replace, the continuum proof in RESULT.md.
"""
import itertools
import math
import random

PI = math.pi
SQ3 = math.sqrt(3.0)
CRIT_T = 1.0 / SQ3
CRIT_R = math.sqrt(8.0 / 3.0)


def simpson(func, lo, hi, steps=800):
    if hi <= lo:
        return 0.0
    if steps % 2:
        raise ValueError('steps must be even')
    h = (hi - lo) / steps
    total = func(lo) + func(hi)
    for j in range(1, steps):
        total += (4 if j % 2 else 2) * func(lo + h * j)
    return total * h / 3.0


def probability_h_ge(t):
    """Exact one-dimensional-quadrature formula for P(|c-a-b| >= t)."""
    if t < 0:
        return 1.0
    if t >= 1:
        return 0.0
    def terms(phi):
        s = math.cos(phi) + math.sin(phi)
        q = 1.0 + s*s
        root = math.sqrt(q-t*t)
        return (s, q, root)
    def left(phi):
        s, q, root = terms(phi)
        return 1.0 - (t+s*root)/q
    accum = simpson(left, 0, PI/4)
    if t < CRIT_T:
        phi_min = math.acos(math.sqrt((1-t*t)/(1+t*t)))
        def right(phi):
            s, q, root = terms(phi)
            return (-t+s*root)/q-math.cos(phi)/math.sqrt(1+math.cos(phi)**2)
        accum += simpson(right, phi_min, PI/4)
    return (12.0/PI)*accum


def cumulative_r(r):
    if r < math.sqrt(2):
        return 0.0
    if r >= SQ3:
        return 1.0
    return probability_h_ge(math.sqrt(3-r*r))


def norm(v):
    return math.sqrt(sum(x*x for x in v))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])


def direction(rng):
    v = [rng.gauss(0.0, 1.0) for _ in range(3)]
    n = norm(v)
    return tuple(x/n for x in v)


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def projected_vertex_radius(u):
    # Independent direct orthogonal coordinates, not the order-statistic formula.
    e0 = (0.,0.,1.) if abs(u[2]) < 0.95 else (0.,1.,0.)
    a = cross(u,e0)
    a = tuple(x/norm(a) for x in a)
    b = cross(u,a)
    return max(math.hypot(dot(v,a),dot(v,b))
               for v in itertools.product((-1.,1.),repeat=3))


def signed_sum_radius(u):
    a,b,c = sorted(abs(x) for x in u)
    return math.sqrt(3-(c-a-b)**2)


def main():
    rng = random.Random(1729)
    assert cumulative_r(0.0) == 0.0
    assert abs(cumulative_r(math.sqrt(2))) < 1e-12
    assert abs(cumulative_r(SQ3)-1.0)<1e-15
    assert abs(probability_h_ge(0.0)-1.0)<2e-10
    prev = 0.0
    for i in range(1,201):
        r = math.sqrt(2)+(SQ3-math.sqrt(2))*i/200
        value = cumulative_r(r)
        assert prev-3e-10<=value<=1+3e-10,(i,prev,value)
        prev = value
    for _ in range(800):
        u = direction(rng)
        r1 = projected_vertex_radius(u)
        r2 = signed_sum_radius(u)
        assert abs(r1-r2)<2e-12,(r1,r2)
    # Independent analytical integration: spherical event by two-dimensional
    # rectangular midpoint quadrature over the sorted positive octant.
    def independent_spherical_cdf(t, size=1050):
        count = 0.0
        total = 0.0
        for i in range(size):
            phi=(i+0.5)*PI/(4*size)
            st_max = math.atan(1/math.cos(phi))
            for j in range(175):
                theta=(j+0.5)*st_max/175
                x=math.sin(theta)*math.sin(phi)
                y=math.sin(theta)*math.cos(phi)
                z=math.cos(theta)
                weight=math.sin(theta)*st_max
                total += weight
                if abs(z-x-y)>=t:
                    count += weight
        return count/total
    for t in (0.15,0.4,CRIT_T,0.72):
        exact=probability_h_ge(t)
        direct=independent_spherical_cdf(t,size=260)
        assert abs(exact-direct)<0.009,(t,exact,direct)
    # Tests of the two endpoint laws and the interior second-derivative jump.
    eps = 0.003
    low = cumulative_r(math.sqrt(2)+eps)
    assert abs(low/((6/PI)*eps**2)-1)<0.025
    high = 1-cumulative_r(SQ3-eps)
    target=(4/SQ3)*math.sqrt(3-(SQ3-eps)**2)
    assert abs(high/target-1)<0.06
    def second_branch(t):
        if t>=CRIT_T:return 0.0
        bottom=math.acos(math.sqrt((1-t*t)/(1+t*t)))
        def right(phi):
            s=math.sin(phi)+math.cos(phi)
            q=1+s*s
            return (-t+s*math.sqrt(q-t*t))/q-math.cos(phi)/math.sqrt(1+math.cos(phi)**2)
        return 12/PI*simpson(right,bottom,PI/4)
    delta=0.0015
    observed=second_branch(CRIT_T-delta)/delta**2
    expected=9*SQ3/(4*PI)
    assert abs(observed/expected-1)<0.015,(observed,expected)
    # Monte Carlo is a diagnostic independent of the order-statistic quadrature.
    N=120000
    thresholds=(0.15,0.4,CRIT_T,0.72)
    hits=[0]*len(thresholds)
    for _ in range(N):
        u=direction(rng)
        r=projected_vertex_radius(u)
        h=math.sqrt(max(0.0,3-r*r))
        for k,t in enumerate(thresholds):
            hits[k]+=h>=t
    for t,hits_count in zip(thresholds,hits):
        observed=hits_count/N
        expected=probability_h_ge(t)
        assert abs(observed-expected)<0.011,(t,observed,expected)
    print('ALL_CUBE_SHADOW_CIRCUMRADIUS_CHECKS_PASSED')

if __name__=='__main__':
    main()
