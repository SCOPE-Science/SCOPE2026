"""Reproduce finite-dimensional information identities and asymptotic diagnostics.

Requires mpmath. This checker is supplementary; the infinite claims follow
from the proofs using the Dirichlet change of variables and Gamma expansions.
"""
import mpmath as mp
mp.mp.dps = 55

def information(d, p):
    a = mp.mpf(1) / p
    t = (d - 1) * a
    b = 1 - t
    assert d >= 2 and b > 0
    return (-mp.loggamma(b) - (d - 1) * mp.loggamma(1 + a)
            + t * (mp.digamma(1 + a) - mp.digamma(b)))

def limit(c):
    t = 1 / mp.mpf(c)
    return -mp.loggamma(1 - t) - t * mp.digamma(1 - t)

def tv_lower(c):
    ell = mp.log(2) / mp.mpf(c)
    return 1 - mp.exp(-ell) * (1 + ell)

def finite_tv_event(d, p):
    q = 1 - mp.power(2, -1 / mp.mpf(p))
    return 1 - (1-q)**d - d*q*(1-q)**(d-1)

# Independent check: direct one-dimensional beta integration of log slack.
for d, p in [(2, 3), (3, 8), (5, 11)]:
    a = mp.mpf(1)/p
    b = 1 - (d-1)*a
    s = d*a
    beta_norm = mp.beta(b, s)
    e_log = mp.quad(lambda w: (w**(b-1)*(1-w)**(s-1)/beta_norm)*mp.log(w), [0, 1])
    direct = -mp.loggamma(b) - (d-1)*mp.loggamma(1+a) - (d-1)*a*e_log
    assert abs(direct-information(d, p)) < mp.mpf('1e-35')

# Independent bivariate closed form from Gamma reflection identities.
for p in [mp.mpf('1.2'), mp.mpf(2), mp.mpf('3.5'), mp.mpf(10)]:
    z = mp.pi/p
    value = mp.log(mp.sin(z)/z) + 1 - z * mp.cot(z)
    assert abs(value-information(2, p)) < mp.mpf('1e-40')

c = mp.mpf(2)
assert abs(limit(c) - (mp.log(2/mp.sqrt(mp.pi))+mp.euler/2)) < mp.mpf('1e-40')
assert mp.mpf('0.4') < limit(c) < mp.mpf('0.42')
assert mp.mpf('0.04') < tv_lower(c) < mp.mpf('0.05')
for d in [100, 1000, 10000]:
    p = 2*(d-1)
    assert information(d,p) > limit(c)
    assert abs(information(d,p) - limit(c)) < mp.mpf(2)/d
    assert abs(finite_tv_event(d,p) - tv_lower(c)) < mp.mpf(1)/d
    for k in [2,3,5]:
        ik = information(k,p)
        leading = mp.pi**2*k*(k-1)/(12*p**2)
        assert abs(ik/leading-1) < mp.mpf(10)/d
print('Finite beta-integral comparisons, reflection identity and three high-dimensional regimes: PASS')
print('c=2: total correlation limit =',mp.nstr(limit(2),24))
print('c=2: total variation lower limit =',mp.nstr(tv_lower(2),24))
