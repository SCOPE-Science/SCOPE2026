#!/usr/bin/env python3
"""Finite decimal diagnostics for a scalar sigmoidal bounded-confidence flow.

Proof of the full large-parameter theorem is analytical and appears in RESULT.md.
"""
from decimal import Decimal as D, getcontext
getcontext().prec = 150


def F(x, delta, gamma):
    return ((1-x) * (gamma*((1+x)**2-delta)).exp()
            - (1+x) * (gamma*((1-x)**2-delta)).exp() - 2*x)


def dF(x, delta, gamma):
    a = (gamma*((1+x)**2-delta)).exp()
    b = (gamma*((1-x)**2-delta)).exp()
    return a*(-1+2*gamma*(1-x*x))-b*(1-2*gamma*(1-x*x))-2


def bisect(a, b, delta, gamma):
    fa, fb = F(a,delta,gamma), F(b,delta,gamma)
    assert fa < 0 < fb or fb < 0 < fa, (a,b,fa,fb)
    for _ in range(550):
        mid = (a+b)/2
        fm = F(mid,delta,gamma)
        if fm == 0:
            return mid
        if (fm > 0) == (fa > 0):
            a, fa = mid, fm
        else:
            b, fb = mid, fm
        if b == a:
            break
    return (a+b)/2


def check(ds, g):
    delta, gamma = D(ds), D(g)
    h = delta.sqrt() - 1
    assert 0 < h < 1
    assert dF(D(0), delta, gamma) < 0
    half = (1+h)/2
    u = bisect(h/20, half, delta, gamma)
    v = bisect(half, D(1), delta, gamma)
    assert 0 < u < v < 1
    assert dF(u,delta,gamma) > 0 and dF(v,delta,gamma) < 0
    assert F(u/2,delta,gamma) < 0
    assert F((u+v)/2,delta,gamma) > 0
    assert F((v+1)/2,delta,gamma) < 0
    assert F(-u,delta,gamma) == -F(u,delta,gamma) or abs(F(-u,delta,gamma)+F(u,delta,gamma)) < D('1e-90')
    pred_u = h + (2*h/(1-h)).ln() / (2*delta.sqrt()*gamma)
    pred_tail = 2 * (-gamma*(4-delta)).exp()
    assert abs((u-pred_u)*gamma*gamma) < 20
    assert abs((1-v)/pred_tail - 1) < D('0.002')
    # Equation (2.1) reconstructed independently from both sigmoid weights.
    for x in (D('0.05'),u/2,(u+v)/2,(v+1)/2):
        wp = 1/(1+(gamma*((1-x)**2-delta)).exp())
        wm = 1/(1+(gamma*((1+x)**2-delta)).exp())
        drift = ((1-x)*wp-(1+x)*wm)/(wp+wm)
        assert (drift > 0) == (F(x,delta,gamma) > 0)
    print('delta=',ds,'gamma=',g,'barrier=',str(u)[:35],
          'outer=',str(v)[:35],'tail=',str(1-v)[:28])


if __name__ == '__main__':
    for d in ('1.2','2','3.5'):
        for g in (30,40):
            check(d,g)
    print('CHECK_OK: six high-precision parameter pairs; proof is analytical.')
