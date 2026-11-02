"""Standalone checks for stationary conditional sheared-reset Brownian moments.
Requires Python 3, sympy, scipy. Deterministic assertions only; analytic proof is in RESULT.md.
"""
from math import exp, sqrt, pi, factorial
from scipy.integrate import quad
import sympy as s

z,r,D,g=s.symbols('z r D g', positive=True)
P1=z+1
P2=z*z+3*z+3
P3=z**3+6*z*z+15*z+15
assert s.expand(P2-P1**2)==z+2
var=s.expand((D/r)*P1 + D*g**2/(48*r**3)*P3 + D*g**2*z*z/(16*r**3)*(P2-P1**2))
assert s.simplify(var-((D/r)*(z+1)+D*g**2/(48*r**3)*(4*z**3+12*z*z+15*z+15)))==0
assert s.diff(var,z).subs(z,0).is_positive
# The marginal |Y| sqrt(r/D) is Exp(1), so the expectation of z**n is n!.
def Epoly(p):
 p=s.Poly(s.expand(p),z)
 return s.simplify(sum(coeff*factorial(m[0]) for m,coeff in p.terms()))
assert s.simplify(Epoly(var)-(2*D/r+13*D*g*g/(8*r**3)))==0
m2=D*g*g/(16*r**3)*z*z*(1+z)**2
assert s.simplify(Epoly(m2)-19*D*g*g/(8*r**3))==0
assert s.simplify(Epoly(var+m2)-(2*D/r+4*D*g*g/r**3))==0
cross=g*D/(4*r*r)*z*z*(1+z)
assert s.simplify(Epoly(cross)-2*D*g/r**2)==0
for dd,rr,gg in [(1.0,1.0,1.0),(0.7,1.3,2.1),(3.5,0.45,-1.4)]:
 for yy in [-2.3,-0.8,0.,0.6,2.]:
  # change A=t*t removes the a**(-1/2) posterior singularity at zero
  def weight(t):
   return 2.0*exp(-rr*t*t-yy*yy/(4*dd*t*t))/sqrt(4*pi*dd) if t>0 else 0.
  ints=[]
  for n in range(4):
   q,_=quad(lambda t: weight(t)*t**(2*n),0,max(15/sqrt(rr),10),epsabs=1e-12,limit=300)
   ints.append(q)
  moments=[v/ints[0] for v in ints]
  zz=abs(yy)*sqrt(rr/dd)
  target=[1,(zz+1)/(2*rr),(zz*zz+3*zz+3)/(4*rr*rr),(zz**3+6*zz**2+15*zz+15)/(8*rr**3)]
  for a,b in zip(moments,target): assert abs(a-b)<2e-8*max(1,abs(b)),(a,b)
  mean=gg*yy*moments[1]/2
  v=2*dd*moments[1]+dd*gg**2*moments[3]/6+gg**2*yy**2*(moments[2]-moments[1]**2)/4
  fmean=gg*yy*(zz+1)/(4*rr)
  fvar=dd*(zz+1)/rr+dd*gg**2*(4*zz**3+12*zz**2+15*zz+15)/(48*rr**3)
  assert abs(mean-fmean)<1e-8*max(1,abs(fmean))
  assert abs(v-fvar)<1e-8*max(1,abs(fvar))
print('PASS: polynomial identities, original-paper covariance and variance, 45 numerical posterior moments and 15 conditional pairs')
