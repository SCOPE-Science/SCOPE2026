#!/usr/bin/env python3
"""Independent finite-parameter checks of the common-driver Ornstein--Uhlenbeck lag theorem.

Execute: python verification.py  (requires NumPy and SciPy).
Numerical checks supplement but do not prove the global assertions.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import expm, solve_continuous_lyapunov
from scipy.optimize import brentq


def kernel(a, d, b, t):
    """Sine-transform representation, stable when relaxation rates coincide."""
    den = lambda w: (w*w + a*a)*(w*w + d*d)*(w*w + b*b)
    integ, _ = quad(lambda w: w / den(w), 0, np.inf,
                    weight="sin", wvar=t, epsabs=1.e-12, limit=400)
    return 2.0 / math.pi * integ


def exponential_kernel(a, d, b, t):
    rates = (a, d, b)
    return sum(math.exp(-r*t) / math.prod(s*s-r*r
               for j, s in enumerate(rates) if i != j)
               for i, r in enumerate(rates))


def lag_asymmetry(a, d, b, c1, c2, D1, D2, Df, t):
    A = np.array([[-a, 0., c1], [0., -d, c2], [0., 0., -b]])
    Q = 2 * np.diag((D1, D2, Df))
    Sigma = solve_continuous_lyapunov(A, -Q)
    cov = expm(A * t) @ Sigma
    return cov[0, 1] - cov[1, 0]


checks = 0
cases = ((1., 2., 3.), (.7, 1.2, .4), (.2, 5., .8),
         (1., 1.01, .98), (1., 1., 1.), (3., .3, .3))
for a, d, b in cases:
    for c1, c2 in ((1., 2.), (-2., .7)):
        for t in (.05, .3, 1.5, 4.5):
            got = lag_asymmetry(a, d, b, c1, c2, .7, 2., 1.5, t)
            predicted = 3.*c1*c2*(d-a)*kernel(a, d, b, t)
            assert abs(got-predicted) < 3.e-9*(1.+abs(got)), (got,predicted)
            checks += 1
        slope = 3.*c1*c2*(d-a)/((a+b)*(d+b)*(a+d))
        epsilon = 1.e-5
        measured = lag_asymmetry(a, d, b, c1, c2, .7, 2., 1.5, epsilon)/epsilon
        assert abs(measured-slope) < 2.e-4*(1.+abs(slope)), (measured,slope)
        checks += 1

for a, d, b in cases:
    for t in np.linspace(.02, 12., 61):
        val = kernel(a,d,b,float(t))
        assert val > 0, (a,d,b,t,val)
        checks += 1

for a,d,b in cases[:4]:
    for t in (.1,.9,3.):
        assert abs(kernel(a,d,b,t)-exponential_kernel(a,d,b,t)) < 1.e-9
        checks += 1

for a,d,b in cases:
    grid=np.geomspace(1.e-3,15.,160)
    vals=np.array([kernel(a,d,b,float(t)) for t in grid])
    kmax=int(np.argmax(vals))
    assert 0 < kmax < len(grid)-1
    assert all(vals[i] < vals[i+1] + 1.e-10 for i in range(kmax-1))
    assert all(vals[i] + 1.e-10 > vals[i+1] for i in range(kmax+1,len(vals)-1))
    checks += 2

phi=(1.+math.sqrt(5.))/2.
for a in (.5, 1., 3.):
    theoretical=math.exp(-a*(phi/a))*phi*(phi+1.)/(8*a**4)
    assert abs(kernel(a,a,a,phi/a)-theoretical) < 1.e-10
    assert abs(kernel(a,a,a,(phi+.01)/a)) < kernel(a,a,a,phi/a)
    assert abs(kernel(a,a,a,(phi-.01)/a)) < kernel(a,a,a,phi/a)
    checks += 3
print(f"PASS: {checks} independent finite checks")
