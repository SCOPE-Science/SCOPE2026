#!/usr/bin/env python3
"""Exact Laurent-series and numerical checks of the four-mode Dirichlet normal form."""
import sympy as s
import mpmath as mp

x, u, v = s.symbols('x u v', real=True)
order = 7

def trunc(expr):
    return s.series(s.expand(expr), x, 0, order).removeO().expand()

a = trunc(s.sqrt(1 - 2*x**2 - 3*u**2*x**4 - 4*v**2*x**6))
coeffs = {1: a, 2: x, 3: u*x**2, 4: v*x**3}
q0 = trunc(sum(t*t for t in coeffs.values()))
q = {j: trunc(sum(coeffs[k+j]*coeffs[k] for k in coeffs if k+j in coeffs)) for j in (1,2,3)}
zpoly = {j: q[j] for j in q}
zpoly.update({-j: q[j] for j in q})

# Multiply Laurent polynomials; propagate only coefficients through degree six in x.
product = {0: s.Integer(1)}
constant_exp = s.Integer(1)
for k in range(1,7):
    nxt = {}
    for i, ci in product.items():
        for j, cj in zpoly.items():
            nxt[i+j] = trunc(nxt.get(i+j,0) + ci*cj)
    product = nxt
    constant_exp += product.get(0,0)/s.factorial(k)

logJ = trunc(q0 + s.log(1 + trunc(constant_exp-1)))
checks = {
    0: s.Integer(1),
    2: s.Integer(0),
    4: -(2*u-3)**2/s.Integer(4),
    6: -s.Rational(2,9)*(9*u**2-27*u*v+30*u+9*v**2-6*v-5),
}
for k, target in checks.items():
    assert s.simplify(logJ.coeff(x,k)-target) == 0, (k, logJ.coeff(x,k), target)
assert s.simplify(checks[6].subs(u,s.Rational(3,2)) + s.Rational(1,24)
                  + 2*(v-s.Rational(31,12))**2) == 0

mp.mp.dps = 65
optu, optv = mp.mpf(3)/2, mp.mpf(31)/12
ratios = []
for xx in [mp.mpf('0.012'),mp.mpf('0.006'),mp.mpf('0.003')]:
    aa = mp.sqrt(1-2*xx**2-3*optu**2*xx**4-4*optv**2*xx**6)
    def integrand(k):
        z = mp.e**(2j*mp.pi*k/1024)
        F = aa*z+xx*z**2+optu*xx**2*z**3+optv*xx**3*z**4
        return mp.exp(abs(F)**2)
    mean = sum(integrand(k) for k in range(1024))/1024
    ratio = (1-mp.log(mean))/xx**6
    ratios.append(ratio)
assert abs(ratios[-1] - mp.mpf(1)/24) < mp.mpf('0.001')
assert abs(ratios[-1]-mp.mpf(1)/24) < abs(ratios[-2]-mp.mpf(1)/24)
assert abs(ratios[-2]-mp.mpf(1)/24) < abs(ratios[-3]-mp.mpf(1)/24)
print('VERIFY_OK exact_coefficients=4 resonance_choices=2 high_precision_integrals=3')
print('sixth_order_ratios:',*[mp.nstr(r,15) for r in ratios])
