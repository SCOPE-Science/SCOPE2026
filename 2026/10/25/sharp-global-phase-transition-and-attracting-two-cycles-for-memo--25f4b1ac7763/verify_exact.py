"""Independent symbolic-algebra identities and rational numerical tests for the stated circle map.
Run: python verify_exact.py. SymPy is required; numeric checks are supplementary.
"""
import sympy as S
from math import atan, cos, sin, pi, sqrt, tan
A,t=S.symbols('a t',positive=True)
p=A+(A+1)*t*t
q=A+t+A*t*t
D=t*t/p+1/q
Q=S.factor(-S.diff(D,t)*p*p*q*q)
P1=1-2*t*t+4*t**3-3*t**4+4*t**5
expectedQ=A*A*P1+2*A*t*t*(1-t+t*t+t**3)+t**4
assert S.simplify(Q-expectedQ)==0
Np=S.factor((D+t*(1+t*t)*S.diff(D,t))*p*p*q*q)
expectedNp=A**3*(1+t*t)**4+A*A*t*t*(2-t)*(3*t+1)*(1+t*t)**2+2*A*t**4*(2-t*t)*(1+t*t)+t**6*(1-t)
assert S.simplify(Np-expectedNp)==0
print('derivative certificates: PASS')
for aa in [S.Rational(1,20),S.Rational(1,2),S.Integer(1),S.Integer(2),S.Integer(20)]:
 for tt in [S.Rational(i,50) for i in range(1,50)]:
  assert D.subs({A:aa,t:tt})>0
  assert Q.subs({A:aa,t:tt})>0
  assert Np.subs({A:aa,t:tt})>0
for aa in [0.05,0.3,1.,4.]:
 for alpha in [aa,2*aa,2*aa+0.02,4*aa,1000.]:
  def w(x):
   ss=sin(x);cc=cos(x)
   return ss*(ss*ss/(aa+ss*ss)+cc*cc/(aa+abs(ss*cc)))
  def f(x):return x-atan(alpha*w(x))
  for x in [pi*z/400 for z in range(-399,400)]:
   xx=f(x)
   assert abs(xx)<pi+1e-13
   if alpha<=2*aa and abs(x)>1e-12:
    assert abs(xx)<abs(x)+1e-11
  if alpha>2*aa:
   lo,hi=0,pi/4
   for i in range(90):
    mid=(lo+hi)/2
    if f(mid)+mid<0:lo=mid
    else:hi=mid
   root=(lo+hi)/2
   assert abs(f(root)+root)<1e-10
   h=1e-6
   deriv=(f(root+h)-f(root-h))/(2*h)
   assert abs(deriv)<1-1e-10,(aa,alpha,root,deriv)
print('supplementary numerical tests: PASS')
