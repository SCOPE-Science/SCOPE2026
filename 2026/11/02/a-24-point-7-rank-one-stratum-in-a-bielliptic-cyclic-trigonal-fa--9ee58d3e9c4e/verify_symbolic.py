#!/usr/bin/env python3
"""Exact identities for a cyclic trigonal genus-four family over characteristic 7."""
import sympy as sp

a, b, u = sp.symbols('a b u')
q = u**3 + a*u**2 + b*u + 1
c4 = sp.Poly(sp.expand(q**4), u)
c2 = sp.Poly(sp.expand(q**2), u)
c = {i:c4.nth(i) for i in [2,3,6,9,10]}
Delta = sp.discriminant(q, u)

def zero(P):
    return sp.Poly(sp.expand(P), a, b, modulus=7).is_zero

assert zero(Delta-(a*a*b*b+3*a**3+3*b**3-3*a*b+1))
assert zero(c[2]-(-3*a-b**2))
assert zero(c[3]-(-2*a*b-3*b**3-3))
assert zero(c[6]+Delta)
assert zero(c[9]-(-3*a**3-2*a*b-3))
assert zero(c[10]-(-a*a-3*b))
D2 = sp.expand(c[3]*c[9]-c[2]*c[10])
assert zero(D2-2*(a*b+1)*Delta)
assert zero(c2.nth(3)-2*(1+a*b))
assert zero(c2.nth(3)*c[6]*D2-3*(1+a*b)**2*Delta**2)

# On ab=-1, B is a rank-one matrix with columns proportional to (1,b^-2).
A, C = -3*b**3-1, 3-b**3
B = sp.Matrix([[c[3],c[2]],[c[10],c[9]]]).subs(a,-1/b)
V = sp.Matrix([[A,C/b],[A/b**2,C/b**3]])
for i in range(2):
    for j in range(2):
        n, d = sp.fraction(sp.cancel(B[i,j]-V[i,j]))
        assert sp.Poly(n,b,modulus=7).is_zero

# Rank(B^[7] B) vanishes iff A^7 + C^7/b^9=0.
P = -3*b**30 - b**21 - b**9+3
n, d = sp.fraction(sp.cancel(b**9*(A**7+C**7/b**9)))
assert sp.Poly(n-P,b,modulus=7).is_zero
D = b**6 + 4*b**3 -1
Q = (b**24+3*b**21+3*b**18+3*b**15+5*b**12
     +4*b**9+3*b**6+4*b**3+1)
assert sp.Poly(P+3*D*Q,b,modulus=7).is_zero
assert sp.gcd(sp.Poly(D,b,modulus=7),sp.Poly(Q,b,modulus=7)).degree()==0
assert sp.gcd(sp.Poly(Q,b,modulus=7),sp.Poly(sp.diff(Q,b),b,modulus=7)).degree()==0
cubics = [b**3+2,b**3+3,b**3+3*b-2,b**3-2*b-2,
          b**3-b-2,b**3+3*b**2-3,b**3-2*b**2-3,b**3-b**2-3]
product = sp.prod(cubics)
assert sp.Poly(Q-product,b,modulus=7).is_zero
for f in cubics:
    assert all(int(f.subs(b,i))%7!=0 for i in range(7))
# On the nonordinary smooth hyperbola, the discriminant is 3D/b^3.
n, d = sp.fraction(sp.cancel(Delta.subs(a,-1/b)-3*D/b**3))
assert sp.Poly(n,b,modulus=7).is_zero
print('SYMBOLIC_GF7_HASSE_DETERMINANT_AND_24_P_RANK_EXCEPTIONAL_PARAMETERS_OK')
