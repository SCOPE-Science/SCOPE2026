#!/usr/bin/env python3
"""Exact identities for the branch-moduli map of binary quartic polars.

Requires SymPy; all computations take place over the rational function field Q(a).
"""
import sympy as S

X,Y,x,t,a,j=S.symbols('X Y x t a j')
f=X*(X+2*Y)*(X+3*Y)*(X+a*Y)
P=S.expand(S.diff(f,X).subs({X:x,Y:1}))
Q=S.expand(S.diff(f,Y).subs({X:x,Y:1}))
H=S.Poly(S.discriminant(P-t*Q,x)/4,t)

def invariants(q, v):
    p=S.Poly(q,v)
    A,B,C,D,E=[p.nth(4-i) for i in range(5)]
    return (S.factor(12*A*E-3*B*D+C**2),
            S.factor(72*A*C*E+9*B*C*D-27*A*D**2-27*E*B**2-2*C**3))

I,J=invariants(f.subs({X:x,Y:1}),x)
assert S.expand(I-(7*a**2-30*a+36))==0
assert S.expand(J-2*(a-6)*(2*a-3)*(5*a-12))==0
B_I,B_J=invariants(H.as_expr(),t)
assert S.expand(B_I-(144*I**4-32*I*J**2))==0
assert S.expand(B_J-(3456*I**6-1152*I**3*J**2+64*J**4))==0
assert S.expand(4*B_I**3-B_J**2-4096*J**6*(4*I**3-J**2))==0
source_j=S.factor(1728*4*I**3/(4*I**3-J**2))
branch_j=S.factor(1728*4*B_I**3/(4*B_I**3-B_J**2))
F=lambda u: u*(u+13824)**3/(64*(u-1728)**3)
assert S.cancel(branch_j-F(source_j))==0
assert S.cancel(F(j)-((j-1728)/64+27)*((j-1728)/64+243)**3/(((j-1728)/64)**3))==0
assert S.factor(S.cancel(F(j)-1728))==(j**2-34560*j-23887872)**2/(64*(j-1728)**3)
assert S.factor(S.diff(F(j),j))==(j+13824)**2*(j**2-34560*j-23887872)/(64*(j-1728)**4)
assert S.factor(4*I**3-J**2)==972*a**2*(a-2)**2*(a-3)**2
for av in [1,4,5,7,10]:
    assert S.cancel((branch_j-F(source_j)).subs(a,av))==0
print('VERIFY_OK: quartic invariants, branch invariants, discriminants, degree-four Belyi map and modular identity')
