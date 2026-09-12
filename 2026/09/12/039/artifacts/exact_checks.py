"""Exact verification of the biextension disproof identities.
All arithmetic exact (Fractions / integers / sympy). No floating point.
"""
from fractions import Fraction
import sympy as sp

print("=== A. Collinearity: line Y+sX+s meets E: Y^2=X^3-X in P1,P2,T ===")
X, s = sp.symbols('X s')
resid = sp.expand((-s*X - s)**2 - (X**3 - X))
print("residual:", resid)
q, r = sp.div(sp.Poly(resid, X), sp.Poly(X**2 + 2*X + 1, X))
print("quotient:", q, "| remainder:", r)
# remainder is -2(X+1): X=-1 is a simple root over Z[s] (the point T=(-1,0)
# lies on the line for every s); full splitting needs s^2=-6:
assert sp.expand(r.as_expr() + 2*(X + 1)) == 0
# quotient should be (s^2+6)*? + ... check s^2=-6 kills constant part
print("quotient coeffs in s^2+6:",
      sp.expand(q.as_expr() - (s**2 + 6)))
# full residual factors as -(X+1)(X+2)(X+3) + (X+1)^2 (s^2+6)
target = -(X + 1)*(X + 2)*(X + 3) + (X + 1)**2 * (s**2 + 6)
assert sp.expand(resid - target) == 0
print("identity residual = -(X+1)(X+2)(X+3) + (X+1)^2(s^2+6): OK")
print("=> over K=Q(s), s^2=-6: intersection X in {-3,-2,-1}: P1+,P2+,T. OK")

print("=== B. P1,P2,T on E over K ===")
# E: Y^2 = X^3-X. P1=(-3,2s), P2=(-2,s), T=(-1,0), s^2=-6.
assert 4*(-6) == -27 + 3 and (-6) == -8 + 2 and 0 == -1 + 1
print("P1,P2,T satisfy Y^2=X^3-X with s^2=-6: OK")

print("=== C. Duplication x(2P) = -25/24 for both; e = 2P1 on E ===")
def dup_x(x):
    return (x**2 + 1)**2 / (4*(x**3 - x))
assert dup_x(Fraction(-3)) == Fraction(-25, 24)
assert dup_x(Fraction(-2)) == Fraction(-25, 24)
print("x(2P1+) = x(2P2+) = -25/24: OK")
# y(2P1) = 35s/288: check (35s/288)^2 = x^3-x at x=-25/24, i.e. 1225 s^2/82944
lhs_num = Fraction(35**2 * (-6), 288**2)   # s^2 -> -6
x = Fraction(-25, 24)
rhs = x**3 - x
print("y^2 =", lhs_num, "| x^3-x =", rhs)
assert lhs_num == rhs
print("e=(-25/24, 35s/288) lies on E(K): OK")
assert x != 0 and x != 1 and x != -1
print("e not 2-torsion (x not in {0,1,-1}), e != O: OK")

print("=== D. Reductions to 2-torsion mod primes above 5 and 7 ===")
# p=5: prime (5,s-2); s->2. denominators 24,288 prime to 5.
assert (24 % 5) != 0 and (288 % 5) != 0
ex5 = (Fraction(-25, 24).numerator * pow(Fraction(-25, 24).denominator, -1, 5)) % 5
# simpler: -25/24 mod5 = 0/4 = 0; 35 s/288 mod5 = 0.
print("x mod5 =", (-25 % 5), "/ (24 mod5 =", 24 % 5, ") => 0")
print("y mod5: 35 mod5 =", 35 % 5, "=> 0")
assert (-25) % 5 == 0 and (35 % 5) == 0
assert (0**2) % 5 == (0**3 - 0) % 5
print("image (0,0) on E(F5), order 2: OK")
# p=7: prime (7,s-1); s->1. -25 mod7=3, 24 mod7=3 => x=1; 35 mod7=0 => y=0.
assert (-25) % 7 == 24 % 7 == 3 and (35 % 7) == 0 and (288 % 7) != 0
assert (0**2) % 7 == (1**3 - 1) % 7
print("image (1,0) on E(F7), order 2: OK")

print("=== E. Monodromy integer matrices: rank 2, N^2=0, weight dims ===")
# basis (a1,a2,a3,b1,b2,b3); N(b1)=-a1, N(b2)=-a2 (sign convention T(v)=v+<v,d>d)
import sympy as sp
N = sp.zeros(6)
N[0, 3] = -1
N[1, 4] = -1
assert N**2 == sp.zeros(6)
assert N.rank() == 2
T = sp.eye(6) + N
assert (T - sp.eye(6)).rank() == 2
# Ker N = span(a1,a2,a3,b3): y1=y2=0
ker = N.nullspace()
assert len(ker) == 4
print("N^2=0, rank N=2, dim Ker N=4: OK")
print("Gr dims: W0=Im (2), W1/W0 (4-2=2), W2/W1 (6-4=2): OK")

print("=== F. Node tangent cones (ordinary double points) ===")
# at x=0: y^2+24x^2 -> tangents y=+-sqrt(-24)x distinct; at x=1: y^2+6(x-1)^2 distinct.
print("c0 = (0-2)(0-3)(0-4) =", (-2)*(-3)*(-4))
print("c1 = (1-2)(1-3)(1-4) =", (-1)*(-2)*(-3))
assert (-2)*(-3)*(-4) == -24 and (-1)*(-2)*(-3) == -6
print("both nonzero => distinct tangents => nodes: OK")

print("ALL EXACT CHECKS PASSED")
