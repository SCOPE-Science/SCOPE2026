"""Independent numerical diagnostics for a truncated Zipf similarity model.

Requires mpmath >= 1.3.0. Checks finite pressure identities, double-scaling
approximations, cutoff crossover signs, and exact interval geometry. Numerical
checks are not substitutes for the infinite-asymptotic proof in RESULT.md.
"""
from __future__ import annotations
import math
import mpmath as mp

mp.mp.dps = 70
checks = 0


def verify(condition, explanation):
    global checks
    if not condition:
        raise AssertionError(explanation)
    checks += 1


def phase_root(lam, tau):
    lam = mp.mpf(lam)
    tau = mp.mpf(tau)

    def g(a):
        z = (a-1)*tau
        return lam*tau*(mp.expm1(z)/z if abs(z) > mp.mpf('1e-25') else 1+z/2+z*z/6)

    lo, hi = mp.mpf('0'), mp.mpf('50')
    verify(g(lo) < 1 and g(hi) > 1, 'phase root bracket')
    for _ in range(210):
        mid = (lo+hi)/2
        if g(mid)<1:
            lo=mid
        else:
            hi=mid
    root = (lo+hi)/2
    verify(abs(g(root)-1) < mp.mpf('1e-45'), 'continuum phase root identity')
    return root


def finite_pressure(lam, eps, N, s):
    q = 1+eps
    c = lam/mp.zeta(q)
    return c**s*(mp.zeta(q*s)-mp.zeta(q*s, N+1))


def finite_root(lam, eps, N):
    lo, hi = mp.mpf('0'), mp.mpf('1')
    for _ in range(180):
        mid = (lo+hi)/2
        if finite_pressure(lam,eps,N,mid)>1:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def infinite_root(lam,eps):
    q=1+eps
    lo,hi=mp.mpf(1)/q,mp.mpf(1)
    for _ in range(190):
        mid=(lo+hi)/2
        if (lam/mp.zeta(q))**mid*mp.zeta(q*mid)>1:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


lam = mp.mpf('0.5')
for tau_str in ['0.5','1.0','2.0','3.0']:
    tau=mp.mpf(tau_str)
    a=phase_root(lam,tau)
    verify((a>1) == (tau < 1/lam) if tau!=1/lam else abs(a-1)<mp.mpf('1e-45'), 'phase side')
    e=mp.mpf('0.0075')
    N=int(mp.exp(tau/e))
    s=finite_root(lam,e,N)
    verify(0<s<1 and abs(finite_pressure(lam,e,N,s)-1)<mp.mpf('1e-35'), 'finite Moran root')
    verify(abs((1-s)/e-a)<mp.mpf('0.5') if tau>=1 else abs((1-s)/e-a)<mp.mpf('2'), 'small-epsilon scaling')
    verify((s > 1/(1+e)) == (tau>1/lam) if tau!=1/lam else True, 'critical exponent crossing')

for e_str in ['0.04','0.015','0.005']:
    e=mp.mpf(e_str)
    s=infinite_root(lam,e)
    verify(abs((1-s)/e-(1-lam)) < mp.mpf('0.30'), 'infinite pressure asymptotic')
    verify(abs((lam/mp.zeta(1+e))**s*mp.zeta((1+e)*s)-1)<mp.mpf('1e-40'), 'infinite pressure root')

q=mp.mpf('1.4');lam=mp.mpf('0.57'); z=mp.zeta(q)
for n in range(1,30):
    p=lambda j:j**(-q)/z
    a=sum([p(k) for k in range(1,n+1)])-lam*p(n)
    b=sum([p(k) for k in range(1,n+1)])
    verify(0<a<b<1, 'valid image interval')
    if n>1:
        b_prev=sum([p(k) for k in range(1,n)])
        verify(abs(a-b_prev-(1-lam)*p(n))<mp.mpf('1e-60'), 'exact gap formula')

print('PASS: %s diagnostics; finite pressure computed using Hurwitz zeta, not enumerating astronomical alphabets.' % checks)
