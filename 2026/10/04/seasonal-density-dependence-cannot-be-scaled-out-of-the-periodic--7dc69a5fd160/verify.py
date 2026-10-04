#!/usr/bin/env python3
from fractions import Fraction as F
import sympy as sp

a1 = a2 = F(7,10)
k1 = k2 = F(1)
mu1 = mu2 = F(1,2)
eta1 = F(1,4)
eta2 = F(3,4)

r1 = a1*k1 + mu1
r2 = a2*k2 + mu2
assert r1 == F(6,5)
assert r2 == F(6,5)
alpha = r1*r2
assert alpha == F(36,25)
assert alpha > 1

def hq(w, r, mu, eta):
    return w * (r + mu*eta*w) / (1 + eta*w)

# Source's ratio-free normalized map.
def gq(z):
    return z * (r1 + mu1*z) / (1 + z)

zstar = F(2,5)
assert gq(zstar) == zstar

w1_source = zstar/eta1
w2_source = zstar/eta2
assert w1_source == F(8,5)
assert w2_source == F(8,15)

# Exact contradiction in one step.
w2_actual = hq(w1_source, r1, mu1, eta1)
assert w2_actual == F(8,5)
assert w2_actual != w2_source

z2_actual = eta2*w2_actual
assert z2_actual == F(6,5)
assert z2_actual == (eta2/eta1)*gq(zstar)

# Periodic phase ratios telescope.
assert (eta2/eta1)*(eta1/eta2) == 1

# Symbolic two-step return map.
x = sp.symbols("x", positive=True)
r = sp.Rational(6,5)
mu = sp.Rational(1,2)
e1 = sp.Rational(1,4)
e2 = sp.Rational(3,4)

def hs(z, e):
    return sp.factor(z*(r + mu*e*z)/(1+e*z))

H = sp.factor(hs(hs(x,e1),e2))
expected_H = sp.factor(3*x*(5*x+48)*(5*x**2+80*x+128) /
                       (20*(x+4)*(15*x**2+184*x+160)))
assert sp.simplify(H-expected_H) == 0

P = 225*x**3 + 2960*x**2 + 4480*x - 5632
expected_diff = -x*P/(20*(x+4)*(15*x**2+184*x+160))
assert sp.simplify((H-x)-expected_diff) == 0

Pprime = sp.diff(P,x)
assert sp.expand(Pprime) == 675*x**2 + 5920*x + 4480
# All coefficients of P' are positive for x>0; P(0)<0 and P tends to +infinity.
assert P.subs(x,0) == -5632

roots = sp.nroots(P, n=40)
positive_real = [
    rr for rr in roots
    if abs(float(sp.im(rr))) < 1e-25 and float(sp.re(rr)) > 0
]
assert len(positive_real) == 1
x1 = sp.N(sp.re(positive_real[0]), 25)
x2 = sp.N(hs(x1,e1), 25)
assert abs(float(x1)-0.8039743678767607) < 1e-14
assert abs(float(x2)-0.8705842366428630) < 1e-14

z1 = sp.N(e1*x1, 25)
z2 = sp.N(e2*x2, 25)
assert abs(float(z1)-0.2009935919691902) < 1e-14
assert abs(float(z2)-0.6529381774821472) < 1e-14

print("VERIFY_OK")
print("alpha", alpha)
print("source_normalized_fixed_point", zstar)
print("source_backscaled_pair", (w1_source, w2_source))
print("actual_first_step", w2_actual)
print("correct_normalized_second_value", z2_actual)
print("return_map", H)
print("positive_cycle", (x1, x2))
print("normalized_cycle", (z1, z2))
