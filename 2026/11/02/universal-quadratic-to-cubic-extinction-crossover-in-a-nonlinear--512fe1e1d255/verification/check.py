from fractions import Fraction
import sympy as S
from scipy.integrate import solve_ivp
import numpy as np
u,z,s,delta,h,e,m,sigma=S.symbols('u z s delta h e m sigma',positive=True)
B=s*delta/(s+delta); H=h+B;a=delta/(s+delta);v0=s/(s+delta)
v=v0+a*u+z
f=u*(u/(m+u)-e-h*u)+delta*u*(v-u)
g=v*(s-s*v)+delta*v*(u-v)
assert S.simplify(f.subs(e,B)-(-sigma*u**2-u**3/(m*(m+u))+delta*u*z).subs(sigma,H-1/m))==0
assert S.simplify(g+(s+delta)*v*z)==0
print('symbolic exact identity PASS')
# Critical center coefficient
assert S.simplify((u**3/(m*(m+u))).subs(m,1/H)/u**3-H**2/(1+H*u))==0
print('critical coefficient PASS')

# choose s=delta=1, h=e=1/2, B=1/2, H=1
def rhs(t,y, sig):
 x,v=y
 mm=1/(1-sig)
 return [x*(x/(mm+x)-.5-.5*x)+(x*(v-x)), v*(1-v)+v*(x-v)]
from scipy.optimize import brentq
from math import log
max_err_at_small_sigma=0.0
for sig in [0.1,0.05,0.025]:
 ttarget=2/sig**2
 sol=solve_ivp(rhs,[0,ttarget],[.1,.55],args=(sig,),rtol=1e-10,atol=1e-13,dense_output=True)
 for tau in [.2, .5, 1.,2.]:
  x=sol.sol(tau/sig**2)[0]
  U=x/sig
  Ur=brentq(lambda q:1/q+log(q/(1+q))-tau,0.01,100)
  if sig == .025:
   max_err_at_small_sigma=max(max_err_at_small_sigma,abs(U-Ur))
  print('sigma',sig,'tau',tau,'U',round(U,8),'profile',round(Ur,8),'diff',round(U-Ur,8))
assert max_err_at_small_sigma < 0.04
sig=0.0
sol=solve_ivp(rhs,[0,20000],[.1,.55],args=(sig,),rtol=1e-10,atol=1e-13,dense_output=True)
for t in [1000,5000,20000]:
 x=sol.sol(t)[0];print('critical t',t,'t*u^2',t*x*x,'expected',.5)
assert abs(20000*sol.sol(20000)[0]**2-0.5)<.02
print('ALL CHECKS PASSED')
