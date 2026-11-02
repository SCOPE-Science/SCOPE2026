"""Exact identities for the octahedral elliptic curve over characteristic zero."""
import sympy as s
from fractions import Fraction

t=s.symbols('t')
I=s.I
A=18*t-4
B=27*t**2*(4*t-1)
F=lambda x:x**3+A*x**2+B*x
T=(s.S(0),s.S(0))
Q=(-3*t,6*I*t*(3*t-1))
assert s.factor(Q[1]**2-F(Q[0]))==0
assert s.factor(F(0))==0
D=s.factor(16*B**2*(A**2-4*B))
assert s.factor(D-186624*t**4*(4*t-1)**2*(1-3*t)**3)==0
C4=s.factor(16*(A**2-3*B))
assert s.simplify(C4-16*(A**2-3*B))==0

def add(P,Z):
    if P is None:return Z
    if Z is None:return P
    x,y=P; z,w=Z
    if s.simplify(x-z)==0:
        if s.simplify(y+w)==0:return None
        m=(3*x*x+2*A*x+B)/(2*y)
    else:m=(w-y)/(z-x)
    m=s.factor(m)
    xx=s.factor(m*m-A-x-z)
    yy=s.factor(m*(x-xx)-y)
    return xx,yy
Q2=add(Q,Q)
Q3=add(Q2,Q)
assert all(s.factor(a-b)==0 for a,b in zip(Q2,(-9*t**2,-9*I*t**2*(3*t-1))))
assert all(s.factor(a-b)==0 for a,b in zip(Q3,(-27*t,54*I*t*(t+1))))
# The fiber at t=0 has node (0,0); Q and 2Q reduce there.
assert [s.simplify(v.subs(t,0)) for v in Q]==[0,0]
assert [s.simplify(v.subs(t,0)) for v in Q2]==[0,0]
# At t=1/3: X(X+1)^2, and Q specializes to its node (-1,0).
r=s.Rational(1,3)
assert s.factor(F(s.symbols('x')).subs(t,r))==s.symbols('x')*(s.symbols('x')+1)**2
assert [v.subs(t,r) for v in Q]==[-1,0]
# At t=1/4: node (0,0); Q specializes to smooth point.
r=s.Rational(1,4)
assert Q[0].subs(t,r)!=0
assert s.simplify(Q[1].subs(t,r)**2-F(Q[0]).subs(t,r))==0
# Infinity minimal coordinates u^2 X,u^3Y, u=1/t. Type III by (v(c4),v(Delta))=(1,3).
u=s.symbols('u')
Ai=s.factor(u**2*A.subs(t,1/u))
Bi=s.factor(u**4*B.subs(t,1/u))
Dinf=s.factor(16*Bi**2*(Ai**2-4*Bi))
C4inf=s.factor(16*(Ai**2-3*Bi))
assert s.simplify(Ai-(18*u-4*u**2))==0
assert s.simplify(Bi-(108*u-27*u**2))==0
assert s.factor(Dinf/u**3).subs(u,0)!=0
assert s.factor(C4inf/u).subs(u,0)!=0
Qinf=[s.factor(u**2*Q[0].subs(t,1/u)),s.factor(u**3*Q[1].subs(t,1/u))]
assert all(v.subs(u,0)==0 for v in Qinf)
height=Fraction(2,1)-Fraction(3,4)-Fraction(2,3)-Fraction(0,1)-Fraction(1,2)
assert height==Fraction(1,12)
print('VERIFY_OK')
print('WEIERSTRASS_DISCRIMINANT',D)
print('TWO_Q',Q2)
print('THREE_Q',Q3)
print('INFINITY',Ai,Bi)
print('HEIGHT',height)

# Uniform symbolic identities in the ground-field parameter r.
r=s.symbols("r", nonzero=True)
Ar=r*(18*t-4*r**2)
Br=27*t**2*(4*t-r**2)
xr=-3*r*t
yr_squared=-36*r*t**2*(3*t-r**2)**2
assert s.factor(yr_squared-(xr**3+Ar*xr**2+Br*xr))==0
assert s.factor(Ar**2-4*Br)==16*(r**2-3*t)**3
assert s.factor(16*Br**2*(Ar**2-4*Br)-186624*t**4*(r**2-4*t)**2*(r**2-3*t)**3)==0
for r0 in [s.Integer(-5),s.Integer(-1),s.Integer(1),s.Integer(4)]:
    a0=Ar.subs(r,r0);b0=Br.subs(r,r0); xx=xr.subs(r,r0)
    y2=yr_squared.subs(r,r0)
    assert s.factor(y2-xx*(xx**2+a0*xx+b0))==0
print('UNIFORM_PARAMETER_VERIFY_OK')
