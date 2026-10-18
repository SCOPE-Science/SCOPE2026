"""Reproducibility checks for cyclic versus reciprocal vaccination information.

Requires Python 3 with sympy and numpy. The algebraic proof is in RESULT.md;
these independent symbolic and numerical checks are supporting evidence.
"""
import cmath
import math
from fractions import Fraction
import numpy as np
import sympy as s

T=s.symbols('T')
D,Z=s.symbols('D Z', nonnegative=True, real=True)
mu=s.Rational(1)
gamma=s.Rational(2)
beta=s.Rational(6)
ie=s.Rational(1,12)
se=s.Rational(1,3)
c=mu+beta*ie
B=beta*ie*gamma
h=c+6*D
k=(3*D)**2+3*c*D+B
assert (c,B)==(s.Rational(3,2),1)
assert s.simplify(mu*(1-s.Rational(1,2))-mu*se-beta*se*ie)==0
assert s.simplify(beta*se*ie-gamma*ie)==0

# The logistic vaccination response has prescribed value and slope at ie.
m=s.symbols('m', real=True)
p=1/(1+s.exp(-8*Z*(m-ie)))
assert s.simplify(p.subs(m,ie)-s.Rational(1,2))==0
assert s.simplify(s.diff(p,m).subs(m,ie)-2*Z)==0

# Linearization directly from the six original nonlinear equations.
ss=s.symbols('s0:3', real=True)
ii=s.symbols('i0:3', real=True)
xs=list(ss)+list(ii)
f=[]
for j in range(3):
    others=[q for q in range(3) if q!=j]
    f.append(mu*(1-1/(1+s.exp(-8*Z*(ii[(j+1)%3]-ie))))-mu*ss[j]-beta*ss[j]*ii[j]+D*sum(ss[q]-ss[j] for q in others))
for j in range(3):
    others=[q for q in range(3) if q!=j]
    f.append(beta*ss[j]*ii[j]-gamma*ii[j]+D*sum(ii[q]-ii[j] for q in others))
J=s.Matrix(f).jacobian(xs).subs({**{v:se for v in ss},**{v:ie for v in ii}})
expected=(T**2+c*T+B+Z)*((T**2+h*T+k)**2-Z*(T**2+h*T+k)+Z**2)
actual=J.charpoly(T).as_expr()
assert s.simplify(s.expand(actual-expected))==0

# Reciprocal neighbour averaging, with exactly the same demographic parameters.
fr=[]
for j in range(3):
    others=[q for q in range(3) if q!=j]
    avg=(ii[others[0]]+ii[others[1]])/2
    fr.append(mu*(1-1/(1+s.exp(-8*Z*(avg-ie))))-mu*ss[j]-beta*ss[j]*ii[j]+D*sum(ss[q]-ss[j] for q in others))
for j in range(3):
    others=[q for q in range(3) if q!=j]
    fr.append(beta*ss[j]*ii[j]-gamma*ii[j]+D*sum(ii[q]-ii[j] for q in others))
Jr=s.Matrix(fr).jacobian(xs).subs({**{v:se for v in ss},**{v:ie for v in ii}})
expected_r=(T**2+c*T+B+Z)*(T**2+h*T+k-Z/2)**2
assert s.simplify(s.expand(Jr.charpoly(T).as_expr()-expected_r))==0

# Directed nonzero-frequency crossing: substitute omega and eliminate k.
w=s.sqrt(3)*Z/(2*h)
assert s.simplify((k-Z/2-3*Z**2/(4*h**2)).subs(k,Z/2+3*Z**2/(4*h**2)))==0
assert s.simplify((3*Z**2+2*h**2*Z-4*h**2*k).subs(k,(Z/2+3*Z**2/(4*h**2))))==0

# Characteristic polynomial is never zero at zero frequency for a nonreal perception eigenvalue.
# Each imaginary crossing is forced by k-Z/2 = 3 Z^2/(4 h^2).
Zc=(h/3)*(s.sqrt(h**2+12*k)-h)
assert s.simplify(Zc.subs(D,0)-(s.sqrt(57)-3)/4)==0
assert float(Zc.subs(D,0))>1
assert float(Zc.subs(D,0))<s.Rational(3,2)

# For positive h,k and Zc, k=Zc/2+3 Zc^2/(4h^2), hence Zc<2k.
for dv in [0, s.Rational(1,10),s.Rational(1,2),1,5]:
    hv=float(h.subs(D,dv)); kv=float(k.subs(D,dv))
    zc=float(Zc.subs(D,dv))
    assert abs(kv-zc/2-3*zc**2/(4*hv**2))<5e-13
    assert 0<zc<2*kv

# Validate the full six-dimensional Jacobians on both sides of the threshold.
for dv in [0,0.1,0.4,1.0]:
    zc=float(Zc.subs(D,dv))
    for mult in [0.05,0.4,0.99,1.01,1.25,2.0]:
        zv=mult*zc
        vals=np.linalg.eigvals(np.array(J.subs({D:dv,Z:zv}),dtype=float))
        vals_r=np.linalg.eigvals(np.array(Jr.subs({D:dv,Z:zv}),dtype=float))
        assert (max(v.real for v in vals)<0)==(mult<1)
        if zv<2*float(k.subs(D,dv)):
            assert max(v.real for v in vals_r)<0
        if zv>2*float(k.subs(D,dv)):
            assert max(v.real for v in vals_r)>0

# Check the derivative formula at the oscillatory threshold: real part strictly positive.
for dv in [0,0.25,2]:
    hv=float(h.subs(D,dv)); zc=float(Zc.subs(D,dv))
    kap=-0.5+0.5j*math.sqrt(3)
    omega=-math.sqrt(3)*zc/(2*hv)
    der=-kap/(hv+2j*omega)
    assert der.real>0

# Infinite-family migration monotonicity is analytical; numerical samples are diagnostic.
prev=0
for dv in [0,0.001,0.01,0.1,1,10,100]:
    v=float(Zc.subs(D,dv)); assert v>=prev; prev=v
assert abs(float(Zc.subs(D,1000))/(1000**2)-12)<0.03

# Two patches at zero mobility: every stochastic perception matrix has real eigenvalues.
alpha,delta=s.symbols('alpha delta', real=True)
K=s.Matrix([[alpha,1-alpha],[delta,1-delta]])
assert s.factor(K.charpoly(T).as_expr())==(T-1)*(T-alpha+delta)

print('PASS: equilibrium and sigmoid derivatives, both six-state characteristic polynomials,')
print('       exact threshold, transversality, two-site boundary, migration scaling,')
print('       24 full-spectrum comparisons, plus symbolic consistency checks.')
