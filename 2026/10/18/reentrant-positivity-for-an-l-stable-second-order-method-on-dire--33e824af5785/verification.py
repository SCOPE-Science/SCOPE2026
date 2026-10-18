#!/usr/bin/env python3
"""Exact symbolic checks for the cyclic L-stable SDIRK2 positivity theorem."""
from math import comb
import sympy as sp

r, x, t = sp.symbols('r x t')
sqrt2 = sp.sqrt(2)
a = 1 + sqrt2
gamma = 1 - sqrt2 / 2
beta = sqrt2 - 1
assert sp.simplify(beta / gamma - sqrt2) == 0

def H(n):
    return 1 - sqrt2 * sum((r**k for k in range(1, n)), sp.Integer(0)) + a*(n - 1)*r**n

def coeff(n, j, r0):
    return sp.factor((1-r0)**2 * r0**j / (1-r0**n)**2 *
                     (H(n).subs(r, r0) + a*j*(1-r0**n)))

# Check exactly the indicated rational stability symbol.
h = r / (gamma * (1-r))
R = (1 + beta*h*(x-1))/(1-gamma*h*(x-1))**2
R_uniform = (1-r) * (1-a*r+(a-1)*r*x) / (1-r*x)**2
assert sp.simplify(R - R_uniform) == 0
checks = 1

# Bernstein positivity: coefficients on each half of [0,1] strictly > 0.
# Rational-algebraic coefficients, no decimal approximations in assertions.
bernstein_minima = []
expected_min = {
 (2, sp.Rational(0)): 1-sqrt2/4,
 (2, sp.Rational(1,2)): sp.Rational(5,4)-sqrt2/4,
 (3, sp.Rational(0)): 1-sp.Rational(5,12)*sqrt2,
 (3, sp.Rational(1,2)): sp.Rational(5,4)-sqrt2/2,
 (4, sp.Rational(0)): (19-11*sqrt2)/16,
 (4, sp.Rational(1,2)): (44-27*sqrt2)/32,
}
for n in range(2,5):
    for low, high in ((sp.Rational(0), sp.Rational(1,2)),
                      (sp.Rational(1,2), sp.Rational(1))):
        pol = sp.Poly(sp.expand(H(n).subs(r, low+(high-low)*t)), t)
        bs = []
        for j in range(n+1):
            b = sp.simplify(sum((pol.nth(k)*sp.Rational(comb(j,k),comb(n,k))
                                  for k in range(j+1)), sp.Integer(0)))
            assert bool(sp.ask(sp.Q.positive(b))), (n,low,high,j,b)
            bs.append(b)
            checks += 1
        bottom = expected_min[n,low]
        assert any(sp.simplify(b-bottom)==0 for b in bs), (n,low,'no attained minimum')
        assert all(bool(sp.ask(sp.Q.nonnegative(b-bottom))) for b in bs), (n,low,'not lower bound')
        checks += 2
        bernstein_minima.append((n, str(low), str(high), str(bottom)))

witness = sp.simplify(H(5).subs(r, sp.Rational(3,5)))
assert witness == (4097-3108*sqrt2)/3125
assert bool(sp.ask(sp.Q.negative(witness)))
checks += 2
# For n>=5, the successive-dimension decrement at r=3/5 is negative.
for n in range(5,19):
    diff = sp.factor(H(n+1)-H(n))
    assert sp.simplify(diff-r**n*(1-a*n*(1-r))) == 0
    assert bool(sp.ask(sp.Q.negative(diff.subs(r,sp.Rational(3,5)))))
    checks += 2

# Verify exact cyclic resolvent identity at rational arguments, each coefficient.
for n in range(2,12):
    for rv in [sp.Rational(1,7),sp.Rational(2,5),sp.Rational(3,5),sp.Rational(9,10)]:
        C = [coeff(n,j,rv) for j in range(n)]
        assert sp.simplify(sum(C)-1) == 0
        checks += 1
        for j in range(n):
            lhs = C[j]-2*rv*C[(j-1)%n]+rv**2*C[(j-2)%n]
            rhs = (1-rv)*((1-a*rv)*int(j==0)+(a-1)*rv*int(j==1))
            assert sp.simplify(lhs-rhs) == 0,(n,rv,j)
            checks += 1

print('VERIFY_OK', checks, 'exact symbolic/algebraic assertions; Bernstein certificates, cyclic transfer identities, sharp five-cycle witness')
print('BERNSTEIN_MINIMA', bernstein_minima)
