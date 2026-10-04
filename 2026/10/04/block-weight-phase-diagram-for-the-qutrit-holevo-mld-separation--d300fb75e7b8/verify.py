#!/usr/bin/env python3
import math

CASES = [
    # r, a, b, c, h; includes RLD-limit and interior regimes.
    (0.40, 2.0, 1.0, 0.30, 1.0),
    (0.70, 1.0, 1.0, 0.00, 3.0),
    (0.30, 4.0, 2.0, 1.00, 0.5),
    (0.55, 1.7, 2.3, -0.40, 2.4),
]

def close(x, y, tol=2e-10):
    return abs(x-y) <= tol * max(1.0, abs(x), abs(y))

def run_case(r,a,b,c,h):
    D = a*b-c*c
    assert 0 < r < 1 and a > 0 and b > 0 and h > 0 and D > 0
    s = math.sqrt(D)
    # Inverse of W.
    wi11, wi12, wi22 = b/D, -c/D, a/D

    def fixed(beta):
        t = beta*r
        # X_beta = t*s*W^{-1}
        x = t*s*wi11
        z = t*s*wi12
        y = t*s*wi22
        detx = x*y-z*z
        trwx = a*x + 2*c*z + b*y
        assert x >= -1e-12 and y >= -1e-12
        assert close(detx, t*t, 2e-9)
        assert close(trwx, 2*t*s, 2e-9)
        return a+b+h+2*beta*r*s-h*beta*beta*r*r

    # Fixed-beta optimizer identities.
    for beta in (0.0, 0.13, 0.51, 0.91, 0.999):
        fixed(beta)

    # Analytic MLD optimum.
    if s >= h*r:
        mld = a+b+h+2*r*s-h*r*r
        beta_star = 1.0
    else:
        beta_star = s/(h*r)
        mld = a+b+h+s*s/h
        assert 0 < beta_star < 1
        assert close(fixed(beta_star), mld)
    # Dense-grid upper check (not the proof).
    grid_max = max(fixed(k/10000.0) for k in range(10000))
    assert grid_max <= mld + 2e-7

    # Joint minimizer X_* = r*s*W^{-1}.
    x = r*s*wi11
    z = r*s*wi12
    y = r*s*wi22
    assert close(x*y-z*z, r*r, 2e-9)
    assert close(a*x + 2*c*z + b*y, 2*r*s, 2e-9)
    for beta in (0.0, 0.2, 0.6, 0.95, 0.999999):
        # Determinant of X_* plus the imaginary beta block.
        det_herm = x*y-z*z-(beta*r)**2
        third_slack = beta*beta*r*r
        assert det_herm >= -1e-10
        assert third_slack >= 0

    holevo = a+b+h+2*r*s
    gap = holevo-mld
    if s >= h*r:
        assert close(gap, h*r*r)
    else:
        assert close(gap, 2*r*s-s*s/h)
    assert gap > 0

for case in CASES:
    run_case(*case)
print('VERIFY_OK')
