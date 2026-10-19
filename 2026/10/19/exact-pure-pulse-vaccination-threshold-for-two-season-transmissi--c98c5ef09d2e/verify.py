#!/usr/bin/env python3
"""Independent numerical and algebraic consistency checks for the two-season pulse theorem.

Uses only the Python standard library. These checks supplement, but do not replace,
the proof of global optimality over arbitrary periodic measures.
"""
import math


def threshold(T, h, delta, high, low):
    assert T > h > 0 and delta > 0 and high > low > 0
    r = math.exp(-delta * T)
    s = math.exp(-delta * h)
    b = high * (1 - s) + low * (s - r)
    qh = math.log(high * (1 - r) / b)
    ql = math.log(b / (low * (1 - r)))
    assert qh > 0 and ql > 0
    return min(qh, ql), qh, ql, b


def objective_two_pulses(T, h, delta, high, low, q, t, eps):
    """Exact interval integration, with masses q-eps at t=0 and eps at t."""
    assert 0 < t < T and 0 <= eps <= q
    a, b = math.exp(-(q - eps)), math.exp(-eps)
    u = math.exp(-delta * t)
    v = math.exp(-delta * (T - t))
    before_zero = (1 - v + b * v * (1 - u)) / (1 - math.exp(-delta*T-q))
    state = before_zero * a
    total = 0.0
    breaks = sorted(set([0.0, t, h, T]))
    for left, right in zip(breaks, breaks[1:]):
        dt = right - left
        f = math.exp(-delta * dt)
        beta = high if (left + right)/2 < h else low
        total += beta*(dt + (state-1)*(1-f)/delta)
        state = 1 + (state - 1)*f
        if right == t:
            state *= b
    assert abs(state-before_zero) < 3e-12
    return total


def marginal(T, h, delta, high, low, q, t):
    """G(t)=S(t)*v(t) for the pure pulse q at zero, 0<t<T."""
    assert 0 < t < T
    _, _, _, b = threshold(T,h,delta,high,low)
    z = math.exp(-q)
    r = math.exp(-delta*T)
    c = (1-z)/(1-z*r)
    st = 1 - c*math.exp(-delta*t)
    v0 = b/(delta*(1-z*r))
    if t < h:
        vh = low/delta+(z*v0-low/delta)*math.exp(-delta*(T-h))
        vt = high/delta+(vh-high/delta)*math.exp(-delta*(h-t))
    else:
        vt = low/delta+(z*v0-low/delta)*math.exp(-delta*(T-t))
    return st*vt


def test_case(T, h, delta, high, low):
    qstar, qh, ql, b = threshold(T,h,delta,high,low)
    r = math.exp(-delta*T)
    for q in [0.4*qstar, qstar, 1.12*qstar]:
        z = math.exp(-q)
        v0=b/(delta*(1-z*r))
        s0=z*(1-r)/(1-z*r)
        sminus=(1-r)/(1-z*r)
        gp0=delta*v0-high*s0
        gpT=delta*z*v0-low*sminus
        assert (gp0 <= 1e-12 and gpT >= -1e-12) == (q <= qstar+1e-12)
        g0=s0*v0
        for frac in [0.025,0.20,0.8*h/T, 0.9, 0.98]:
            t=T*frac
            eps=1e-6*max(1.0,q)
            finite=(objective_two_pulses(T,h,delta,high,low,q,t,eps)
                -objective_two_pulses(T,h,delta,high,low,q,t,0.0))/eps
            predicted=g0-marginal(T,h,delta,high,low,q,t)
            assert abs(finite-predicted)<2e-5, (q,t,finite,predicted)
        if q < qstar - 1e-10:
            assert all(g0 >= marginal(T,h,delta,high,low,q,T*j/500)-1e-12
                       for j in range(1,500))
    if qh < ql:
        above=qstar+0.1*min(1,qstar)
        assert marginal(T,h,delta,high,low,above,0.001*T) > (
            math.exp(-above)*(1-r)*b/(delta*(1-math.exp(-above)*r)**2))
    elif ql < qh:
        above=qstar+0.1*min(1,qstar)
        assert marginal(T,h,delta,high,low,above,0.999*T) > (
            math.exp(-above)*(1-r)*b/(delta*(1-math.exp(-above)*r)**2))
    return qstar,qh,ql


if __name__=='__main__':
    qstar,qh,ql=test_case(1.0,0.5,1.0,1.75,0.25)
    assert 0.39097995 < qstar < 0.39097997
    assert qh < ql
    qb, qhb, qlb=test_case(1.0,0.02,1.0,2.0,1.0)
    assert qlb < qhb  # opposite loss-of-optimality side
    for T,h,d,H,L in [
        (1.0,0.25,0.6,3.0,0.7),
        (3.0,1.7,2.1,1.4,0.3),
        (1.0,0.3,0.2,1.05,1.0),
    ]:
        test_case(T,h,d,H,L)
    print('PASS: exact two-pulse integrals, directional derivatives, both transitions')
    print('Motivating example: q* = %.12f, qH = %.12f, qL = %.12f'%(qstar,qh,ql))
