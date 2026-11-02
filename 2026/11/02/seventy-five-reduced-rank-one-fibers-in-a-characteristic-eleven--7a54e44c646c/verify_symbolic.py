#!/usr/bin/env python3
"""Exact symbolic verification of a characteristic-11 cyclic-quartic stratum."""
import sympy as sp
x, a, b = sp.symbols('x a b')
p = 11
f = x**5 + a*x**3 + b*x + 1
F = {j: sp.Poly(f**j, x) for j in (2,5,8)}
red = lambda z: sp.Poly(sp.expand(z), a, b, modulus=p).as_expr()
def coeff(j, n): return red(F[j].coeff_monomial(x**n))
V = sp.Matrix([coeff(8, 10+11*i) for i in range(3)])
W = sp.Matrix([[coeff(2,10-i) for i in range(3)]])
B = sp.Matrix([[coeff(5,10+11*i-j) for j in range(2)] for i in range(2)])
L = red(V[0]+2*a**11*V[2])
D = red(B.det())
K = red(B[1,0]**11*B[0,1]+3)
Delta=red(sp.discriminant(f,x))
assert W == sp.Matrix([[1,0,2*a]])
assert B[1,1] == 5
assert D == red(-a**5-a**4*b**3-a**2*b**4-3*b**5-5)
assert L == red(-3*a**15-5*a**13*b+a**11*b**2+5*a**3*b+2*a**2*b**4-3*a*b**7+4*a*b**2+3*b**5-5)
assert Delta == red(-2*a**5+5*a**4*b**3+2*a**3*b+4*a**2*b**4-2*a*b**2+3*b**5+1)
# Smoothness excludes degeneration of the 3x1 off-diagonal block.
GV=sp.groebner(list(V),a,b,modulus=p,order='lex')
assert GV.polys[0].as_expr() == red(a-4*b**13-b**8-3*b**3)
assert GV.polys[-1].as_expr() == red((b**5+2)**3)
assert sp.rem(sp.Poly(Delta.subs(a,6*b**3),b,modulus=p),sp.Poly(b**5+2,b,modulus=p)).is_zero
# Intersection divisors: lexicographic elimination gives a graph over the b-coordinate.
GD=sp.groebner([L,D],a,b,modulus=p,order='lex')
GK=sp.groebner([D,K],a,b,modulus=p,order='lex')
assert len(GD.polys)==len(GK.polys)==2
assert GD.polys[0].degree(a)==GK.polys[0].degree(a)==1
hD=sp.Poly(GD.polys[-1].as_expr(),b,modulus=p)
hK=sp.Poly(GK.polys[-1].as_expr(),b,modulus=p)
assert hD.degree()==75 and hK.degree()==70
assert sp.gcd(hD,hD.diff()).degree()==0
assert sp.gcd(hK,hK.diff()).degree()==0
# The complete two finite schemes lie in the smooth quintic locus.
rDJ=sp.Poly(sp.resultant(D,Delta,a),b,modulus=p)
assert sp.gcd(hD,rDJ).degree()==sp.gcd(hK,rDJ).degree()==0
# No simultaneous vanishing of L,D,K, even on singular coefficient tuples.
assert [q.as_expr() for q in sp.groebner([L,D,K],a,b,modulus=p,order='lex').polys]==[sp.Integer(1)]
# A direct degree-five explicit member of the 75-point rank-one locus.
special_a=-3*b**3
modpoly=sp.Poly(b**5+2,b,modulus=p)
for z in (L,D): assert sp.rem(sp.Poly(z.subs(a,special_a),b,modulus=p),modpoly).is_zero
assert sp.rem(sp.Poly(Delta.subs(a,special_a),b,modulus=p),modpoly)==sp.Poly(-1,b,modulus=p)
assert sp.rem(sp.Poly(K.subs(a,special_a),b,modulus=p),modpoly)==sp.Poly(-3,b,modulus=p)
# Published Fermat specialization can be checked without relying on a general theorem.
assert int(Delta.subs({a:0,b:0})) %p != 0
assert int(D.subs({a:0,b:0}))%p !=0
assert int(L.subs({a:0,b:0}))%p !=0
print('CHAR11_CYCLIC_QUARTIC_SYMBOLIC_75_70_TRANSVERSE_AND_SMOOTH_OK')
