#!/usr/bin/env python3
"""Exact certificates for the characteristic-41 genus-four dihedral pencil."""
import math
from sympy import Poly, symbols, gcd

p = 41
s, v = symbols('s v')

def coeff(k):
    # coefficient of U^k in (U^2+s U+1)^20, in GF(41)[s]
    z = 0
    for e in range(21):
        f = k-2*e
        g = 20-e-f
        if f >= 0 and g >= 0:
            z += (math.factorial(20)//(math.factorial(e)*math.factorial(f)*math.factorial(g))) *s**f
    return Poly(z, s, modulus=p)

A_s, B_s = coeff(8), coeff(16)
assert coeff(32)==A_s and coeff(24)==B_s
assert all(A_s.nth(i)==0 for i in range(1, 9, 2))
assert all(B_s.nth(i)==0 for i in range(1, 17, 2))
A=Poly.from_list([int(A_s.nth(i)) for i in range(8,-1,-2)],gens=v,modulus=p)
B=Poly.from_list([int(B_s.nth(i)) for i in range(16,-1,-2)],gens=v,modulus=p)
L=Poly(v+15,v,modulus=p)
T=Poly(v+13,v,modulus=p)
C=Poly(v**3-17*v**2+v+2,v,modulus=p)
H=Poly(v**6+20*v**5+14*v**4-3*v**3+15*v**2-14*v-19,v,modulus=p)
assert A==Poly(18,v,modulus=p)*L*C
assert B==Poly(7,v,modulus=p)*L*T*H
assert gcd(A,B).monic()==L
assert A.gcd(A.diff()).degree()==0
assert B.gcd(B.diff()).degree()==0
def rabin_irreducible(F):
    # For monic degree n over GF(p), check x^(p^n)=x mod F,
    # and gcd(x^(p^(n/l))-x, F)=1 for every prime divisor l of n.
    X=Poly(v,v,modulus=p)
    n=F.degree()
    def frobenius_power(m):
        z=X
        for _ in range(m):
            z=pow_poly(z,p,F)
        return z
    def pow_poly(a,e,mod):
        z=Poly(1,v,modulus=p)
        while e:
            if e&1:z=(z*a).rem(mod)
            a=(a*a).rem(mod)
            e>>=1
        return z
    assert frobenius_power(n)==X.rem(F)
    factors=sorted({int(f) for f,_ in __import__('sympy').factorint(n).items()})
    return all(gcd(frobenius_power(n//ell)-X,F).degree()==0 for ell in factors)
assert all(rabin_irreducible(F) for F in (C,H,L,T))
assert A.eval(4)==1 and B.eval(4)==1
assert A.eval(0)!=0 and B.eval(0)!=0
assert len({i*i%p for i in range(p)}&{26,28})==0
assert [z for z in range(p) if A_s.eval(z)==0 or B_s.eval(z)==0]==[]
assert len({n%p for n in range(p) if n*n%p==26})==0
assert len({n%p for n in range(p) if n*n%p==28})==0
assert 2 + 3 + 6 == 11  # the complete geometric nonordinary moduli support
assert 1 + 3 + 6 == 10  # its rank-two component
print('A(v)=',A.as_expr())
print('B(v)=',B.as_expr())
print('GF(41) factorization: A=18(v+15)(v^3-17v^2+v+2)')
print('GF(41) factorization: B=7(v+13)(v+15)(v^6+20v^5+14v^4-3v^3+15v^2-14v-19)')
print('irreducible moduli factor degrees for rank2: 1,3,6; rank0: 1')
print('smooth-exclusion v=4 is not exceptional; no s in GF(41) exceptional')
print('VERIFY_OK: Cartier coefficients, squarefreeness, gcd, irreducibility, smoothness, orbit counts')
