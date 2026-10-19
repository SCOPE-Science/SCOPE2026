#!/usr/bin/env python3
"""Finite companion checks for the two-cell saturating Euler map theorem.

Only rational inequalities in this program are exact; sampled trajectories
are diagnostics rather than proofs of assertions about all real states.
"""
from fractions import Fraction as Q
from math import tanh, atanh, isfinite
from random import Random

A = Q(17, 10)
S = Q(1)
BIAS = Q(3, 10)
HMAX = A + S + BIAS
T = Q(9, 4)
ALPHA = Q(1, 4)

# The full-map forcing bound and the supercritical escape threshold.
assert HMAX == 3
assert T * HMAX / (T - 2) == 27

# At T=2, the two-step difference has a uniform inward increment
# whenever one coordinate is large, despite the neutral affine multiplier.
theta = Q(9, 10)
K = 4 * (A + S)
inward = 4 * (A * theta - S)
assert K == Q(54, 5)
assert inward == Q(53, 25)
assert inward > 0
assert Q(11) > K

# Banach contraction for the equilibrium equation x=A*tanh(x/4)+bias.
L = ALPHA * (A + S)
fixed_radius_bound = BIAS / (1 - L)
assert L == Q(27, 40)
assert fixed_radius_bound == Q(12, 13) < 1

# At the fixed point, d_i=sech^2(x_i/4)/4 lies in [15/64,1/4].
d_min, d_max = Q(15, 64), Q(1, 4)
diag_min = 1 - T + T * A * d_min
diag_max = 1 - T + T * A * d_max
cross_max = T * S * d_max
inf_norm_bound = max(abs(diag_min), abs(diag_max)) + cross_max
assert diag_min == Q(-181, 512)
assert diag_max == Q(-47, 160)
assert cross_max == Q(9, 16)
assert inf_norm_bound == Q(469, 512) < 1


def h(x, alpha):
    u, v = (tanh(alpha * a) for a in x)
    return (1.7*u - v - .3, u + 1.7*v + .3)


def f(x, t, alpha):
    y = h(x, alpha)
    return tuple((1-t)*a + t*b for a,b in zip(x,y))


x = (0.,0.)
for _ in range(100):
    x = h(x,.25)
assert max(abs(x[0]),abs(x[1])) < 12/13
assert max(abs(y-z) for y,z in zip(f(x,2.25,.25),x)) < 2.e-15

rand = Random(271828)
for _ in range(300):
    p = (x[0]+rand.uniform(-1/13,1/13),x[1]+rand.uniform(-1/13,1/13))
    old = max(abs(a-b) for a,b in zip(p,x))
    q = f(p,2.25,.25)
    new = max(abs(a-b) for a,b in zip(q,x))
    assert new <= float(inf_norm_bound)*old + 1e-14

for t in (2.01,2.25,2.5,3.):
    threshold=3*t/(t-2)
    for _ in range(20):
        z=(1.3*threshold*rand.choice([-1,1]),rand.uniform(-threshold,threshold))
        radii=[]
        for n in range(15):
            radii.append(max(map(abs,z)))
            z=f(z,t,rand.uniform(.001,5.))  # changing slope preserves uniform escape comparison
            assert all(isfinite(v) for v in z)
        assert all(b>a for a,b in zip(radii,radii[1:]))

# Outside the supercritical escape radius, the alternating rescaling
# approaches a nonzero limit; its analytic bound comes from a geometric series.
z0 = (40., 0.)
assert max(map(abs,z0)) > 27
rho = 1.25
z = z0
scaled = {}
for n in range(121):
    if n in (50, 120):
        scaled[n] = tuple(v/((-rho)**n) for v in z)
    if n < 120:
        z = f(z, 2.25, .25)
assert max(map(abs, scaled[120])) >= 40 - 27 - 1e-6
assert max(abs(a-b) for a,b in zip(scaled[120],scaled[50])) < 27*rho**(-50) + 1e-7

# Tests close to the endpoint; long transients are possible for small alpha.
for alpha in (.1, .25,1., 8.):
    for start in ((100.,-100.),(-80.,10.),(2.,3.)):
        z=start
        for _ in range(2000):
            z=f(z,2.,alpha)
        assert max(map(abs,z)) < 200

print('PASS: exact-rational constants, equilibrium neighborhood, escape diagnostics, endpoint trajectories')
print('fixed point numerical location:', tuple(round(t,12) for t in x))
print('exact two-step inward margin:', inward)
print('exact local infinity-norm bound:', inf_norm_bound)
