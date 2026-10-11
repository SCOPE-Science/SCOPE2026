#!/usr/bin/env python3
"""Numerical cross-check of elliptic and quarter-time identities; not a proof."""
import mpmath as m
m.mp.dps = 48
J = 2 * m.log(2)
for integer_L in (4, 8, 16, 32):
    L = m.mpf(integer_L)
    Q = m.exp(L)
    g = lambda t: 1 / m.sqrt(1 - m.exp(-t))
    h = lambda w: g(L*w) * g(L*(1-w))
    I = m.quad(h, [0, m.mpf('0.5'), 1])
    physical_period_quarter = 2 * L * I / m.sqrt(Q)
    physical_period_elliptic = 4 * m.ellipk(-(Q-1))
    assert abs(physical_period_quarter / physical_period_elliptic - 1) < m.mpf('1e-20')
    assert I > 1
    assert h(m.mpf('0.5')) < I
    lo, hi = m.mpf('1e-24'), m.mpf('0.5')
    for _ in range(110):
        mid = (lo + hi) / 2
        if h(mid) > I:
            lo = mid
        else:
            hi = mid
    w = (lo+hi)/2
    assert abs(h(w)/I-1) < m.mpf('1e-22')
    Fw = m.quad(h, [0, w]) / I
    tv = 2 * (Fw-w)
    assert 0 < tv < 1
    assert abs(tv - m.quad(lambda z: abs(h(z)/I-1),[0,w,m.mpf('0.5'),1-w,1])/2) < m.mpf('1e-18')
    print('L=', integer_L, 'L*(I-1)=',m.nstr(L*(I-1),13), 'L*TV=',m.nstr(L*tv,13))
assert abs(L*(I-1) - 2*J) < m.mpf('1e-7')
assert m.quad(lambda t: g(t)-1, [0,1, 5, 15, 60, m.inf]) - J < m.mpf('1e-20')
print('CHECK_OK')
