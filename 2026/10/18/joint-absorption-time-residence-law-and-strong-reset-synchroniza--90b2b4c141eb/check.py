"""Numerical cross-checks for a two-region resetting Brownian occupation law.

Execute: python check.py
Requires numpy and scipy; see requirements.txt.
"""
import math
import random
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

TESTS = 0

def check(condition, label):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(label)


def transform(p, q, a, D=1.0, r=1.0):
    mu = math.sqrt((r + q) / D)
    nu = math.sqrt((r + p) / D)
    den = (r + q * math.cosh(mu * a)) / (r + q)
    den += (p / (r + p)) * (nu / mu) * math.sinh(mu * a)
    return 1.0 / den


def moments(z):
    sh, ch = math.sinh(z), math.cosh(z)
    vu = sh * (sh + 1)
    vl = sh * (sh - z)
    co = (math.sinh(2*z) - sh - z*ch)/2
    return sh, ch - 1, vu, vl, co


def defect(z):
    # Exponential form of E[(U/EU - L/EL)^2].
    # For large z, evaluate using exp(-z) for stability.
    w = math.exp(-z)
    return 4*w*(1 - (1 + z)*w) / ((1-w)**3*(1+w))


def finite_difference_transform(p, q, z, mesh=.01):
    # Independently discretize the nonlocal backward generator.
    k = round(z / mesh)
    check(abs(k * mesh - z) < 1e-12, 'aligned grid')
    n = round((z + 14.0) / mesh)
    matrix = lil_matrix((n+1, n+1), dtype=float)
    rhs = np.zeros(n+1)
    matrix[0, 0] = 1.0
    rhs[0] = 1.0
    v = mesh**-2
    for j in range(1, n):
        penalty = q if j < k else (p if j > k else (p+q)/2)
        matrix[j, j-1] += v
        matrix[j, j] += -2*v - 1.0 - penalty
        matrix[j, j+1] += v
        matrix[j, k] += 1.0
    # Exact asymptotic constant at infinity, up to exp(-14 sqrt(1+p)).
    matrix[n, n] = 1.0
    matrix[n, k] += -1/(1+p)
    solution = spsolve(matrix.tocsr(), rhs)
    return float(solution[k])

rng = random.Random(76491)
for _ in range(160):
    z = rng.uniform(.1, 5.0)
    p = rng.uniform(0.0, 2.5)
    q = rng.uniform(0.0, 2.5)
    f = transform(p,q,z)
    check(0 < f <= 1 + 1e-13, 'Laplace positivity and bound')
    check(transform(0,0,z) == 1, 'normalization')
    check(abs(transform(p,p,z) - (1+p)/(1+p*math.exp(z*math.sqrt(1+p)))) < 1e-13, 'first-passage diagonal')
    check(abs(transform(p,0,z) - math.sqrt(1+p)/(math.sqrt(1+p) + p*math.sinh(z))) < 1e-13, 'upper residence marginal')
    check(abs(transform(0,q,z) - (1+q)/(1+q*math.cosh(z*math.sqrt(1+q)))) < 1e-13, 'lower residence marginal')
    check(transform(p+.05,q,z) < f, 'upper monotonicity')
    check(transform(p,q+.05,z) < f, 'lower monotonicity')
    eu, el, vu, vl, co = moments(z)
    check(vu > 0 and vl > 0 and co > 0, 'positive variances and covariance')
    check(co**2 < vu*vl, 'strict nonsingular covariance')
    mse = vu/(eu**2)+vl/(el**2)-2*co/(eu*el)
    check(abs(mse-defect(z)) < 8e-9 * max(1,abs(mse)), 'exact synchronization defect')

for z,p,q in [(.5,.2,.3),(1,.7,.1),(2,.4,.9),(2,1,1),(1,.3,0),(1,0,.8)]:
    check(abs(finite_difference_transform(p,q,z)-transform(p,q,z)) < 1.0e-5, 'independent generator finite-difference boundary-value solution')

for z in [.3,1.0,2.0,4.0]:
    step = 1.0e-5
    fpp = transform(step,0,z)
    fmm = transform(-step,0,z)
    fqq = transform(0,step,z)
    fqqm= transform(0,-step,z)
    fu, fl, vu, vl, co = moments(z)
    check(abs(-(fpp-fmm)/(2*step)-fu) < 2e-6*max(1,fu), 'upper mean by differentiation')
    check(abs(-(fqq-fqqm)/(2*step)-fl) < 2e-6*max(1,fl), 'lower mean by differentiation')
    h = 3.0e-5
    mixed = (transform(h,h,z)-transform(h,-h,z)-transform(-h,h,z)+transform(-h,-h,z))/(4*h*h)
    check(abs(mixed-(co+fu*fl)) < 3e-5 * max(1,abs(mixed)), 'mixed moment by independent differentiation')

for z in [9,11,13,16]:
    eu, el, vu, vl, co = moments(z)
    check(abs(defect(z)/(4*math.exp(-z))-1) < (1+z)*5*math.exp(-z), 'sharp synchronization rate')
    corr = co / math.sqrt(vu*vl)
    check(abs((1-corr)/(2*math.exp(-z))-1) < (1+z)*7*math.exp(-z), 'sharp correlation defect')
    for s,t in [(.1,.2),(.8,.3),(1.1,1.7),(3.5,.4)]:
        f = transform(s/eu,t/el,z)
        check(abs(f-1/(1+s+t)) < (1+z)*(1+s+t)*5*math.exp(-z), 'joint diagonal exponential limit')

for _ in range(60):
    D = rng.uniform(.3,4.5)
    r = rng.uniform(.2,3)
    a = rng.uniform(.2,2.0)
    p = rng.uniform(.01,1.2)
    q = rng.uniform(.01,1.2)
    z = a*math.sqrt(r/D)
    check(abs(transform(p,q,a,D,r) - transform(p/r,q/r,z)) < 2e-13, 'dimensional normalization')

print(f'PASS: {TESTS} numerical assertions')
