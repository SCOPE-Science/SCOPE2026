"""Supplementary algebraic and finite numerical checks for three Hermite half-line concentration.

Python 3; requires sympy and scipy for symbolic simplification and numerical quadrature.
The full stationary-point theorem rests on the written sign argument, not on a grid.
"""
from fractions import Fraction
from math import factorial, exp, erf, erfc, pi, sqrt
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

x, E, w = sp.symbols('x E w', real=True)
B = sp.Matrix([[0, 1/sp.sqrt(2), x/sp.sqrt(2)],
               [1/sp.sqrt(2), x, x*x+sp.Rational(1,2)],
               [x/sp.sqrt(2), x*x+sp.Rational(1,2), x**3+x/2]])
P = x*(2*x*x+3)/2
Q = (2*x*x+1)*(2*x**4+5*x*x+6)/4
assert sp.simplify(sp.trace(B)-P) == 0
assert sp.simplify(sp.trace(B*B)-Q) == 0
V = sp.Rational(3,4)*(1-E*E) + w*E*P-w*w*Q
DV = sp.diff(V,x)+2*w*sp.diff(V,E)-2*x*w*sp.diff(V,w)
M = 8*x**6+12*x**4+14*x*x+1
assert sp.simplify(DV-w*(w*x*M-E*(4*x**4+3))/2) == 0
R = x*M/(4*x**4+3)
W = sp.factor(2+2*x*R-sp.diff(R,x))
poly = 64*x**12+144*x**8-32*x**6-36*x**4-120*x*x+15
assert sp.simplify(W-poly/(4*x**4+3)**2) == 0
U = sp.factor(sp.Rational(3,4)*R*R-P*R+Q)
U_explicit = (64*x**14+192*x**12+432*x**10+400*x**8+348*x**6+36*x**4+69*x*x+27)/(2*(4*x**4+3)**2)
assert sp.simplify(U-U_explicit) == 0
assert sp.simplify(sp.diff(U,x)-4*x*U + x*(8*x**6+12*x**4+18*x*x-3)*poly/(4*x**4+3)**3) == 0

# Exact-rational positive margins for the crucial global-max comparison.
t = Fraction(129,100); z=t*t; y=2*z
rf=lambda n: Fraction(1,factorial(n))
I_lower = sum(((-1)**j)*t**(2*j+1)*rf(j)/Fraction(2*j+1) for j in range(12))
exp_z_lower = sum(z**j*rf(j) for j in range(6))
R_t = t*(8*t**6+12*t**4+14*t*t+1)/(4*t**4+3)
assert 2*I_lower*exp_z_lower > R_t
U_t = (64*t**14+192*t**12+432*t**10+400*t**8+348*t**6+36*t**4+69*t*t+27)/(2*(4*t**4+3)**2)
exp_y_upper = sum(y**j*rf(j) for j in range(13)) + Fraction(7,5)*y**13*rf(13)
assert y < 4
assert 2*U_t > 3*exp_y_upper
print('Exact rational lower margins:', float(2*I_lower*exp_z_lower -R_t), float(2*U_t-3*exp_y_upper))

# Independently quadrature-check all nine entries of A(t) for representative thresholds.
def h(j,v):
    f = exp(-v*v/2) * pi**(-.25)
    return (f, sqrt(2)*v*f,(2*v*v-1)/sqrt(2)*f)[j]
def amat(v):
    g=erfc(v)/2; wv=exp(-v*v)/sqrt(pi)
    bv = ((0,1/sqrt(2),v/sqrt(2)),
          (1/sqrt(2),v,v*v+.5),
          (v/sqrt(2),v*v+.5,v**3+v/2))
    return [[(g if i==j else 0)+wv*bv[i][j] for j in range(3)] for i in range(3)]
def d(v):
    ev=erf(v);wv=exp(-v*v)/sqrt(pi)
    return (wv/2)*(wv*v*(8*v**6+12*v**4+14*v*v+1)-ev*(4*v**4+3))
def vv(v):
    ev=erf(v);wv=exp(-v*v)/sqrt(pi)
    pv=v*(2*v*v+3)/2
    qv=(2*v*v+1)*(2*v**4+5*v*v+6)/4
    return .75*(1-ev*ev)+wv*ev*pv-wv*wv*qv
for t0 in [-2.5,-1.0,-.3,0,.6,1.3,2.5]:
    mat=amat(t0)
    for i in range(3):
        for j in range(3):
            integral,err=quad(lambda v:h(i,v)*h(j,v),t0,12,epsabs=2e-13,epsrel=2e-13)
            assert abs(mat[i][j]-integral)<8e-12
    dv=(vv(t0+1e-5)-vv(t0-1e-5))/(2e-5)
    assert abs(dv-d(t0)) < 1e-7
r1=brentq(d,.5,.9,xtol=1e-14)
r2=brentq(d,1.0,1.29,xtol=1e-14)
assert .65<r1<.68 and 1.28<r2<1.29
assert vv(0)>vv(r2)>vv(r1)>0
print('Critical points:',r1,r2)
print('Critical defects:',vv(0),vv(r1),vv(r2))
print('All exact identities and finite quadrature checks passed.')
