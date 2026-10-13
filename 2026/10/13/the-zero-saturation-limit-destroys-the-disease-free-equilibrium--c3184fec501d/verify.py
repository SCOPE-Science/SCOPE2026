#!/usr/bin/env python3
import sympy as sp

I,b,a,A,k2,beta,g1,d1,B,pi,k1,eps,mu3,alpha,r = sp.symbols(
    "I b a A k2 beta g1 d1 B pi k1 eps mu3 alpha r", positive=True
)

T = a*I/(b+I)
assert sp.limit(T, I, 0, dir="+") == 0

T0_positive = sp.simplify(T.subs(b,0))
assert T0_positive == a
assert sp.limit(T0_positive, I, 0, dir="+") == a

S0 = A/k2
Sdot = A/(1+alpha*I) - beta*g1*d1*S0*I - pi*S0*B - k2*S0 + T0_positive
Idot = beta*g1*d1*S0*I + pi*S0*B - k1*I - T0_positive
Bdot = eps*I - mu3*B

limits = tuple(sp.simplify(sp.limit(expr.subs(B,0), I, 0, dir="+")) for expr in (Sdot,Idot,Bdot))
assert limits == (a,-a,0)

R0 = A*b*(eps*pi + beta*g1*d1*mu3) / (mu3*k2*(b*k1+a))
assert sp.simplify(R0.subs(b,0)) == 0

regular = r*b*I/(b+I)
assert sp.limit(regular, b, sp.oo) == r*I

# Pointwise limit is nonuniform at the disease-free state.
assert T.subs(I,0) == 0
assert sp.limit(T, b, 0, dir="+").subs(I,sp.Integer(1)) == a

print("VERIFY_OK")
print("positive_branch_T0", T0_positive)
print("disease_free_one_sided_field", limits)
print("R0_at_b0", sp.simplify(R0.subs(b,0)))
print("regular_linear_limit", sp.limit(regular,b,sp.oo))
