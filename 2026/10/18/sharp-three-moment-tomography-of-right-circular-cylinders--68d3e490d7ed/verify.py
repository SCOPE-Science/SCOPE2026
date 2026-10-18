#!/usr/bin/env python3
"""Reproduce the algebraic identities and numerical checks for cylinder width moments.
Requires sympy (>=1.10) and mpmath; no external data/network calls.
"""
import math
import random
import sympy as sp
import mpmath as mp

p,x,m=sp.symbols('p x m',real=True)
H=2*m-p*x/2
M1=p*x/4+H/2
M2=sp.expand((2*x*x+2*x*H+H*H)/3)
M3=sp.expand(3*p*x**3/16+3*x*x*H/4+3*p*x*H*H/16+H**3/4)
assert sp.simplify(M1-m)==0
C2=sp.expand(M2).coeff(x,2)
P=sp.factor(-sp.expand(M2).coeff(x,1)/C2)
assert sp.simplify(P-8*m*(p-2)/(p*p-4*p+8))==0
# Difference at the two roots of the quadratic prescribed by M1 and M2.
N=sp.together((M3-M3.subs(x,P-x))/(2*x-P))
N=sp.factor(sp.cancel(N))
c2=sp.factor(sp.expand(N).coeff(x,2))
c1=sp.factor(sp.expand(N).coeff(x,1))
c0=sp.factor(sp.expand(N).coeff(x,0))
# sympy simplification to normalize the rational functions.
assert sp.simplify(c2-p*(p*p-12)/64)==0
assert sp.simplify(c1+m*p*(p-2)*(p*p-12)/(8*(p*p-4*p+8)))==0
assert sp.simplify(c0-m*m*(p**5+8*p**4-80*p**3+96*p*p+384*p-768)/(4*(p*p-4*p+8)**2))==0
Q=p**4-6*p**3+4*p*p+36*p-64
Disc=sp.factor(c1*c1-4*c0*c2)
assert sp.simplify(Disc+3*m*m*p*(p*p-12)*Q/(16*(p*p-4*p+8)**2))==0
assert Q.subs(p,sp.Rational(22,7))==sp.Rational(-104,2401)
# Q''(p)=12p(p-3)+8 positive for p>=3; Q'(3)=6 positive.
assert sp.diff(Q,p).subs(p,3)==6
assert sp.factor(sp.diff(Q,p,2)- (12*p*(p-3)+8))==0
assert sp.Rational(22,7)**2 < 12
# Hence Q(pi)<0, pi^2<12, Disc<0, c2<0: N strictly negative for any x,m>0.

# Raw moments checked independently by 1D numerical integration.
mp.mp.dps=50
rng=random.Random(271828)
for _ in range(25):
    D=mp.mpf(str(math.exp(rng.uniform(-2,2))))
    h=mp.mpf(str(math.exp(rng.uniform(-2,2))))
    f=lambda t: D*mp.sqrt(1-t*t)+h*t
    analytic=[(mp.pi/4)*D+h/2,
              (2*D*D+2*D*h+h*h)/3,
              3*mp.pi*D**3/16+3*D*D*h/4+3*mp.pi*D*h*h/16+h**3/4]
    for k in [1,2,3]:
        numerical=mp.quad(lambda t:f(t)**k,[0,0.5,1])
        assert abs(numerical-analytic[k-1]) < mp.mpf('1e-39')*max(1,abs(analytic[k-1]))

# Explicit positive distinct cylinders with coincident first two moments.
def vals(D,h):
    return (math.pi*D/4+h/2, (2*D*D+2*D*h+h*h)/3,
            3*math.pi*D**3/16+3*D*D*h/4+3*math.pi*D*h*h/16+h**3/4)
D1,H1=1.0,0.5
mu1,mu2,mu3=vals(D1,H1)
Pnum=8*mu1*(math.pi-2)/(math.pi**2-4*math.pi+8)
D2=Pnum-D1
H2=2*mu1-math.pi*D2/2
assert D2>0 and H2>0 and abs(D1-D2)>0.1
mu1b,mu2b,mu3b=vals(D2,H2)
assert abs(mu1-mu1b)<1e-13 and abs(mu2-mu2b)<1e-13
assert abs(mu3-mu3b)>1e-4
print('PASS: symbolic exact identities, Archimedean bound, 25*3 quadratures, two-moment collision')
print(f'collision 1: diameter={D1:.12g}, height={H1:.12g}, moments={vals(D1,H1)}')
print(f'collision 2: diameter={D2:.12g}, height={H2:.12g}, moments={vals(D2,H2)}')
