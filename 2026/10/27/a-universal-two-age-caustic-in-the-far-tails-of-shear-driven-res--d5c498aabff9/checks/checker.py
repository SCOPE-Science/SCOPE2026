"""Independent algebraic and numerical checks for the shear-reset rare-event age transition."""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

s,c=sp.symbols('s c',positive=True,real=True)
f=s+1/s-3*c/s**2+3*c**2/s**3
fp=sp.diff(f,s)
assert sp.simplify(fp-(1-(s-3*c)**2/s**4))==0
u=(sp.sqrt(3)-1)/4
v=(sp.sqrt(3)+1)/4
c0=sp.sqrt(3)/24
for t in (u,v):
 assert sp.simplify(fp.subs({s:t,c:c0}))==0
 assert sp.simplify(f.subs({s:t,c:c0})-sp.sqrt(3))==0
assert sp.simplify(v-u-sp.Rational(1,2))==0
assert sp.simplify(sp.diff(f,s,2).subs({s:u,c:c0})-2*(1+2*u)/u**2)==0
assert sp.simplify(sp.diff(f,s,2).subs({s:v,c:c0})-2*(2*v-1)/v**2)==0
fu=sp.simplify(sp.diff(f,c).subs({s:u,c:c0}))
fv=sp.simplify(sp.diff(f,c).subs({s:v,c:c0}))
assert sp.simplify(fu+12+4*sp.sqrt(3))==0
assert sp.simplify(fv+12-4*sp.sqrt(3))==0
wyoung=1/(u*sp.sqrt(1+sp.sqrt(3)))
wold=1/(v*sp.sqrt(sp.sqrt(3)-1))
assert sp.simplify((wyoung/wold)**2-(2+sp.sqrt(3)))==0
root=lambda c:(-1+math.sqrt(1+12*c))/2
old=lambda c:(1+math.sqrt(1-12*c))/2
ff=lambda c,s:s+1/s-3*c/s**2+3*c*c/s**3
for cc in np.linspace(.001,.083,83):
 e_y=ff(cc,root(cc)); e_o=ff(cc,old(cc))
 if cc<float(c0)-1e-5: assert e_o<e_y
 if cc>float(c0)+1e-5: assert e_y<e_o

# Independent Gaussian covariance versus path-action quadratic optimization
T=sp.symbols('T', positive=True)
U,V=sp.symbols('U V')
AB=sp.solve([U*T+V*T*T-1,U*T*T/2+V*T**3/3-c],[U,V])
action=sp.integrate((AB[U]+2*AB[V]*s)**2/4,(s,0,T))
assert sp.simplify(action-(1/T-3*c/T**2+3*c**2/T**3))==0
q=sp.symbols('q',positive=True)
Sig=sp.Matrix([[2*q*T+sp.Rational(2,3)*T**3,T**2],[T**2,2*T]])
assert sp.simplify(Sig.det()-4*q*T*T-T**4/3)==0
G=(sp.Matrix([[c,1]])*Sig.inv()*sp.Matrix([c,1]))[0]/2
# finite-age covariance inverse equivalent to standard Gaussian conditional form
assert sp.simplify(G-(2*T*c*c-2*T*T*c+(2*q*T+sp.Rational(2,3)*T**3))/(2*(4*q*T*T+T**4/3)))==0

# Direct Laplace quadrature of the exact stationary density, no use of rate function in integrand.
def likelihood(L,delta,t):
 if t<=0: return 0.
 det=4*delta*t*t+t**4/3
 x=float(c0)*L*L; y=L
 numer=2*t*x*x-2*t*t*x*y+(2*delta*t+2*t**3/3)*y*y
 ex=t+numer/(2*det)
 return math.exp(-ex+L*math.sqrt(3))/(2*math.pi*math.sqrt(det)) if ex-L*math.sqrt(3)<700 else 0.

cut=(1-math.sqrt(1-12*float(c0)))/2
for delta in (0.,1.,4.):
 for L in (100.,500.,2000.,5000.):
  low=quad(lambda z: L*likelihood(L,delta,L*z),.00001,cut,points=[float(u)],epsabs=1e-60,epsrel=1e-9,limit=500)[0]
  high=quad(lambda z: L*likelihood(L,delta,L*z),cut,3.,points=[float(v)],epsabs=1e-60,epsrel=1e-9,limit=500)[0]
  prob=low/(low+high)
  target=float(wyoung/(wyoung+wold))
  assert abs(prob-target)<(.35 if L<500 else .1 if L<2000 else .04),(delta,L,prob,target)
  rate=math.sqrt(3)-math.log(low+high)/L
  assert abs(rate-math.sqrt(3))<.16,(delta,L,rate)
  print('delta',delta,'L',L,'young weight',round(prob,8),'rate',round(rate,8))

# The exact finite-L covariance contains delta at order only L^-2 in rescaled Gaussian exponent.
print('EXACT_ALL_TESTS_PASSED')
