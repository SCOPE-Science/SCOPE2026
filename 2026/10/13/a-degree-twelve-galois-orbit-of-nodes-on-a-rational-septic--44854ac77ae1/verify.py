"""Exact algebraic checks for the rational singular-node orbit of a plane septic.
Requires Python 3 and SymPy. This script checks polynomial identities and a
finite-field irreducibility certificate; it does not substitute for the geometric
interpretation of the discriminant and normalization.
"""
from sympy import Poly, Symbol, diff, discriminant, gcd, rem, resultant, symbols, expand

u, x, y = symbols('u x y')
D = y**12 + 15*y**10 + 71*y**8 + 84*y**6 + 9*y**4 - 3*y**2 - 1
R = y*(17*y**10+254*y**8+1193*y**6+1371*y**4+134*y**2-1)/40
E = (x**5*(y**2+1) + 5*x**4*(y**3-y)
     +10*x**3*(y**4-y**2)+5*x**2*(2*y**5-y**3+y)
     +5*x*(y**6+y**2)+y**7-y)
# Polynomial equation from the rational normalization, with a fixed sign.
assert Poly(resultant(u**5-y, x*(1+u*u)-u+u**7, u)+E, x, y).is_zero
assert expand(discriminant(E,x) - 3125*y**4*D**2) == 0
assert discriminant(D,y) == -(2**36)*(5**18)*(821**2)
assert rem(D,y*y+1,y) == -16
assert D.subs(y,0)==-1
# Every root of D supplies the unique double root x=R(y): it lies in the
# Jacobian ideal, as checked modulo the irreducible degree-twelve polynomial.
for pol in [E,diff(E,x),diff(E,y)]:
    assert Poly(rem(Poly(pol.subs(x,R),y),Poly(D,y)),y).is_zero
# Rabin finite-field irreducibility test for degree 12 over F_7:
# x^(7^12)=x mod D; gcd with x^(7^6)-x and x^(7^4)-x is one.
D7 = Poly(D,y,modulus=7)
def polynomial_power_mod(exp):
    base=Poly(y,y,modulus=7)
    out=Poly(1,y,modulus=7)
    while exp:
        if exp&1: out=(out*base).rem(D7)
        base=(base*base).rem(D7)
        exp//=2
    return out
assert polynomial_power_mod(7**12) == Poly(y,y,modulus=7)
for n in (4,6):
    assert gcd(D7,polynomial_power_mod(7**n)-Poly(y,y,modulus=7)).degree()==0
# Reproduce concrete rational-node counts away from bad characteristics.
for p,expected in [(3,0),(7,0),(11,2),(13,0),(71,4),(89,8)]:
    c=sum(int(D.subs(y,i))%p==0 for i in range(p))
    assert c==expected,(p,c)
print('VERIFY_OK: normalization resultant, discriminants, 12-node graph, irreducibility mod 7, sample primes')
