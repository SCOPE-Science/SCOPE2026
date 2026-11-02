#!/usr/bin/env python3
"""Exact symbolic coefficient and geometric checks for a genus-six cyclic cover."""
import sympy as S
x,a,b,c,r=S.symbols('x a b c r')
p=7
f=x**5+a*x**3+b*x+c
P=S.Poly(S.expand(f**5),x)
R=S.Poly(S.expand(f**3),x)
T=S.Poly(f,x)
red=lambda e:S.Poly(S.expand(e),a,b,c,modulus=7).as_expr()
U=a**4*b+6*a*a*b*b+6*a*c*c+2*b**3
E=a*b*b+c*c
W=c*(a*a+2*b)
assert red(P.nth(13)-5*U)==0
assert red(P.nth(20)-5*c)==0
assert red(P.nth(6)-10*c*(a*a*c*c+2*a*b**3+2*b*c*c))==0
M=S.Matrix([[R.nth(6),R.nth(5)],[R.nth(13),R.nth(12)]])
assert all(red(v)==0 for v in [M[0,0]-3*W,M[0,1]-3*E,M[1,0]-3*a,M[1,1]])
assert red(M.det()+9*a*E)==0
assert [T.nth(i) for i in (6,5,4)]==[0,1,0]
Disc=red(S.discriminant(f,x))
assert red(Disc.subs({a:0,b:0})-3*c**4)==0
assert red(Disc.subs({a:0,c:0})+3*b**5)==0
# For rank-one locus: b=r*a^2, r^2=3 and c^2=4*a^5.
# Reduce discriminant modulo the ideal (b-r*a^2, c^2-4*a^5, r^2-3).
poly=S.Poly(S.expand(Disc.subs(b,r*a**2)),c)
expr=S.expand(poly.rem(S.Poly(c**2-4*a**5,c)).as_expr())
assert S.expand(expr).subs(a,0)==0
expr=S.rem(S.Poly(S.expand(expr).subs(a,1),r,modulus=7),S.Poly(r*r-3,r,modulus=7)).as_expr()
assert S.Poly(S.expand(expr-(-2*r-3)),r,modulus=7).is_zero
# c^2 = 4a^5, b=r a^2: r=-3/2 is not a root of r^2=3 in F7.
assert (2**2-3)%7!=0
assert red(U.subs({a:0,b:0}))==0
print('GENUS6_CHAR7_SYMBOLIC_CARTIER_AND_RANK_ONE_GEOMETRY_OK')
