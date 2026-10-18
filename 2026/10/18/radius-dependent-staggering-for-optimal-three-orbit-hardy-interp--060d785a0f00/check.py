"""Independent numerical checks of the explicit three-orbit Vandermonde determinant and optimizer.
Scientific notation and provenance only.
"""
import cmath
import math
import numpy as np
from scipy.optimize import differential_evolution


def nodes(m, r, s, alpha, beta):
    w = np.exp(2j * np.pi * np.arange(m) / m)
    return np.concatenate([r * np.exp(1j * alpha / m) * w,
                           r * np.exp(1j * beta / m) * w,
                           s * w])


def squared_determinant(m, r, s, alpha, beta):
    z = nodes(m, r, s, alpha, beta)
    E = np.vander(z, len(z), increasing=True)
    logabs = np.linalg.slogdet(E)[1]
    return np.exp(2 * logabs)


def product_formula(m, r, s, alpha, beta):
    R, S = r**m, s**m
    return (m ** (3 * m) * (r ** (2*m) * s ** m)**(m-1)
            * abs(R * np.exp(1j * alpha) - R * np.exp(1j * beta)) ** (2*m)
            * abs(S - R * np.exp(1j * alpha)) ** (2*m)
            * abs(S - R * np.exp(1j * beta)) ** (2*m))


def predicted_angles(m, r, s):
    q = (r / s)**m
    t = (1 + q*q - math.sqrt(1 + 34*q*q + q**4)) / (8*q)
    delta = math.acos(-t)
    return (math.pi - delta, math.pi + delta), t


def normalized_factor(q, t):
    return (1-t*t) * (1+q*q-2*q*t)**2

for m in range(1, 6):
    for r,s in [(0.31,0.95),(0.72,0.98)]:
        for a,b in [(0.57,2.67),(2.45,4.07),(0.14,0.31)]:
            v = squared_determinant(m,r,s,a,b)
            f = product_formula(m,r,s,a,b)
            assert abs(v/f-1) < 1.e-7, (m,r,s,a,b,v,f)
        (a,b), t = predicted_angles(m,r,s)
        res = differential_evolution(
            lambda angles: -product_formula(m,r,s,*angles),
            bounds=[(0, 2*math.pi)]*2, tol=1.e-9, popsize=10,
            polish=True, maxiter=280, seed=m,
        )
        value_opt = product_formula(m,r,s,a,b)
        assert (abs(-res.fun/value_opt-1) < 1e-7), (m,r,s, t, res.x, -res.fun/value_opt)
        assert normalized_factor((r/s)**m,t) > normalized_factor((r/s)**m,-0.5)
        print('m',m,'ratio-true/analytic',round(squared_determinant(m,r,s,a,b)/value_opt,12),
              'numerical-global-ratio',round(-res.fun/value_opt,12),'t',round(t,6))
print('PASS 30 determinant tests, 10 global optimization tests, and 10 strict inequalities')
