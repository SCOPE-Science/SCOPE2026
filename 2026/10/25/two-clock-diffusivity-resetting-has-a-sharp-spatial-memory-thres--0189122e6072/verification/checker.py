"""Checks for independently reset diffusivity and position clouds."""
import sympy as s
A,B,L,t,N,z,w,x=s.symbols('a b L t N z w x',positive=True,real=True)
# a: medium reset rate, b: common position reset rate.
M_y2=2*L**2/A
M_y4=24*L**4/A**2
M_x2=4*L**2/(A*B)
M_xy2=s.factor((2*M_y4+2*L**2*M_x2)/(A+B))
Cov_xy=s.factor(M_xy2-M_x2*M_y2)
M_x4=s.factor(12*M_xy2/B)
M_x2z2=s.factor(2*(M_xy2+M_xy2)/B)
M_q2=s.factor(M_x2z2)
Var_q=s.factor(M_q2-M_x2**2)
assert s.simplify(Cov_xy-40*L**4/(A**2*(A+B)))==0
assert s.simplify(Var_q-(16*L**4/(A**2*B**2)+160*L**4/(A**2*B*(A+B))))==0
assert s.simplify(M_q2-(32*L**4/(A**2*B**2)+160*L**4/(A**2*B*(A+B))))==0
assert s.simplify(M_x4-3*M_q2)==0
# Independent stationary integration: Brownian diffusivity autocovariance 20 L^4/a^2 exp(-a t).
# Q=2 integral since previous position reset, Exp(b) age independent of stationary medium.
# E Q^2=4 m^2 E age^2+4 sigma^2 E double integral exp(-a |u-v|).
mean=M_y2
sigma=20*L**4/A**2
assert s.simplify(4*mean**2*(2/B**2)+4*sigma*(2/(B*(A+B)))-M_q2)==0
# Generator with position-reset-to-origin rate b and independent diffusivity reset rate a.
def G(f):
 return s.expand(L**2*s.diff(f,w,2)+w**2*(s.diff(f,x,2)+s.diff(f,z,2))+A*(f.subs(w,0)-f)+B*(f.subs({x:0,z:0})-f))
m={s.Integer(1):s.Integer(1),w**2:M_y2,w**4:M_y4,x**2:M_x2,z**2:M_x2,x**2*w**2:M_xy2,z**2*w**2:M_xy2,x**2*z**2:M_q2,x**4:M_x4}
def E(poly):
 ans=0
 for power,c in s.Poly(s.expand(poly),x,z,w).terms():
  key=x**power[0]*z**power[1]*w**power[2]
  assert key in m,('unknown moment',key)
  ans+=c*m[key]
 return s.factor(ans)
for f in [w**2,w**4,x**2,z**2,x**2*w**2,z**2*w**2,x**2*z**2,x**4]:
 assert E(G(f))==0,f
# Stationary lag covariance differential equation C'=-b C+2cov(x_0^2,w_t^2).
Cq=s.exp(-B*t)*Var_q+2*Cov_xy*s.exp(-B*t)*s.Integral(s.exp((B-A)*s.Symbol('h')),(s.Symbol('h'),0,t))
# Write expression analytically for a!=b and continuous resonance.
Cq_closed=s.exp(-B*t)*Var_q+2*Cov_xy*(s.exp(-A*t)-s.exp(-B*t))/(B-A)
assert s.simplify(Cq_closed.subs(t,0)-Var_q)==0
assert s.simplify(s.diff(Cq_closed,t)+B*Cq_closed-2*Cov_xy*s.exp(-A*t))==0
Ceq=s.exp(-B*t)*(Var_q+2*Cov_xy*t)
assert s.simplify(s.limit(Cq_closed,A,B)-Ceq.subs(A,B))==0
# For i=j, Gaussian squares share pre-0 Brownian increment only when no position reset:
C_same=Cq_closed+2*M_q2*s.exp(-B*t)
C_emp=s.factor(Cq_closed+2*M_q2*s.exp(-B*t)/N)
assert s.simplify(C_emp - (Cq_closed+(C_same-Cq_closed)/N))==0
# ratio limiting when medium slower, equal, faster than position resets.
Clead_fast=s.factor(Var_q+2*Cov_xy/(A-B)) # a>b
Rfast=s.factor(Clead_fast/(Clead_fast+2*M_q2))
print('EXACT: independent Poisson generator stationarity and two-time ODE identity passed')
print('cross variance =',s.factor(Var_q))
print('common-medium covariance =',s.factor(Cov_xy))
print('same-coord extra amplitude=',s.factor(2*M_q2))
print('fast-medium ratio:',Rfast)
for aa in [s.Rational(1,3),s.Rational(1),s.Rational(2),s.Rational(5)]:
 for bb in [s.Rational(1,4),s.Rational(1),s.Rational(3)]:
  for ll in [s.Rational(1),s.Rational(7,5)]:
   P={A:aa,B:bb,L:ll}
   for lag in [s.Rational(0),s.Rational(1,2),s.Rational(4)]:
    c=float((Ceq if aa==bb else Cq_closed).subs(P).subs(t,lag))
    auto=float((Ceq if aa==bb else Cq_closed).subs(P).subs(t,lag)+2*M_q2.subs(P)*s.exp(-bb*lag))
    assert c>0 and auto>c
print('PASS: 72 exact parameter-lag comparisons and positivity')
