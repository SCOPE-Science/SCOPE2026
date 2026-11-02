"""Exact symbolic checks and sampled numerical checks for two- and three-pulse susceptibility scheduling."""
import sympy as s
from math import exp, log, sqrt
p,q,r,x,y,E,u=s.symbols('p q r x y E u',positive=True)
D2=1-(1-p)*(1-q)*E
jA=(p+(1-p)*q*E/x)/D2
jB=(q+(1-q)*p*x)/D2
F2=s.factor(jA*(1-x)+jB*(1-E/x))
F2_target=((p+q)*(1-E)+2*E*p*q-p*q*(x+E/x))/D2
assert s.factor(F2-F2_target)==0
A=s.factor(x*jA)
B=s.factor((E/x)*jB)
assert s.factor(A-(p*x+(1-p)*q*E)/D2)==0
assert s.factor(B-(q*E/x+(1-q)*p*E)/D2)==0
assert s.factor(D2*(A-B)-(p*x-q*E/x+(q-p)*E))==0
D3=1-(1-p)*(1-q)*(1-r)*E
z=E/(x*y)
j0=(p+(1-p)*r*z+(1-p)*(1-r)*q*y*z)/D3
j1=q+(1-q)*x*j0
j2=r+(1-r)*y*j1
F3=s.factor(j0*(1-x)+j1*(1-y)+j2*(1-z))
dFx=s.factor(s.diff(F3,x).subs(E,u**3).subs({x:u,y:u},simultaneous=True))
dFy=s.factor(s.diff(F3,y).subs(E,u**3).subs({x:u,y:u},simultaneous=True))
assert s.factor(dFx-p*(q-r)*(u-1)/(1-(1-p)*(1-q)*(1-r)*u**3))==0
assert s.factor(dFy-r*(q-p)*(u-1)/(1-(1-p)*(1-q)*(1-r)*u**3))==0
args={p:s.Rational(3,4),q:s.Rational(1,2),r:s.Rational(1,4),E:s.Rational(1,8)}
fe=s.factor(F3.subs({**args,x:s.Rational(1,2),y:s.Rational(1,2)}))
fu=s.factor(F3.subs({**args,x:s.Rational(2,5),y:s.Rational(1,2)}))
print('Equal 3-pulse deficit integral:', fe, '; unequal:', fu, '; delta:', s.factor(fu-fe))
assert fe==s.Rational(257,253) and fu==s.Rational(2573,2530) and fu-fe==s.Rational(3,2530)
P,Q=.6,.2
EM=exp(-2)
D=1-(1-P)*(1-Q)*EM
xx=(EM*(P-Q)+sqrt(EM**2*(P-Q)**2+4*P*Q*EM))/(2*P)
assert EM<xx<1

def values(X):
    ja=(P+(1-P)*Q*EM/X)/D
    jb=(Q+(1-Q)*P*X)/D
    mean=1-(ja*(1-X)+jb*(1-EM/X))/2
    peak=1-min(X*ja, EM*jb/X)
    return mean, peak
print('Two-pulse equal phase:',values(sqrt(EM)), '; peak-optimum:', values(xx),'; tau/T:',-log(xx)/2)
assert values(sqrt(EM))[0]<values(xx)[0]
assert values(xx)[1]<values(sqrt(EM))[1]
for pp in (.1,.3,.75,.93):
 for qq in (.08,.4,.88):
  for k in (.3,.9,3.7):
   e=exp(-k)
   xstar=(e*(pp-qq)+sqrt(e**2*(pp-qq)**2+4*pp*qq*e))/(2*pp)
   assert e<xstar<1
   d=1-(1-pp)*(1-qq)*e
   def v(a):
    j1=(pp+(1-pp)*qq*e/a)/d
    j2=(qq+(1-qq)*pp*a)/d
    return 1-(j1*(1-a)+j2*(1-e/a))/k,1-min(a*j1,e*j2/a)
   assert v(sqrt(e))[0]<=v(xstar)[0]+1e-12
   assert v(xstar)[1]<=v(sqrt(e))[1]+1e-12
print('Symbolic equations, exact rational witness, and',4*3*3,'numeric parameter checks PASSED')
