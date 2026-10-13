#!/usr/bin/env python3
from fractions import Fraction as F
import cmath, math
r,K,alpha,nu,beta=F(5,3),F(5),F(1),F(1),F(2)
a,b,m,n,e1,e2=[F(1)]*6
x,y=F(1),F(1)
assert r*x*(1-(x+y)/K)-beta*x*y/(alpha+y)==0
assert beta*x*y/(alpha+y)-nu*y==0
A11=-r*x/K
A12=-r*x/K-beta*alpha*x/(alpha+y)**2
A21=beta*y/(alpha+y)
A22=-nu*y/(alpha+y)
assert (A11,A12,A21,A22)==(F(-1,3),F(-5,6),F(1),F(-1,2))
trace=A11+A22
det=A11*A22-A12*A21
assert trace==F(-5,6) and det==F(1)
p=e1*m*x/(b*(a+x))+e2*n
Q=e1*m*K/(b*(a+K))+e2*n
assert p==F(3,2) and Q==F(11,6)
assert F(2)>Q>p>F(1)
h=1.0
w=math.sqrt(float(p)**2-h*h)
theta=math.acos(h/float(p))
assert abs(w-math.sqrt(5)/2)<1e-13
for j in range(6):
    tau=(2*math.pi*(j+1)-theta)/w
    lam=1j*w
    residual=abs(lam+h-float(p)*cmath.exp(-lam*tau))
    speed=w*w/((1+h*tau)**2+(w*tau)**2)
    assert residual<2e-13, (j,residual)
    assert speed>0
    assert abs(math.cos(w*tau)-h/float(p))<2e-13
assert math.isclose((2*math.pi-theta)/w,4.86,abs_tol=0.1)
print('VERIFY_OK')
print('predator p',str(p),'global harvest Q',str(Q))
print('omega',w,'tau_0',(2*math.pi-theta)/w)
print('prey trace',str(trace),'det',str(det))
