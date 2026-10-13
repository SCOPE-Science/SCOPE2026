#!/usr/bin/env python3
import sympy as sp

I = sp.symbols("I", nonnegative=True)
h = I*(1-3*I/(1+I)**2)
hp = sp.factor(sp.diff(h,I))

assert sp.simplify(hp - (1-6*I/(1+I)**3)) == 0
# 6I/(1+I)^3 <= 8/9 is equivalent to
# 8(1+I)^3 - 54I >= 0 = 2(2I-1)^2(I+4).
gap = sp.factor(8*(1+I)**3 - 54*I)
assert gap == 2*(2*I-1)**2*(I+4)
assert sp.factor(I-h) == 3*I**2/(I+1)**2
assert sp.diff(h,I).subs(I,0) == 1

Lam=sp.Rational(96)
pi=sp.Rational(1,2)
mu=sp.Rational(1)
delta=sp.Rational(2)
beta=sp.Rational(1,10)

S0=(1-pi)*Lam/mu
V0=pi*Lam/mu
R0=sp.simplify((beta*S0+beta*V0)/(mu+delta))
assert R0 == sp.Rational(16,5)

S=sp.simplify((1-pi)*Lam/(mu+beta*h))
V=sp.simplify(pi*Lam/(mu+beta*h))
res=sp.factor(beta*S*h+beta*V*h-(mu+delta)*I)
expected=-3*I*(I-2)*(I**2-21*I+11)/(I**3+9*I**2+21*I+10)
assert sp.simplify(res-expected)==0

roots=[(sp.Integer(21)-sp.sqrt(397))/2, sp.Integer(2), (sp.Integer(21)+sp.sqrt(397))/2]
for r in roots:
    assert sp.N(r)>0
    assert sp.simplify(res.subs(I,r))==0
    assert sp.N(r)<21

Ssym,Vsym=sp.symbols("S V")
F1=(1-pi)*Lam-mu*Ssym-beta*Ssym*h
F2=pi*Lam-mu*Vsym-beta*Vsym*h
F3=beta*Ssym*h+beta*Vsym*h-(mu+delta)*I
J=sp.Matrix([F1,F2,F3]).jacobian([Ssym,Vsym,I])
J2=sp.simplify(J.subs({Ssym:45,Vsym:45,I:2}))
expectedJ=sp.Matrix([
    [-sp.Rational(16,15),0,-sp.Rational(5,2)],
    [0,-sp.Rational(16,15),-sp.Rational(5,2)],
    [sp.Rational(1,15),sp.Rational(1,15),2]
])
assert J2==expectedJ

eigs=J2.eigenvals()
expected_eigs=[
    -sp.Rational(16,15),
    (sp.Integer(7)-sp.sqrt(454))/15,
    (sp.Integer(7)+sp.sqrt(454))/15
]
for e in expected_eigs:
    assert e in eigs
assert expected_eigs[-1] > 0

h2=sp.simplify(h.subs(I,2))
hp2=sp.simplify(hp.subs(I,2))
assert h2 == sp.Rational(2,3)
assert hp2 == sp.Rational(5,9)
assert h2/2 < hp2

l33=sp.simplify(-beta*45*hp2-beta*45*hp2+mu+delta)
assert l33 == -2

print("VERIFY_OK")
print("R0",R0)
print("endemic_residual",res)
print("roots",roots)
print("J2",J2)
print("eigenvalues",expected_eigs)
print("l33",l33)
