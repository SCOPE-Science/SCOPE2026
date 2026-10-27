import numpy as np,math
from scipy.optimize import brentq
from scipy.integrate import quad

def density(a,s):
 q=math.exp(-a);h=math.sinh(a/2);c=math.cosh(a/2)
 def LEU(t):
  D=1-2*q*math.cos(t)+q*q
  fac=16*a*q*q/D**2
  L=fac*h*h*math.cos(t/2)**2
  E=fac*(h*h*math.cos(t/2)**2+c*c*math.sin(t/2)**2)
  return L,E,L+E*h*h
 L0,E0,U0=LEU(0); Lp,Ep,Up=LEU(math.pi)
 lo=brentq(lambda t:LEU(t)[0]-s,0,math.pi) if 0<s<L0 else 0
 hi=brentq(lambda t:LEU(t)[2]-s,0,math.pi) if Up<s<U0 else math.pi
 if lo>=hi:return 0
 def f(t):
  L,E,U=LEU(t)
  if s<=L:return 0
  return 1/math.sqrt((s-L)*(s-L+E))
 v,e=quad(f,lo,hi,epsabs=1e-9,limit=150,points=[lo,hi])
 return v/(math.pi*a)
for a in (1,3):
 q=math.exp(-a);e=a*math.tanh(a/2)**2
 Ae=2*a*a*math.tanh(a/2);Be=2*e*q/(1+q)**2
 J=2/(math.pi*Ae*math.sqrt(Be))
 base=density(a,e)
 print('a',a,'base',base,'pred',J)
 for eps in [1e-3,1e-4,1e-5]:
  print(eps,'plus',density(a,e+eps),'ratio',(base-density(a,e+eps))/math.sqrt(eps),'minus',density(a,e-eps))
