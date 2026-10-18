#!/usr/bin/env python3
"""Independent high-precision numerical checks for Gaussian annular localization.

Dependencies: Python 3 and mpmath. Scientific proof for all parameters is in RESULT.md.
"""
import mpmath as mp

mp.mp.dps = 65
checks = 0

def check(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)

def eig(n, a, w):
    return mp.gammainc(n + 1, a, a + w) / mp.factorial(n)

def pmf(n, u):
    if u == 0:
        return mp.mpf(1) if n == 0 else mp.mpf(0)
    return mp.exp(-u + n * mp.log(u) - mp.loggamma(n + 1))

def threshold(a, w):
    return w / mp.log1p(w / a) if a > 0 else mp.mpf(0)

def close(a, b, atol=mp.mpf('1e-48')):
    return abs(a - b) <= atol * (1 + abs(a) + abs(b))

# Incomplete-gamma integrals versus the exact boundary difference identity.
for w in ['0.25', '1', '2.5']:
    w = mp.mpf(w)
    for a in ['0', '0.1', '0.75', '2.4', '12.125', '40.5']:
        a = mp.mpf(a)
        for n in [0, 1, 2, 4, 8, 17, 42]:
            difference = eig(n + 1, a, w) - eig(n, a, w)
            boundary = (mp.exp(-a) * a ** (n + 1)
                        - mp.exp(-a - w) * (a + w) ** (n + 1)) / mp.factorial(n + 1)
            check(close(difference, boundary), 'boundary difference')
            h = threshold(a, w)
            if a > 0:
                sgn1 = mp.sign(difference)
                sgn2 = mp.sign(h - n - 1)
                check(sgn1 == sgn2, 'mode sign law')
            else:
                check(difference < 0, 'disk descending modes')

# A genuine scan of all nearby eigenvalues, not just use of the recurrence.
for w in ['0.35', '1', '2']:
    w = mp.mpf(w)
    for a in ['0', '0.4', '1.3', '4.5', '11.1', '24.7', '50.2']:
        a = mp.mpf(a)
        h = threshold(a, w)
        n = int(mp.floor(h))
        vals = [eig(j, a, w) for j in range(max(40, int(a+w)+24))]
        check(vals[n] == max(vals), 'complete bounded eigenvalue scan')
        check(vals[n] > vals[n-1] if n > 0 else True, 'left neighbor')
        check(vals[n] > vals[n+1], 'right neighbor')

# Crossing exactly ties two and only two modes, with a sharp derivative corner.
for w in ['0.4', '1', '2.3']:
    w = mp.mpf(w)
    for m in [1, 2, 3, 5, 9, 20, 50, 100]:
        a = w / mp.expm1(w / m)
        left, right = eig(m-1, a, w), eig(m, a, w)
        check(close(left, right), 'crossing tie')
        if m > 1:
            check(left > eig(m-2, a, w), 'crossing left strictness')
        check(right > eig(m+1, a, w), 'crossing right strictness')
        derivative_gap = ((pmf(m, a+w) - pmf(m, a))
                          - (pmf(m-1, a+w) - pmf(m-1, a)))
        predicted_jump = w * pmf(m-1, a) / (a+w)
        check(close(derivative_gap, predicted_jump), 'derivative cusp jump')
        check(predicted_jump > 0, 'positive corner')

# The periodic coefficient is an actual limit profile, not a constant.
for w in ['0.5', '1', '3']:
    w = mp.mpf(w)
    for c in ['30.25', '50.5', '100.7', '200', '500.25', '1000.5']:
        c = mp.mpf(c)
        a = c - w/2
        n = int(mp.floor(threshold(a, w)))
        theta = c - mp.floor(c)
        coeff = -(theta**2-theta+mp.mpf(1)/6)/2-w**2/24
        scaled = c*(mp.sqrt(2*mp.pi*c)*eig(n,a,w)/w-1)
        check(abs(scaled-coeff) < 2*(1+w**4)/c, 'Bernoulli second-order residual')

print('PASS:', checks, 'high-precision assertions (finite tests; proof is analytic).')
