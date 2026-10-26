#!/usr/bin/env python3
"""Arbitrary-precision check for a cyclic MMPP survival crossing.

Requires: python -m pip install mpmath
The strict mathematical sign is proved independently in RESULT.md.
"""
import mpmath as mp

mp.mp.dps = 55
n = 16
one = mp.mpf(1)
eps = one / 1000
theta = mp.pi / 8
v = [mp.cos(theta*j) for j in range(n)]
lam = [one + eps*z for z in v]
Q = mp.zeros(n)
for j in range(n):
    Q[j,j] = -one
    Q[j,(j+1)%n] = one
C = Q - mp.diag(lam)
pi = mp.matrix([[one/n for _ in range(n)]])
alpha = mp.matrix([[lam[j]/n for j in range(n)]])
target = 3*mp.pi/(2*mp.sin(theta))
vec = mp.expm(C*target)*mp.ones(n,1)
st = (pi*vec)[0]
se = (alpha*vec)[0]
delta = st - se
assert delta < 0
assert abs(sum(v)) < mp.mpf('1e-48')
assert abs(sum(z*z for z in v)/n - mp.mpf('0.5')) < mp.mpf('1e-48')
a = 1-mp.cos(theta)
b = mp.sin(theta)
k = a/b
I = (1-mp.exp(-3*mp.pi*k/2)/k)/4
error_bound = eps*target**2*mp.exp(eps*target)/2
assert I < -mp.mpf(1)/6
assert error_bound < mp.mpf(169)/1974
assert delta < -(mp.mpf(80)/987)*eps**2*mp.exp(-target)
assert eps**2/mp.mpf(2) > 0
print('target =', mp.nstr(target, 40))
print('time-stationary survival =', mp.nstr(st, 40))
print('event-stationary survival =', mp.nstr(se, 40))
print('difference =', mp.nstr(delta, 40))
print('strict elementary certificate =', mp.nstr(-mp.mpf(80)/987*eps**2*mp.exp(-target), 40))
print('all numerical cross-checks passed')
