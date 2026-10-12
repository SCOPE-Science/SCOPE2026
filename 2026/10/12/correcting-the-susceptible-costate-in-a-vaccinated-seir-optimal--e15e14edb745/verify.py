#!/usr/bin/env python3
import sympy as sp

S,E,I = sp.symbols("S E I", positive=True)
u1,u2 = sp.symbols("u1 u2", real=True)
A0,A1,mu,z0,delta1,delta2,alpha,omega1,omega2,C1,C2,C3 = sp.symbols(
    "A0 A1 mu z0 delta1 delta2 alpha omega1 omega2 C1 C2 C3", positive=True
)
l1,l2,l3 = sp.symbols("l1 l2 l3", real=True)
theta = sp.Function("theta")

f1 = A0-(1-u2)*theta(I)*S*E-(mu+z0*u1)*S
f2 = A1+(1-u2)*theta(I)*S*E-(mu+delta1+alpha+omega1)*E
f3 = alpha*E-(mu+delta2+omega2)*I
H = C1*u1**2+C2*u2**2+C3*I+l1*f1+l2*f2+l3*f3

correct1 = sp.simplify(-sp.diff(H,S))
correct2 = sp.simplify(-sp.diff(H,E))
correct3 = sp.simplify(-sp.diff(H,I))

a = (1-u2)*theta(I)
v = mu+z0*u1

expected1 = sp.expand(l1*(a*E+v)-l2*a*E)
expected2 = sp.expand(l1*a*S-l2*a*S+l2*(mu+delta1+alpha+omega1)-l3*alpha)
expected3 = sp.expand((1-u2)*sp.diff(theta(I),I)*S*E*l1
                      -(1-u2)*sp.diff(theta(I),I)*S*E*l2
                      +l3*(mu+delta2+omega2)-C3)

assert sp.simplify(correct1-expected1) == 0
assert sp.simplify(correct2-expected2) == 0
assert sp.simplify(correct3-expected3) == 0

printed1 = sp.expand(l1*(a*E+v)-l2*(a*E+v))
assert sp.simplify(printed1-correct1 + v*l2) == 0

# Terminal coefficient check in tau=T-t:
# lambda3 = C3*tau + ...
# -d(lambda2)/d(tau) = -alpha*lambda3 + higher order,
# so d(lambda2)/d(tau)=alpha*C3*tau+...
tau = sp.symbols("tau", positive=True)
a2 = sp.simplify(sp.integrate(alpha*C3*tau, (tau, 0, tau)) / tau**2)
assert a2 == alpha*C3/2

# Exact interior witness for the discrepancy.
witness = sp.simplify((-v*l2).subs({mu:1,z0:2,u1:sp.Rational(1,5),l2:5}))
assert witness == -7

print("VERIFY_OK")
print("correct_first_costate", correct1)
print("printed_minus_correct", sp.factor(printed1-correct1))
print("terminal_lambda2_coefficient", a2)
print("exact_witness_difference", witness)
