"""Exact finite checks for the one- and two-oasis mutation-selection threshold.
This verifies selected algebraic identities and finite-state residuals; the infinite classification is proved in RESULT.md.
"""
import sympy as s
from math import isfinite

mu=s.Integer(1); p=s.Rational(3,4); q=1-p; delta=s.Rational(2,5)
w=2*s.sqrt(p*q)
t=s.simplify((mu-2*delta+s.sqrt(mu**2+4*delta*(mu-delta)))/2)
a=s.simplify(t/w)
Delta=s.simplify(s.sqrt(mu**2-(a*w)**2))
z=s.simplify((mu-Delta)/(a*w))
r=s.simplify(s.sqrt(p/q)*z)
lo=s.simplify(s.sqrt(q/p)*z)
alpha=s.sqrt(p/q)
assert s.simplify(a-8/(5*s.sqrt(3)))==0
assert s.simplify(r-s.sqrt(3)/2)==0
assert s.simplify(lo-1/(2*s.sqrt(3)))==0
assert s.simplify(alpha-s.sqrt(3))==0

def shape(i):
    return lo**(-i) if i<=0 else alpha*r**(i-1)
def mortality(i):return mu-delta if i in (0,1) else mu
for i in range(-20,21):
    assert s.simplify(a*(p*shape(i-1)+q*shape(i+1))-mortality(i)*shape(i))==0, i
S=s.simplify(1/(1-lo)+alpha/(1-r))
pi0=s.simplify(1/S)
assert float(pi0)>0
m=s.simplify(1-a)
assert float(m)>0
for i in range(-20,21):
    assert s.simplify((1-m)*(p*shape(i-1)+q*shape(i+1))-mortality(i)*shape(i))==0
single_critical=mu*abs(p-q)
adj_critical=s.simplify(mu*(1+abs(p-q)-2*s.sqrt(p*q))/2)
assert adj_critical<delta<single_critical

# Check symbolic formulas and normalizability for a parameter grid.
for px in [s.Rational(1,2),s.Rational(3,5),s.Rational(3,4),s.Rational(9,10)]:
 qx=1-px; v=abs(px-qx); h=2*s.sqrt(px*qx)
 ds=s.simplify((1+v-h)/2)
 assert 0<=ds<v if v>0 else ds==0
 for d in [ds+s.Rational(1,7)*(1-ds), ds+s.Rational(3,5)*(1-ds)]:
  t=s.simplify((1-2*d+s.sqrt(1+4*d*(1-d)))/2)
  av=s.simplify(t/h)
  dv=s.simplify(s.sqrt(1-t*t)); zz=s.simplify((1-dv)/t)
  rp=s.sqrt(px/qx)*zz; rm=s.sqrt(qx/px)*zz
  assert 0<float(rp)<1 and 0<float(rm)<1
  assert abs(float(((1+dv-2*d)/2)**2-(av**2)*px*qx))<1e-12
  assert abs(float(av*(px*rm+qx*s.sqrt(px/qx))-(1-d)))<1e-11
  assert abs(float(av*(px+qx*s.sqrt(px/qx)*rp)-(1-d)*s.sqrt(px/qx)))<1e-11

# Critical asymptotic at nonzero drift: occupation at left oasis is asymptotic to 1-r_+.
import mpmath as mp
mp.mp.dps=60
pmp=mp.mpf(3)/4; qmp=mp.mpf(1)/4; dcrit=(1+abs(pmp-qmp)-2*mp.sqrt(pmp*qmp))/2
for eta in [mp.mpf('0.0001'),mp.mpf('0.00001'),mp.mpf('0.000001')]:
 d=dcrit+eta
 t=(1-2*d+mp.sqrt(1+4*d*(1-d)))/2
 av=t/(2*mp.sqrt(pmp*qmp)); Delta=mp.sqrt(1-t*t); zz=(1-Delta)/t
 rr=mp.sqrt(pmp/qmp)*zz; ll=mp.sqrt(qmp/pmp)*zz; al=mp.sqrt(pmp/qmp)
 pi0=1/(1/(1-ll)+al/(1-rr))
 assert 0<pi0<1
 print('delta-dcrit=',mp.nstr(eta,8),'pi0=',mp.nstr(pi0,12),'r_right=',mp.nstr(rr,12),'a=',mp.nstr(av,12))
print('Exact checks passed; a=',a,'two-site rescue delta=',delta,'single critical=',single_critical,'two-site critical=',adj_critical)
