"""Reproduce the exact two-kernel spreading-speed comparison.

Requires Python 3.9+ standard library only.  This numerical test supports,
but does not replace, the algebraic proof of the all-parameter theorem.
"""
import math
import random


def root_bisect(fn, a, b, iterations=100):
    fa, fb = fn(a), fn(b)
    assert fa <= 0 <= fb, (a, b, fa, fb)
    for _ in range(iterations):
        m = (a + b) / 2
        if fn(m) < 0:
            a = m
        else:
            b = m
    return (a + b) / 2


def psi(q, t):
    """Log moment-generating function and its first derivative."""
    if q == 0:
        return (math.log(math.cosh(t)), math.tanh(t))
    logs = [math.log(1-q), math.log(q/2) + 2*t, math.log(q/2) - 2*t] if q < 1 else [math.log(.5)+2*t, math.log(.5)-2*t]
    m = max(logs)
    ws = [math.exp(x-m) for x in logs]
    z = sum(ws)
    if q < 1:
        v = (2*ws[1] - 2*ws[2])/z
    else:
        v = (2*ws[0] - 2*ws[1])/z
    return (m + math.log(z), v)


def speed(q, ell):
    maxstep = 1 if q == 0 else 2
    at_max = math.log(2) if q == 0 else math.log(2/q)
    if ell >= at_max:
        return float(maxstep)
    def loss(t):
        f, v = psi(q, t)
        return t*v - f
    hi = 1.0
    while loss(hi) < ell:
        hi *= 2
        assert hi < 1024
    t = root_bisect(lambda a: loss(a)-ell, 0.0, hi)
    return psi(q, t)[1]


def rate(q, v):
    assert 0 <= v <= 1
    if v == 0:
        return 0.0
    if q == 0 and v == 1:
        return math.log(2)
    hi = 1.0
    while psi(q, hi)[1] < v:
        hi *= 2
        assert hi < 1024
    t = root_bisect(lambda x: psi(q, x)[1]-v, 0., hi)
    f, _ = psi(q, t)
    return t*v-f


def q_critical():
    z = root_bisect(lambda z: z**3-4*z**2+3*z-4, 3., 4.)
    return 2*z*z/((z*z+3)*(z*z-1))


def threshold(q):
    assert 0 < q < .25
    qc = q_critical()
    if q <= qc:
        return rate(q, 1.)
    # At q>qc, the first positive zero of J is in (0,1), after its maximum.
    t0 = math.asinh(math.sqrt((1-4*q)/(2*q)))
    v0 = math.tanh(t0)
    vstar = root_bisect(lambda v: rate(0., v)-rate(q, v), v0, 1.)
    return rate(0., vstar)


def run():
    rng = random.Random(20261124)
    qc = q_critical()
    assert .1452003 < qc < .1452004
    assert abs(rate(qc, 1)-math.log(2)) < 4e-13
    assert abs(threshold(.125)-math.log(2.1327104114122517)) < 2e-12
    assert abs(speed(0, math.log(5))-1) < 1e-12
    assert abs(speed(.125, math.log(50))-2) < 1e-12
    # Test exact algebraic MGF factorization on random positive tilts.
    for _ in range(2000):
        q = rng.random()
        t = rng.random()*3
        left = (1-q)+q*math.cosh(2*t)-math.cosh(t)
        right = (math.cosh(t)-1)*(2*q*(math.cosh(t)+1)-1)
        assert abs(left-right) < 1e-10
    # Verify single-change ordering against direct minimizations.
    for _ in range(6000):
        q = .005 + .99*rng.random()
        ell = .005 + 5.5*rng.random()
        c0, cq = speed(0., ell), speed(q, ell)
        if q >= .25:
            assert cq > c0 - 2e-10, (q, ell, c0, cq)
        else:
            ell_star = threshold(q)
            if abs(ell-ell_star) > 1e-7:
                assert (cq > c0) == (ell > ell_star), (q, ell, ell_star, c0, cq)
    # Critical and either side: boundary formulas in both regimes.
    for q in (.03, .125, qc, .2, .24, .25, .7):
        if q < .25:
            ellstar = threshold(q)
            assert abs(speed(q, ellstar)-speed(0., ellstar)) < 5e-10
            eps = min(.01, ellstar/5)
            assert speed(q, ellstar-eps) < speed(0., ellstar-eps)
            assert speed(q, ellstar+eps) > speed(0., ellstar+eps)
        else:
            for ell in (.01, .1, .5, 1.0, 2.0, 5.0):
                assert speed(q, ell) > speed(0, ell)
    print('PASS: 2,000 MGF identities; 6,000 direct speed comparisons; boundary/threshold tests')
    print('q_critical',format(qc,'.15f'))
    for q in (.125, .2):
        ellstar = threshold(q)
        print('q',q,'R_switch',format(math.exp(ellstar),'.15f'),
              'speed_at_switch',format(speed(0, ellstar),'.15f'))

if __name__ == '__main__':
    run()
