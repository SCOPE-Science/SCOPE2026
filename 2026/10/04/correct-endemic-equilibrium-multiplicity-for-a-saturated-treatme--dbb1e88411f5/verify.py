#!/usr/bin/env python3
from fractions import Fraction as F
import math

mu_h=mu_v=delta=gamma=u=alpha1=alpha2=beta2=Lv=F(1)
b=F(100); Lh=F(10); beta1=F(29,100)
R02=beta1*beta2*Lh*Lv/(mu_v**2*mu_h*(mu_h+delta+gamma*u))
C0=b*u*(delta+mu_h)*(mu_h*(alpha1*beta2*Lv+mu_v*(beta2+alpha2*mu_v))+beta1*beta2*Lv)
C1=mu_h*(mu_v*(mu_v*(b*u*(delta+mu_h)+alpha2*(delta+mu_h+gamma*u))+beta2*(delta+mu_h+gamma*u))+alpha1*beta2*Lv*(delta+mu_h+gamma*u))+beta1*beta2*Lv*(-b*u*Lh+delta+mu_h+gamma*u)
C2=mu_h*mu_v**2*(delta+mu_h+gamma*u)*(1-R02)
D=C1*C1-4*C0*C2
assert R02==F(29,30)
assert C0==658 and C1==F(-8013,100) and C2==F(1,10)
assert D==F(61576169,10000) and D>0 and C1<0 and C2>0
roots=[(-float(C1)-math.sqrt(float(D)))/(2*float(C0)),(-float(C1)+math.sqrt(float(D)))/(2*float(C0))]
assert 0<roots[0]<roots[1]

def reconstruct(I):
    Iv=I/(1+2*I)
    Sv=(1+I)/(1+2*I)
    Sh=10/(1+0.29*Iv/(1+Iv))
    Rh=I/(1+100*I)
    res=[
      10-0.29*Sh*Iv/(1+Iv)-Sh,
      0.29*Sh*Iv/(1+Iv)-2*I-I/(1+100*I),
      I/(1+100*I)-Rh,
      1-Sv*I/(1+I)-Sv,
      Sv*I/(1+I)-Iv]
    assert max(abs(x) for x in res)<2e-13
    assert min(Sh,I,Rh,Sv,Iv)>0
    assert Sh+I+Rh<10+1e-12 and abs(Sv+Iv-1)<2e-13
    return Sh,I,Rh,Sv,Iv
states=[reconstruct(I) for I in roots]
print('VERIFY_OK')
print('R0_squared',R02)
print('C0',C0,'C1',C1,'C2',C2,'Delta',D)
for j,(I,s) in enumerate(zip(roots,states),1):
    print('root',j,repr(I),'state',tuple(repr(x) for x in s))
