"""Symbolic audits for the finite-field paraboloid Gram decomposition.

Run with: python symbolic_certificate.py
Requires SymPy; this checks polynomial algebra used in the written proof.
"""
import sympy as S
q, s, x, u, h = S.symbols('q s x u h')
r = q-1
L = (q+1)/2
A2 = (q-1)/(q+1)
y = x+s
# Determinant after Schur elimination of the first two coordinates.
D4 = x**2*y**2 - x*s*y**2*r - 4*s**2*L*x*y + 4*s**3*L*y*(r-A2)
P = u**3+(2-q)*u**2-(3*q+1)*u+2*q*(q-1)
assert S.simplify(D4 - y*s**3*P.subs(u,x/s)) == 0
# Independently form the actual four-dimensional Hermitian block with generic
# coupling variables; this verifies the Schur determinant rather than assuming it.
a,d,w = S.symbols('a d w')
M = S.Matrix([[1,0,s*a,s*d],
              [0,1,2*s*w,0],
              [s*a,2*s*w,1-s+s*a*a,s*a*d],
              [s*d,0,s*a*d,1-s+s*d*d]])
actual_det = S.factor(((1+x)*S.eye(4)-M).det())
reduced_det = S.expand(actual_det).subs(w**2,L).subs(a**2,A2).subs(d**2,r-A2)
assert S.simplify(reduced_det - D4) == 0
assert S.simplify(S.resultant(P, u**2+u-4*q,u) - 4*q*(q-3)*(q-1)**2) == 0
assert S.simplify(P.subs(u,q) - q*(q-3)) == 0
assert S.simplify(P.subs(u,-q) + q*(2*q*q-7*q+1)) == 0
assert S.simplify(P.subs(u,-1) - 2*(q*q+1)) == 0
assert S.simplify(P.subs(u,0) - 2*q*(q-1)) == 0
expected = 8*h**5+73*h**4+306*h**3+933*h**2+2172*h+2420
assert S.expand(S.discriminant(P,u).subs(q,h+3)-expected) == 0
assert S.simplify(P.subs(u,q-1) + 2*(q-1)) == 0
print('SYMBOLIC_CERTIFICATE_OK determinant_cubic resultant discriminant boundary substitutions')
