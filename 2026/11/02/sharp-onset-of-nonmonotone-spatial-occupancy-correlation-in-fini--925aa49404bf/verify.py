"""Exact reproducibility checks for finite-patch occupancy correlation theorem.

Requires Python 3.10+ and sympy. All arithmetic here is exact.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

u, v = sp.symbols('u v', positive=True)
A = (1 + u)**2
Z = (1 + u)**3 + 3*u*(1+u)*v + 2*u*v**2
W3 = [1, 3*u, 3*u*(u+v), u*(u+v)*(u+2*v)]
p3 = u*(A+(3*u+2)*v+2*v**2)/Z
q3 = u*(u+v)*(1+u+2*v)/Z
cov3 = u*v*(A+(u+2)*v)/Z**2
rho3 = v*(A+(u+2)*v)/((A+u*v)*(A+(3*u+2)*v+2*v**2))
H = ((1+u)**6 + 2*(1+u)**4*(u+2)*v
     -(1+u)**2*(u*u-4*u-2)*v**2
     -4*u*(1+u)**2*v**3 -2*u*(u+2)*v**4)
B1 = A+u*v
B2 = A+(3*u+2)*v+2*v**2
assert sp.expand(sum(W3)-Z) == 0
assert sp.factor(sum(k*W3[k] for k in range(4))/(3*Z)-p3) == 0
assert sp.factor(sum(k*(k-1)*W3[k] for k in range(4))/(6*Z)-q3) == 0
assert sp.factor(q3-p3**2-cov3) == 0
assert sp.factor(p3*(1-p3)) == sp.factor(u*B1*B2/Z**2)
assert sp.factor(cov3/(p3*(1-p3))-rho3) == 0
assert sp.factor(sp.diff(rho3,v)*B1**2*B2**2-H) == 0
assert sp.factor(sp.diff(p3,v)*Z**2 -
                 2*u*(u**3 + 2*u*u*v + 3*u*u + u*v*v + 4*u*v + 3*u + 2*v+1)) == 0

# Independent stationary law for two habitat patches.
W2 = [1, 2*u, u*(u+v)]
Z2 = sum(W2)
p2 = (W2[1]+2*W2[2])/(2*Z2)
q2 = W2[2]/Z2
rho2 = v/((1+u)*(1+u+v))
assert sp.factor((q2-p2**2)/(p2*(1-p2))-rho2) == 0
assert sp.factor(sp.diff(rho2,v)-(1+u+v)**(-2)) == 0

checks = 0
for n in range(2,7):
    for U,V in product([F(1,6),F(1,3),F(1,2),F(1),F(2),F(5)],
                       [F(0),F(1,7),F(1,2),F(1),F(2),F(3),F(5),F(10)]):
        rates_plus = [(n-k)*(U+k*V) for k in range(n)]
        rates_minus = [k for k in range(n+1)]
        weights = [F(1)]
        for k in range(n):
            weights.append(weights[-1]*rates_plus[k]/rates_minus[k+1])
        # Detailed balance and normalization.
        assert sum(w/sum(weights) for w in weights)==1
        for k in range(n):
            assert weights[k]*rates_plus[k]==weights[k+1]*rates_minus[k+1]
            checks += 1
        K = sum(k*weights[k] for k in range(n+1))/sum(weights)
        JJ = sum(k*(k-1)*weights[k] for k in range(n+1))/sum(weights)
        P = K/n
        Q = JJ/(n*(n-1))
        R = (Q-P*P)/(P*(1-P))
        # Directly compare from independent stationary computation.
        if n in (2,3):
            target = rho2 if n==2 else rho3
            assert R==F(target.subs({u:sp.Rational(U.numerator,U.denominator),
                                     v:sp.Rational(V.numerator,V.denominator)}))
        elif V>0:
            assert R>0  # finite-volume positive association; proof uses Gamma mixture.
        else:
            assert R==0  # independent immigration/death at zero colonization.
        checks += 1

assert rho3.subs({u:1,v:1})==sp.Rational(7,55)
assert rho3.subs({u:1,v:2})==sp.Rational(5,33)
assert rho3.subs({u:1,v:3})==sp.Rational(39,259)
assert sp.Rational(5,33)>sp.Rational(7,55)
assert sp.Rational(5,33)>sp.Rational(39,259)
assert (sp.expand(H).coeff(v,0)>0) is sp.S.true
assert sp.factor(sp.expand(H).coeff(v,0))==(1+u)**6
assert sp.factor(sp.expand(H).coeff(v,1))==2*(1+u)**4*(u+2)
assert sp.factor(sp.expand(H).coeff(v,2))==-(1+u)**2*(u**2-4*u-2)
assert sp.factor(sp.expand(H).coeff(v,3))==-4*u*(1+u)**2
assert sp.factor(sp.expand(H).coeff(v,4))==-2*u*(u+2)
# The above coefficient signs leave one sign change in descending order,
# irrespective of the quadratic coefficient. Descartes + IVT prove one root.

print('PASS: symbolic laws, normalizations, derivative identity and exact 2/3-patch chains;'
      f' {checks} detailed-balance/correlation rational assertions across 240 parameter cases;'
      ' example and quartic coefficients.')
