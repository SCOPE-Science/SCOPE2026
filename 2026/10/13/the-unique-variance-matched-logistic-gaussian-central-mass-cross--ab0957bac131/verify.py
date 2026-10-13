#!/usr/bin/env python3
import math
a=math.pi/(2*math.sqrt(3))
beta=2*a
phi=lambda x: math.exp(-x*x/2)/math.sqrt(2*math.pi)
Phi=lambda x: (1+math.erf(x/math.sqrt(2)))/2
H=lambda x: math.tanh(a*x)-(2*Phi(x)-1)
R=lambda x: math.log(a/(2*phi(x)))-2*math.log(math.cosh(a*x))
r1,r2=R(1.0),R(2.0)
assert r1 < -0.10 and r2 < -0.16
assert H(1.0)>0.036 and H(2.0)<-0.006
lt=2/(1+math.exp(2*beta))
nu=(15/16)*phi(2)
assert lt>nu and lt>0.0517 and nu<0.0507
lo,hi=1.7,1.8
for _ in range(100):
    m=(lo+hi)/2
    if H(m)>0: lo=m
    else: hi=m
cs=(lo+hi)/2
assert abs(H(cs))<1e-14
for j in range(1,400):
    assert H(cs*j/400)>-5e-14
for j in range(1,400):
    x=cs+(8-cs)*j/400
    assert H(x)<5e-14
print("VERIFY_OK cstar=%.15f R1=%.15f R2=%.15f"%(cs,r1,r2))
