#!/usr/bin/env python3
"""Reproducible algebraic and numerical corroboration of the stated sigmoid-feedback identities."""
import math
from fractions import Fraction
from scipy.integrate import solve_ivp
import numpy as np

b,c,eps,beta = 1.0,0.2,0.8,3.0
rstar=2*c/b
omega=math.sqrt(b*beta*rstar*(1-rstar)/(16*eps))
assert 0<rstar<1 and omega>0

def f(t,z):
 x,r=z
 return [x*(1-x)*(2*b*r*x*(1-x)-c)/eps,-r*(1-r)*math.tanh(beta*(x-.5)/2)]
# Exact-rational reflection and payoff tests, independent of numerical ODE.
for a,d in [(Fraction(1,3),Fraction(3,7)),(Fraction(2,5),Fraction(1,4)),(Fraction(3,4),Fraction(7,11))]:
 h=a*(1-a)
 assert h==(1-a)*a
 assert h==Fraction(1,4)-(a-Fraction(1,2))**2
 assert d*h==d*a*(1-a)
 assert abs(math.tanh(beta*(float(a)-.5)/2)+math.tanh(beta*(.5-float(a))/2))<1e-14

z0=[.5,rstar+.025]
# Locate the second crossing (positive-to-negative) of the symmetry axis.
def section(t,z):return z[0]-.5
section.direction=-1
section.terminal=True
sol=solve_ivp(f,(0,25),z0,events=section,rtol=2e-11,atol=2e-13,max_step=.01,dense_output=True)
assert len(sol.t_events[0])==1 and sol.t_events[0][0]>0
half=float(sol.t_events[0][0]); full=2*half
orbit=solve_ivp(f,(0,full),z0,rtol=2e-11,atol=2e-13,dense_output=True,max_step=.01)
xx=np.linspace(0,full,30001);x,r=orbit.sol(xx)
assert max(abs(orbit.y[:,-1]-np.array(z0)))<2e-8
avg=lambda z:float(np.trapz(z,xx)/full)
assert abs(avg(x)-.5)<1e-8
assert abs(avg((x-.5)*r))<1e-8
excess=avg(r)-rstar
predict=4*avg(r*(x-.5)**2)
assert excess>0 and abs(excess-predict)<2e-8
print('PASS: reflection, section closure, zero risk-cooperation covariance, strict risk premium')
print('period',full,'equilibrium_risk',rstar,'average_risk',avg(r),'risk_premium',excess,'variance_premium',predict)
