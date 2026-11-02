"""Exact and independent checks for ambient chord moments of a cylinder sidewall.

Run with Python 3, sympy, numpy, scipy: python verify_cylinder.py
"""
from fractions import Fraction
from math import comb, cos, pi
import random
import sympy as s
from scipy.integrate import quad

x,y=s.symbols('x y', positive=True)  # squared radius and squared height
m=s.symbols('m', positive=True)

def exact_moment(k):
    return s.expand(sum(s.binomial(k,j)*s.binomial(2*j,j)*x**j *
        s.Rational(2,(2*(k-j)+1)*(2*(k-j)+2))*y**(k-j)
        for j in range(k+1)))

mu,nu,omega=(exact_moment(k) for k in (1,2,3))
assert s.expand(mu-(2*x+y/6))==0
assert s.expand(nu-(6*x*x+s.Rational(2,3)*x*y+y*y/15))==0
assert s.expand(omega-(20*x**3+3*x*x*y+s.Rational(2,5)*x*y*y+y**3/28))==0

u=s.symbols('u',real=True)
nu_fixed=s.factor(nu.subs(x,(m-y/6)/2))
omega_fixed=s.factor(omega.subs(x,(m-y/6)/2))
assert s.simplify(nu_fixed-(540*m*m-60*m*y+19*y*y)/360)==0
assert s.factor((nu_fixed/m**2).subs(y,s.Rational(30,19)*m))==s.Rational(26,19)
assert s.factor((nu_fixed/m**2).subs(y,6*m))==s.Rational(12,5)

inversion=(7581*omega+23082*mu**3-28023*mu*nu)/(1672*nu-1628*mu**2)
assert s.factor(inversion-y)==0

z=s.symbols('z')
diffquot=s.factor((omega_fixed-omega_fixed.subs(y,z))/(y-z))
assert s.factor(diffquot.subs(z,s.Rational(60,19)*m-y)-s.Rational(11,945)*(y*y+y*(s.Rational(60,19)*m-y)+(s.Rational(60,19)*m-y)**2))==0

t=s.symbols('t', positive=True)
kappa=s.factor((nu/mu**2).subs(y,t*x))
assert s.factor(kappa-12*(t*t+10*t+90)/(5*(t+12)**2))==0
partner=9*(40-3*t)/(7*t+27)
assert s.factor(kappa-kappa.subs(t,partner))==0
assert s.factor(partner.subs(t,partner)-t)==0
assert s.factor(kappa.subs(t,s.Rational(30,7))-s.Rational(26,19))==0
assert s.factor(kappa.subs(t,s.Rational(40,3))-s.Rational(3,2))==0

# Numeric independent quadrature integrates two random angular coordinates
# (via their difference) and two random heights (via the triangular kernel).
rng=random.Random(8277)
for _ in range(16):
    radius=10**rng.uniform(-1,1)
    height=10**rng.uniform(-1,1)
    for k in (1,2,3):
        theory=float(exact_moment(k).subs({x:radius**2,y:height**2}))
        # E[D^(2k)] = integral over delta theta and absolute height difference.
        def angintegral(dz):
            return quad(lambda ang:(2*radius**2*(1-cos(ang))+dz*dz)**k,
                        0,2*pi,epsabs=1e-8,epsrel=1e-11)[0]/(2*pi)
        numeric=quad(lambda dz:2*(height-dz)/height**2*angintegral(dz),
                     0,height,epsabs=1e-8,epsrel=1e-10)[0]
        assert abs(theory-numeric)/max(theory,1)<1e-9,(radius,height,k,theory,numeric)

# Exact dual-shape ambiguity and strict sixth-moment branch ordering.
for a in (Fraction(1,10),Fraction(1),Fraction(3),Fraction(6),Fraction(12)):
    b=Fraction(9)*(40-3*a)/(7*a+27)
    assert b>0 and b!=a
    r2a=Fraction(1,1)/(2+a/6)
    r2b=Fraction(1,1)/(2+b/6)
    ya=a*r2a; yb=b*r2b
    mea={x:s.Rational(r2a.numerator,r2a.denominator),y:s.Rational(ya.numerator,ya.denominator)}
    meb={x:s.Rational(r2b.numerator,r2b.denominator),y:s.Rational(yb.numerator,yb.denominator)}
    assert s.simplify(mu.subs(mea)-mu.subs(meb))==0
    assert s.simplify(nu.subs(mea)-nu.subs(meb))==0
    diff=s.simplify(omega.subs(mea)-omega.subs(meb))
    assert diff!=0
    assert s.simplify(diff-s.Rational(11,945)*(s.Rational(ya.numerator,ya.denominator)**3-s.Rational(yb.numerator,yb.denominator)**3))==0

print('VERIFY_OK: exact moment/inversion/involution identities, 48 independent quadratures, 5 exact noncongruent moment pairs')
