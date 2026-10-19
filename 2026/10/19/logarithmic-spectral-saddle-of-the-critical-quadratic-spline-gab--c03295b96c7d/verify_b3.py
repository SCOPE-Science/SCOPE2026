#!/usr/bin/env python3
"""Checks of quadratic-cardinal-spline critical Zak symbol and density law."""
import math
import numpy as np
from scipy.integrate import quad
rng=np.random.default_rng(27072)
N=600000
xx=rng.random(N)
ww=rng.random(N)
def b3(t):
 t=abs(t)
 return np.where(t<0.5, .75-t*t, np.where(t<1.5,.5*(1.5-t)**2,0))
z=sum(b3(xx-k)*np.exp(2j*np.pi*k*ww) for k in range(-2,4))
y=np.minimum(xx,1-xx)
v=np.sin(np.pi*ww)**2
T=1-4*y**2
s=1-v+.25*v*v*T*T
assert np.max(abs(abs(z)**2-s))<2e-14
assert np.min(s)>=0 and np.max(s)<=1+1e-14
print('EXACT ZAK S FORMULA verified 600000 random fibers; discrepancy',np.max(abs(abs(z)**2-s)))
# Independent CDF formula using the conditional arcsine tail, versus raw torus area.
def cdf(lev):
 tmax=min(1,2*math.sqrt(lev))
 def f(t):
  vs=2*(1-lev)/(1+math.sqrt(1-t*t*(1-lev)))
  return math.acos(math.sqrt(min(1.,max(0.,vs))))/(math.pi*math.sqrt(1-t))
 return quad(f,0,tmax,epsabs=2e-9,limit=250)[0]
for lev in (.05,.2,.25,.5,.8):
 a=cdf(lev)
 mc=np.mean(s<=lev)
 assert abs(a-mc)<.004,(lev,a,mc)
 print('CDF',lev,'conditional',a,'MC',mc)

def density(s):
 def vsol(t):
  return 2*(1-s)/(1+math.sqrt(max(0.,1-t*t*(1-s))))
 def fun(t):
  v=vsol(t)
  if v>=1: return 0.
  return 1/(2*math.pi*math.sqrt(1-t)*math.sqrt(v*(1-v))*math.sqrt(1-t*t*(1-s)))
 tmax=min(1,2*math.sqrt(s))
 # regularize at tmax, choosing t=tmax*sin^2theta
 def phi(p):
  t=tmax*math.sin(p)**2
  dt=2*tmax*math.sin(p)*math.cos(p)
  if p==0: return 0
  if p==math.pi/2: return 0
  return dt*fun(t)
 return quad(phi,0,math.pi/2,epsabs=2e-8,limit=250)[0]
for s0 in (0.0001,.005,.05,.15,.24,.249,.251,.26,.4,.7,.95,.99):
 d=density(s0)
 h=.002 if s0<.1 else .004
 if s0>=.005:
  m=np.mean((s>s0-h/2)&(s<s0+h/2))/h
  print('DENSITY',s0,'quad',round(d,9),'MC',round(m,4))
 else:
  print('DENSITY',s0,'quad',round(d,9),'MC skipped (rare lower-tail event)')
# crosscheck analytic saddle law slope at deltas
vals=[]
for delta in (.01,.003,.001,.0003,.0001,.00003):
 dpos=density(.25+delta)
 dneg=density(.25-delta)
 print('SADDLE',delta,'plus',round(dpos,9),'minus',round(dneg,9),'ratio+',round(dpos/math.log(1/delta),7),'ratio-',round(dneg/math.log(1/delta),7))
 vals.append((delta,dpos,dneg))
# a finite-difference estimate of the logarithmic coefficient cancels the O(1) term
from math import log, pi
a,b=vals[-2],vals[-1]
slope=(b[1]-a[1])/log(a[0]/b[0])
assert abs(slope-1/pi)<.006,(slope,1/pi)
assert abs(density(.0001)-.5)<.01
print('SADDLE LOGARITHMIC SLOPE',slope,'expected',1/pi)
# high spectral edge
for eps in (.002,.0002):
 d=density(1-eps)
 assert abs(d*math.sqrt(eps)-1/math.pi)<.005
 print('UPPER_EDGE',eps, 'density*sqrt(eps)',d*math.sqrt(eps),'expected',1/math.pi)
print('PASSED')
