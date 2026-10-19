"""Independent reproducibility calculations for the nilpotent boundary return-map coefficient.

Requires Python 3, sympy, scipy. The analytic proof is in RESULT.md; this
script checks polynomial and exact rational integral identities and a
separate finite-amplitude ODE integration. Numerical tests are not a proof.
"""
import math
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.special import beta

C, S, r, u = sp.symbols('C S r u', real=True)
A = C**12 / 3 - S**6
B = C*S**5 + sp.Rational(2, 3)*C**9*S
F = C*S*(3 + C**8)/12
G = sp.groebner([C**4 + 2*S**2 - 1], S, C, order='lex', domain=sp.QQ.frac_field(r))
reduce_curve = lambda e: sp.factor(G.reduce(sp.expand(e))[1])

assert reduce_curve(sp.diff(F, C)*(-S) + sp.diff(F, S)*C**3 - A) == 0
# Verify exact generalized-polar time equations by differentiating X=rC, Y=r^2 S.
radial_time = r**9 * A
angular_time = r*(1-r**7*B)
assert reduce_curve(radial_time*C-r*S*angular_time-(-r**2*S+r**9*C**9/3)) == 0
assert reduce_curve(2*r*S*radial_time+r**2*C**3*angular_time-(r**3*C**3-r**10*S**5)) == 0

A_u = (11*u**3 - 9*u**2 + 9*u - 3)/24
b_u = (11*u**2 - 6*u + 3)/12
f_u = (u**2 + 3)/12
P_u = sp.expand(A_u * (1-u)/2 * b_u * (b_u+7*f_u))
# Formula: I = (integral C^2 dtheta) * E_{Beta(3/4,1/2)}[P(U)].
weighted_average = sp.factor(sum(
    coeff * sp.rf(sp.Rational(3,4), exponent[0]) /
        sp.rf(sp.Rational(5,4), exponent[0])
    for exponent, coeff in sp.Poly(P_u,u).terms()
))
assert weighted_average == sp.Rational(158, 49725)
assert sp.rf(sp.Rational(1,4),3)/sp.rf(sp.Rational(3,4),3) == sp.Rational(15,77)
assert weighted_average > 0

T = math.sqrt(2)*beta(0.25,0.5)
I = math.sqrt(2)*beta(0.75,0.5)*float(weighted_average)
K = 15*T/77
assert abs(I-0.010767997377371438) < 2e-14
assert K>0

# Compare the rigorously obtained rho^22 coefficient against the actual
# nonlinear generalized-polar ODE, without using the asymptotic expansion.
for rho in (0.65,0.70,0.75):
    def rhs(theta, v):
        c,s,rad = v
        aa = c**12/3 - s**6
        bb = c*s**5 + (2/3)*c**9*s
        return (-s, c**3, rad**8*aa/(1-rad**7*bb))
    sol=solve_ivp(rhs,(0,T),(1.,0.,rho),method='DOP853',
                  rtol=2e-13,atol=2e-14)
    assert sol.success
    assert abs(sol.y[0,-1]-1) < 1e-9
    assert abs(sol.y[1,-1]) < 1e-9
    ratio=(sol.y[2,-1]-rho)/rho**22
    assert 0.009 < ratio < 0.012

print('VERIFY_OK: exact polar identities, primitive, beta moments, positive coefficient; numerical ODE cross-check')
print('T=',repr(T),'I=',repr(I),'K=',repr(K),'K/I=',repr(K/I))
