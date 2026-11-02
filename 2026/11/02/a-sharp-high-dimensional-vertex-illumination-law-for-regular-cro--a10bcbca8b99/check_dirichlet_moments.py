"""Symbolic check of Dirichlet moment identities used in the illumination theorem.

Requires SymPy.  Independent verification of fourth-moment cancellation
uses the exact joint factorial-moment formula of uniform Dirichlet laws.
"""
import sympy as sp

d=sp.symbols('d',integer=True,positive=True)
n=d-1

def raw_Y(k):
    # Partitions enumerate distinguishable monomials of (sum T_i^2)^k.
    # The explicit numerators below follow from the Dirichlet factorial rule.
    numerators = {
      0: 1,
      1: 2*n,
      2: 24*n+4*n*(n-1),
      3: 720*n+144*n*(n-1)+8*n*(n-1)*(n-2),
      4: 40320*n+7488*n*(n-1)+576*n*(n-1)*(n-2)
         +16*n*(n-1)*(n-2)*(n-3),
    }
    return (d/sp.Integer(2))**k * numerators[k]/sp.rf(d,2*k)

EY=sp.factor(raw_Y(1))
var=sp.factor(raw_Y(2)-EY**2)
ES2=sp.factor(raw_Y(2)*4/d**2)
central4=sp.factor(sum(sp.binomial(4,k)*(-1)**(4-k)*raw_Y(k) for k in range(5)))
expected_var=(d-1)*(d**2+3*d+6)/((d+1)**2*(d+2)*(d+3))
expected_ES2=4*(d-1)*(d+4)/(d*(d+1)*(d+2)*(d+3))
expected4=(3*d**5+244*d**4-1311*d**3+11324*d**2+4860*d+25200)/sp.prod(d+j for j in range(1,8))
assert sp.simplify(EY-(d-1)/(d+1))==0
assert sp.simplify(var-expected_var)==0
assert sp.simplify(ES2-expected_ES2)==0
assert sp.simplify(central4-expected4)==0
assert sp.limit(d*var,d,sp.oo)==1
assert sp.limit(d**2*central4,d,sp.oo)==3
assert sp.limit(d**2*ES2,d,sp.oo)==4
print('Exact expectation:', EY)
print('Variance:',var)
print('Fourth centered moment:',central4)
print('PASS: symbolic moments and sharp asymptotic orders')
