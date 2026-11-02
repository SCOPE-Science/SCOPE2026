"""Independent deterministic finite diagnostics for the affine Fock factor-length theorem.

These numerical assertions supplement, but do not prove, the analytic inequalities.
No external dependencies beyond Python's standard library are required.
"""
import cmath
import math
import random

rng = random.Random(273415)
checks = 0


def assert_close(a, b, tol=2e-10):
    global checks
    assert abs(a-b) <= tol * max(1.0, abs(a), abs(b)), (a, b)
    checks += 1


def c_bound(n, theta):
    if n <= 0 or abs(theta) / n >= math.pi / 2:
        return 0.0
    return math.cos(theta / n) ** n


def min_n(rho, theta):
    assert 0 < rho < 1
    n = 1
    while n < 100000 and rho > c_bound(n, theta) + 2e-15:
        n += 1
    assert n < 100000
    return n


def compose(a, b):
    # Affine pair (slope, intercept); a after b means a(b(z)).
    return (a[0]*b[0], a[0]*b[1] + a[1])


# Boundary classes: exact phase-radius thresholds, including two sharp examples.
for theta, rho, expected in [(math.pi/2, 0.5, 2), (math.pi, 0.125, 3),
                             (0.0, 0.9, 1), (math.pi/2, 0.1, 2)]:
    n = min_n(rho, theta)
    assert n == expected
    checks += 1
    if theta != 0 and abs(rho-c_bound(n,theta)) < 2e-15:
        assert c_bound(n+1, theta) > rho
        checks += 1

# Every product of n one-symbol Toeplitz composition slopes obeys the polar bound.
for n in range(1, 12):
    for _ in range(1600):
        angles = [rng.uniform(-1.53, 1.53) for _ in range(n)]
        slopes = [rng.uniform(0.001, 1.0)*math.cos(t)*cmath.exp(1j*t)
                  for t in angles]
        total = math.prod(slopes)
        principal = cmath.phase(total)
        assert abs(total) <= c_bound(n,principal)+1e-12, (n,total)
        checks += 1
        if abs(total) > 1e-6:
            r = abs(total)
            if r < 1-1e-13:
                assert min_n(r,principal) <= n
                checks += 1

# Realization: identical phase factors; any prescribed translation is obtained
# by putting the entire intercept in the outermost affine factor.
for n in range(1, 10):
    for _ in range(1900):
        theta = rng.uniform(-math.pi, math.pi)
        bound = c_bound(n,theta)
        if bound < 1e-12:
            continue
        rho = (0.005+rng.random()*0.985)*bound
        mu = rho**(1/n) * cmath.exp(1j*theta/n)
        assert mu.real > abs(mu)**2 - 1e-13
        checks += 1
        b = complex(rng.uniform(-1.0,1.0),rng.uniform(-1.0,1.0))
        # Generate symbolic affine maps where one (outermost) has intercept b.
        affine = (1+0j, 0+0j)
        for k in range(n):
            affine = compose((mu,b if k==n-1 else 0j), affine)
        assert_close(affine[0], rho*cmath.exp(1j*theta))
        assert_close(affine[1], b)

# Strict increase of centered threshold for nonzero argument in admissible n.
for theta in [0.2,0.8,1.6,2.4,math.pi]:
    valid = [c_bound(n,theta) for n in range(1,31)]
    for a,b in zip(valid,valid[1:]):
        if a > 1e-12:
            assert b > a
            checks += 1

# Angular blow-up of minimal length near the boundary.
theta = 1.15
for eps in [0.04,0.02,0.01,0.005,0.002]:
    n = min_n(math.exp(-eps),theta)
    leading = theta*theta/(2*eps)
    assert abs(n-leading) < 2.0
    checks += 1

print(f'PASS {checks} deterministic finite assertions')
