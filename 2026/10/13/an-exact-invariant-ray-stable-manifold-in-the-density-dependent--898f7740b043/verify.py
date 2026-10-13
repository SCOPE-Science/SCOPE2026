#!/usr/bin/env python3
import sympy as sp

b=sp.Rational(1,5)
d=sp.Rational(1,20)
r=sp.Rational(1,2)
s=sp.Rational(1091,1000)

assert sp.simplify(b*r*(b-1-b*d)+(s-1-b*d)) == 0

kappa=sp.simplify(1-s/(1+b*r))
lperp=sp.simplify(b*(d+r-2*b*r*(1-d))/(1+b*r))
assert kappa == sp.Rational(9,1100)
assert lperp == sp.Rational(18,275)

x,y=sp.symbols("x y", positive=True)
f1=x*(1-x-s*y/(x+y))
f2=b*y*(-d-r*y+x/(x+y))
J=sp.Matrix([f1,f2]).jacobian([x,y])

E1=(sp.Rational(9,1100),sp.Rational(9,110))
assert sp.simplify(f1.subs({x:E1[0],y:E1[1]})) == 0
assert sp.simplify(f2.subs({x:E1[0],y:E1[1]})) == 0

J1=sp.simplify(J.subs({x:E1[0],y:E1[1]}))
assert J1 == sp.Matrix([
    [sp.Rational(248,3025), -sp.Rational(1091,121000)],
    [sp.Rational(20,121), -sp.Rational(299,12100)]
])
eigs1=J1.eigenvals()
assert sp.Rational(-9,1100) in eigs1
assert sp.Rational(18,275) in eigs1

lower=sp.simplify(1/(1-d))
upper=sp.simplify(1/(1-d)+(d-r)**2/(4*r*(1-d)))
assert lower == sp.Rational(20,19)
assert upper == sp.Rational(881,760)
assert lower < s < upper
assert sp.simplify(s*(2-d-r)) == sp.Rational(31639,20000)
assert s*(2-d-r) < 2

q=sp.symbols("q")
poly=sp.expand(r*(1-s)*q**2+(r+d)*q+(d-1))
assert sp.simplify(sp.factor(poly) + (q-10)*(91*q-190)/2000) == 0
roots=sp.solve(poly,q)
assert sp.Rational(10,1) in roots
assert sp.Rational(190,91) in roots

def eq_from_q(qv):
    xv=sp.simplify((1+(1-s)*qv)/(1+qv))
    yv=sp.simplify(qv*xv)
    return xv,yv

assert eq_from_q(sp.Rational(10,1)) == E1
E2=eq_from_q(sp.Rational(190,91))
assert E2 == (sp.Rational(7371,28100),sp.Rational(1539,2810))

J2=sp.simplify(J.subs({x:E2[0],y:E2[1]}))
tr2=sp.factor(sp.trace(J2))
det2=sp.factor(J2.det())
a1_source=sp.factor(-tr2)
assert a1_source == sp.Rational(963171,7896100)
assert a1_source > 0
assert det2 > 0

print("VERIFY_OK")
print("kappa", kappa)
print("lambda_perp", lperp)
print("E1", E1)
print("J1", J1)
print("E1_eigenvalues", sorted([str(v) for v in eigs1]))
print("H4_lower", lower)
print("H4_upper", upper)
print("E2", E2)
print("E2_trace", tr2)
print("E2_det", det2)
print("source_a1_E2", a1_source)
