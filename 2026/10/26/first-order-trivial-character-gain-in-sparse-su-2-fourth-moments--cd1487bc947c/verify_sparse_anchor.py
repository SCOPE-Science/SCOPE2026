#!/usr/bin/env python3
"""Exact fusion-count checks and independent numerical optimizer stress tests.
Scientific scope: SU(2) Haar fourth moments of {0,n,2n}, not a proof by enumeration.
"""
from collections import defaultdict
from math import sqrt, sin, cos, pi
from scipy.optimize import minimize_scalar, minimize
import sympy as sp

# Independent exact coefficient array by SU(2) character fusion.
def fusion_formula(n):
    a,b,c=sp.symbols('a b c')
    xs={0:a,n:b,2*n:c}
    prod=defaultdict(lambda:sp.Integer(0))
    for i,ai in xs.items():
        for j,aj in xs.items():
            for k in range(abs(i-j),i+j+1,2):prod[k]+=ai*aj
    return sp.Poly(sp.expand(sum(x*x for x in prod.values())),a,b,c)

def asserted_formula(n):
    a,b,c=sp.symbols('a b c')
    base=a**4+6*a*a*(b*b+c*c)+12*a*b*b*c+4*a*c**3
    base+=(n+1)*b**4+6*(n+1)*b*b*c*c+(2*n+1)*c**4
    if n%2==0:
        base+=4*a*b**3+12*a*b*c*c+(2*n+4)*b**3*c+4*(n+1)*b*c**3
    return sp.Poly(sp.expand(base),a,b,c)

for n in range(1,61):
    assert fusion_formula(n)==asserted_formula(n),n

T=sp.sqrt(3)-1
FE=sp.simplify((T**4+2*T**3+6*T**2+4*T+2)/(1+T*T)**2)
RE2=sp.simplify((1+T)**6/(1+T*T)**3)
assert sp.simplify(FE-(30+12*sp.sqrt(3))/13)==0
assert sp.simplify(2*RE2/FE-(333+180*sp.sqrt(3))/169)==0
assert sp.simplify((2*sp.Rational(1,3) + sp.Rational(1,3)) - 1)==0
assert sp.simplify(2*(sp.Rational(50,27))/(sp.Rational(7,3)) -sp.Rational(100,63))==0

# Exact scalar expression for the positive-modulus norm.
def fgR(n,theta):
    x=sin(theta); y=cos(theta)
    if n%2:
        f=x**4+6*x*x*y*y+2*y**4
        g=x**4+6*x*x*y*y+y**4
        R=y*(3*x*x+y*y)
    else:
        f=x**4+2*x**3*y+6*x*x*y*y+4*x*y**3+2*y**4
        g=(x+y)**4
        R=(x+y)**3
    return f,g,R

def Mvalue(n,r,theta):
    f,g,R=fgR(n,theta)
    q2=1-r*r
    return r**4+6*r*r*q2+4*r*q2**1.5*R+q2*q2*(n*f+g)

def Bvalue(n,theta):
    f,g,R=fgR(n,theta)
    return n*f+g

answers=[]
for n in [9,10,19,20,49,50,99,100,199,200,399,400,799,800]:
    B = minimize_scalar(lambda th:-Bvalue(n,th),bounds=(0,pi/2),method='bounded',options={'xatol':1e-13})
    M = minimize(lambda v: -Mvalue(n,*v), x0=[1/n, B.x], bounds=[(0,0.5),(0,pi/2)],method='L-BFGS-B',options={'ftol':1e-15,'gtol':1e-13, 'maxiter':5000})
    # Nelder Mead refinement avoids rounding gradient steps for large n
    MM=minimize(lambda v: -Mvalue(n,*v),x0=M.x,method='Nelder-Mead', options={'xatol':1e-13, 'fatol':1e-14, 'maxiter':10000})
    r,th=MM.x
    assert 0<r<.5 and 0<th<pi/2
    gain=Mvalue(n,r,th)-Bvalue(n,B.x)
    target = 100/63 if n%2 else float((333+180*sp.sqrt(3))/169)
    expected_r = 5*sqrt(6)/21 if n%2 else sqrt(float(RE2))/float(FE)
    answers.append((n,round(n*gain,6),round(target,6),round(n*r,6),round(expected_r,6)))
    assert abs(n*gain-target)<3.0/n, (n,gain,target)
print('EXACT_FUSION_POLYNOMIALS: 60 degrees passed')
print('EXACT_ALGEBRAIC_LIMITS: passed')
for row in answers:print('n, n*gain, predicted_gain, n*anchor_modulus, predicted_anchor:',*row)
print('NUMERICAL_STRESS: 14 cases passed; analytic proof required for all-n asymptotics')

# Independent Weyl integration checks (including genuinely complex coefficients).
# This uses the SU(2) class-angle Haar density, not the coefficient polynomial.
from scipy.integrate import quad
from math import pi

def fusion_fourth_complex(n, aa, bb, cc):
    products = defaultdict(complex)
    xs = {0:aa,n:bb,2*n:cc}
    for i,vi in xs.items():
        for j,vj in xs.items():
            for k in range(abs(i-j),i+j+1,2):
                products[k] += vi*vj
    return sum(abs(v)**2 for v in products.values())

def angle_fourth(n, aa, bb, cc):
    def f(theta):
        sn=sin(theta)
        if abs(sn)<1e-12:return 0.0
        poly=aa+bb*sin((n+1)*theta)/sn+cc*sin((2*n+1)*theta)/sn
        return (2/pi)*sn*sn*(abs(poly)**4)
    return quad(f,0,pi,epsabs=1e-10,epsrel=1e-10,limit=250)[0]
for n in [1,2,3,4,5,7]:
    for aa,bb,cc in [(.7+0.3j,.2-0.5j,.9+0.1j), (1j,1-1j,.4j)]:
        exact=fusion_fourth_complex(n,aa,bb,cc)
        observed=angle_fourth(n,aa,bb,cc)
        assert abs(exact-observed)<=5e-9*max(1,exact),(n,exact,observed)
print('WEYL_HAAR_QUADRATURE: 12 complex-coefficient cases passed')
