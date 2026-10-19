#!/usr/bin/env python3
"""Independent finite tests for a periodic two-population competition identity.
No finite check establishes its asymptotic theorem.
"""
from math import sin, cos, pi, exp, log
from scipy.integrate import solve_ivp, quad
import numpy as np

T=1.; lam=.75
p=(.9,.85); q=(.9,.88); phases=(.3,.8)
rbar=1.5
s0=lam*rbar + lam*log(np.prod(p))-log(np.prod(q))
def rates(t):
 r=1.5+.2*sin(2*pi*t)
 a=1.+.1*cos(2*pi*t)
 b=.35+.03*sin(2*pi*t)
 g=.7+.05*cos(2*pi*t)
 return r,a,b,g

def vf(t,Z):
 x,y,H=Z;r,a,b,g=rates(t)
 return [x*(r-a*x-b*y), y*(s0-lam*a*x-(lam*b+g)*y),g*y]

# Numerically determine the positive resident periodic orbit.
def resident_step(x):
 out=x
 last=0
 for end,pulse in zip((*phases,T),(*p,1.)):
  def fv(t,U):
   r,a,b,g=rates(t);return [U[0]*(r-a*U[0])]
  out=solve_ivp(fv,(last,end),[out],rtol=3e-11,atol=3e-12).y[0,-1]*pulse
  last=end
 return out
xstar=.5
for _ in range(180):xstar=resident_step(xstar)
assert abs(resident_step(xstar)-xstar)<1e-10
# Periodic forcing normalization at t=T (multipliers).
assert abs(exp(s0-lam*rbar)*np.prod(q)/(np.prod(p)**lam)-1)<2e-14

def sav(t):
 integral=(s0-lam*rbar)*t + .2*lam/(2*pi)*(cos(2*pi*t)-1)
 # NOTE integral r = 1.5t+0.2(1-cos)/2pi => integral s-lam*r = (s-lam*1.5)t -lam*0.2(1-cos)/2pi
 for phase,pp,qq in zip(phases,p,q):
  if t>phase+1e-12:integral+=log(qq)-lam*log(pp)
 return exp(integral)

def build_I():
 states=[(0.,xstar)]
 val=xstar
 last=0.
 for end,pulse in zip((*phases,T),(*p,1.)):
  def f(t,U):
   r,a,b,g=rates(t);return [U[0]*(r-a*U[0])]
  sol=solve_ivp(f,(last,end),[val],rtol=3e-11,atol=3e-12,dense_output=True)
  states.append((last,end,sol, pulse))
  val=sol.y[0,-1]*pulse;last=end
 I=0.
 for j,record in enumerate(states[1:]):
  lo,hi,sol,pulse=record
  I+=quad(lambda t: rates(t)[3]*sav(t)*sol.sol(t)[0]**lam,lo,hi,epsabs=1e-10)[0]
 return I
I=build_I()

x,y=.42,.23
z0=y/x**lam
max_error=0.; results=[]
for k in range(2800):
 z_prev=y/x**lam
 last=0.;H=0.
 for end,pp,qq in zip((*phases,T),(*p,1.),(*q,1.)):
  sol=solve_ivp(vf,(last,end),(x,y,H),rtol=1e-9,atol=1e-11)
  x,y,H=sol.y[:,-1]
  x*=pp;y*=qq
  last=end
 z_now=y/x**lam
 max_error=max(max_error,abs((log(z_now/z_prev)+H)))
 if k in (99,499,999,1999,2799):
  results.append((k+1,(k+1)*H,(k+1)*z_now*I,(k+1)*y*I/xstar**lam))
assert max_error<3e-7, max_error
assert abs(x-xstar)<.003
assert abs((2800)*H-1)<.015, (2800*H,I)
assert abs((2800)*z_now*I-1)<.015
print('s0',s0,'resident_x_post0',xstar,'I',I,'z0',z0)
print('maximum cycle log-ratio identity error',max_error)
for record in results:print('cycle, n*load, n*z*I, n*y*I/(x*_0^lambda):',record)
print('PASS finite numerical and analytic-identity diagnostics')
