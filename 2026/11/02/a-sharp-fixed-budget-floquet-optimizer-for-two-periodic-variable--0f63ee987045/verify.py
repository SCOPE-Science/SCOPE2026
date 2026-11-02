"""Independent algebraic and finite-parameter checks for periodic variable-step BDF2 decay.
Run: python verify.py  (requires sympy and numpy). The analytical proof is in RESULT.md.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as S
r, z, q=S.symbols('r z q',positive=True)
a=z+2; b=2-z; c=a*a+1
D1=1+(z+2)*r
D2=(r+z+2)/r
T1=S.Matrix([[(1+r)**2/D1, -r**2/D1],[1,0]])
T2=S.Matrix([[(1+1/r)**2/D2, -(1/r)**2/D2],[1,0]])
M=S.simplify(T2*T1)
B=a*q+c;N=b*q+6
assert S.simplify(S.trace(M)-N.subs(q,r+1/r)/B.subs(q,r+1/r))==0
assert S.simplify(M.det()-1/B.subs(q,r+1/r))==0
assert S.factor((N*N-4*B) - (q+2)*((z-2)**2*q-2*(z*z+4*z-4)))==0
assert S.factor(B-N+1-z*(2*q+z+4))==0
assert S.factor(B+N+1-(4*q+z*z+4*z+12))==0
assert S.factor((c*b*b-6*a*b+a*a)/a**2-z**4/a**2)==0
qstar=2*(z*z+4*z-4)/(z-2)**2
assert S.factor(B.subs(q,qstar)-(z*z+z+2)**2/(z-2)**2)==0
assert S.factor(qstar-2 -16*(z-1)/(z-2)**2)==0

def spectral(zv,rv):
    w=float(rv); s=float(zv)
    T_r=np.array([[(1+w)**2/(1+(2+s)*w),-w*w/(1+(2+s)*w)],[1,0]])
    T_inv=np.array([[(1+1/w)**2/(1+2/w+s/w),-(1/w)**2/(1+2/w+s/w)],[1,0]])
    return float(max(abs(np.linalg.eigvals(T_inv@T_r))))

def theoretical(zv,rv):
    x=float(zv); qq=rv+1/rv; BB=(x+2)*qq+(x+2)**2+1;NN=(2-x)*qq+6
    dd=NN*NN-4*BB
    return (abs(NN)+math.sqrt(dd))/(2*BB) if dd>=0 else 1/math.sqrt(BB)

for zv in [0.001,0.1,0.5,0.999,1,1.01,1.25,1.9,2,2.01,2.5,3,4,10,30,100]:
  for rv in [0.001,0.02,0.1,0.3,1,3,10,50,1000]:
    x=spectral(zv,rv); y=theoretical(zv,rv)
    assert abs(x-y)<3e-9,(zv,rv,x,y)
    assert 0<x<1,(zv,rv,x)

for zv in [0.1,.5,1,1.01,1.2,1.9,2.1,3,4,10,25,100]:
  qs=np.linspace(2,2000,15000)
  radii=np.array([theoretical(zv,(qq+math.sqrt(qq*qq-4))/2) for qq in qs])
  if zv<=1:
    assert np.min(radii)>=theoretical(zv,1)-1e-9
  else:
    qsopt=2*(zv*zv+4*zv-4)/(zv-2)**2
    if qsopt<=2000:
      r_opt=(qsopt+math.sqrt(qsopt*qsopt-4))/2
      target=abs(zv-2)/(zv*zv+zv+2)
      assert abs(theoretical(zv,r_opt)-target)<1e-8
      assert np.min(radii)>=target-1e-8

q4=S.Integer(14)
assert S.factor(qstar.subs(z,4)-q4)==0
rsmall=7-4*S.sqrt(3)
M4=S.simplify(M.subs({z:S.Integer(4),r:rsmall}))
assert S.factor(M4.trace()+S.Rational(2,11))==0
assert S.factor(M4.det()-S.Rational(1,121))==0
assert S.simplify(M4+S.eye(2)/11)!=S.zeros(2)
assert S.simplify((M4+S.eye(2)/11)**2)==S.zeros(2)
assert abs(spectral(4,1)-1/7)<1e-12
assert abs(spectral(4,float(rsmall))-1/11)<1e-10
assert abs(spectral(2,1)-1/5)<1e-12
for rv in [1e-2,1e-4,1e-6]:
    ratio=spectral(2,rv)/(math.sqrt(rv)/2)
    assert abs(ratio-1)<.03
print('VERIFY_OK symbolic identities=8, 135 spectral comparisons, grid minima=12, exact defective optimum and resonant asymptotics')
