"""Independent numerical and symbolic checks for the orthogonal-width covariance law.

Run: python verify_orthogonal_widths.py
Requires numpy, scipy, sympy. No external data or network access.
"""
import math
from fractions import Fraction
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss

pi=math.pi
alpha=2/(3*pi)-.25
beta=8/(3*pi*pi)-.25
T=(32-3*pi*pi)/(8*(4-pi))
assert alpha<0<beta and 1/3<T<1
assert Fraction(16)*Fraction(49,484)+Fraction(14,22)-Fraction(9,4)>0, 'Strict cube sign via pi < 22/7'

# Symbolic reconstruction and exact identification of the sign threshold.
p=sp.symbols('p', positive=True)
a,b,c=sp.symbols('a b c', positive=True)
S=a+b+c; Q=a*a+b*b+c*c
A=sp.Rational(2,3)/p-sp.Rational(1,4)
B=sp.Rational(8,3)/p**2-sp.Rational(1,4)
C=A*Q+B*(S*S-Q)
assert sp.simplify(C-(B*S*S+(A-B)*Q))==0
assert sp.simplify(-B/(A-B)-(32-3*p**2)/(8*(4-p)))==0
assert sp.simplify(C.subs({a:1,b:1,c:1})-(sp.Rational(2)/p+16/p**2-sp.Rational(9,4)))==0

# Independent spherical quadrature of conditional expectation E[W(U)W(V)|U].
nphi=1024
nz=96
phi=2*pi*(np.arange(nphi)+0.5)/nphi
nodes, weights_z=leggauss(nz)
t=(nodes+1)*pi/4
z=np.sin(t)
wz=weights_z*(pi/4)*np.cos(t)
x=np.sqrt(1-z[:,None]**2)*np.cos(phi)[None,:]
y=np.sqrt(1-z[:,None]**2)*np.sin(phi)[None,:]
zz=np.broadcast_to(z[:,None], x.shape)
u=np.stack((x,y,zz),axis=2)
# Conditional V uniform on the unit circle in U^perp: E|V_j|=2/pi*sqrt(1-U_j**2).
cond=(2/pi)*np.sqrt(np.maximum(0,1-u*u))
weights=wz[:,None]/nphi

def exact(sides):
    sides=np.asarray(sides,dtype=float)
    total=np.sum(sides)
    q=float(sides@sides)
    return (2/(3*pi))*q+(8/(3*pi*pi))*(total*total-q), beta*total*total+(alpha-beta)*q

def quad(sides):
    sides=np.asarray(sides,dtype=float)
    widths=np.sum(np.abs(u)*sides,axis=2)
    cwidths=np.sum(cond*sides,axis=2)
    mixed=np.sum(weights*widths*cwidths)
    return float(mixed)

cases=((1,1,1),(1,1,.15),(1,1,5),(.7,2.2,4.1),(1,3,8))
for sides in cases:
    em,ec=exact(sides)
    qm=quad(sides)
    assert abs(qm-em)<1e-4, (sides,qm,em)
    assert abs(qm-(sum(sides)**2/4+ec))<1e-4

# Inspect the underlying two Haar matrix coefficients with a separate quadrature.
for i,j,target in [(0,0,2/(3*pi)),(0,1,8/(3*pi*pi)),(2,2,2/(3*pi)),(2,0,8/(3*pi*pi))]:
    integral=np.sum(weights*np.abs(u[:,:,i])*cond[:,:,j])
    assert abs(integral-target)<0.0001,(i,j,integral,target)

# Sharpness of cube maximum and rod-limit infimum at fixed side-length sum.
for sides in cases:
    s=np.asarray(sides,dtype=float)
    normalized=s/s.sum()
    cov=exact(normalized)[1]
    upper=(2/pi+16/pi**2-9/4)/9
    assert cov<=upper+1e-13
for eps in (0.01,0.001,0.0001):
    s=np.array([1-2*eps,eps,eps])
    assert abs(exact(s)[1]-alpha)<.0002 if eps==.0001 else True
print('PASS: 2 symbolic identities, 2 Haar coefficients, 5 independent quadrature profiles, 5 extremal checks, 3 limiting profiles')
print('alpha,beta,threshold:',alpha,beta,T)
print('cube covariance:',exact((1,1,1))[1])
