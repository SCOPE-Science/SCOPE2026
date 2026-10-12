#!/usr/bin/env python3
"""Exact characteristic-three polynomial identities supporting an even-octic curve theorem."""
import sympy as s
x,a,b=s.symbols('x a b')

def equal_mod3(p,q):
    assert s.Poly(s.expand(p-q),x,a,b,modulus=3).is_zero

f=x**8+b**3*x**6+a**3*x**2+1
# Derivative and parameter boundary.
equal_mod3(s.diff(f,x),-x*(x*x+a)**3)
equal_mod3((x*x+a)**3*(x*x+b**3),f+(a*b)**3-1)
# The quotient equations, their coefficient-extraction Hasse matrices.
v=s.symbols('v')
Q=v**4+b**3*v**3+a**3*v+1
D=v*Q
for i in range(1,4):
    for j in range(1,4):
        desired = [[a**3,0,1],[0,0,0],[1,0,b**3]][i-1][j-1]
        equal_mod3(s.Poly(f,x).coeff_monomial(x**(3*i-j)),desired)
for i in range(1,3):
    for j in range(1,3):
        desired = [[a**3,1],[1,b**3]][i-1][j-1]
        assert s.Poly(s.expand(s.Poly(D,v).coeff_monomial(v**(3*i-j))-desired),a,b,modulus=3).is_zero
assert s.Poly(Q,v).coeff_monomial(v**2)==0
# Boundary normalization and the supersingularity equation.
equal_mod3((x*x+a)*(x*x+b**3),x**4+(a+b**3)*x*x+a*b**3)
assert not s.Poly(s.expand(a**3*(a+b**3)-a**4-1),a,b,modulus=3).is_zero
# The previous polynomial is zero under ab=1, not in the free ring.
assert s.Poly(s.expand((a**3*(a+b**3)-a**4-1).subs(b,1/a)*a**3),a,modulus=3).is_zero
assert s.Poly(s.expand((x*x+a)**4-(x**8+a*x**6+a**3*x*x+a**4)),x,a,modulus=3).is_zero
# Test special boundaries in F9, represented by u^2=-1 over F3.
# Disjoint polynomials a^4-1 and a^4+1 are coprime in F3[a].
A=s.Poly(a**4-1,a,modulus=3)
B=s.Poly(a**4+1,a,modulus=3)
assert A.gcd(B).degree()==0
assert A.gcd(A.diff()).degree()==0
assert B.gcd(B.diff()).degree()==0
print('VERIFY_OK')
