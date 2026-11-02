#!/usr/bin/env python3
"""Exact independent regenerations of explicit polynomial identities over GF(5)."""
import sympy as S
x,s,t=S.symbols('x s t')
def eq5(p,q): return S.Poly(S.expand(p-q),s,t,modulus=5).is_zero
f=x**4-(s+1)*x**3+(t+s)*x**2-t*x
P=S.Poly(S.expand(f**3),x)
c4=-2*t**2*(t+s)
c9=-(s-1)*(s**2+t-1)
d=-(s+1)
assert eq5(P.nth(4),c4) and eq5(P.nth(9),c9)
H=-2*t**3-2*s*t**2+(s-1)*(s+1)**5*(t+s**2-1)
assert eq5(c4+c9*d**5,H)
print('CARTIER_COEFFICIENTS_OK; TWO_STEP_HASSE_POLYNOMIAL_OK')
G=S.groebner([H,S.diff(H,s),S.diff(H,t)],t,s,modulus=5)
expected=[t+s**6-s**5+s-1,(s-1)*(s+1)**5*(s+2)**5]
assert len(G.polys)==2
assert all(eq5(G.polys[i].as_expr(),expected[i]) for i in (0,1))
for sv,tv in [(1,0),(-1,0),(3,2)]:
 assert int(S.expand(H).subs({s:sv,t:tv}))%5==0
 assert (tv%5==0 or (1-sv+tv)%5==0)
print('SINGULAR_LOCUS_GROEBNER_OK; BOUNDARY_EXCLUSION_OK')
B,C,u,v,w,z=S.symbols('B C u v w z')
quad=S.Poly(S.expand(H.subs(t,-s**2+B*s+C)),s)
assert S.Poly(quad.nth(7)-B,B,C,modulus=5).is_zero
assert S.Poly(quad.nth(6)-(-B+C+1),B,C,modulus=5).is_zero
assert quad.nth(4).subs({B:0,C:-1})%5==1
# For the cubic case, reduce by u^2=3 and substitute recursively implied coefficients.
cubic=S.Poly(S.expand(H.subs(t,u*s**3+(2*u-2)*s**2+(u+2)*s+(u-2))),s)
assert S.Poly(cubic.nth(4)-1,u,modulus=5).rem(S.Poly(u*u-3,u,modulus=5)).is_zero
print('ABSOLUTE_IRREDUCIBILITY_ROOT_OBSTRUCTIONS_OK')
assert int(H.subs({s:-1,t:1}))%5==0
assert ((-1)**2-4*1)%5 != 0
print('NONEMPTY_SMOOTH_LIFT_EXAMPLE_OK')
print('VERIFY_OK')
