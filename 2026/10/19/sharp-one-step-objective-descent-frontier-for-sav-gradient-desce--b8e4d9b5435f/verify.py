#!/usr/bin/env python3
"""Independent algebra and numerical checks for a scalar SAV one-step energy frontier.
Run: python verify.py
Requires sympy and mpmath. Numerical probes corroborate, not replace, analytic proof.
"""
from fractions import Fraction
import math
import random
import sympy as S
import mpmath as M
x, t, u, h = S.symbols('x t u h', real=True)
F=lambda z:(z*z-1)**2/S.Integer(4)
g=x*(x*x-1)
s=F(x)+S.Rational(1,4)
beta=S.cancel(g*g/(2*s))
assert S.simplify(beta-2*x*x*(x*x-1)**2/(1+(x*x-1)**2))==0
X=S.factor(x-h*g/(1+h*beta))
R=S.factor(S.sqrt(s)/(1+h*beta))
assert S.simplify(X-x*(1-h*(x*x-1)/(1+h*beta)))==0
assert S.simplify(R/S.sqrt(s)-1/(1+h*beta))==0
rt=(1+u)*(1-3*u*u)/(1+u*u)
assert S.factor(S.diff(rt,u,2)-8*(u-1)*(u*u+4*u+1)/(1+u*u)**3)==0
assert S.factor(S.diff(rt,u).subs(u,0)-1)==0
# Exact rational isolating bracket for the unique critical point.
for q,expected in [(S.Rational(99745258,10**9),1),(S.Rational(99745260,10**9),-1)]:
    dpq=S.diff(rt,u).subs(u,q)-q/S.sqrt(1-q*q)
    assert (dpq>0 if expected>0 else dpq<0)
# Rational exact counterexample, no floating point involved.
xx=S.Rational(21,20);hh=S.Rational(49,50)
yy=S.cancel(X.subs({x:xx,h:hh}))
delta=S.cancel(F(yy)-F(xx))
assert delta>0, delta
# Modified SAV energy decreases exactly.
bb=beta.subs(x,xx)
assert (1+hh*bb)>1
# Large-step asymptotics at a near the minimizer; use symbolic epsilon.
e=S.symbols('e', positive=True)
t0=1-e
beta0=2*t0*e**2/(1+e**2)
H=e**(-3)
X0=S.sqrt(t0)*(1+H*e/(1+H*beta0))
R0sq=(1+e**2)/4/(1+H*beta0)**2
assert S.limit(e*X0,e,0,dir='+')==S.Rational(1,2)
assert S.limit(e**4*F(X0),e,0,dir='+')==S.Rational(1,64)
assert S.limit(R0sq/e**2,e,0,dir='+')==S.Rational(1,16)
assert S.limit(F(S.sqrt(1-e))/e**2,e,0,dir='+')==S.Rational(1,4)
# The shape d has one global maximizer by strictly negative second derivative on (0,1).
M.mp.dps=90
D=lambda w: M.sqrt(1-w*w)+(1+w)*(1-3*w*w)/(1+w*w)
Dp=lambda w: -w/M.sqrt(1-w*w)-(3*w**4+10*w*w+8*w-1)/(1+w*w)**2
u0=M.findroot(Dp,(M.mpf('0.09'),M.mpf('0.11')))
crit=2/D(u0)
assert M.mpf('0.099745258')<u0<M.mpf('0.099745260')
assert M.mpf('0.974932803')<crit<M.mpf('0.974932806')
assert abs(Dp(u0))<M.mpf('1e-80')
assert D(u0)>2
# Independent direct one-step energy test.
def evalstep(a,H):
 ff=(a*a-1)**2/4
 G=a*(a*a-1)
 b=G*G/(2*(ff+0.25))
 yp=a-H*G/(1+H*b)
 ff1=(yp*yp-1)**2/4
 return ff1-ff
rng=random.Random(730012)
for j in range(4000):
 a=(rng.random()*2-1)*10**rng.uniform(-2,3)
 H=float(crit)*(1-rng.random()*0.999)
 assert evalstep(a,H)<=1e-10*max(1, (a*a-1)**2/4), (a,H)
assert evalstep(21/20,49/50)>0
# Near minimizer fixed-step linearized amplification.
for Hn in [1.01,2,4]:
 a=1-1e-5
 f0=(a*a-1)**2/4
 assert (evalstep(a,Hn)+f0)/f0>1
print('PASS: symbolic map, strict concavity, exact positive rational witness, asymptotic mismatch, 4000 numerical probes')
print('u_star =', M.nstr(u0,60))
print('h_star =', M.nstr(crit,60))
print('rational witness delta =', delta)
print('rational witness decimal =',S.N(delta,22))
