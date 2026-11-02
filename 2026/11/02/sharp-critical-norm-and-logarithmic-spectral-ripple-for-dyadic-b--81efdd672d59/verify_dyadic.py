#!/usr/bin/env python3
"""Supplementary finite checks for a Bergman dyadic-line sampling theorem.

Requires mpmath (tested with 1.3.0). Infinite claims are proved in RESULT.md.
"""
import mpmath as mp

mp.mp.dps = 75
ln2 = mp.log(2)
checks = 0


def near(a, b, tol):
    global checks
    assert abs(a - b) < tol, (mp.nstr(a, 28), mp.nstr(b, 28), tol)
    checks += 1


def p_bilateral(beta, theta):
    # Infinite tails bounded outside these ranges in the tested cases.
    return mp.fsum(mp.power(2, beta * (k + theta)) *
                   mp.exp(-mp.power(2, k + theta))
                   for k in range(-220, 50))


def p_fourier(beta, theta):
    return mp.fsum(mp.gamma(beta - 2j * mp.pi * k / ln2) *
                   mp.exp(2j * mp.pi * k * theta) / ln2
                   for k in range(-15, 16))


def multiplier(beta, u):
    return mp.fsum(u * mp.power(2, -beta * j) *
                   mp.exp(-u * mp.power(2, -j)) for j in range(240))


def omitted(beta, u):
    return mp.fsum(mp.power(mp.power(2, k) * u, beta) *
                   mp.exp(-mp.power(2, k) * u) for k in range(1, 45))


for beta in (mp.mpf('0.75'), mp.mpf('1'), mp.mpf('1.7')):
    for theta in (mp.mpf('0.07'), mp.mpf('0.3'), mp.mpf('0.619'), mp.mpf('0.861')):
        near(p_bilateral(beta, theta), p_fourier(beta, theta), mp.mpf('1e-35'))
        near(p_bilateral(beta, theta), p_bilateral(beta, theta+1), mp.mpf('1e-43'))
    for u in (mp.mpf('.2'), mp.mpf('1'), mp.mpf('2.5'), mp.mpf('30')):
        right = mp.power(u, 1-beta) * (p_bilateral(beta, mp.log(u)/ln2) - omitted(beta, u))
        near(multiplier(beta, u), right, mp.mpf('1e-35'))

c = lambda k: mp.gamma(1-2j*mp.pi*k/ln2)/ln2
f = lambda x: mp.re(p_fourier(1, x))
df = lambda x: mp.re(mp.fsum(2j*mp.pi*k*c(k)*mp.exp(2j*mp.pi*k*x)
                              for k in range(-15,16)))
theta0 = (-mp.arg(c(1))/(2*mp.pi)) % 1
star = mp.findroot(df, theta0)
value = f(star)
near(star, mp.mpf('0.861103525077780269341238665519588398'), mp.mpf('1e-30'))
near(value, mp.mpf('1.442709301132949454201681684297836380'), mp.mpf('1e-30'))
assert value > 1/ln2
checks += 1
assert mp.exp(-mp.pi**2/ln2) < mp.mpf('1e-6')
checks += 1
q = mp.exp(-mp.pi**2/ln2)
tail_bound = (1+4*q+q*q)/(1-q)**4-1
assert 0 < tail_bound < mp.mpf('9e-6')
checks += 1
for n in (4, 8, 15, 22):
    u = mp.power(2, n+star)
    val = multiplier(1, u)
    assert val < value
    checks += 1
    near(value-val, omitted(1,u), mp.mpf('1e-35'))
for u in (mp.mpf('0.0001'), mp.mpf('0.03')):
    for beta in (mp.mpf('.75'), mp.mpf('1'), mp.mpf('1.7')):
        assert multiplier(beta,u)>0
        checks += 1
print('PASS', checks, 'finite checks')
print('critical_phase', mp.nstr(star,35))
print('optimal_norm', mp.nstr(value,35))
print('first_harmonic_abs', mp.nstr(abs(c(1)),20))
print('tail_bound', mp.nstr(tail_bound,20))
