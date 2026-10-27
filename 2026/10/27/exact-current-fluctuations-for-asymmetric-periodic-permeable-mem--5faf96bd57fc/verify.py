#!/usr/bin/env python3
"""Reproducible checks for the exact periodic membrane current law."""
import math
import sympy as sp
D,L,a,b=sp.symbols('D L a b',positive=True)
S=a+b; Delta=a-b; H=2*D+L*S
F1=L+S*L**2/(2*D)
F2=L**3/(3*D)+S*L**4/(12*D**2)
vcount=2*D*Delta/(L*H)
second=sp.factor((S-F2*vcount**2)/F1)
computed=sp.factor(L**2*second/2)
claimed=D*L*S/H - D*L**2*(4*D+L*S)*Delta**2/(3*H**3)
assert sp.simplify(computed-claimed)==0
printed=D*L*(24*D**2*S+2*D*L*(7*a*a+34*a*b+7*b*b)+L**2*S*(5*a*a+14*a*b+5*b*b))/(6*H**3)
diff=D*L**2*(2*D-L*S)*Delta**2/(6*H**3)
assert sp.simplify(computed-printed-diff)==0
assert computed.subs({D:1,L:1,a:1,b:0})==sp.Rational(22,81)
assert printed.subs({D:1,L:1,a:1,b:0})==sp.Rational(43,162)
s=sp.symbols('s')
lap=1/(sp.cosh(sp.sqrt(s))+sp.sqrt(s)*sp.sinh(sp.sqrt(s)))
series=sp.series(lap,s,0,3).removeO()
assert sp.simplify(series-(1-sp.Rational(3,2)*s+sp.Rational(49,24)*s*s))==0
mean=sp.Rational(3,2)
var=2*sp.Rational(49,24)-mean**2
assert var==sp.Rational(11,6)
assert var/(2*mean**3)==sp.Rational(22,81)
print('PASS: exact cumulant derivatives and published-expression comparison')
print('PASS: independent one-way renewal certificate')
# Finite-lattice approximation with correct crossing weights and an explicit
# finite-dimensional eigenvalue reference. Supplementary numerical check only.
import numpy as np
from scipy.optimize import brentq
from scipy.linalg import eigvals
ad,bd,dd,ell,theta=2.0,1.0,1.0,1.0,0.03
rhs=ad*math.exp(theta)+bd*math.exp(-theta)
def F(lam):
    if abs(lam)<1e-15: return ad+bd
    if lam>0:
        k=math.sqrt(lam/dd)
        return (ad+bd)*math.cosh(ell*k)+dd*k*math.sinh(ell*k)
    k=math.sqrt(-lam/dd)
    return (ad+bd)*math.cos(ell*k)-dd*k*math.sin(ell*k)
exact=brentq(lambda z:F(z)-rhs,-0.25,0.5,xtol=1e-13)
for n in [30,60,90]:
    step=ell/n
    mat=np.zeros((n,n),dtype=float)
    rate=dd/step**2
    for i in range(n-1):
        mat[i,i]-=rate;mat[i+1,i]+=rate
        mat[i+1,i+1]-=rate;mat[i,i+1]+=rate
    right=ad/step;left=bd/step
    mat[n-1,n-1]-=right
    mat[0,n-1]+=right*math.exp(theta)
    mat[0,0]-=left
    mat[n-1,0]+=left*math.exp(-theta)
    approx=max(eigvals(mat).real)
    assert abs(approx-exact)<0.02,(n,approx,exact)
print('PASS: finite-lattice leading eigenvalues approach continuum root')
