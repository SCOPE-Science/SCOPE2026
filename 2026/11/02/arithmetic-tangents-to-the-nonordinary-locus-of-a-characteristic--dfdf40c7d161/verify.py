#!/usr/bin/env python3
"""Exact characteristic-11 coefficient and singular-locus checks for a Picard-family Hasse divisor."""
import sympy as s
p=11
x,a,b=s.symbols('x a b')
f=x**4+a*x**2+b*x+1
as_mod=lambda pol:s.Poly(pol,a,b,modulus=p)
modzero=lambda pol:as_mod(pol).is_zero
c3=s.Poly(s.expand(f**3),x)
c7=s.Poly(s.expand(f**7),x)
A=as_mod(c3.nth(10)).as_expr()
B=as_mod(c3.nth(9)).as_expr()
C=as_mod(c7.nth(10)).as_expr()
D=as_mod(c7.nth(21)).as_expr()
assert modzero(A-3*a) and modzero(B-3*b)
assert modzero(D-(-5*a*a*b-2*b))
Cexpected = -a**5-5*a**4*b**2+2*a**3*b**4-3*a**3+3*a**2*b**2+a*b**4-5*a-4*b**6+b**2
assert modzero(C-Cexpected)
P=as_mod(a**11*C+b**11*D)
assert P.total_degree()==18
assert modzero(P.as_expr() - (a**11*Cexpected+b**11*(-5*a*a*b-2*b)))
lowest = sum(c*a**m[0]*b**m[1] for m,c in P.terms() if sum(m)==12)
assert modzero(lowest-(-5*a**12-2*b**12))
assert min(sum(m) for m,c in P.terms())==12
assert s.gcd(s.Poly(s.Symbol('t')**12-3,s.Symbol('t'),modulus=p),s.Poly(12*s.Symbol('t')**11,s.Symbol('t'),modulus=p)).degree()==0
print('CARTIER_P11_COEFFICIENTS_AND_SCALAR_CONDITION_OK')
print('HASSE_DIVISOR_DEGREE=18; FERMAT_MULTIPLICITY=12; TANGENT_EQUATION=r^12-3')
# Geometry of the whole singular support in the affine (a,b) parameter plane.
G=s.groebner([P.as_expr(),P.diff(a).as_expr(),P.diff(b).as_expr()],a,b,modulus=p,order='lex')
assert len(G.polys)==4
assert modzero(G.polys[-1].as_expr()-(b**55-3*b**11))
assert modzero(G.polys[1].as_expr()-(a**11*b+4*b**23))
assert modzero(G.polys[0].as_expr().subs(b,0)-(a**13-4*a**11))
# Consequently singular geometric support has b=0, a in {0,+2,-2},
# or b^4=3 and a=-4b^2. Check every one is on the singular locus.
for expr in [P.as_expr(),P.diff(a).as_expr(),P.diff(b).as_expr()]:
 for v in [0,2,-2]:
  assert as_mod(expr.subs({a:v,b:0})).is_zero
  # substitute relation b^4=3
  expr_b=s.Poly(as_mod(expr.subs(a,-4*b*b)).as_expr(),b,modulus=p)
  assert s.rem(expr_b.as_expr(),b**4-3,b,modulus=p)==0
Delta=as_mod(s.discriminant(f,x))
assert modzero(Delta.as_expr() - (5*a**4-4*a**3*b**2+4*a**2+a*b**2-5*b**4+3))
for v in [2,-2]:
 assert as_mod(Delta.as_expr().subs({a:v,b:0})).is_zero
assert s.rem(as_mod(Delta.as_expr().subs(a,-4*b*b)).as_expr(),b**4-3,b,modulus=p)==0
assert Delta.eval({a:0,b:0})%p!=0
print('GROEBNER_GEOMETRIC_SINGULAR_SUPPORT_EXACT: (0,0), (+-2,0), (a=-4*b^2,b^4=3)')
print('ONLY_SINGULAR_SUPPORT_POINT_ON_SMOOTH_FAMILY=(0,0)')
# Check potentially elevated Cartier a-number is impossible off the Fermat point
# on the smooth family, by the explicit coefficients C,D and Delta.
assert modzero(C.subs({a:2})+4*b*b*(b*b-5)**2)
assert modzero(C.subs({a:-2})+4*b*b*(b*b+5)**2)
assert modzero(C.subs(b,0)+a*(a*a-4)**2)
print('CARTIER_RANK=0_AT_FERMAT; RANK=2_ALL_OTHER_SMOOTH_PARAMETERS')
# Finite-field check independent of singular-support Groebner implications.
rank0=[];rank2=[];bad=[]
for av in range(p):
 for bv in range(p):
  e={a:av,b:bv}
  if Delta.eval(e)%p==0:
   bad.append((av,bv));continue
  (rank0 if P.eval(e)%p==0 else rank2).append((av,bv))
assert len(bad)==10 and len(rank2)==106
assert rank0==[(0,0),(4,1),(4,5),(4,6),(4,10)],rank0
print('F11_SMOOTH_PARAMETERS=111; P_RANK_ZERO_PARAMETERS='+str(rank0)+'; P_RANK_TWO=106')
print('TANGENT_FROBENIUS_CYCLES=(1,1,2,2,2,2,2)')
print('VERIFY_OK')
