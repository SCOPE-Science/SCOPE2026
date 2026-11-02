"""Exact and independent numerical checks of spherical-zone chord moment identities.

Usage: python check.py
Dependencies: Python 3, sympy, numpy.
"""
import math
import numpy as np
import sympy as sp

m,q=sp.symbols('m q', real=True)
u=m*(3*q-2*m**2)
f2=sp.Rational(1,2)-q+sp.Rational(3,2)*q**2
f3=sp.expand(u**2+sp.Rational(3,2)*(m-u)**2)
assert sp.simplify(f3-(m**2/sp.Integer(2))*(20*m**4-60*m**2*q+12*m**2+45*q**2-18*q+3))==0
assert sp.factor(f2-f2.subs(q,sp.Rational(2,3)-q))==0
assert sp.factor(f3-f3.subs(q,sp.Rational(2,3)-q))==-4*m**2*(5*m**2-1)*(3*q-1)
assert sp.factor(m**2+(1-m)**2/sp.Integer(3)-sp.Rational(1,3))==2*m*(2*m-1)/3
print('SYMBOLIC_MOMENT_AND_FOLD_IDENTITIES_PASSED')

x=sp.Rational(11,20)
h2s=[sp.Rational(17,400),sp.Rational(57,400)]
results=[]
for h2 in h2s:
  qq=x*x+h2/3
  v1=x*x
  v2=f2.subs(q,qq)
  v3=f3.subs({m:x,q:qq})
  results.append((v1,v2,v3))
  assert x+sp.sqrt(h2)<1
assert results[0][:2]==results[1][:2]
assert results[0][2]!=results[1][2]
assert results[0][:2]==(sp.Rational(121,400),sp.Rational(267,800))
assert results[0][2]-results[1][2]==sp.Rational(4961,160000)
print('EXPLICIT_NONISOMETRIC_TWO_MOMENT_COLLISION_PASSED')

from numpy.polynomial.legendre import leggauss
z_nodes,z_weights=leggauss(26)
phi=2*math.pi*np.arange(64)/64
cosphi=np.cos(phi)

def independent_direct_integration(mm,hh):
    z=mm+hh*z_nodes
    v=z_weights/2
    zz=z[:,None]*z[None,:]
    transverse=np.sqrt(1-z[:,None]**2)*np.sqrt(1-z[None,:]**2)
    s=zz[:,:,None]+transverse[:,:,None]*cosphi
    weights=v[:,None]*v[None,:]
    return [float(np.sum(weights*np.mean(s**k,axis=2))) for k in (1,2,3)]

for mm,hh in [(0.0,1.0),(0.3,0.2),(0.55,math.sqrt(17)/20),(0.55,math.sqrt(57)/20),(0.7,0.21)]:
    if mm+hh>1+1e-14:continue
    qv=mm*mm+hh*hh/3
    analytical=[mm*mm, float(f2.subs(q,qv)), float(f3.subs({m:mm,q:qv}))]
    numerical=independent_direct_integration(mm,hh)
    assert max(abs(a-b) for a,b in zip(analytical,numerical))<5e-13,(mm,hh,analytical,numerical)
print('INDEPENDENT_THREE_FOLD_SPHERICAL_SURFACE_QUADRATURE_PASSED')

for mm in [0.0,0.14,0.49,0.505,0.55,0.572,0.6,0.75,0.999]:
    lo=mm**2
    hi=mm**2+(1-mm)**2/3
    vals=np.linspace(lo,hi,101)
    for qq in vals:
        dual=2/3-qq
        if abs(qq-dual)<1e-9:continue
        if lo-1e-12<=dual<=hi+1e-12:
            assert 0.5<mm<1/math.sqrt(3)
            d=float(f3.subs({m:mm,q:qq})-f3.subs({m:mm,q:dual}))
            assert abs(d)>1e-10
print('GLOBAL_ADMISSIBILITY_AND_THIRD_MOMENT_SEPARATION_PASSED')
print('ALL_CHECKS_PASSED')
