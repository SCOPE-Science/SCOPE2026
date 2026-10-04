#!/usr/bin/env python3
from math import isclose

def h_direct(lam, lp, lm):
    w_plus = lp / (lp + lm)
    w_minus = lm / (lp + lm)
    d_plus = lam / (lp - lam)
    d_minus = -lam / (lm + lam)
    return w_plus * d_plus + w_minus * d_minus

def h_closed(lam, lp, lm):
    return lam * lam / ((lp - lam) * (lm + lam))

def check(mu, L, lp, lm):
    assert 0.0 < mu < L < lp and L < lm
    vals = {}
    for lam in (-L, -mu, mu, L):
        a = h_direct(lam, lp, lm)
        b = h_closed(lam, lp, lm)
        assert a > 0.0
        assert isclose(a, b, rel_tol=1e-13, abs_tol=1e-15)
        vals[lam] = a
    kappa_v = max(vals.values()) / min(vals.values())
    kappa = L / mu
    pair_bound = kappa**2 * (((lp*lp-mu*mu)*(lm*lm-mu*mu))/((lp*lp-L*L)*(lm*lm-L*L)))**0.5
    assert kappa_v + 1e-12 >= pair_bound
    assert pair_bound > kappa**2
    eta = 2.0 / (min(vals.values()) + max(vals.values()))
    q = max(abs(1.0 - eta*v) for v in vals.values())
    q_formula = (kappa_v - 1.0) / (kappa_v + 1.0)
    assert isclose(q, q_formula, rel_tol=1e-12, abs_tol=1e-14)
    assert q > (kappa**2 - 1.0) / (kappa**2 + 1.0)
    return kappa_v, pair_bound, q

for args in [
    (1.0, 5.0, 7.0, 9.0),
    (2.0, 6.0, 6.5, 11.0),
    (1.0, 3.0, 10.0, 4.0),
    (1.0, 8.0, 80.0, 120.0),
]:
    kv, lower, q = check(*args)
    print('case', args, 'kappa_V=', format(kv, '.12g'), 'lower=', format(lower, '.12g'), 'q=', format(q, '.12g'))

# The analytic limit is checked numerically along a diverging symmetric sequence.
mu, L = 1.0, 5.0
last = None
for R in (10.0, 30.0, 100.0, 1000.0, 10000.0):
    kv, _, _ = check(mu, L, R, R)
    if last is not None:
        assert kv < last
    last = kv
assert abs(last - (L/mu)**2) < 1e-4
print('VERIFY_OK')
