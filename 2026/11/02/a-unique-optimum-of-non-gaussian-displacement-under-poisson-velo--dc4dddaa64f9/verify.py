#!/usr/bin/env python3
"""Independent algebraic and numerical checks of the stated velocity-reset result."""
from sympy import symbols, factor, diff, Rational, expand, simplify, Poly, exp, integrate, oo
from mpmath import mp

r, D, g = symbols('r D g', positive=True)
z = symbols('z', positive=True)
H = 6*z*(7*z*z + 28*z + 27)/((z+1)*(z+2)*(z+3)*(z+4))
P = 7*z**6+56*z**5+116*z**4-160*z**3-959*z**2-1344*z-648
assert factor(diff(H,z)+6*P/((z+1)**2*(z+2)**2*(z+3)**2*(z+4)**2)) == 0
assert Poly(P,z).all_coeffs() == [7,56,116,-160,-959,-1344,-648]
assert P.subs(z,Rational(2556536,1000000)) < 0
assert P.subs(z,Rational(2556537,1000000)) > 0

# Normalized OU excursion q(t) at gamma=D=1. Exponential moments
# are reconstructed by expanding polynomial and e^{-jt} terms.
from sympy import integrate
s = symbols('s', positive=True)
q = 2*(s-Rational(3,2)+2*exp(-s)-exp(-2*s)/2)
expect = lambda f: integrate(r*exp(-r*s)*expand(f), (s,0,oo))
Eq = 4/(r*(r+1)*(r+2))
Etq = 4*(4*r**2+9*r+4)/(r**2*(r+1)**2*(r+2)**2)
Eq2 = 32*(10*r**2+25*r+12)/(r**2*(r+1)**2*(r+2)**2*(r+3)*(r+4))
assert factor(expect(q) - Eq) == 0
assert factor(expect(s*q) - Etq) == 0
assert factor(expect(q*q) - Eq2) == 0
c = factor(r*Eq)
K4 = factor(3*r*(Eq2 - 2*c*Etq+c**2*2/r**2))
formula_K4 = 96*r*(7*r**2+28*r+27)/((r+1)**3*(r+2)**3*(r+3)*(r+4))
assert factor(K4-formula_K4) == 0
assert factor(r*Eq-4/((r+1)*(r+2))) == 0
assert factor(K4/c**2-H.subs(z,r)) == 0

# Independent polynomial tilted-generator recursion for the eigenvalue
# of the velocity-reset generator plus k*v, to order k^4.
a = 1/((r+g)*(r+2*g))
lam2 = 2*D*a
b = a/(r+3*g)
c3 = (6*D*b-lam2/(r+g))/(r+g)
d = b/(r+4*g)
e = (12*D*d+c3-lam2*a)/(r+2*g)
lam4 = factor(2*D*e)
exact_K4general = 96*D**2*r*(7*r*r+28*r*g+27*g*g)/((r+g)**3*(r+2*g)**3*(r+3*g)*(r+4*g))
assert factor(24*lam4-exact_K4general) == 0
assert factor(2*lam2-4*D/((r+g)*(r+2*g))) == 0

mp.dps = 55
for gv,rv,Dv in [(1,0.1,1),(1,1,1),(1,2.5,2),(0.4,2.3,0.7),(5,3,1.1),(2.6,0.03,4.3)]:
    gg,rr,dd=mp.mpf(str(gv)),mp.mpf(str(rv)),mp.mpf(str(Dv))
    qn=lambda t: 2*dd/gg**2*(t-2*(-mp.expm1(-gg*t))/gg+(-mp.expm1(-2*gg*t))/(2*gg))
    cn=4*dd/((rr+gg)*(rr+2*gg))
    integrand=lambda t: rr*mp.exp(-rr*t)*(qn(t)-cn*t)**2
    k_num=3*rr*mp.quad(integrand,[0,1/rr,5/rr,mp.inf])
    k_exact=96*dd**2*rr*(7*rr**2+28*gg*rr+27*gg**2)/((rr+gg)**3*(rr+2*gg)**3*(rr+3*gg)*(rr+4*gg))
    assert mp.almosteq(k_num,k_exact,rel_eps=mp.mpf('1e-38')), (gv,rv,Dv,k_num,k_exact)
root=mp.findroot(lambda x:7*x**6+56*x**5+116*x**4-160*x**3-959*x**2-1344*x-648,(mp.mpf('2.5'),mp.mpf('2.6')))
assert mp.mpf('2.556536')<root<mp.mpf('2.556537')
print('ALL PASS: symbolic renewal moments, independent tilted-generator recursion,')
print('positive-root certificate, derivative factorization, and six quadratures')
print('beta_star=',mp.nstr(root,17),'H_max=',mp.nstr(6*root*(7*root**2+28*root+27)/((root+1)*(root+2)*(root+3)*(root+4)),17))
