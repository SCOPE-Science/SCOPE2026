#!/usr/bin/env python3
from fractions import Fraction
from math import comb, log, sqrt, erf


def prob_count(n, q, s):
    return Fraction(comb(n, s), 1) * q**s * (1-q)**(n-s)


def ru_zero_from_definition(n, q, t, s):
    # RU is defined exactly for 0 < s < n.
    if s == 0 or s == n:
        return False
    y = Fraction(s, n)
    nb_all = (y - t) / (1 - t)
    default = max(Fraction(0), nb_all)
    if q >= t:  # perfect predictor treats all
        model = nb_all
    else:       # perfect predictor treats none
        model = Fraction(0)
    return model == default


def ru_zero_from_formula(n, q, t, s):
    if s == 0 or s == n:
        return False
    if q >= t:
        return Fraction(s, n) >= t
    return Fraction(s, n) <= t


def exact_check(n, q, t):
    p_def = Fraction(0)
    p_zero_definition = Fraction(0)
    p_zero_formula = Fraction(0)
    for s in range(n+1):
        p = prob_count(n, q, s)
        if 0 < s < n:
            p_def += p
        if ru_zero_from_definition(n, q, t, s):
            p_zero_definition += p
        if ru_zero_from_formula(n, q, t, s):
            p_zero_formula += p
    assert p_def == 1 - q**n - (1-q)**n
    assert p_zero_definition == p_zero_formula
    return p_zero_definition / p_def


def binom_probs_float(n, q):
    # Stable enough for the moderate n and q used below.
    p = (1-q)**n
    out = [p]
    for s in range(n):
        p *= (n-s) / (s+1) * q / (1-q)
        out.append(p)
    return out


def conditional_zero_float(n, q, t):
    ps = binom_probs_float(n, q)
    denom = 1.0 - ps[0] - ps[-1]
    if q >= t:
        lo = max(1, int(n*t) if (n*t).is_integer() else int(n*t)+1)
        num = sum(ps[lo:n])
    else:
        hi = min(n-1, int(n*t))
        num = sum(ps[1:hi+1])
    return num / denom


def conditional_failure_float(n, q, t):
    ps = binom_probs_float(n, q)
    denom = 1.0 - ps[0] - ps[-1]
    if q >= t:
        lo = max(1, int(n*t) if (n*t).is_integer() else int(n*t)+1)
        num = sum(ps[1:lo])
    else:
        hi = min(n-1, int(n*t))
        num = sum(ps[hi+1:n])
    return num / denom


def kl(t, q):
    return t*log(t/q) + (1-t)*log((1-t)/(1-q))


def phi(x):
    return 0.5*(1+erf(x/sqrt(2)))


cases = [
    (5, Fraction(1,5), Fraction(1,10)),
    (10, Fraction(1,5), Fraction(3,10)),
    (10, Fraction(1,2), Fraction(1,2)),
    (17, Fraction(7,10), Fraction(2,5)),
    (17, Fraction(3,10), Fraction(2,5)),
]
for c in cases:
    exact_check(*c)

# Diagnostic convergence for the fixed off-threshold exponent.
t = 0.30
q = 0.60
D = kl(t, q)
rates = []
for n in (100, 200, 400):
    failure = conditional_failure_float(n, q, t)
    rates.append(-log(failure)/n)
assert abs(rates[-1] - D) < 0.03

# Diagnostic convergence in a root-n local window.
t = 0.30
c = 0.50
n = 1600
q = t + c/sqrt(n)
z = conditional_zero_float(n, q, t)
target = phi(abs(c)/sqrt(t*(1-t)))
assert abs(z-target) < 0.03

print('exact conditional values:', [str(exact_check(*c)) for c in cases])
print('large-deviation rates:', rates, 'target:', D)
print('local-window value:', z, 'target:', target)
print('VERIFY_OK')
