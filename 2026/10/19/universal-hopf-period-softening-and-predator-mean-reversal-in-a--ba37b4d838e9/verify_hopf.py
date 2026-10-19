#!/usr/bin/env python3
"""Exact nonlinear Hopf coefficient and finite ODE consistency checks.

Only neutral scientific verification is performed. Needs sympy, numpy, scipy.
"""
import sympy as S
import numpy as np
from scipy.integrate import solve_ivp

a,e=S.symbols('a e', positive=True)
phi=1/(2-a)
w=(1-a)/S.sqrt(e*(2-a))
assert S.simplify(w**2-(1-a)*(1-phi)/e)==0

t=S.symbols('t',real=True)
al,be,ga,eta=S.symbols('al be ga eta',real=True)
c,s=S.cos(t),S.sin(t)
# Second-order Fourier solution of x'=-y+al*x*x+be*x*y;
# y'=x+eta*x*y, all in the dimensionless critical phase.
X2=(-be/S.Integer(3))*S.cos(2*t)+(eta+2*al)/6*S.sin(2*t)
Y2=al/2-(al+2*eta)/6*S.cos(2*t)-be/6*S.sin(2*t)
F2=al*c*c+be*c*s;G2=eta*c*s
assert S.trigsimp(S.diff(X2,t)+Y2-F2)==0
assert S.trigsimp(S.diff(Y2,t)-X2-G2)==0
F3=2*al*c*X2+be*(c*Y2+s*X2)+ga*c**3
G3=eta*(c*Y2+s*X2)
rad=S.simplify(S.integrate(S.expand_trig(c*F3+s*G3),(t,0,2*S.pi))/(2*S.pi))
phase=S.simplify(S.integrate(S.expand_trig(c*G3-s*F3),(t,0,2*S.pi))/(2*S.pi))
assert S.simplify(rad-(al*be/8+3*ga/8))==0
assert S.simplify(phase-(-al**2/6+5*al*eta/24-be**2/24-eta**2/24))==0
rstar=S.simplify((w*rad).subs({al:-phi/(e*w),be:-1,ga:-phi/(e*w),eta:1/w}))
assert S.simplify(rstar+phi/(4*e))==0
P=phase.subs({al:-phi/(e*w),be:-1,ga:-phi/(e*w),eta:1/w})
coef=(1-a)/(2*e*w)+2*(2-a)**2*w*P
C=((2-a)**2*e**2+(6-4*a+4*a**2-a**3)*e+4)/(12*e**2*w)
assert S.simplify(coef+C)==0
# Positivity: 6-4*a>2 for 0<a<1, and 4*a*a-a**3>0.
assert S.factor((1-a)*(1-phi)) == S.factor(w**2*e)
assert S.simplify((1-a)-(phi*(2-a)**2)+1)==0
for aa,ee in [(S.Rational(1,2),S.Rational(1,10)),(S.Rational(1,3),S.Rational(1,2)),(S.Rational(4,5),2)]:
 cval=float(C.subs({a:aa,e:ee}))
 assert cval>0

# Independently integrate a fixed equation, not substituted normal-form data.
for ee,dd in [(0.1,0.0005),(0.1,0.001),(1.0,0.005)]:
 aa=.5;pp=1/(2-aa)-dd;vv=(1-aa)*(1-pp)
 def ode(t,z):
  u,v=z
  return [u*((1-pp*u)*(u-aa)-v)/ee,v*(u-1)]
 def event(t,z):return z[0]-1
 event.direction=1;event.terminal=False
 horizon=600 if ee<.5 else 1800
 sol=solve_ivp(ode,(0,horizon),[1.02,vv],events=event,rtol=3e-9,atol=1e-11,max_step=.3)
 ts=sol.t_events[0];late=ts[ts>.75*horizon]
 assert len(late)>3
 observed=np.diff(late)[-3:].mean()
 omega=(1-aa)/np.sqrt(ee*(2-aa))
 cv=float(C.subs({a:S.Rational(1,2),e:S.Rational(str(ee))}))
 predicted=2*np.pi/(omega-cv*dd)
 assert abs(observed/predicted-1)<0.015,(ee,dd,observed,predicted)
print('Exact symbolic Fourier, Hopf, moment, and finite-orbit checks PASS')
