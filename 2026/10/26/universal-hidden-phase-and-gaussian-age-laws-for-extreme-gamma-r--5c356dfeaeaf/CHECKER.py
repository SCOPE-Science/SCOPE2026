import numpy as np
from scipy.integrate import quad
from scipy.special import gammaincc,gammaln, ndtr
from math import sqrt,pi,exp,lgamma
checks=0
for s in (0.6,1.,2.4):
 for r,D,v in ((1.,1.,1.),(1.3,0.7,1.8)):
  k=sqrt(r/D)
  prob=v/(v+sqrt(D*r))
  for x in (25.,55.,105.):
   t0=x/(2*sqrt(D*r)); h=sqrt(t0/(2*r))
   def p(t):return 1/sqrt(4*pi*D*t)*exp(-x*x/(4*D*t))
   def psi(t):return exp(s*np.log(r)+(s-1)*np.log(t)-r*t-gammaln(s))
   def a(t):return gammaincc(s,r*t)*p(t)
   def b(t):return psi(t)*ndtr(-x/sqrt(2*D*t))/v
   tlo=max(1.e-7,t0-12*h);thi=t0+12*h
   na=quad(a,tlo,thi,epsrel=1e-9)[0];nb=quad(b,tlo,thi,epsrel=1e-9)[0]
   pa=na/(na+nb)
   mA=quad(lambda t: (t-t0)/h*a(t),tlo,thi,epsrel=1e-9)[0]/na
   mB=quad(lambda t: (t-t0)/h*b(t),tlo,thi,epsrel=1e-9)[0]/nb
   va=quad(lambda t: ((t-t0)/h)**2*a(t),tlo,thi,epsrel=1e-9)[0]/na-mA*mA
   vb=quad(lambda t: ((t-t0)/h)**2*b(t),tlo,thi,epsrel=1e-9)[0]/nb-mB*mB
   print('s,r,D,v,x=',s,r,D,v,x,'phase',round(pa,5),'limit',round(prob,5),'Zmean',round(mA,4),round(mB,4),'Zvar',round(va,4),round(vb,4))
   assert abs(pa-prob)<0.12
   assert abs(mA)<1.5 and abs(mB)<1.5
   assert 0.65<va<1.35 and 0.65<vb<1.35
   checks+=5
print('ASSERTIONS',checks)
