"""Exact arithmetic checks for a conformist two-strategy Snowdrift ODE.

Execute: python verify_symmetric_snowdrift.py
Requires: sympy (for rational symbolic verification).
The mathematical proof of global behavior is in RESULT.md; this program checks
an explicit witness and samples the sign classification, not an infinite proof.
"""
import math
import sympy as sp

x, t = sp.symbols('x t', positive=True)
a = sp.Rational(5, 9)*(1-2*x)     # alpha D(x) for b=15, c=10, alpha=1/9
F = x*(1-x)*(sp.sqrt(x)*(1+a)-sp.sqrt(1-x)*(1-a))
assert all(sp.simplify(F.subs(x,z))==0 for z in
           [sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)])
# t=sqrt(x/(1-x)); the full interior zero equation is a cubic in t.
a_t=sp.factor(a.subs(x,t*t/(1+t*t)))
P=sp.factor(9*(1+t*t)*(t*(1+a_t)-(1-a_t)))
assert sp.simplify(P-2*(t-2)*(t-1)*(2*t-1))==0
for z, target in [(sp.Rational(1,5), 2*sp.sqrt(5)/75),
                  (sp.Rational(1,2),-sp.sqrt(2)/36),
                  (sp.Rational(4,5), 2*sp.sqrt(5)/75)]:
    assert sp.simplify(sp.diff(F,x).subs(x,z)-target)==0, (z,sp.diff(F,x).subs(x,z))
assert sp.simplify(sp.limit(F/x,x,0,dir='+')+sp.Rational(4,9))==0
assert sp.simplify(sp.limit(F/(1-x),x,1,dir='-')-sp.Rational(4,9))==0

def f_float(xx,k,lam):
    return xx*(1-xx)*(xx**k*(1+lam*(.5-xx))
                  -(1-xx)**k*(1-lam*(.5-xx)))

# Checks are illustrative finite tests; analytic monotonicity supplies the theorem.
for k, lam, roots in [(0.5,10/9,3), (0.5,0.95,1), (0.25,1.1,3),
                      (0.75,1.6,3), (0.75,1.45,1), (1,1.2,1),
                      (1.4,1.8,1), (3,0.3,1)]:
    zz=[i/20000 for i in range(1,20000)]
    sg=[math.copysign(1., f_float(v,k,lam)) for v in zz if abs(v-.5)>1e-6]
    # Count sign changes across the open interval, excluding the central exact zero.
    changes=sum(sg[i]!=sg[i-1] for i in range(1,len(sg)))
    assert changes==roots, (k,lam,roots,changes)
print('PASS: exact cubic factorization, all five fixed points, exact slopes, and 8 qualitative parameter samples')
