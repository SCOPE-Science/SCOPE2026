#!/usr/bin/env python3
import sympy as sp

B=eta=mu=M=alpha=sp.Integer(1)
gamma=sp.Integer(10)
S,I,R=sp.symbols("S I R")
f1=B-eta*S-M*I*S*(1+gamma*I)+alpha*R
f2=M*I*S*(1+gamma*I)-(mu+eta)*I
f3=mu*I-(alpha+eta)*R

Rhat=M*B/(mu*(B+mu))
Rinv=M*B/(eta*(mu+eta))
assert Rhat == sp.Rational(1,2)
assert Rinv == sp.Rational(1,2)

K=B/eta
a=(mu+eta)/M
c=1+mu/(alpha+eta)
gamma_sn=sp.simplify(c*(sp.sqrt(a)+sp.sqrt(a-K))**2/K**2)
assert sp.simplify(gamma_sn-(sp.Rational(9,2)+3*sp.sqrt(2))) == 0
assert gamma > gamma_sn

Q=sp.expand(c*gamma*I**2+(c-K*gamma)*I+(a-K))
assert sp.factor(2*Q) == (6*I-1)*(5*I-2)

points=[
    (sp.Integer(1),sp.Integer(0),sp.Integer(0)),
    (sp.Rational(3,4),sp.Rational(1,6),sp.Rational(1,12)),
    (sp.Rational(2,5),sp.Rational(2,5),sp.Rational(1,5)),
]
for p in points:
    residual=[sp.simplify(expr.subs({S:p[0],I:p[1],R:p[2]})) for expr in (f1,f2,f3)]
    assert residual == [0,0,0]

J=sp.Matrix([f1,f2,f3]).jacobian([S,I,R])
lam=sp.symbols("lambda")
polys=[]
for p in points:
    Jp=J.subs({S:p[0],I:p[1],R:p[2]})
    polys.append(sp.factor(Jp.charpoly(lam).as_expr()))

assert sp.factor(polys[0]-(lam+1)**2*(lam+2)) == 0
assert sp.factor(polys[1]-(lam+1)*(36*lam**2+43*lam-42)/36) == 0
assert sp.factor(polys[2]-(lam+1)*(5*lam**2+12*lam+14)/5) == 0

for p, expected in [(points[0],"stable"),(points[1],"saddle"),(points[2],"stable")]:
    vals=[complex(v.evalf()) for v in J.subs({S:p[0],I:p[1],R:p[2]}).eigenvals().keys()]
    if expected=="stable":
        assert all(z.real < 0 for z in vals)
    else:
        assert any(z.real > 0 for z in vals)

print("VERIFY_OK")
print("Rhat", Rhat)
print("Rinv", Rinv)
print("gamma_SN", sp.N(gamma_sn,20))
print("Q_factor", sp.factor(2*Q))
for label,p,poly in zip(["E0","Eminus","Eplus"],points,polys):
    print(label,p,sp.factor(poly))
