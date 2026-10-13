#!/usr/bin/env python3
import mpmath as mp
mp.mp.dps = 80


def gamma_of_x(d, x):
    d = mp.mpf(d)
    return x * (2*d*(1-x)/(1-2*d*x)) ** ((d-1)/(d+1))


def delta_of_x(d, x):
    d = mp.mpf(d)
    return (((1-x)**d * (1-2*d*x))/(2*d)) ** (1/(d+1))


def boundary(d, gamma):
    gamma = mp.mpf(gamma)
    lo = mp.mpf('0')
    hi = (mp.mpf(1)/(2*d))*(1-mp.mpf('1e-50'))
    assert gamma_of_x(d, hi) > gamma
    for _ in range(260):
        mid = (lo+hi)/2
        if mid == lo or mid == hi:
            break
        if gamma_of_x(d, mid) < gamma:
            lo = mid
        else:
            hi = mid
    x = (lo+hi)/2
    return x, delta_of_x(d, x)


def source_quartic(gamma, delta):
    g = mp.mpf(gamma)
    z = mp.mpf(delta)
    return 16*g**2*z**4 + 24*g**3*z**2 + (16*g**5-4*g**2)*z - 3*g**4

max_ab_err = mp.mpf('0')
max_quartic_rel = mp.mpf('0')
checks = 0
for d in range(2, 41):
    for gamma in ('1.01', '1.2', '2', '7', '50', '1000'):
        g = mp.mpf(gamma)
        x, D = boundary(d, g)
        assert 0 < x < mp.mpf(1)/(2*d)
        eps = (x/g) ** (mp.mpf(1)/(d-1))
        A = eps - g*eps**d
        B = (1-2*d*g*eps**(d-1))/(2*d*eps**d)
        scale = max(mp.mpf(1), abs(D), abs(A), abs(B))
        err = max(abs(A-D)/scale, abs(B-D)/scale)
        max_ab_err = max(max_ab_err, err)
        assert err < mp.mpf('1e-60')
        delta = mp.mpf('0.999')*D
        assert delta + g*eps**d <= eps
        assert 2*d*g*eps**(d-1) + 2*d*delta*eps**d < 1
        N = 2*d*(d+1)*x*x - 6*d*x + d + 1
        assert N > 0
        checks += 1
        if d == 2:
            q = source_quartic(g, D)
            norm = max(mp.mpf(1), 3*g**4)
            rel = abs(q)/norm
            max_quartic_rel = max(max_quartic_rel, rel)
            assert rel < mp.mpf('1e-55')

asymptotic_err = mp.mpf('0')
for d in (2, 3, 5, 10):
    g = mp.mpf('1e12')
    _, D = boundary(d, g)
    C = mp.mpf(2*d-1)/(mp.mpf(2*d)**(mp.mpf(d)/(d-1)))
    scaled = D * g**(mp.mpf(1)/(d-1))
    rel = abs(scaled/C - 1)
    asymptotic_err = max(asymptotic_err, rel)
    assert rel < mp.mpf('0.002')

print("VERIFY_OK checks=%d degrees=2..40 max_ab_err=%s d2_quartic_rel=%s asymptotic_rel=%s" %
      (checks, mp.nstr(max_ab_err, 5), mp.nstr(max_quartic_rel, 5), mp.nstr(asymptotic_err, 5)))
