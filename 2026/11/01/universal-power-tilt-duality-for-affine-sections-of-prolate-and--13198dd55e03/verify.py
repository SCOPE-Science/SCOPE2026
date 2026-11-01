#!/usr/bin/env python3
"""Standalone numerical checks for spheroid section shape duality.
Run: python3 verify.py   (Python 3 standard library only).
"""
import math
import random


def simpson(f, lo=0.0, hi=1.0, steps=4096):
    assert steps % 2 == 0
    h = (hi-lo)/steps
    total = f(lo)+f(hi)
    for j in range(1,steps):
        total += (4 if j % 2 else 2)*f(lo+j*h)
    return h*total/3


def parameters(dim, k):
    assert dim >= 3 and k > 1
    b = k*k-1
    alpha = (dim-3)/2
    p = lambda u: math.sqrt(1+b*u*u)*max(0,1-u*u)**alpha
    o = lambda u: math.sqrt(k*k-b*u*u)/k*max(0,1-u*u)**alpha
    return b, alpha, p, o, simpson(p), simpson(o)


def p_density(r, d, k, b, alpha, jp):
    return k**d*(r*r-1)**alpha/(b**((d-2)/2)*jp*r**d*math.sqrt(k*k-r*r))


def o_density(r, d, k, b, alpha, jo):
    return r*r*(r*r-1)**alpha/(k*b**((d-2)/2)*jo*math.sqrt(k*k-r*r))


def survival(r, d, k, version):
    b, alpha, p, o, jp, jo = parameters(d, k)
    if version == 'p':
        u = math.sqrt((k*k-r*r)/(b*r*r))
        return simpson(p, 0, u)/jp
    u = math.sqrt((k*k-r*r)/b)
    return simpson(o, 0, u)/jo


def test_exact():
    for d in (3, 4, 7, 15):
        for k in (1.25, 2, 3):
            b, alpha, p, o, jp, jo = parameters(d,k)
            moment = k**(d+1)*jo/jp
            for frac in (.1, .4, .75, .95):
                r = 1+frac*(k-1)
                fp = p_density(r, d, k,b,alpha,jp)
                fo = o_density(r, d, k,b,alpha,jo)
                assert abs(fo/fp-r**(d+2)/moment) < 1e-10*max(1,fo/fp)
            threshold = moment**(1/(d+2))
            tv = survival(threshold,d,k,'o')-survival(threshold,d,k,'p')
            assert 0 < tv < 1
            assert 1 < threshold < k
            # transformation is a strict monotone-likelihood-ratio tilt
            assert survival(1+.2*(k-1),d,k,'o') > survival(1+.2*(k-1),d,k,'p')
    print('EXACT_DENSITY_RATIO_AND_STOCHASTIC_ORDER_PASSED')


def direct_shape_ratio(n, k, oblate):
    """Independent quadratic-form restriction in a three-dimensional section."""
    nz = n[-1]
    s = math.sqrt(1-nz*nz)
    v = (-nz*n[0]/s, -nz*n[1]/s, s)
    w = (n[1]/s, -n[0]/s, 0.)
    q = (1.,1.,k*k if oblate else 1./(k*k))
    a = sum(q[j]*v[j]*v[j] for j in range(3))
    c = sum(q[j]*w[j]*w[j] for j in range(3))
    z = sum(q[j]*w[j]*v[j] for j in range(3))
    assert abs(z)<1e-10
    return math.sqrt(max(a,c)/min(a,c))


def test_independent_geometry():
    rng = random.Random(52831)
    k = 2.; d = 3
    b,alpha,p,o,jp,jo = parameters(d,k)
    moment=k**(d+1)*jo/jp
    t=moment**(1/(d+2))
    for oblate in (False,True):
        count = hits = 0
        while count < 30000:
            n=[rng.gauss(0,1) for _ in range(3)]
            nr=math.sqrt(sum(z*z for z in n))
            n=[z/nr for z in n]
            u=abs(n[2])
            h=math.sqrt(1+b*u*u) if not oblate else math.sqrt(k*k-b*u*u)/k
            # Rejection samples the width-weighted orientation marginal.
            if rng.random() > h/(k if not oblate else 1):
                continue
            count+=1
            _offset=(2*rng.random()-1)*h
            rr=direct_shape_ratio(n,k,oblate)
            hits += rr>=t
        exact=survival(t,d,k,'o' if oblate else 'p')
        empirical=hits/count
        assert abs(empirical-exact)<.014,(oblate,empirical,exact)
    print('INDEPENDENT_THREEDIMENSIONAL_QUADRATIC_FORM_TEST_PASSED')


def test_limit():
    for k in (1.2,2.,4.):
        b=k*k-1
        limiting=math.erf(math.sqrt(k*k*math.log(k)/b))-math.erf(math.sqrt(math.log(k)/b))
        d=150
        _,_,_,_,jp,jo=parameters(d,k)
        # logarithms avoid unstable large powers for the threshold
        t=math.exp(((d+1)*math.log(k)+math.log(jo/jp))/(d+2))
        scaled=d*(k-t)
        tv=survival(t,d,k,'o')-survival(t,d,k,'p')
        assert abs(tv-limiting)<.020, (k,tv,limiting)
        assert abs(scaled-k*math.log(k))<.14, (k,scaled,k*math.log(k))
    print('SHARP_HIGH_DIMENSIONAL_TV_LIMIT_CHECK_PASSED')


if __name__=='__main__':
    test_exact()
    test_independent_geometry()
    test_limit()
    print('ALL_CHECKS_PASSED')
