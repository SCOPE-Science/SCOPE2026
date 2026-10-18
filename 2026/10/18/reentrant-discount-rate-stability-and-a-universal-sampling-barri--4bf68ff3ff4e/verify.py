"""Reproducibility checks for the scalar discounted sampled-feedback theorem.

Python 3.10+ with sympy and mpmath. This checks finite algebra and
representative numerical cases, not the infinite sign argument in the proof.
"""
import math
from fractions import Fraction
import mpmath as mp
import sympy as sp

mp.mp.dps = 65
z = sp.symbols('z', positive=True)
E = sp.exp(z)
A = 1-sp.exp(-z)
B = 1-(z+1)*sp.exp(-z)
C = 2-(z*z+2*z+2)*sp.exp(-z)
Phi = (z*B-2*C)/(2*A)
Psi = (z-4)/(2*z*z)+(z+4)/(2*z*(E-1))
assert sp.simplify(sp.together(Phi/z**2-Psi))==0
K_derivative_numerator = sp.factor(2*z**3*(E-1)**2*sp.diff(Psi,z))
expected = (8-z)*E**2-(16+2*z+4*z**2+z**3)*E+8+3*z
assert sp.simplify(K_derivative_numerator-expected)==0

# Maclaurin coefficients of 2*z^3*(exp(z)-1)^2*Psi'(z), after n! scaling.
values=[10,52,168,432,966,1956,3652,6304,9906,13428,12768]
for n in range(2,16):
    c=2**(n-1)*(16-n)-(n**3+n**2+16)
    if 2<=n<=4: assert c==0
    else: assert c==values[n-5]>0
for n in range(16,1000):
    assert 2**(n-1)*(16-n)-(n**3+n**2+16)<0

# Independent exact integration check on a rational undiscouted stage.
h=sp.Rational(6); r=sp.Rational(1); t=sp.symbols('t')
base=sp.integrate(t,(t,0,h)); denom=sp.integrate(t*t+r,(t,0,h))
assert h*base/denom==sp.Rational(18,13)
assert sp.simplify(1-h*base/denom)==-sp.Rational(5,13)
# Discounted h=6,r=1,rho=1 rational-in-exp closed-loop witness.
w=sp.exp(-6)
multip=sp.factor(1-6*(1-7*w)/(3-51*w))
assert sp.simplify(multip-(-1-3*w)/(1-17*w))==0
assert sp.simplify(multip+1+20*w/(1-17*w))==0

fPhi=lambda zz:(zz-4)/2+zz*(zz+4)/(2*mp.expm1(zz))
fPsi=lambda zz:fPhi(zz)/(zz*zz)
fK=lambda zz:(8-zz)*mp.expm1(zz)**2-4*zz*mp.expm1(zz)-zz**2*(zz+4)*mp.exp(zz)
z0=mp.findroot(fPhi,(mp.mpf('2'),mp.mpf('3')))
zcrit=mp.findroot(fK,(mp.mpf('7'),mp.mpf('8')))
M=fPsi(zcrit)
crit=1/mp.sqrt(M)
assert mp.mpf('2.6879') < z0 < mp.mpf('2.6881')
assert mp.mpf('7.66360') < zcrit < mp.mpf('7.66361')
assert mp.mpf('0.0315473') < M < mp.mpf('0.0315474')
assert mp.mpf('5.63013') < crit < mp.mpf('5.63014')
assert fK(mp.mpf('7.66'))>0 and fK(mp.mpf('7.67'))<0
for zz in (mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('1.0'),mp.mpf('4'),mp.mpf('7.5'),mp.mpf('12'),mp.mpf('200')):
    assert abs(fPsi(zz)-mp.mpf(str(sp.N(Psi.subs(z,sp.Rational(str(zz))),50)))) < mp.mpf('1e-43')

# Example with two separate discount thresholds at fixed h=6,r=1.
lo=mp.findroot(lambda zz:fPsi(zz)-mp.mpf(1)/36,(5,6))
hi=mp.findroot(lambda zz:fPsi(zz)-mp.mpf(1)/36,(10,15))
assert z0<lo<zcrit<hi
assert mp.mpf('0.8927')<lo/6<mp.mpf('0.8928')
assert mp.mpf('2.0005')<hi/6<mp.mpf('2.0007')

def multiplier(h,r,rho):
    if rho==0:
        return 1-h*h/(2*r+mp.mpf(2)*h*h/3)
    zz=rho*h; beta=r*rho*rho
    aa=-mp.expm1(-zz)
    bb=1-(zz+1)*mp.exp(-zz)
    cc=2-(zz*zz+2*zz+2)*mp.exp(-zz)
    return 1-zz*bb/(beta*aa+cc)

# Cross-check gain against direct positive-weight quadrature and objective minimization.
for hh in (mp.mpf('0.2'),mp.mpf('1'),mp.mpf('3'),mp.mpf('6'),mp.mpf('12')):
  for rr in (mp.mpf('0.3'),mp.mpf('1'),mp.mpf('5')):
    for rho in (mp.mpf('0'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('4')):
      c01=mp.quad(lambda tt:mp.exp(-rho*tt)*tt,[0,hh])
      c11=mp.quad(lambda tt:mp.exp(-rho*tt)*(tt*tt+rr),[0,hh])
      m=1-hh*c01/c11
      assert abs(m-multiplier(hh,rr,rho))<mp.mpf('1e-45')
      for trial in (mp.mpf('-0.0001'),mp.mpf('0.0001')):
        u=-c01/c11+trial
        opt=-c01/c11
        cost=lambda v:mp.quad(lambda tt:mp.exp(-rho*tt)*((1+tt*v)**2+rr*v*v),[0,hh])
        assert cost(u)>cost(opt)
      if rho>0:
        stability_pred=rr/(hh*hh)>fPsi(hh*rho)
        assert stability_pred==(abs(m)<1)

assert abs(multiplier(mp.mpf('6'),mp.mpf('1'),mp.mpf('1'))-(-1-3*mp.exp(-6))/(1-17*mp.exp(-6)))<mp.mpf('1e-58')
assert abs(multiplier(mp.mpf('6'),mp.mpf('1'),mp.mpf('1')))>1
assert abs(multiplier(mp.mpf('6'),mp.mpf('1'),mp.mpf('0')))<1
assert abs(multiplier(mp.mpf('6'),mp.mpf('1'),mp.mpf('4')))<1
print('PASS symbolic identities, exact-coefficient sign pattern, and quadrature tests.')
print('positive root of phi=', mp.nstr(z0,25))
print('unique peak location=', mp.nstr(zcrit,25))
print('peak M=',mp.nstr(M,25))
print('critical h/sqrt(r)=',mp.nstr(crit,25))
print('h=6,r=1 discount crossings=',mp.nstr(lo/6,25),mp.nstr(hi/6,25))
print('h=6,r=1,rho=1 multiplier=',mp.nstr(multiplier(6,1,1),25))
