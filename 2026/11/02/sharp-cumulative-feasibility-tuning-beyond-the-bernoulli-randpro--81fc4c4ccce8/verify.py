#!/usr/bin/env python3
"""Exact symbolic and rational checks for the stated scalar RandProx-LC theorem."""
from fractions import Fraction as F
from itertools import product
import sympy as s

a, p, mu, x, u, tau, bit = s.symbols('a p mu x u tau bit', positive=True)
gamma = 1 / mu
# Reconstruction of Algorithm 4 from its four scalar updates.
xhat = x - gamma * mu * x - gamma * u
u_next = u + tau * p * (bit / p) * xhat
x_next = xhat - gamma / p * (u_next - u)
assert s.simplify(xhat + gamma * u) == 0
assert s.simplify(u_next.subs(tau, a / gamma) - (1-a*bit)*u) == 0
assert s.simplify(x_next.subs(tau, a / gamma) + gamma*(1-a*bit/p)*u) == 0
Q = (1-p)*1**2 + p*(1-a)**2
C = (1-p)*1**2 + p*(1-a/p)**2
assert s.simplify(Q - (1-p*a*(2-a))) == 0
assert s.simplify(C - (1-2*a+a*a/p)) == 0
S = s.factor(C/(1-Q))
G = (1-p)*a*a+p*a-p
assert s.simplify(s.diff(S,a)-2*G/(p*p*a*a*(2-a)**2)) == 0
assert s.simplify(G.subs(a,p)+p*(1-p)**2) == 0
assert s.simplify(G.subs(a,1)-(1-p)) == 0
A = 2*s.sqrt(p)/(s.sqrt(p)+s.sqrt(4-3*p))
assert s.simplify(G.subs(a,A)) == 0
assert s.simplify(S.subs(a,p) - (1-p)/(p*p*(2-p))) == 0
assert s.simplify(S.subs(a,1) - (1-p)/(p*p)) == 0
# Leading asymptotic constants are exactly 1, 1/2 and 1.
assert s.limit(A/s.sqrt(p),p,0,dir='+') == 1
assert s.limit(S.subs(a,A)*p**s.Rational(3,2),p,0,dir='+') == 1
assert s.limit(S.subs(a,p)*p*p,p,0,dir='+') == s.Rational(1,2)
assert s.limit(S.subs(a,1)*p*p,p,0,dir='+') == 1
# Each of the 96 parameter/horizon cases enumerates every Bernoulli path.
count = 0
for prob in [F(1,3),F(1,2),F(3,4),F(1)]:
    for step in [F(1,4),F(3,4),F(1),F(3,2)]:
        qq = 1-prob*step*(2-step)
        cc = 1-2*step+step*step/prob
        for n in range(1,7):
            ue, xe = F(0), F(0)
            for word in product((0,1),repeat=n):
                ud, xd, weight = F(1), F(3,7), F(1)
                for sample in word:
                    weight *= prob if sample else 1-prob
                    xd = -(1-step*sample/prob)*ud
                    ud = (1-step*sample)*ud
                ue += weight*ud*ud
                xe += weight*xd*xd
            assert ue == qq**n
            assert xe == cc*qq**(n-1)
            count += 1
print(f'VERIFY_OK exact source stages, symbolic frontier and optimizer, {count} exhaustive rational Bernoulli trees')
