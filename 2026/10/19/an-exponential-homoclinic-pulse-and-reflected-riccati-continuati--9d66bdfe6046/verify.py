#!/usr/bin/env python3
"""Independent algebraic and numerical diagnostics for a quadratic mass-action flow.

Requires sympy and mpmath. The theorem's all-parameter statements are established
by analysis, not by finite computation.
"""
import sympy as sp
import mpmath as mp

checks = 0
x, y, a, delta = sp.symbols('x y a delta', positive=True)
xd = a*x*x - (a+delta)*x*y
yd = (a+delta)*x*y - a*y*y
u = x+y
q = (x-y)/u
D = lambda f: sp.simplify(sp.diff(f,x)*xd + sp.diff(f,y)*yd)
assert sp.simplify(D(u) - a*u*u*q) == 0; checks += 1
assert sp.simplify(D(q) + delta*u*(1-q*q)/2) == 0; checks += 1
H = x*y/u**(2+delta/a)
assert sp.simplify(D(H)) == 0; checks += 1
# At balanced initial concentrations, the reaction flow is not stationary when delta>0.
assert sp.simplify(xd.subs(y,x) + delta*x*x) == 0; checks += 1
assert sp.simplify(yd.subs(y,x) - delta*x*x) == 0; checks += 1

mp.mp.dps = 65
A = mp.mpf('1.3'); U = mp.mpf('2.2'); Q = mp.mpf('0.5')
r = 1-Q*Q
critical_time = 1/(A*U*Q)
first_correction = r/(2*A*A*U*Q**3)
def peak(d):
    k = A/d
    return 2/(d*U)*mp.quad(
        lambda v: mp.exp(-(k+1)*mp.log1p(-v*v) + k*mp.log(r)),
        [0, Q])

errors = []
for value in ['0.05','0.025','0.0125','0.00625']:
    d = mp.mpf(value)
    tp = peak(d)
    assert tp > critical_time; checks += 1
    errors.append(abs((tp-critical_time)/d-first_correction))
assert all(errors[i+1] < errors[i] for i in range(len(errors)-1)); checks += 1
assert errors[-1] < mp.mpf('0.03'); checks += 1

# Nonlinear profile by its inverse strictly monotone quadrature.
def inverse_profile(sigma, d=None):
    if d is None:
        fun = lambda z: mp.quad(lambda v:mp.exp(v*v), [0,z]) + sigma
        z = mp.findroot(fun, (-1 if sigma>0 else 1)*mp.mpf('0.4'))
        return mp.exp(-z*z)
    k = A/d
    fun = lambda z: mp.quad(
        lambda v: (1-d*v*v/A)**(-k-1), [0,z]) + sigma
    z = mp.findroot(fun, (-1 if sigma>0 else 1)*mp.mpf('0.4'))
    return (1-d*z*z/A)**k
for sig in ['0.25','0.8']:
    s = mp.mpf(sig)
    limit = inverse_profile(s)
    ep = []
    for ds in ['0.2','0.05','0.0125']:
        d = mp.mpf(ds)
        v = inverse_profile(s,d)
        w = inverse_profile(-s,d)
        assert abs(v-w) < mp.mpf('1e-40'); checks += 1
        ep.append(abs(v-limit))
    assert ep[-1] < ep[0] and ep[-1] < mp.mpf('0.001'); checks += 1

# Finite-parameter exact time reflection around the unique concentration maximum.
d = mp.mpf('0.3'); k=A/d; C=U*r**(-k)
f=lambda v:(1-v*v)**(-k-1)
tpeak = 2/(d*C)*mp.quad(f,[0,Q])
for test in ['0.1','0.2','0.35']:
    w=mp.mpf(test)
    tpos = 2/(d*C)*mp.quad(f,[w,Q])
    tneg = 2/(d*C)*mp.quad(f,[-w,0,w,Q])
    assert abs((tpos+tneg)-2*tpeak)<mp.mpf('1e-50'); checks+=1
print(f'{checks} diagnostic assertions passed; no claim of computer-assisted exhaustive proof')
