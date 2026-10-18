#!/usr/bin/env python3
"""Numerical illustrations for the semiprime real-cut theorem; not an infinite proof.

Requires mpmath. All mathematics in the theorem is established analytically.
"""
import mpmath as mp

mp.mp.dps = 28
N = 44
mu = [1] * (N + 1)
mu[0] = 0
for p in range(2, N+1):
    if any(p % q == 0 for q in range(2, int(p**.5) + 1)):
        continue
    for j in range(p, N+1, p):
        mu[j] *= -1
    for j in range(p*p, N+1, p*p):
        mu[j] = 0

def U(t):
    return sum(mu[n]*mp.log(abs(mp.zeta(n*t)))/n
               for n in range(1, N+1) if mu[n])

samples = [(mp.mpf('0.55'), -1), (mp.mpf('0.65'), -1),
           (mp.mpf('0.66'), +1), (mp.mpf('0.8'), +1)]
for t, sign in samples:
    assert sign * U(t) > 0
root = mp.findroot(U, (mp.mpf('0.65'), mp.mpf('0.67')))
assert mp.mpf('0.65') < root < mp.mpf('0.66')

def B(x):
    return mp.quad(lambda t: U(t) * mp.power(x,t)/t,
                   [mp.mpf('0.5'), mp.mpf('0.6'), root,
                    mp.mpf('0.8'), mp.mpf('1')])

assert B(mp.mpf('0.03')) < 0
assert B(mp.mpf('0.1')) > 0
assert B(mp.mpf('1')) > 0
print('VERIFY_OK density_signs=4 transform_signs=3')
print('Illustrative, non-certified density zero:', mp.nstr(root, 18))
