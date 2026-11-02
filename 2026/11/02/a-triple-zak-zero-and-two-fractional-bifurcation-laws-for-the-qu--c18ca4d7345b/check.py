"""Exact identities for the centered quadratic-spline vertical Zak zero theorem.
Requires SymPy. Run: python check.py
"""
import sympy as S
from math import pi, cos, sin, sqrt
b,y,t,d,h=S.symbols('b y t d h',real=True)
a0=(3*b*b-1)/(4*b*b)
a1=9*(b-1)**2/(8*b*b)
a2=(3*b-5)**2/(8*b*b)
a3=(3*b-7)**2/(8*b*b)
H=S.expand(a0+a1*(4*y-3)+a2*(16*y*y-20*y+5)+a3*(64*y**3-112*y**2+56*y-7))
Q=2349*b**4-20844*b**3+67662*b**2-95084*b+48621
assert S.factor(S.discriminant(H,y)-81*(b-3)**4*Q/b**8)==0
assert S.factor(H.subs(y,0)+(39*b*b-198*b+247)/(8*b*b))==0
assert S.factor(H.subs(y,S.Rational(1,4))-3*(b-3)**2/(4*b*b))==0
assert S.factor(H.subs(y,1)-3*(11*b*b-30*b+27)/(8*b*b))==0
bern=S.Rational(793,3)*(1-t)**4+1296*t*(1-t)**3+6*S.Rational(1088,3)*t*t*(1-t)**2+4*S.Rational(1024,3)*t**3*(1-t)+192*t**4
assert S.factor(bern+Q.subs(b,(8+t)/3))==0
beta=(99+2*S.sqrt(42))/39
assert S.simplify((39*beta**2-198*beta+247))==0
K=(33*S.sqrt(42)-28)/76
assert S.simplify(-S.diff(H,b).subs({b:beta,y:0})/S.diff(H,y).subs({b:beta,y:0})-K)==0
assert S.factor(H.subs(b,3)-(4*y-1)**3/18)==0
Nendpoint=S.factor(4*(d-3)**2*H.subs({b:3-d,y:S.Rational(1,4)+h}))
assert S.expand(Nendpoint-(288*d*d*h**3-216*d*d*h**2+18*d*d*h+3*d*d-384*d*h**3+192*d*h**2+128*h**3))==0
# Independent direct finite Zak sum compared with the Chebyshev factor.
for bnum in (2.67,2.8,2.87,2.89,2.99):
    for nu in (0,0.1,0.2,0.3,0.4,0.5,0.6):
        def bs(x):
            q=abs(x)
            return .75-q*q if q <= .5 else (.5*(1.5-q)**2 if q<1.5 else 0)
        import cmath
        zak=sum(bs((.5-k)/bnum)*cmath.exp(2j*pi*k*nu) for k in range(-15,16))/sqrt(bnum)
        yy=cos(pi*nu)**2
        pred=(2/sqrt(bnum))*cmath.exp(1j*pi*nu)*cos(pi*nu)*float(H.subs({b:bnum,y:yy}))
        assert abs(zak-pred)<2e-12,(bnum,nu,zak,pred)
print('EXACT_ZAK_CUBIC_OK; discriminant, Bernstein positivity certificate, signs, critical slope and endpoint cusp; 35 direct-sum comparisons')
