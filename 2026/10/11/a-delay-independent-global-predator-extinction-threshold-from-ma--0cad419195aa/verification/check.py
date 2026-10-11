from fractions import Fraction
import sympy as sp

r,d1,c1,b1,b2,b3,d2,d3,c2,c3,k,f,eta = sp.symbols(
    "r d1 c1 b1 b2 b3 d2 d3 c2 c3 k f eta", positive=True
)
P1,P2,P2d,P3 = sp.symbols("P1 P2 P2d P3", nonnegative=True)

g = 1+b1*P1+k*b3*P3+k*b1*b3*P1*P3
assert sp.expand((1+b1*P1)*(1+k*b3*P3) - g) == 0

a = c2/(d2+c2)
pred = b2*P1*P3/g
P2dot = eta*pred-(d2+c2)*P2
P3dot = c2*P2d-d3*P3-c3*P3**2
Ldot = sp.expand(a*P2dot + P3dot + c2*(P2-P2d))
target = a*eta*pred-d3*P3-c3*P3**2
assert sp.simplify(Ldot-target) == 0
assert sp.simplify(-a*(d2+c2)+c2) == 0

Rmat = eta*b2*c2/(d3*(d2+c2)) * (r-d1)/(c1+b1*(r-d1))
local = (d2+c2)*d3 - eta*c2*b2*(r-d1)/(c1+b1*(r-d1))
assert sp.simplify(local-(d2+c2)*d3*(1-Rmat)) == 0

vals = {
    r:sp.Rational(3), d1:sp.Rational(1,10), c1:sp.Rational(1,10),
    b1:sp.Rational(1,2), b2:sp.Rational(3,5), d2:sp.Rational(1,10),
    d3:sp.Rational(1,10), c2:sp.Rational(4,5)
}
coef = sp.simplify((Rmat/eta).subs(vals))
assert coef == sp.Rational(928,93)
sharp_eta = sp.simplify(1/coef)
crude_eta = sp.simplify((d3*b1/b2).subs(vals))
assert sharp_eta == sp.Rational(93,928)
assert crude_eta == sp.Rational(1,12)
assert sharp_eta > crude_eta
assert sp.simplify(sharp_eta-crude_eta) == sp.Rational(47,2784)

print("VERIFY_OK")
print("Rmat_coefficient =", coef)
print("sharp_eta_threshold =", sharp_eta, float(sharp_eta))
print("source_crude_eta_threshold =", crude_eta, float(crude_eta))
print("threshold_gain =", sp.simplify(sharp_eta-crude_eta))
