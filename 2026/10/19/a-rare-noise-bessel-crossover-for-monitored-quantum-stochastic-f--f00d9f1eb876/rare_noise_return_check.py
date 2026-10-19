#!/usr/bin/env python3
"""Independent finite-step and asymptotic checks for a monitored two-state walk.

Run with Python 3 and mpmath>=1.3: python rare_noise_return_check.py
The analytical theorem is proved in RESULT.md; these checks are supplementary.
"""
from collections import defaultdict
from fractions import Fraction
import math
import mpmath as mp

checks = 0

def check(test, message):
    global checks
    checks += 1
    if not test:
        raise AssertionError(message)


def coefficients(p, count):
    """Taylor coefficients of sqrt((1-(1-2p)z)/(1-z))."""
    out = [type(p)(1), p]
    q = 1-2*p
    for n in range(1, count):
        out.append((((1+q)*n+p)*out[n] - q*(n-1)*out[n-1])/(n+1))
    return out[:count+1]


def exact_survivals(p, steps):
    """Unconditioned two-state Markov walk, monitoring position zero after each step."""
    state = {('R', 0): Fraction(1)}
    survivors = [Fraction(1)]
    for _ in range(steps):
        new = defaultdict(Fraction)
        for (coin, x), weight in state.items():
            if coin == 'R':
                moves = [('L', x-1, 1-p), ('R', x+1, p/2), ('R', x-1, p/2)]
            else:
                moves = [('R', x+1, 1-p), ('L', x+1, p/2), ('L', x-1, p/2)]
            for c2, x2, probability in moves:
                if x2 != 0:
                    new[(c2, x2)] += weight*probability
        state = new
        survivors.append(sum(state.values(), Fraction(0)))
    return survivors


# (1) Exact rational full-walk checks, independent of return Green functions.
for p in [Fraction(0), Fraction(1,10), Fraction(1,4), Fraction(2,3), Fraction(1)]:
    sur = exact_survivals(p, 20)
    a = coefficients(p, 20)
    for t in range(21):
        check(sur[t] == a[2*(t//2)], f'exact survival mismatch p={p}, step={t}')
    for n in range(1,11):
        f2n = sur[2*n-2] - sur[2*n]
        check(f2n >= 0, f'negative first detection mass p={p}, n={n}')
    check(sur[2] == p - p*p/2, f'first two-step return mismatch p={p}')

# (2) Independent Fourier integral for the return Green function, not using matrix formula.
mp.mp.dps = 50
for p in [mp.mpf('0.04'), mp.mpf('0.2'), mp.mpf('0.7'), mp.mpf('1')]:
    for z in [mp.mpf('0.2'), mp.mpf('0.55'), mp.mpf('0.9')]:
        a=1-(1-p)*z; b=1+(1-p)*z; c=p*z
        u=mp.sqrt(a*a-c*c); v=mp.sqrt(b*b-c*c)
        grow=mp.quad(lambda k: (1+(1-2*p)*z*mp.cos(k)) / ((a-c*mp.cos(k))*(b-c*mp.cos(k))), [0, mp.pi]) / mp.pi
        closed=2/((1-z)*v + (1+z)*u)
        check(abs(grow-closed)<mp.mpf('1e-35'), 'Fourier resolvent disagreement')

# (3) Bessel rare-noise survival crossover and its density.
for t in [mp.mpf('0.1'), mp.mpf('0.5'), mp.mpf('1'), mp.mpf('2'), mp.mpf('3')]:
    phi = mp.exp(-t)*(mp.besseli(0,t)+mp.besseli(1,t))
    deriv = mp.diff(lambda x: mp.exp(-x)*(mp.besseli(0,x)+mp.besseli(1,x)),t)
    check(abs(deriv + mp.exp(-t)*mp.besseli(1,t)/t)<mp.mpf('1e-39'), 'Bessel derivative identity')
    check(0 < phi < 1, 'invalid limiting survival')
    for target_p in ['0.01','0.002','0.0005']:
        p = mp.mpf(target_p)
        n = max(1, int(mp.nint(t/(2*p))))
        a = coefficients(p,2*n)
        val = a[2*n]/p
        exact_t = 2*n*p
        ref = mp.exp(-exact_t)*(mp.besseli(0,exact_t)+mp.besseli(1,exact_t))
        check(abs(val-ref)< 6*p, f'rare-noise mismatch p={p}, t={t}: val={val}, ref={ref}')

# (4) Fixed-positive-noise square-root tail constant.
for p in [mp.mpf('0.02'), mp.mpf('0.25'), mp.mpf('1')]:
    a = coefficients(p, 14000)
    for n in [1500, 3500, 7000]:
        asymptotic = mp.sqrt(p)/(mp.sqrt(mp.pi*n))
        check(abs(a[2*n]/asymptotic-1)<mp.mpf('0.04'), f'tail mismatch p={p},n={n}')
        first_hit = a[2*n-2]-a[2*n]
        expected = mp.sqrt(p)/(2*mp.sqrt(mp.pi)*n**mp.mpf('1.5'))
        check(abs(first_hit/expected-1)<mp.mpf('0.08'), f'first-hit tail mismatch p={p},n={n}')

print(f'PASS: {checks} independent checks (rational finite-state evolution, Fourier resolvent, Bessel crossover, fixed-noise tails).')
