"""Reproducible numerical tests for random rectangle support measurements.

Run: python3 check.py  (Python standard library only).
The infinite-dimensional limit and inverse-moment threshold are proved analytically;
these finite experiments are deliberately not offered as their proof.
"""
import math
import random

L = math.pi / 2
R = random.Random(20261016)


def eig_min(angles):
    m = len(angles)
    c = sum(math.cos(2*t) for t in angles)
    s = sum(math.sin(2*t) for t in angles)
    return (m - math.hypot(c, s))/2


def det_gram(angles):
    xx = sum(math.cos(t)**2 for t in angles)
    yy = sum(math.sin(t)**2 for t in angles)
    xy = sum(math.cos(t)*math.sin(t) for t in angles)
    return xx*yy - xy*xy


def det_pairs(angles):
    return sum(math.sin(angles[i]-angles[j])**2
               for i in range(len(angles)) for j in range(i+1,len(angles)))


def unit_ball_volume(d):
    return math.pi**(d/2) / math.gamma(d/2 + 1)


def small_tail_constant(m):
    return math.sqrt(m)*unit_ball_volume(m-1)/L**(m-1)


for m in range(2, 9):
    for j in range(300):
        angles = [R.random()*L for _ in range(m)]
        d = det_gram(angles)
        d2 = det_pairs(angles)
        lam = eig_min(angles)
        assert math.isclose(d, d2, abs_tol=2e-13, rel_tol=5e-13)
        assert -1e-12 <= lam <= m/2+1e-12
        # The other eigenvalue equals m-lambda_min.
        assert math.isclose(d, lam*(m-lam), abs_tol=2e-12, rel_tol=3e-12)

# m=2 exact CDF: positive angle gap has density 2(L-gap)/L^2.
for t in [0.001, 0.03, 0.1, 0.5, 0.95]:
    threshold = math.acos(1-t)
    exact = 2*threshold/L-(threshold/L)**2
    # Independently integrate the angle-gap density with composite midpoint quadrature.
    step = threshold/10000
    numerical = sum(2*(L - (j+0.5)*step)/L**2*step for j in range(10000))
    assert math.isclose(exact, numerical, abs_tol=1e-12)
assert math.isclose(small_tail_constant(2), 4*math.sqrt(2)/math.pi, rel_tol=1e-14)

# Check mean determinant exact formula against a numerical experiment.
for m in [2, 3, 5, 7]:
    n = 20000
    emp = sum(det_gram([R.random()*L for _ in range(m)]) for _ in range(n))/n
    pred = m*(m-1)/4*(1-4/math.pi**2)
    assert abs(emp-pred) <= 0.06*max(1,pred), (m,emp,pred)

# The finite-epsilon rate is compared with its epsilon -> 0 constant.
# Convergence is not exact at finite epsilon and is not used as proof.
for m, eps, samples in [(2,0.03,100000),(3,0.16,100000),(4,0.24,100000)]:
    count = 0
    for _ in range(samples):
        angles = [R.random()*L for _ in range(m)]
        if eig_min(angles) <= eps**2:
            count += 1
    observed = count/samples / eps**(m-1)
    predicted = small_tail_constant(m)
    assert 0.60*predicted <= observed <= 1.35*predicted,(m,observed,predicted)
    print(f"m={m}: scaled empirical tail {observed:.5f}, asymptotic {predicted:.5f}")

# For f(t)=2t/L^2, its m-th density norm relative to uniform is 2^m/(m+1).
for m in range(2, 12):
    density_ratio = 2**m/(m+1)
    assert density_ratio > 1

print('PASS: spectral identities, exact two-point CDF, mean determinants, finite-sample tails.')
