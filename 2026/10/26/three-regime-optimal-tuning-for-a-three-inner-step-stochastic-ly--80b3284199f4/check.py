#!/usr/bin/env python3
"""Reproducible symbolic and numerical checks for a Lyapunov-iteration theorem."""
import math
from fractions import Fraction
import numpy as np
import sympy as s
from scipy.optimize import minimize_scalar

r, a = s.symbols('r a', real=True)
mu = s.symbols('mu', real=True)
g = (1-a)*mu+a*(1-a)*mu**2+a*a*mu**3
gp=s.factor(g.subs(mu,r)); gm=s.factor(g.subs(mu,-r))
assert s.simplify(gp+gm-2*r*r*a*(1-a))==0
assert s.simplify(gp-gm-2*r*(1-a+r*r*a*a))==0
assert s.simplify(gp-r*(1-(1-r)*a*(1+r*a)))==0
assert s.simplify(gm+r*(1-(1+r)*a*(1-r*a)))==0
assert s.simplify(gp.subs(a,1)-r**3)==0
assert s.simplify(gm.subs(a,1)+r**3)==0
assert s.simplify(gm.subs(a,1/(2*r))+(3*r-1)/4)==0
assert s.simplify(gp.subs(a,1/(2*r))-(7*r-3)/4)==0
assert s.factor(r**3-(3*r-1)/4)==(r+1)*(2*r-1)**2/4
assert s.simplify(gp.subs(a,1)-gm.subs(a,1)-2*r**3)==0

def opt(x):
    if not (0<x<1):raise ValueError('r must be (0,1)')
    if x <= .4:
        al=2/(1+math.sqrt(1-4*x*x))
        val=x*x*al*(al-1)
    elif x <= .5:
        al=1/(2*x);val=(3*x-1)/4
    else:
        al=1.;val=x*x*x
    return al,val

for x in [0.0005,.02,.1,.2,.399,.4,.4001,.41,.45,.49,.499999,.5,.5001,.65,.98]:
    al, q=opt(x)
    gp_num=float(gp.subs({r:x,a:al})); gm_num=float(gm.subs({r:x,a:al}))
    assert abs(max(abs(gp_num),abs(gm_num))-q)<1e-10,(x,gp_num,gm_num,q)
    f=lambda alpha:max(abs(float(gp.subs({r:x,a:alpha}))),abs(float(gm.subs({r:x,a:alpha}))))
    for alpha in np.concatenate((np.linspace(-3,6,300),np.linspace(max(0,al-.2),al+.2,301))):
        assert f(alpha)>=q-2e-9,(x,alpha, f(alpha),q)
    result=minimize_scalar(f,bounds=(0,10),method='bounded',options={'xatol':1e-11})
    assert result.fun >=q-2e-9,(x,result)

# Exact rational test at phase boundaries and in all regions.
for x in [s.Rational(1,5),s.Rational(2,5),s.Rational(9,20),s.Rational(1,2),s.Rational(3,5)]:
    xf=float(x);al,_=opt(xf)
    if x<=s.Rational(2,5): aa=2/(1+s.sqrt(1-4*x*x));qq=s.simplify(x*x*aa*(aa-1))
    elif x<=s.Rational(1,2): aa=1/(2*x);qq=(3*x-1)/4
    else:aa=s.Integer(1);qq=x**3
    assert s.simplify(s.Max(s.Abs(gp.subs({r:x,a:aa})),s.Abs(gm.subs({r:x,a:aa})))-qq)==0

# Independent 2x2 symmetric-matrix action and three inner recurrences.
J=np.array([[0.,1.],[1.,0.]])
rng=np.random.default_rng(349127)
for _ in range(300):
    x=float(rng.uniform(.02,.97));al,q=opt(x)
    Q=rng.normal(size=(2,2));Q=Q.T@Q+np.eye(2)
    E=rng.normal(size=(2,2));E=(E+E.T)/2
    Xstar=(Q+x*J@Q@J)/(1-x*x)
    X=Xstar+E
    inner=X.copy()
    for j in range(3): inner=al*x*J@inner@J+(1-al)*x*J@X@J+Q
    actual=inner-Xstar
    expected=float(gp.subs({r:x,a:al}))*(E+J@E@J)/2+float(gm.subs({r:x,a:al}))*(E-J@E@J)/2
    assert np.linalg.norm(actual-expected)<3e-12
    assert np.linalg.norm(actual)<=q*np.linalg.norm(E)+1e-11
print('PASS: polynomial identities, exact rational boundaries, 15 minimax sweeps, 300 stochastic-Lyapunov recurrences')
