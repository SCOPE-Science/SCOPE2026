"""Numerical corroboration for sharp cross-norm Lorentz projector stability.
This does not replace the analytic all-dimension proof in RESULT.md.
"""
import math, random

def proj(z):
 t=z[0]; x=z[1:]; r=math.sqrt(sum(v*v for v in x))
 if r<=t: return z[:]
 if r<=-t: return [0.]*len(z)
 q=(t+r)/2
 return [q]+[q*v/r for v in x]

def J(lam,u):
 d=len(u)
 return [[.5]+[.5*v for v in u]]+[[.5*u[i]]+[(.5*((1+lam if i==j else 0)-lam*u[i]*u[j])) for j in range(d)] for i in range(d)]

def formula(d):
 if d==1: return 1.
 lo,hi=0.,1.
 def deriv(a):return 1-2*a+math.sqrt(d-1)*(1-2*a*a)/math.sqrt(1-a*a)
 for _ in range(100):
  mid=(lo+hi)/2
  if deriv(mid)>0:lo=mid
  else:hi=mid
 a=(lo+hi)/2
 F=1+(a-a*a+a*math.sqrt((d-1)*(1-a*a)))/2
 return max((1+math.sqrt(d))/2,F)

random.seed(2417)
checks=0
for d in range(1,21):
 sharp=formula(d)
 for k in range(180):
  u=[random.gauss(0,1) for _ in range(d)]
  rr=math.sqrt(sum(v*v for v in u));u=[v/rr for v in u]
  lam=random.uniform(-.9999,.9999)
  jac=J(lam,u)
  rowmax=max(sum(abs(v) for v in row) for row in jac)
  assert rowmax<=sharp+2e-12, (d,rowmax,sharp)
  checks+=1
  # Symmetric finite-difference consistency, interior mixed branch.
  z=[lam]+u
  delta=1e-6
  h=[random.uniform(-1,1) for _ in range(d+1)]
  plus=proj([z[i]+delta*h[i] for i in range(d+1)])
  minus=proj([z[i]-delta*h[i] for i in range(d+1)])
  deriv=[sum(jac[i][j]*h[j] for j in range(d+1)) for i in range(d+1)]
  assert max(abs((plus[i]-minus[i])/(2*delta)-deriv[i]) for i in range(d+1))<1e-5
  checks+=1
 for k in range(40):
  t=random.uniform(-2,2)
  x=[random.uniform(-1,1) for _ in range(d)]
  y=[random.uniform(-1,1) for _ in range(d+1)]
  z=[t]+x
  nz=max(abs(a-b) for a,b in zip(z,y))
  ratio=max(abs(a-b) for a,b in zip(proj(z),proj(y)))/nz
  assert ratio<=sharp+1e-10,(d,ratio,sharp)
  checks+=1
 if d>=5: assert abs(sharp-(1+math.sqrt(d))/2)<2e-12
 if d in (2,3,4):assert sharp>(1+math.sqrt(d))/2
 checks+=1
print('PASSED',checks,'tests across spatial dimensions 1..20')
print('Low-dimensional sharp constants:',[(d,round(formula(d),12)) for d in range(1,7)])
