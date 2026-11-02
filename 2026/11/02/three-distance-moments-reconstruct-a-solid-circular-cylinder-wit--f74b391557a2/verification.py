"""Reproducibility checks for moment identifiability of solid circular cylinders."""
from fractions import Fraction as F
import math
import numpy as np
import sympy as sp

s,v=sp.symbols('s v',positive=True)
u=s-v
m2=sp.expand(sp.Rational(5,3)*u*u+2*u*v+sp.Rational(12,5)*v*v)
m3=sp.expand(sp.Rational(7,2)*u**3+5*u*u*v+sp.Rational(36,5)*u*v*v+sp.Rational(54,7)*v**3)
assert sp.simplify(m2 - (sp.Rational(5,3)*s**2-sp.Rational(4,3)*s*v+sp.Rational(31,15)*v**2))==0
assert sp.simplify(m3 - (sp.Rational(7,2)*s**3-sp.Rational(11,2)*s*s*v+sp.Rational(77,10)*s*v*v+sp.Rational(141,70)*v**3))==0
q=4371*m2-5912*s*s
rhs=sp.Rational(3,13454)*(s*(19529*m2-16852*s*s)+v*q)
assert sp.factor(m3-rhs)==0, sp.factor(m3-rhs)
assert sp.factor(q.subs(v,sp.Rational(10,31)*s))==sp.Rational(433,1)*s*s, sp.factor(q.subs(v,sp.Rational(10,31)*s))
reconstructed_v=sp.factor((sp.Rational(13454,3)*m3-s*(19529*m2-16852*s*s))/q)
assert sp.simplify(reconstructed_v-v)==0
print('EXACT_FORWARD_MOMENTS_AND_GLOBAL_INVERSE_PASSED')

v1=F(8,31); v2=F(12,31); ss=F(1)
def moments(v):
    u=ss-v
    m2=F(5,3)*u*u+2*u*v+F(12,5)*v*v
    m3=F(7,2)*u**3+5*u*u*v+F(36,5)*u*v*v+F(54,7)*v**3
    return ss,m2,m3
assert moments(v1)[:2]==moments(v2)[:2]
assert moments(v1)[2]!=moments(v2)[2]
assert moments(v1)[1]==F(679,465), moments(v1)
assert moments(v1)[2]==F(5480483,2085370), moments(v1)
assert moments(v2)[2]==F(5508719,2085370), moments(v2)
print('SHARP_TWO_MOMENT_AMBIGUITY_PASSED')

# Independent numerical check by sampling cylinders, not by sampling the derived differences.
rng=np.random.default_rng(20261026)
for radius,height in [(1.,2.),(.63,3.7),(1.4,.35)]:
    n=350000
    angle1=rng.uniform(0.,2*math.pi,n)
    angle2=rng.uniform(0.,2*math.pi,n)
    rr1=radius*np.sqrt(rng.uniform(size=n))
    rr2=radius*np.sqrt(rng.uniform(size=n))
    z1=rng.uniform(0.,height,n)
    z2=rng.uniform(0.,height,n)
    dist2=(rr1*np.cos(angle1)-rr2*np.cos(angle2))**2+(rr1*np.sin(angle1)-rr2*np.sin(angle2))**2+(z1-z2)**2
    ui=radius**2
    vi=height**2/6.
    expected=np.array([ui+vi,5*ui**2/3+2*ui*vi+12*vi**2/5,7*ui**3/2+5*ui**2*vi+36*ui*vi**2/5+54*vi**3/7])
    draws=np.array([np.mean(dist2**k) for k in (1,2,3)])
    rel=np.abs(draws-expected)/expected
    print(f'NUMERICAL radius={radius} height={height} rel_errors={rel}')
    assert max(rel) < .025
print('DIRECT_INDEPENDENT_CYLINDER_SIMULATION_PASSED')
print('ALL_CHECKS_PASSED')
