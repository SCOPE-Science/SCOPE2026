"""Reproduce algebraic and finite numerical consistency checks for the exterior two-wave theorem.

This is a checker of critical symbolic identities and examples, not a substitute for the
analytic inequalities for all real parameter values in RESULT.md.
"""
from __future__ import annotations
import math
import sympy as sp

u, q = sp.symbols('u q', positive=True)
q0 = u / 6 - u**2 / 120
F = lambda t: 2*t*(3 - 2*t) - (1-t)*u
assert sp.simplify(F(q0) - u**2*(20+10*u-u**2)/3600) == 0
assert sp.simplify(sp.diff(F(q),q) -(6-8*q+u)) == 0

# Unit-norm kernel formula and sharpness at frequency collision.
x,h = sp.symbols('x h',real=True,nonzero=True)
gram = sp.Matrix([[1,sp.sin(h)/h],[sp.sin(h)/h,1]])
assert sp.simplify(gram.det() - (1-(sp.sin(h)/h)**2)) == 0

# Smooth cluster witness: g_h = cos(ht) + 3x sin(ht)/h.
def witness_ratio(x0,h0):
    si=lambda y: math.sin(y)/y if abs(y)>1e-12 else 1.
    # normalized integral of cos^2(ht) = (1+sinc(2h))/2,
    # of sin^2(ht) = (1-sinc(2h))/2; odd cross term vanishes.
    mean=(1+si(2*h0))/2 + (3*x0/h0)**2*(1-si(2*h0))/2
    val=math.cos(h0*x0)+3*x0*math.sin(h0*x0)/h0
    return val*val/mean

def eval_kernel(x0,d0):
    s=math.sin(d0)/d0
    return 2*(1-s*math.cos(d0*x0))/(1-s*s)

for x0 in [1.,1.1,2.,4.,10.]:
    cap=1+3*x0*x0
    for d0 in [.015,.03,.1,.5,1.,1.8,2.,3.,5.,10.,30.,100.]:
        k=eval_kernel(x0,d0)
        assert k < cap + 3e-9,(x0,d0,k,cap)
    for h0 in [.03,.01,.005]:
        ratio=witness_ratio(x0,h0)
        assert ratio < cap + 2e-6,(x0,h0,ratio,cap)
    assert abs(witness_ratio(x0,.002)/cap-1)<.0005

# Interior failure: x=0 has proposed 1 but two frequencies give >1.
assert eval_kernel(0.,4.5)>2
print('PASS: exact polynomial identities, 60 fixed-gap kernel checks, '+
      '15 confluent-witness checks, and interior-boundary counterexample')
