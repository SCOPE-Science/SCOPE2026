#!/usr/bin/env python3
"""Exact identities for a genus-three characteristic-five hyperelliptic family."""
import sympy as S
x,a,b,z=S.symbols('x a b z')
P=x**7+a*x**5+b*x**3+x
coeff=S.Poly(S.expand(P**2),x)
H=S.Matrix(3,3,lambda i,j: coeff.nth(5*(i+1)-(j+1)))
expected=S.Matrix([[2*b,0,1],[0,2*(a*b+1),0],[1,0,2*a]])
assert H==expected
poly=lambda expr:S.Poly(S.expand(expr),a,b,modulus=5)
assert poly(H.det())==poly(-2*(a*b+1)**2)
G=z**3+a*z**2+b*z+1
D=S.discriminant(G,z)
assert poly(D)==poly(a**3+a*a*b*b+3*a*b+b**3+3)
# discriminant on the nonordinary divisor ab=-1, away from b=0
assert S.Poly(S.together(D.subs(a,-1/b)*b**3),b,modulus=5)==S.Poly((b**3-2)**2,b,modulus=5)
# On the rank-drop conic, the semilinear rank-one block vanishes
# in the second Frobenius iterate iff b^5+a=0 iff b^6=1.
assert S.Poly(S.expand(b*(b**5-1/b)),b,modulus=5)==S.Poly(b**6-1,b,modulus=5)
# Exception locus cannot lie on the singular discriminant: b^6=1 implies
# D|_{ab=-1}=1, because b^3=+/-1.
q=S.Poly((b**3-2)**2,b,modulus=5)
r=S.Poly(b**6-1,b,modulus=5)
assert S.gcd(q,r).degree()==0
assert S.gcd(r,r.diff()).degree()==0
print('EXACT_HASSE_DISCRIMINANT_AND_EXCEPTION_OK')
