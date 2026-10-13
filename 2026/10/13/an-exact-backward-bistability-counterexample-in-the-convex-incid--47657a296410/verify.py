#!/usr/bin/env python3
import sympy as sp

S,I,R = sp.symbols("S I R")
B,eta,mu,alpha,M,gamma = sp.symbols("B eta mu alpha M gamma", positive=True)
lam = sp.symbols("lam")

f1 = B-eta*S-M*I*S*(1+gamma*I)+alpha*R
f2 = M*I*S*(1+gamma*I)-(mu+eta)*I
f3 = mu*I-(alpha+eta)*R
J = sp.Matrix([f1,f2,f3]).jacobian([S,I,R])

Rinv = sp.simplify(M*B/(eta*(mu+eta)))
infected = sp.simplify(M*B/eta-(mu+eta))
assert sp.simplify(infected-(mu+eta)*(Rinv-1)) == 0

k = sp.simplify(eta*(mu+alpha+eta)/(alpha+eta))
Send = sp.simplify((mu+eta)/(M*(1+gamma*I)))
Rend = sp.simplify(mu*I/(alpha+eta))
res = sp.factor(f1.subs({S:Send,R:Rend})*(1+gamma*I))
quad = sp.expand(-res)
target = sp.expand(k*gamma*I**2+(k-B*gamma)*I+B*(1/Rinv-1))
assert sp.simplify(quad-target) == 0

RR,z = sp.symbols("RR z", positive=True)
boundary = sp.expand((z-1)**2-4*z*(1-RR)/RR)
zplus = sp.simplify((1+sp.sqrt(1-RR))**2/RR)
assert sp.simplify(boundary.subs(z,zplus)) == 0

w = {B:1,eta:1,mu:1,alpha:1,M:1,gamma:10}
assert sp.simplify(Rinv.subs(w)) == sp.Rational(1,2)
qw = sp.expand(target.subs(w))
assert sp.simplify(qw-(15*I**2-sp.Rational(17,2)*I+1)) == 0
roots = sp.solve(qw,I)
assert roots == [sp.Rational(1,6),sp.Rational(2,5)]

eqs = [
    (sp.Integer(1),sp.Integer(0),sp.Integer(0)),
    (sp.Rational(3,4),sp.Rational(1,6),sp.Rational(1,12)),
    (sp.Rational(2,5),sp.Rational(2,5),sp.Rational(1,5)),
]
polys = []
for s,i,r in eqs:
    assert sp.simplify(f1.subs(w).subs({S:s,I:i,R:r})) == 0
    assert sp.simplify(f2.subs(w).subs({S:s,I:i,R:r})) == 0
    assert sp.simplify(f3.subs(w).subs({S:s,I:i,R:r})) == 0
    JJ = J.subs(w).subs({S:s,I:i,R:r})
    polys.append(sp.factor(JJ.charpoly(lam).as_expr()))

assert sp.simplify(polys[0]-(lam+1)**2*(lam+2)) == 0
assert sp.simplify(polys[1]-(lam+1)*(36*lam**2+43*lam-42)/36) == 0
assert sp.simplify(polys[2]-(lam+1)*(5*lam**2+12*lam+14)/5) == 0
assert 12**2-4*5*14 < 0

print("VERIFY_OK")
print("R", sp.Rational(1,2))
print("endemic_roots", roots)
print("char_DFE", polys[0])
print("char_low", polys[1])
print("char_high", polys[2])
