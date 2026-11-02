"""Supplementary finite checks for weighted real-variable Cesàro spectral formulas.

Run: python verify.py
Requires mpmath. These checks do not certify infinite-dimensional spectral claims.
"""
import mpmath as mp

mp.mp.dps = 35
checks = 0


def close(a, b, relative=mp.mpf('2e-18')):
    global checks
    if abs(a-b) > relative * (1 + abs(a) + abs(b)):
        raise AssertionError((a, b, abs(a-b)))
    checks += 1


def hs_direct(g):
    # t=1-s, avoid the removable endpoint cancellation at s=1
    return mp.quad(lambda s: (s**(-g)-1)**2*s/(1-s), [0, mp.mpf('0.2'), mp.mpf('0.8'), 1])


def hs_digamma(g):
    return 2*mp.digamma(2-g)-mp.digamma(2-2*g)-mp.digamma(2)


for gamma in [mp.mpf('-1.3'), mp.mpf('-0.2'), mp.mpf('0.0'), mp.mpf('0.25'), mp.mpf('0.5'), mp.mpf('0.7')]:
    close(hs_direct(gamma), hs_digamma(gamma))


def eig(g, lam, x):
    J = mp.quad(lambda t: ((1-t)**(-g)-1)/t if t else g, [0,x])
    return x**(1/lam-1)*mp.exp(J/lam)


for gamma in [mp.mpf('-0.5'), mp.mpf('0'), mp.mpf('0.4'), mp.mpf('0.8')]:
    for lam in [mp.mpf('0.7'), mp.mpf('1.2'), mp.mpc('1','0.2')]:
        for x in [mp.mpf('0.13'), mp.mpf('0.41'), mp.mpf('0.8')]:
            F = mp.quad(lambda t: (1-t)**(-gamma)*eig(gamma,lam,t), [0,x]) / x
            close(F,lam*eig(gamma,lam,x),relative=mp.mpf('3e-17'))

# Check the exact Mellin/Hardy model on exponential test vectors.
for z in [mp.mpf('0.2'),mp.mpf('0.7'),mp.mpc('0.8','0.4')]:
    for s in [mp.mpf('0.1'),mp.mpf('1.2'),mp.mpf('2.3')]:
        observed=mp.quad(lambda v:mp.exp(-v/2)*mp.exp(-z*(s+v)),[0,mp.inf])
        close(observed,mp.exp(-z*s)/(z+mp.mpf('0.5')))

# Normalized subcritical singular-value scale, computed from digamma.
for eps in [mp.mpf('0.1'),mp.mpf('0.05'),mp.mpf('0.01')]:
    val=2*eps*hs_digamma(1-eps)
    if not (0 < val < 1 and abs(val-1) < 12*eps):
        raise AssertionError((eps,val))
    checks += 1

print(f'PASS: {checks} supplementary numerical and analytic-identity checks')
