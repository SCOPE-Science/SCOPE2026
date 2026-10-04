#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction
s,t,x,q=sp.symbols('s t x q')
u1=x**3+(-2*s-22*t+36)*x**2+(s**2+22*s*t+157*t**2-72*s-504*t+396)*x-360*t**3+72*s*t+1692*t**2-2592*t+1296
u2=x**3-(2*s+22*t-36)*x**2-(-s**2-32*s*t-157*t**2+62*s+504*t-396)*x-10*s**2*t-120*s*t**2-360*t**3+25*s**2+432*s*t+1692*t**2-360*s-2592*t+1296

def same(a,b):
    return sp.expand(a-b)==0

def leading3(u):
    ans=0
    for (at,ax),c in sp.Poly(u,t,x).terms():
        if at+ax==3:
            ans += c*t**at*x**ax
    return sp.factor(ans)
expected_lead=(x-5*t)*(x-8*t)*(x-9*t)
assert same(leading3(u1),expected_lead)
assert same(leading3(u2),expected_lead)

G1=sp.groebner([u1,sp.diff(u1,x),sp.diff(u1,t)],x,t,s,order='lex')
G2=sp.groebner([u2,sp.diff(u2,x),sp.diff(u2,t)],x,t,s,order='lex')
elim1=[sp.factor(p.as_expr()) for p in G1.polys if not p.as_expr().has(x,t)]
elim2=[sp.factor(p.as_expr()) for p in G2.polys if not p.as_expr().has(x,t)]
P1=s**2*(s-84)**2*(2*s+1)*(10*s+1)*(20*s+1)
P2=s**2*(s-14)**2*(s+18)*(5*s+2)*(20*s+9)
assert any(sp.simplify(z/P1).is_number and z!=0 for z in elim1)
assert any(sp.simplify(z/P2).is_number and z!=0 for z in elim2)
tri=(x-9*t+18)*(x-8*t+12)*(x-5*t+6)
assert same(u1.subs(s,0),tri)
assert same(u2.subs(s,0),tri)

pts1={sp.Rational(84):(-1,1),sp.Rational(-1,2):(sp.Rational(11,2),27),sp.Rational(-1,10):(sp.Rational(19,10),1),sp.Rational(-1,20):(sp.Rational(31,10),sp.Rational(45,4))}
pts2={sp.Rational(14):(-1,1),sp.Rational(-18):(3,-3),sp.Rational(-2,5):(sp.Rational(13,5),7),sp.Rational(-9,20):(sp.Rational(12,5),sp.Rational(21,4))}
expected1=[sp.Integer(-2225808),sp.Integer(-468),sp.Rational(-1044,25),sp.Rational(369,25)]
expected2=[sp.Integer(-6528),sp.Integer(-1728),sp.Rational(96,25),sp.Rational(-459,100)]
def check_pts(u,pts,expected):
    H=sp.Matrix([[sp.diff(u,x,2),sp.diff(u,x,t)],[sp.diff(u,t,x),sp.diff(u,t,2)]])
    got=[]
    for sv,(tv,xv) in pts.items():
        f=sp.together(u.subs(s,sv))
        gb=sp.groebner([f,sp.diff(f,x),sp.diff(f,t)],x,t,order='lex')
        assert sp.simplify(f.subs({t:tv,x:xv}))==0
        assert sp.simplify(sp.diff(f,x).subs({t:tv,x:xv}))==0
        assert sp.simplify(sp.diff(f,t).subs({t:tv,x:xv}))==0
        assert len(gb.polys)==2
        got.append(sp.factor(H.det().subs({s:sv,t:tv,x:xv})))
    assert got==expected
check_pts(u1,pts1,expected1)
check_pts(u2,pts2,expected2)

# Condition (b): L1 is x=0.
dL1=sp.factor(sp.discriminant(sp.Poly(u1.subs(x,0),t),t))
dL2=sp.factor(sp.discriminant(sp.Poly(u2.subs(x,0),t),t))
assert same(dL1,6718464*(80*s**3-6431*s**2-288*s+36))
assert same(dL2,20736*(5*s-36)**2*(s**2+18*s+9))

# Condition (c), C1: x=t^2.
h11=s*t-t**3+11*t**2-36*t+36
h21=s*t-5*s-t**3+11*t**2-36*t+36
assert same(u1.subs(x,t**2),h11**2)
assert same(u2.subs(x,t**2),h21**2)
assert same(sp.discriminant(sp.Poly(h11,t),t),4*s**3-311*s**2-288*s+144)
assert same(sp.discriminant(sp.Poly(h21,t),t),4*(s**3+s**2+103*s+36))

# Condition (c), C2 under a rational parametrization.
tq=-(q**2+27*q-10)/(q*(q-10))
xq=-36*q/(q-10)
g1=s*q**3-10*q**3-10*s*q**2+80*q**2-170*q+100
g2=s*q**3+60*q**3-20*s*q**2-480*q**2+100*s*q+1020*q-600
den=(q*(q-10))**3
assert sp.simplify(u1.subs({t:tq,x:xq})*den + 36*g1**2)==0
assert sp.simplify(u2.subs({t:tq,x:xq})*den + g2**2)==0
assert same(sp.discriminant(sp.Poly(g1,q),q),4000*(100*s**3-980*s**2+133*s+360))
assert same(sp.discriminant(sp.Poly(g2,q),q),-72000*(1200*s**3+18235*s**2-42924*s-25920))
assert [sp.expand(g1.subs(q,a)) for a in [0,10]]==[100,-3600]
assert [sp.expand(g2.subs(q,a)) for a in [0,10]]==[-600,21600]

# C1∩C2 has t-values 3,2,6,-1; no support overlap in the target disk.
assert all(sp.simplify(a-b)==0 for a,b in zip([h11.subs(t,a) for a in [3,2,6,-1]],[3*s,2*s,6*s,84-s]))
assert all(sp.simplify(a-b)==0 for a,b in zip([h21.subs(t,a) for a in [3,2,6,-1]],[-2*s,-3*s,s,-6*(s-14)]))

r=Fraction(1,20)
def dom(constant, terms):
    return sum(Fraction(abs(c))*r**k for k,c in terms) < Fraction(abs(constant))
assert dom(36,[(3,80),(2,-6431),(1,-288)])
assert dom(9,[(2,1),(1,18)])
assert dom(144,[(3,4),(2,-311),(1,-288)])
assert dom(36,[(3,1),(2,1),(1,103)])
assert dom(360,[(3,100),(2,-980),(1,133)])
assert dom(-25920,[(3,1200),(2,18235),(1,-42924)])

sv=sp.Rational(-1,20); tv=sp.Rational(31,10); xv=sp.Rational(45,4)
assert sp.simplify(u1.subs({s:sv,t:tv,x:xv}))==0
assert sp.simplify(sp.diff(u1,x).subs({s:sv,t:tv,x:xv}))==0
assert sp.simplify(sp.diff(u1,t).subs({s:sv,t:tv,x:xv}))==0
print('VERIFY_OK')
