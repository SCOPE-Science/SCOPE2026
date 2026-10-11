#!/usr/bin/env python3
import math
from fractions import Fraction
import sympy as sp

x,y,z,u,X=sp.symbols('x y z u X', real=True)
P=0
for a in range(5):
    for b in range(5-a):
        c=4-a-b
        m=math.factorial(4)//(math.factorial(a)*math.factorial(b)*math.factorial(c))
        P += m*m*x**a*y**b*z**c
s1=x+y+z
s2=x*y+x*z+y*z
s3=x*y*z
P_expected=sp.expand(s1**4+12*s1**2*s2+6*s2**2+60*s1*s3)
assert sp.expand(P-P_expected)==0
Q=sp.expand(P_expected.subs({x:u,y:u,z:1-2*u})+2*u**4)
Q_expected=56*u**4-192*u**3+48*u**2+24*u+1
assert sp.expand(Q-Q_expected)==0
f=28*u**3-72*u**2+12*u+3
assert sp.expand(sp.diff(Q,u)-8*f)==0
res=sp.factor(sp.resultant(f,X-Q,u))
expected=1792*(343*X**3+155931*X**2-1117059*X-1095481)
assert sp.expand(res-expected)==0
lo=sp.Rational(334719056638195,10**15)
hi=sp.Rational(334719056638197,10**15)
assert f.subs(u,lo)>0 and f.subs(u,hi)<0
roots=[r for r in sp.nroots(f, n=60) if abs(sp.im(r))<sp.Float('1e-50')]
ur=[sp.re(r) for r in roots if 0<sp.re(r)<sp.Rational(1,2)][0]
val=sp.N(Q.subs(u,ur),40)
k=sp.N(val**sp.Rational(1,8),40)
# Concrete model: dual Z x Z/4, characters (0,0),(0,1),(1,0).
# Sample T densely and average exactly over the Z/4 factor.
u_float=float(ur)
a=math.sqrt(u_float); b=a; c=math.sqrt(1-2*u_float)
M=20000
acc=0.0
for j in range(M):
    t=(j+0.5)/M
    et=complex(math.cos(2*math.pi*t),math.sin(2*math.pi*t))
    for r in range(4):
        er=complex(math.cos(math.pi*r/2),math.sin(math.pi*r/2))
        F=a+b*er+c*et
        acc += abs(F)**8
sample=acc/(4*M)
assert abs(sample-float(val))<2e-10
print('VERIFY_OK polynomial=exact resultant=exact root_isolated=1 sample_error=%.3e X=%.15f K=%.15f' % (abs(sample-float(val)),float(val),float(k)))
