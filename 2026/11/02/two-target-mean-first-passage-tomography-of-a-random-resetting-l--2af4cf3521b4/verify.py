"""Reproducible numerical checks for two-target resetting-source tomography.
Requires only the Python standard library; no external data or services.
Numerical checks corroborate, but do not replace, the measure-theoretic proof.
"""
from math import exp, sqrt, sin, cos, pi, log
from random import Random
from statistics import fmean, stdev

D = 2.0
X0 = -3.0
ANCHORS = (0.0, 2.0)
MU = ((-1.0, 0.2), (0.5, 0.5), (3.0, 0.3))
N_CHECKS = 0


def check(cond, label):
    global N_CHECKS
    if not cond:
        raise AssertionError(label)
    N_CHECKS += 1


def fold_laplace(site, s, law=MU):
    return sum(p * exp(-s * abs(y - site)) for y, p in law)


def mean_time(site, r, law=MU):
    s = sqrt(r / D)
    return (1.0 - exp(-s * abs(X0 - site))) / (r * fold_laplace(site, s, law))


def inferred_transform(site, r):
    s = sqrt(r / D)
    return (1.0 - exp(-s * abs(X0 - site))) / (r * mean_time(site, r))


def cos_view(site, k):
    return sum(p * cos(k * (y - site)) for y, p in MU)


for site in ANCHORS:
    for r in (0.01, 0.1, 0.4, 1.0, 2.5, 9.0, 20.0):
        check(abs(inferred_transform(site, r) - fold_laplace(site, sqrt(r / D))) < 1e-12,
              'transform from mean')

# Two folded-distance cosine views recover the full characteristic function.
a, b = ANCHORS
for k in (0.13, 0.37, 0.9, 1.4, 2.31, 3.5, 5.9):
    d = sin(k * (b - a))
    check(abs(d) > 0.1, 'chosen nonresonant frequency')
    ca, cb = cos_view(a, k), cos_view(b, k)
    real = (ca * sin(k * b) - cb * sin(k * a)) / d
    imag = (cb * cos(k * a) - ca * cos(k * b)) / d
    check(abs(real - sum(p * cos(k * y) for y, p in MU)) < 1e-12,
          'characteristic real part')
    check(abs(imag - sum(p * sin(k * y) for y, p in MU)) < 1e-12,
          'characteristic imaginary part')

# One target is blind to reflection, but the other need not be.
reflect = tuple((2.0 * a - y, p) for y, p in MU)
for s in (0.01, 0.2, 1.0, 2.0, 7.0):
    check(abs(fold_laplace(a, s, MU) - fold_laplace(a, s, reflect)) < 1e-13,
          'one-target reflection ambiguity')
check(abs(fold_laplace(b, 1.0, MU) - fold_laplace(b, 1.0, reflect)) > 0.1,
      'second-target separation')

# Exact polynomial null vector at one rate r=D for targets 0 and 1:
# v=(-1,z,-z,1), z=e^-1, sources at (-1,0,1,2).
z = exp(-1.0)
xs = (-1.0, 0.0, 1.0, 2.0)
v = (-1.0, z, -z, 1.0)
check(abs(sum(v)) < 1e-15, 'finite-data mass nullspace')
for site in (0.0, 1.0):
    check(abs(sum(vi * exp(-abs(xi - site)) for xi, vi in zip(xs, v))) < 1e-15,
          'finite-data kernel nullspace')

# Inverse instability on [0,1]: f_n^pm(y)=1+/-eps*sin(2*pi*n*y).
# Exact sine-Laplace integral is k*(1-exp(-s))/(s*s+k*k).
eps = 0.3
for n in (5, 10, 25, 100):
    k = 2 * pi * n
    for s in (0.5, 1.0, 1.5, 2.0):
        base = -(-1.0 + exp(-s))/s  # (1-e^-s)/s
        integ = k * (1.0 - exp(-s)) / (s*s + k*k)
        plus = base + eps * integ
        minus = base - eps * integ
        check(plus > 0 and minus > 0, 'perturbed Laplace positive')
        check(abs(plus - minus) <= 2*eps/k, 'uniform O(1/n) transform gap')
        check(abs((1.0 / plus - 1.0 / minus)) < 3.0 / n,
              'uniform O(1/n) inverse gap')
check(abs(2 * eps / pi - 0.1909859317102744) < 1e-13,
      'fixed total variation distance')

# Independent event-driven simulation: Brownian point-hitting time is a Levy law.
def simulate(site, rate, n, seed):
    rng = Random(seed)
    positions = tuple(x for x, _ in MU)
    weights = tuple(p for _, p in MU)
    boundaries = [weights[0], weights[0] + weights[1], 1.0]
    out = []
    for _ in range(n):
        pos = X0
        elapsed = 0.0
        while True:
            dist = abs(pos - site)
            if dist == 0.0:
                out.append(elapsed)
                break
            g = rng.gauss(0, 1)
            hit = dist * dist / (2 * D * g * g) if g else float('inf')
            re = -log(max(1e-300, 1.0-rng.random())) / rate
            if hit <= re:
                elapsed += hit
                out.append(elapsed)
                break
            elapsed += re
            u = rng.random()
            pos = positions[0] if u < boundaries[0] else (positions[1] if u < boundaries[1] else positions[2])
    return fmean(out), stdev(out) / sqrt(n)

for j,site in enumerate(ANCHORS):
    rate = 1.3
    observed, se = simulate(site, rate, 30000, 3417+j)
    analytic = mean_time(site,rate)
    check(abs(observed-analytic)<7*se+0.02,'renewal formula independent Monte Carlo')
    print(f'target={site:.1f} simulated={observed:.8f} +/-{se:.8f} analytic={analytic:.8f}')

print('PASS:', N_CHECKS, 'independent deterministic and probabilistic assertions')
