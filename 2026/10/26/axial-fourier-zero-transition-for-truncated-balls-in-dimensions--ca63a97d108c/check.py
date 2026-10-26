"""Finite symbolic and high-precision checks for truncated-ball axial Fourier zeros.

Execute: python check.py
Requires sympy and mpmath. The checks supplement, not replace, the proofs.
"""
from __future__ import annotations

import sympy as sp
import mpmath as mp

x, h, t, z = sp.symbols('x h t z', real=True)


def q_symbolic(m, endpoint):
    p = (1 - x*x)**m
    return sp.expand(sum((-1)**k * sp.diff(p, x, k).subs(x, endpoint)
                         * z**(2*m-k) for k in range(2*m+1)))


def d_symbolic(m):
    a, b = q_symbolic(m, 1), q_symbolic(m, h)
    return sp.factor(sp.expand((b.subs(z, sp.I*t)*b.subs(z, -sp.I*t)
                                - a.subs(z, sp.I*t)*a.subs(z, -sp.I*t))))


expected = {
    1: (1-h*h)**2 * t**4,
    2: (1-h*h)**3 * t**6*((1-h*h)*t**2+8),
    3: (1-h*h)**4 * t**8*((1-h*h)**2*t**4+12*(1-2*h*h)*t**2+180),
}
for m in (1, 2, 3):
    assert sp.simplify(d_symbolic(m)-expected[m]) == 0
print('Exact endpoint-modulus identities: 3 PASS')

mp.mp.dps=65


def q_numeric(m, a, s):
    value=mp.mpc(0)
    for j in range(m+1):
        c=(-1)**j * mp.binomial(m,j)
        for k in range(2*j+1):
            value += (-1)**k * c*mp.factorial(2*j)/mp.factorial(2*j-k) * a**(2*j-k) *s**(2*m-k)
    return value


def exact_integral(m, a, tau):
    s=1j*tau
    return (mp.exp(s)*q_numeric(m,1,s)-mp.exp(s*a)*q_numeric(m,a,s))/(s**(2*m+1))


def direct_integral(m,a,tau):
    return mp.quad(lambda y:(1-y*y)**m*mp.exp(1j*tau*y), [a,1])

for m in (1,2,3):
    for aa in ('-0.9','-0.32','0.45'):
        for tt in ('0.35','2.5','12'):
            a,tau=mp.mpf(aa),mp.mpf(tt)
            err=abs(exact_integral(m,a,tau)-direct_integral(m,a,tau))
            assert err < mp.mpf('1e-48'), (m,aa,tt,err)
print('Independent endpoint/integral comparisons: 27 PASS')


def high_branch(a):
    k=1-a*a
    return mp.sqrt(6*(1-2*k+mp.sqrt(1-4*k-k*k)))/k


def phase_gap(a):
    tau=high_branch(a)
    angle=mp.arg(q_numeric(3,a,1j*tau)/q_numeric(3,1,1j*tau))
    return tau*(1-a)-angle

for n in (10, 20, 40):
    start=-1+mp.sqrt(3)/(mp.pi*n)
    root=mp.findroot(lambda a:phase_gap(a)-2*mp.pi*n,(start-mp.mpf('0.002'),start+mp.mpf('0.002')))
    tau=high_branch(root)
    err=abs(direct_integral(3,root,tau))
    assert -1 < root < -mp.sqrt(3-mp.sqrt(5))
    assert err < mp.mpf('1e-48'), (n,err)
    print('Dimension seven witness n={} cutoff={} frequency={} residual={}'.format(
        n,mp.nstr(root,20),mp.nstr(tau,20),mp.nstr(err,5)))
print('All finite checks PASS')
