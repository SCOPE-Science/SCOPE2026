#!/usr/bin/env python3
"""Supplementary finite arithmetic checks for a degree-two Bergman kernel transition.
Requires SymPy. Checks are supplemental; the all-parameter theorem has an analytic proof.
"""
from math import comb, ceil, tan, pi
from fractions import Fraction
import sympy as S

x = S.symbols('x')
assertions = 0

def check(flag, desc):
    global assertions
    assert bool(flag), desc
    assertions += 1

# Integer parameter alpha=m. The coefficient series is exactly
# K_m(x)=sum_{n>=0}binomial(2n+m+1,m+1)x^n.
# Multiplication by (1-x)^(m+2) yields a numerator of degree at most m+1.
for m in range(0, 13):
    N = m + 2
    coeffs = []
    for j in range(0, 2*N+9):
        c = sum((-1)**k*comb(N,k)*comb(2*(j-k)+m+1, m+1)
                for k in range(0, min(N,j)+1))
        coeffs.append(c)
    for c in coeffs[N:]:
        check(c == 0, ('tail coefficient',m,c))
    poly = S.Poly(sum(coeffs[j]*x**j for j in range(N)), x)
    # Sturm's theorem counts *distinct real roots* in (-1,0).
    # All roots in the open disk are proved to be negative and simple analytically.
    n_inside = S.Poly(poly,x).count_roots(-1,0) - int(poly.eval(-1) == 0)
    check(n_inside == ceil(m/4), ('negative root count',m, n_inside))
    if m == 0:
        check(poly.as_expr() == 1+x, 'alpha=0 numerator')
    if m == 1:
        check(poly.as_expr() == 1+3*x, 'alpha=1 numerator')
    if m == 2:
        check(poly.as_expr() == 1+6*x+x*x, 'alpha=2 numerator')
    if m == 4:
        check(S.simplify(poly.as_expr().subs(x,-1)) == 0, 'alpha=4 boundary zero')

# Even-binomial closed form at representative noninteger parameters:
# K_s(t)=0.5*((1-sqrt(t))**(-s)+(1+sqrt(t))**(-s)).
# Test both the closed form and the coefficient series at selected interior points.
import mpmath as mp
mp.mp.dps = 75
for alpha in [-mp.mpf('0.8'), -mp.mpf('0.2'), mp.mpf('0.125'), mp.mpf('0.5'),
              mp.mpf('1.5'), mp.mpf('4.01'), mp.mpf('8.3')]:
    s = alpha + 2
    for t in [mp.mpf('-0.15'),mp.mpf('0.2'),mp.mpf('-0.6')]:
        v = mp.sqrt(mp.mpc(t))
        closed = ((1-v)**(-s)+(1+v)**(-s))/2
        coeff_series = mp.nsum(lambda n: mp.rf(s,2*n)*t**n/mp.factorial(2*n),[0, mp.inf])
        check(abs(closed-coeff_series) < mp.mpf('1e-51'), ('closed form', alpha,t))
    if alpha > 0:
        rho = mp.tan(mp.pi/(2*s))**2
        z=1j*mp.sqrt(rho)
        v=((1-z)**(-s)+(1+z)**(-s))/2
        check(abs(v)<mp.mpf('1e-52'), ('predicted smallest zero',alpha))
        check((rho<1), ('inside disk',alpha))
    else:
        rho=mp.tan(mp.pi/(2*s))**2
        check(rho>1, ('outside disk',alpha))
print('PASS: %s finite exact/numerical assertions' % assertions)
