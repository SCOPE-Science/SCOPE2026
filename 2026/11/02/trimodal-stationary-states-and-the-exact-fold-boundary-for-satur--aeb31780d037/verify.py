"""Standalone checks for the three-peak stationary law in a saturating run-and-tumble process.

Run: python verify.py
Requires: Python 3, sympy, mpmath. This program provides symbolic identities
and finite diagnostic checks; the all-parameter theorem uses the proof in RESULT.md.
"""

import math
import random

import mpmath as mp
import sympy as sp

CHECKS = 0


def check(condition, label):
    global CHECKS
    if not condition:
        raise AssertionError(label)
    CHECKS += 1


v0, v1, gamma0, gamma1, u, t = sp.symbols(
    "v0 v1 gamma0 gamma1 u t", positive=True
)
s = sp.symbols("s", real=True)
A, B, C = sp.symbols("A B C", positive=True)
phi = -3 * A * s**2 + (2 * A - 3 * B - C) * s + A - B - 3 * C

# Directly differentiate the logarithm of the exact stationary density,
# with tanh(3ux) replaced by its triple-angle identity.
source_log_derivative = (
    2 * u * v1**2 * t * (1 - t**2)
    - 2 * (gamma0 * v1 * t + gamma1 * v0 * t * (3 + t**2) / (1 + 3 * t**2))
) / (v0**2 - v1**2 * t**2)
proposed_log_derivative = (
    2 * t * phi.subs({s: t**2, A: u*v1**2, B: gamma0*v1, C: gamma1*v0})
    / ((v0**2 - v1**2 * t**2) * (1 + 3*t**2))
)
check(sp.cancel(source_log_derivative - proposed_log_derivative) == 0,
      "stationary density log derivative")
check(sp.expand(phi.subs(s, 1) + 4*(B+C)) == 0, "endpoint sign")
check(sp.factor(phi.subs(s, 0)) == A - B - 3*C, "central curvature")
check(sp.factor(sp.discriminant(phi, s) -
                (16*A**2 - 8*(3*B + 5*C)*A + (3*B + C)**2)) == 0,
      "fold discriminant")
check(sp.factor(phi.subs(A, B+3*C) -
                s*((5*C-B) - 3*(B+3*C)*s)) == 0,
      "central-threshold polynomial")
check(sp.factor(phi.subs({A: 8, B: 1, C: sp.Rational(13, 5)}) +
                sp.Rational(4,5)*(3*s-1)*(10*s-1)) == 0,
      "exact three-peak witness factorization")
check(sp.factor(phi.subs({A: 8*C, B: 5*C})) == -24*C*s**2,
      "sixth-order critical polynomial")

mp.mp.dps = 45
sample = dict(v0=mp.mpf(3), v1=mp.mpf(1), gamma0=mp.mpf(1),
              gamma1=mp.mpf(13)/15, u=mp.mpf(8), g=mp.mpf(24))


def log_unnormalized_density(x, par):
    v0, v1, gamma0, gamma1, u, g = (par[k] for k in
                       ('v0', 'v1', 'gamma0', 'gamma1', 'u', 'g'))
    integral = mp.quad(lambda y:
        -2*(gamma0*v1*mp.tanh(u*y)+gamma1*v0*mp.tanh(g*y))
        /(v0*v0-v1*v1*mp.tanh(u*y)**2), [0, x])
    return -mp.log(v0*v0-v1*v1*mp.tanh(u*x)**2) + integral


x1 = mp.atanh(1/mp.sqrt(10))/8
x2 = mp.atanh(1/mp.sqrt(3))/8
check(0 < x1 < x2, "ordered off-axis points")
f1 = mp.exp(log_unnormalized_density(x1, sample) -
            log_unnormalized_density(0, sample))
f2 = mp.exp(log_unnormalized_density(x2, sample) -
            log_unnormalized_density(0, sample))
check(f1 < 1 < f2, "distinct three-peak and two-valley heights")
for x, sign in ((mp.mpf('.01'), -1), (mp.mpf('.055'), 1),
                (mp.mpf('.11'), -1)):
    dt = mp.mpf('1e-7')
    numerical = (log_unnormalized_density(x+dt, sample)
                 - log_unnormalized_density(x-dt, sample))/(2*dt)
    ss = mp.tanh(sample['u']*x)**2
    a, b, c = mp.mpf(8), mp.mpf(1), mp.mpf(13)/5
    pol = -3*a*ss**2+(2*a-3*b-c)*ss+a-b-3*c
    predicted = (2*mp.tanh(sample['u']*x)*pol
                 /((sample['v0']**2-sample['v1']**2*ss)*(1+3*ss)))
    check(abs(numerical-predicted) < mp.mpf('1e-10'),
          "density derivative agrees with stationary formula")
    check(sign*numerical > 0, "sample derivative has prescribed sign")

# Randomized tests only corroborate the analytically proved sign diagram.
rng = random.Random(20241028)
for i in range(100):
    b = mp.mpf(rng.randint(1, 30))/10
    c = mp.mpf(rng.randint(1, 30))/10
    ac = b + 3*c
    af = (3*b + 5*c + 2*mp.sqrt(6*c*(b+c)))/4
    if b < 5*c:
        a = (af+ac)/2 if i%2 else af/2
        expected = 2 if i%2 else 0
    else:
        a = ac*(mp.mpf('1.3') if i%2 else mp.mpf('0.7'))
        expected = 1 if i%2 else 0
    l = 2*a - 3*b - c
    q = a-b-3*c
    disc = l*l+12*a*q
    roots = [] if disc < 0 else [(l-mp.sqrt(disc))/(6*a),
                                    (l+mp.sqrt(disc))/(6*a)]
    actual = sum(1 for r in roots if r > mp.mpf('1e-15') and r < 1)
    check(actual == expected, "root-count diagnostic")

print("PASS:", CHECKS, "symbolic and numerical checks")
print("Exact witness interior stationary points:")
print("  x_min =", mp.nstr(x1, 18), "; p(x_min)/p(0) =", mp.nstr(f1, 18))
print("  x_max =", mp.nstr(x2, 18), "; p(x_max)/p(0) =", mp.nstr(f2, 18))
