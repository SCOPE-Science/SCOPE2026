"""Finite-time moment and critical scaling reproducibility checks (Python 3 standard library)."""
from math import exp,expm1,isclose
from fractions import Fraction as F
ncheck=0

def chk(x):
 global ncheck
 ncheck+=1
 if not x: raise AssertionError(ncheck)

def vals(s,theta,u,lam=1.,D=1.):
 gam=lam*(1-1.5*s+theta*s*s)
 a1=2*(lam-gam)-lam*s
 a2g=4*(lam-gam)-6*lam*s
 a2p=lam/s*(1-(1-s)**4)-4*gam
 t=u/(lam*s*s)
 m1=2*D*(-expm1(-a1*t))/a1
 def m2(a2):
  v1=(-expm1(-a2*t))/a2
  v2=(exp(-a1*t)-exp(-a2*t))/(a2-a1) if abs(a2-a1)>1e-10 else t*exp(-a2*t)
  return 8*D*D/a1*(v1-v2)
 return a1,a2p,a2g,m1,m2(a2p)-m1*m1,m2(a2g)-m1*m1

for s in [0.25,0.1,0.02,0.005]:
 for theta in [0.1,0.3,0.7]:
  for u in [0.1,0.5,1,2,4]:
   a1,ap,ag,m,c1,c2=vals(s,theta,u)
   chk(a1>0 and ap>ag and c2>c1>0)
   chk(isclose(ap-ag,s*s*(4-s),rel_tol=1e-8,abs_tol=1e-12))
for theta in [0.2,0.5,0.8]:
 for u in [0.2,1,3]:
  P=(1-exp(-4*(1-theta)*u))/(1-theta)
  G=expm1(4*theta*u)/theta
  chk(G>P>0)
  errors=[]
  for s in [0.02,0.005,0.001]:
   _,_,_,_,cp,cg=vals(s,theta,u)
   errors.append(abs(cp*s**3-P)+abs(cg*s**3-G))
  chk(errors[-1]<errors[0]*0.3)
for s in [F(1,20),F(1,10),F(1,4)]:
 for theta in [F(1,10),F(2,5),F(3,4)]:
  gam=1-F(3,2)*s+theta*s*s
  a1=2*(1-gam)-s
  ag=4*(1-gam)-6*s
  ap=(1-(1-s)**4)/s-4*gam
  chk(a1==2*s*(1-theta*s))
  chk(ag==-4*theta*s*s)
  chk(ap==s*s*(4*(1-theta)-s))
  chk(ap-ag==s*s*(4-s))
print('PASS',ncheck,'finite consistency checks')
