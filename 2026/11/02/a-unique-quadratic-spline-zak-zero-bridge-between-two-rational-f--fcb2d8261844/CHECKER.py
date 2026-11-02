"""Exact identities underlying the quadratic-spline Zak-zero calculation.

Requires SymPy. The infinite or interval-wide mathematical statements are
proved in RESULT.md; finite tests here check algebra and representative values.
"""
from fractions import Fraction
import sympy as s

b,t,u=s.symbols('b t u',real=True)
a0=s.Rational(3,4)
a1=s.Rational(3,4)-1/b**2
a2=s.Rational(1,2)*(s.Rational(3,2)-2/b)**2
a3=s.Rational(1,2)*(s.Rational(3,2)-3/b)**2
P=s.factor(a0+2*a1*t+2*a2*(2*t**2-1)+2*a3*(4*t**3-3*t))
N=(36*b**2*t**3+18*b**2*t**2-21*b**2*t-6*b**2
   -144*b*t**3-48*b*t**2+108*b*t+24*b
   +144*t**3+32*t**2-116*t-16)/(4*b**2)
assert s.cancel(P-N)==0
assert s.factor(P.subs(t,-1))==-3*(b-2)**2/(4*b**2)
assert s.factor(P.subs(t,s.Rational(-1,2)))==(3*b-8)**2/(8*b**2)
assert s.factor(P.subs(b,2))==(t+1)**2/2
H=s.Poly(s.cancel(P.subs(t,(u-1)/(u+1))*(u+1)**3),u)
expected=[-3*(b-2)**2/(4*b**2),
          3*(b-2)*(31*b-78)/(4*b**2),
          -(165*b**2-660*b+628)/(4*b**2),
          (27*b**2-60*b+44)/(4*b**2)]
for i,v in enumerate(expected):
    assert s.cancel(H.nth(i)-v)==0
D=s.factor(s.discriminant(s.diff(P,t),t))
assert s.factor(D-8*(9*b**2-42*b+47)*(9*b**2-36*b+34)/b**4)==0
bstar=s.Rational(8,3)
pt={b:bstar,t:-s.Rational(1,2)}
assert P.subs(pt)==0
assert s.diff(P,t).subs(pt)==s.Rational(3,32)
assert s.diff(P,b).subs(pt)==0
assert s.diff(P,b,2).subs(pt)==s.Rational(81,256)
assert s.factor(s.diff(P,t,b).subs({b:2,t:-1}))==-s.Rational(3,2)
assert s.diff(P,t,2).subs({b:2,t:-1})==1
assert s.diff(P,b,2).subs({b:2,t:-1})==-s.Rational(3,8)

def spline3(x):
    x=abs(x)
    if x>=s.Rational(3,2):return s.S(0)
    if x<=s.Rational(1,2):return s.Rational(3,4)-x*x
    return (s.Rational(3,2)-x)**2/2
for B in (s.Rational(201,100),s.Rational(9,4),s.Rational(13,5),s.Rational(8,3)):
    for theta in (s.S(0),s.pi/2,2*s.pi/3,s.pi):
        # The factor b^(-1/2) is omitted on both sides.
        direct=sum(spline3(s.Rational(k,1)/B)*s.cos(k*theta) for k in range(-4,5))
        assert s.simplify(direct-P.subs({b:B,t:s.cos(theta)}))==0
    if B<bstar:
        lo,hi=-1.,-.5
        pp=s.lambdify(t,P.subs(b,B),'math')
        assert pp(lo)<0<pp(hi)
        for _ in range(80):
            mid=(lo+hi)/2
            if pp(mid)<0:lo=mid
            else:hi=mid
        print('b=',B,' unique zero cosine bracket=',(lo,hi))
print('PASS: exact Zak identity, root-sign factors, Möbius coefficients, discriminant and endpoint jets')
