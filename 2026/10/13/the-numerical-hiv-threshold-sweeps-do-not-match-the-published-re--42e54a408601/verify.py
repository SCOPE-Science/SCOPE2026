#!/usr/bin/env python3
import sympy as sp

Lam=sp.Integer(10000)
d=sp.Rational(1,100)
beta1=sp.Rational(24,10**9)
beta2=sp.Rational(1,10**6)
alpha=sp.Rational(1,100)
deltaI=sp.Rational(1,20)
deltaL=sp.Rational(1,250)
N=sp.Integer(2000)
c=sp.Integer(23)

B=sp.simplify(N*beta1*Lam/(c*d)+beta2*Lam/(deltaI*d))
assert B == sp.Rational(508,23)
assert sp.simplify(alpha/(alpha+deltaL)) == sp.Rational(5,7)

xi1=sp.Rational(1,1000)
coef1=sp.simplify(B*(1-sp.Rational(2,7)*xi1))
assert coef1 == sp.Rational(444373,20125)

R05=coef1*sp.exp(-sp.Rational(1,2))
R175=coef1*sp.exp(-sp.Rational(7,4))
assert R05 > 1
assert R175 > 1
assert sp.N(R05,20) > sp.Float("13.3925")
assert sp.N(R175,20) > sp.Float("3.8370")

tau_c=sp.log(coef1)
assert tau_c > sp.Rational(3)
assert tau_c < sp.Rational(31,10)

xi_a=sp.Rational(1,20)
xi_b=sp.Rational(1,40)
Ra=sp.simplify(B*(1-sp.Rational(2,7)*xi_a)*sp.exp(-sp.Rational(7,4)))
Rb=sp.simplify(B*(1-sp.Rational(2,7)*xi_b)*sp.exp(-sp.Rational(7,4)))
assert sp.simplify(B*(1-sp.Rational(2,7)*xi_a)) == sp.Rational(762,35)
assert sp.simplify(B*(1-sp.Rational(2,7)*xi_b)) == sp.Rational(17653,805)
assert Ra > 1 and Rb > 1
assert Rb > Ra

derivative=sp.simplify(-sp.Rational(2,7)*B*sp.exp(-sp.Rational(7,4)))
assert derivative < 0
assert sp.simplify(-sp.Rational(2,7)*B) == -sp.Rational(1016,161)

lower=sp.simplify(B*sp.Rational(5,7)*sp.exp(-sp.Rational(7,4)))
assert lower > 1
assert sp.simplify(B*sp.Rational(5,7)) == sp.Rational(2540,161)

claimed_ratio=sp.Rational(81268,10000)/sp.Rational(6690,10000)
exact_ratio=sp.exp(sp.Rational(5,4))
assert sp.simplify(claimed_ratio-exact_ratio) != 0

print("VERIFY_OK")
print("B", B)
print("figure1_R0_tau_0_5", sp.N(R05,20))
print("figure1_R0_tau_1_75", sp.N(R175,20))
print("critical_tau", sp.N(tau_c,20))
print("figure2_R0_xi_0_05", sp.N(Ra,20))
print("figure2_R0_xi_0_025", sp.N(Rb,20))
print("figure2_uniform_lower_bound", sp.N(lower,20))
print("dR0_dxi", sp.N(derivative,20))
