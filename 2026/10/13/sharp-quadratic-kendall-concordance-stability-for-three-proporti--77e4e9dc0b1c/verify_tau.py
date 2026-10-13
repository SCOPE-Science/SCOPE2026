"""Exact rational certificate for three-component first-two-failure Kendall tau.
Requires Python 3.10+ and SymPy 1.12+; run: python verify_tau.py.
Every polynomial identity is verified symbolically, not by sampling.
"""
from fractions import Fraction
import sympy as sp

a, b, c = sp.symbols('a b c')
S = 3*a + 2*b + c
p = [a/S, (a+b)/S, (a+b+c)/S]

def exact_tau(z):
    q = [1-w for w in z]
    return sum(z[i]*z[j]*q[i]*q[j]/(q[i]+q[j]) *
               (1/(1+q[i])+1/(1+q[j])) for i in range(3) for j in range(3))

T = exact_tau(p)
variance = sum((v-sp.Rational(1,3))**2 for v in p)
G = sp.Rational(2,5)*(1-variance)-T
D = 15*S**2*(4*a+2*b+c)*(4*a+3*b+c)*(4*a+3*b+2*c)*\
    (5*a+3*b+c)*(5*a+3*b+2*c)*(5*a+4*b+2*c)
P = sp.Poly(sp.cancel(D*G), a, b, c)
assert P.total_degree() == 8
assert len(P.terms()) == 40, len(P.terms())
assert all(coeff.is_Integer and coeff > 0 for coeff in P.coeffs())
assert P.eval({b:0,c:0}) == 0
assert P.eval({a:1,b:0,c:1}) > 0
assert P.eval({a:1,b:1,c:0}) > 0
# The boundary with one inactive hazard and the two others tied saturates C=2/5.
assert sp.simplify(exact_tau([0,sp.Rational(1,2),sp.Rational(1,2)])) == sp.Rational(1,3)
assert sp.simplify(exact_tau([sp.Rational(1,3)]*3)) == sp.Rational(2,5)
assert sp.simplify(variance.subs({a:0,b:1,c:0})) == sp.Rational(1,6)
for aa,bb,cc in [(1,0,0),(1,2,0),(2,0,3),(1,1,1),(2,3,4),(5,8,13)]:
    v=sp.simplify(G.subs({a:aa,b:bb,c:cc}))
    assert v>=0,(aa,bb,cc,v)
print('PASS: exact rational identity; 40 positive integer monomials; homogeneous degree 8; equality and boundary checks.')
print('Certifier coefficient count:', len(P.terms()))
print('Coefficient-sum check:', sum(P.coeffs()))
print('Boundary tau:', sp.Rational(1,3), 'uniform tau:', sp.Rational(2,5))
