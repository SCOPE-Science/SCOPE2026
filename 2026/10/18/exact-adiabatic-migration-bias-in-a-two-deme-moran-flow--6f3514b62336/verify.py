#!/usr/bin/env python3
"""Standalone algebraic and numerical consistency checks for a seasonal two-deme mean-field model.

Requires sympy, numpy and scipy. Algebraic assertions are exact; numerical
trajectory checks illustrate, but do not prove, the adiabatic limit.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.optimize import root

x, y, m = sp.symbols('x y m', real=True)
d1 = 2 + (1 - m) * x - m * y
d2 = 2 + m * x - (1 - m) * y
n1 = 3 * (1 - m) * x + m * y
n2 = (1 - m) * y + 3 * m * x
f1 = (n1 / d1 - x) / 2
f2 = (n2 / d2 - y) / 2
p = sp.expand(n1 - x * d1)
r = sp.expand(n2 - y * d2)
assert sp.expand(p + r - (x - y) * (1 - (1 - m) * (x + y))) == 0
assert sp.simplify(sp.Matrix([f1, f2]).jacobian([x, y]).subs({x:1, y:0, m:0}) -
                   sp.diag(sp.Rational(-1, 6), sp.Rational(-1, 4))) == sp.zeros(2)

u = (1-2*m)**2
rad = u*u + 4*m*(1-m)
X = (u + sp.sqrt(rad))/(2*(1-m))
Y = 1/(1-m) - X
assert sp.simplify((1-m)*X**2 - u*X - m) == 0
assert sp.simplify(sp.together(p.subs(y,1/(1-m)-x)) -
                   ((1-m)*x*x-u*x-m)/(m-1)) == 0
assert sp.series(X,m,0,3).removeO().expand() == 1-2*m+4*m*m
assert sp.series(Y,m,0,3).removeO().expand() == 3*m-3*m*m
assert sp.series(1/(2*sp.sqrt(1-m))-1/(2*(1-m/2)),m,0,3).removeO().expand() == m*m/16
print('PASS: exact equation identities, equilibrium branch and asymptotic coefficient')

def field(z, migration):
    x1,y1 = z
    a = (3*(1-migration)*x1 + migration*y1)/(2+(1-migration)*x1-migration*y1)
    b = ((1-migration)*y1 + 3*migration*x1)/(2+migration*x1-(1-migration)*y1)
    return np.array([(a-x1)/2,(b-y1)/2])

def equilibrium(migration):
    sol = root(lambda z:field(z,migration), [1-2*migration, 3*migration], tol=1e-12)
    assert np.linalg.norm(field(sol.x,migration)) < 2e-11
    assert np.all(sol.x > 0) and np.all(sol.x < 1)
    return sol.x

for rate in (0.01,0.02,0.05,0.10):
    e = equilibrium(rate)
    assert abs(e.sum() - 1/(1-rate)) < 2e-11
print('PASS: direct constant-migration equilibria')

amplitude = 0.05
baseline = np.mean(equilibrium(amplitude/2))
slow = 1/(2*math.sqrt(1-amplitude))
assert baseline < slow < 1/(2*(1-amplitude))
for period in (100.,400.):
    def forced(t,z):
        return field(z,amplitude*math.cos(math.pi*t/period)**2)
    initial = equilibrium(amplitude/2)
    transient = solve_ivp(forced,(0,period),initial,method='DOP853',
                          rtol=1e-11,atol=1e-13,max_step=2.)
    start = transient.y[:,-1]
    sol = solve_ivp(forced,(0,period),start,method='DOP853',
                    rtol=1e-11,atol=1e-13,max_step=2.,dense_output=True)
    nodes = np.linspace(0,period,4001)
    vals = sol.sol(nodes)
    observed = np.trapezoid((vals[0]+vals[1])/2,nodes)/period
    assert np.min(vals)>0 and np.max(vals)<1
    assert abs(observed - slow) < 5e-4
    print('period',int(period),'mean',f'{observed:.12f}',
          'adiabatic_limit',f'{slow:.12f}','constant_mean',f'{baseline:.12f}')
print('PASS: finite-period numerical comparisons (illustrative, not an infinite-time proof)')
