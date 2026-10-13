import math

LN2 = math.log(2.0)

def h2(x):
    if x == 0.0 or x == 1.0:
        return 0.0
    return (-x*math.log(x) - (1.0-x)*math.log(1.0-x))/LN2

def h2inv(y):
    lo, hi = 0.0, 0.5
    for _ in range(120):
        mid = (lo+hi)/2.0
        if h2(mid) < y:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2.0

def asech(x):
    return math.acosh(1.0/x)

def beta_cl(R):
    p = h2inv(1.0-R)
    return asech(1.0-2.0*p)

def beta_q(R):
    q = h2inv(R)
    direct = asech(2.0*math.sqrt(q*(1.0-q)))
    closed = 0.5*math.log((1.0-q)/q)
    if abs(direct-closed) > 2e-11*max(1.0, abs(closed)):
        raise AssertionError((R,direct,closed))
    return closed

# Corroborative finite checks of the exact identity and endpoint normalizations.
for R in [0.001, 0.01, 0.1, 0.5, 0.9, 0.99, 0.999]:
    assert beta_q(R) > beta_cl(R) > 0.0

for eps in [1e-4, 1e-6, 1e-8]:
    R = 1.0-eps
    L = math.log(1.0/eps)
    rq = beta_q(R)/math.sqrt(2.0*LN2*eps)
    rc = beta_cl(R)/(2.0*math.sqrt(LN2*eps/L))
    rr = (beta_q(R)/beta_cl(R))/math.sqrt(L/2.0)
    assert 0.75 < rq < 1.25 and 0.70 < rc < 1.35 and 0.65 < rr < 1.45

for R in [1e-4, 1e-6, 1e-8]:
    L = math.log(1.0/R)
    d = beta_q(R)-beta_cl(R)
    approx = 0.5*math.log(L)-0.5*LN2
    # Slow logarithmic convergence; require only consistency of sign and scale.
    assert d > 0.0 and abs(d-approx) < 0.35
    assert 0.75 < beta_q(R)/beta_cl(R) < 1.6

print('VERIFY_OK')
