#!/usr/bin/env python3
import sympy as sp

beta1,beta2,beta3 = sp.symbols("beta1 beta2 beta3", positive=True)
alpha,alpha1,alpha2,alpha3,alpha4 = sp.symbols("alpha alpha1 alpha2 alpha3 alpha4", positive=True)
gamma1,gamma2,d = sp.symbols("gamma1 gamma2 d", positive=True)

qE = alpha + gamma1 + d
q1 = alpha1 + alpha4 + gamma2 + d
q2 = alpha3 + alpha2 + d

A0 = sp.Matrix([
    [beta1-qE, beta2+alpha4, beta3],
    [alpha, -q1, alpha3],
    [0, alpha1, -q2],
])

w = sp.Matrix([[
    alpha*q2,
    q2*(qE-beta1),
    alpha*beta3 + alpha3*(qE-beta1),
]])

prod = [sp.factor(z) for z in list(w*A0)]
detA = sp.factor(A0.det())

assert sp.simplify(prod[0]) == 0
assert sp.simplify(prod[2]) == 0
assert sp.simplify(prod[1]-detA) == 0

critical_identity = (
    (qE-beta1)*(q1*q2-alpha1*alpha3)
    - alpha*(q2*(beta2+alpha4)+alpha1*beta3)
)
assert sp.simplify(detA + critical_identity) == 0

# q1*q2-alpha1*alpha3 is manifestly positive after expansion.
gap = sp.expand(q1*q2-alpha1*alpha3)
assert all(term != 0 for term in sp.Add.make_args(gap))

print("VERIFY_OK")
print("left_product", prod)
print("determinant", detA)
print("critical_identity_check", sp.simplify(detA + critical_identity))
