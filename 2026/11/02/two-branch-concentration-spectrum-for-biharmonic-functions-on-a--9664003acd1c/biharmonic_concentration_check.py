"""Finite consistency checks for the biharmonic-ball concentration formulas.

This is not a proof of any all-degree or asymptotic statement.
Requires Python 3 standard library only.
"""

from fractions import Fraction
from math import comb, factorial, log, sqrt

CHECKS = 0


def require(ok, message):
    global CHECKS
    if not ok:
        raise AssertionError(message)
    CHECKS += 1


def full_gram(p):
    return ((Fraction(1, p), Fraction(1, p + 2)),
            (Fraction(1, p + 2), Fraction(1, p + 4)))


def partial_gram(p, numerator, denominator):
    t = Fraction(numerator, denominator)
    # p is any integer >= 3; p/2 may be half-integral, so the
    # common t^(p/2) factor is removed for exact rational checks.
    return ((Fraction(1, p), t / (p + 2)),
            (t / (p + 2), t * t / (p + 4)))


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def trace_g_inverse_h(g, h):
    return (g[1][1] * h[0][0] + g[0][0] * h[1][1]
            - 2 * g[0][1] * h[0][1]) / det(g)


def branches(m, d, t):
    p = 2 * m + d
    u = (p + 2)**2 * (1 - t)**2 + 8*t
    delta = sqrt(1 - 64*t*t/(u*u))
    s = (t**(p/2)) * u / 4
    plus = 0.5 * s * (1 + delta)
    # Use the determinant for stable evaluation of the smaller branch.
    minus = (t**(p + 2)) / plus
    return plus, minus


def log_branches(m, d, t):
    p = 2 * m + d
    u = (p + 2)**2 * (1 - t)**2 + 8*t
    lp = (p/2) * log(t) + log(u/8) + log(1 + sqrt(1 - 64*t*t/u**2))
    return lp, (p + 2) * log(t) - lp


def dimension(m, d):
    return comb(m + d - 1, d - 1) - (comb(m + d - 3, d - 1)
            if m >= 2 else 0)


for d in (3, 4, 5, 8):
    for m in range(13):
        p = 2*m + d
        g = full_gram(p)
        require(det(g) == Fraction(4, p*(p+4)*(p+2)**2), 'Gram determinant')
        for num, den in ((1, 5), (1, 2), (3, 4)):
            t = Fraction(num, den)
            h0 = partial_gram(p, num, den)
            exp_trace = ((p+2)**2*(1-t)**2 + 8*t)/4
            require(trace_g_inverse_h(g, h0) == exp_trace, 'Gram trace')
            require(det(h0)/det(g) == t*t, 'scaled Gram product')
            pp, mm = branches(m, d, float(t))
            require(0 < mm < pp < 1, 'positive strict contraction')
            require(abs((pp+mm) - float(exp_trace)*float(t)**(p/2))
                    < 1e-12, 'quadratic sum')
            require(abs((pp*mm)/(float(t)**(p+2)) - 1) < 1e-9,
                    'quadratic product')

for d in (3, 4, 7):
    for t in (0.12, 0.37, 0.81):
        for m in range(150):
            a, b = branches(m, d, t)
            c, e = branches(m+1, d, t)
            require(c < a and e < b, 'strict degree monotonicity')

for d in (3, 4, 5):
    for t in (0.25, 0.5, 0.75):
        m = 2000
        lp, lm = log_branches(m, d, t)
        c_plus = t**(d/2)*(1-t)**2
        c_minus = t**(d/2+2)/(1-t)**2
        err_plus = lp - (m*log(t) + 2*log(m) + log(c_plus))
        err_minus = lm - (m*log(t) - 2*log(m) + log(c_minus))
        require(abs(err_plus) < 0.006 and abs(err_minus) < 0.006,
                'asymptotic constants, finite diagnostic')

for d in (3, 4, 5):
    t = 0.5
    ell = -log(t)
    for L in (300, 1000):
        cp = cm = 0
        for m in range(int(L/ell)+100):
            lp, lm = log_branches(m, d, t)
            h = dimension(m, d)
            if lp > -L:
                cp += h
            if lm > -L:
                cm += h
        gap_prediction = (8 / (factorial(d-2)*ell**(d-1))
                          * L**(d-2)*log(L))
        total_prediction = (4 / (factorial(d-1)*ell**(d-1))
                            * L**(d-1))
        require(abs((cp-cm)/gap_prediction - 1) < 0.035,
                'asymptotic gap, finite diagnostic')
        require(abs((cp+cm)/total_prediction - 1) < 0.025,
                'total counting, finite diagnostic')

print('PASS:', CHECKS, 'finite assertions')
