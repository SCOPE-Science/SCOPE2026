"""Numerical support for a three-node spectral condition-number asymptotic.
This checks finite examples only; the analytic global minimax proof is separate.
Requires Python 3 and NumPy.
"""
import math
import numpy as np

PI = math.pi
C = PI * (1 + math.sqrt(3)) / 3
omega = np.exp(2j * PI / 3)
D = np.diag([1, omega**2, omega])


def matrix(n, t):
    rows = np.array([0, 1, n], dtype=float)
    cols = np.arange(3, dtype=float)
    return np.exp(2j * PI * rows[:, None] * (t * cols[None, :]))


def squared_condition(n, t):
    v = matrix(n, t)
    sv = np.linalg.svd(v, compute_uv=False)
    return (sv[0] / sv[-1])**2


def candidate_t(n):
    if n % 3 == 2:
        return 1 / 3
    s = -1 if n % 3 == 0 else 1
    return 1 / 3 + s / (3*n) + s / (6*n*n)


def H(a, d):
    return np.array([[0., -d, a],[-d, 0., d-a],[a, d-a, 0.]])


checks = 0
for n in [5,8,11,14,17,20,101,302]:
    v = matrix(n, candidate_t(n))
    np.testing.assert_allclose(v.conj().T @ v, 3*np.eye(3), atol=1e-10)
    checks += 1
for n in [3,4,6,7,9,10,30,31,60,61,90,91,300,301,600,601,1200,1201]:
    t = candidate_t(n)
    ratio = squared_condition(n,t)
    assert ratio > 1.0
    err = abs(n*(ratio-1) - C)
    if n >= 30:
        assert err < 7/n + .002, (n,ratio,err)
    checks += 1

# Verify the exact first-order Gram derivative in representative branches.
for n in [30,31,300,301,900,901]:
    s = -1 if n%3 == 0 else 1
    d = s*2*PI/3
    a = d/2
    t = candidate_t(n)
    v = matrix(n,t)
    gram = v @ v.conj().T
    v = matrix(n,t).T
    gram = v.conj().T @ v
    spread = np.linalg.eigvalsh(gram)[-1] - np.linalg.eigvalsh(gram)[0]
    lin = math.sqrt(3)/n *(3+math.sqrt(3))*abs(d)/2
    assert abs(spread/lin - 1) < 4/n
    checks += 1

# The local minimax Hessian has a convex spectral spread and reflection symmetry.
for d in [-2*PI/3, 2*PI/3, 4*PI/3]:
    center = d/2
    e = np.linalg.eigvalsh(H(center,d))
    expected = (3+math.sqrt(3))*abs(d)/2
    assert abs((e[-1]-e[0]) - expected)<1e-12
    for a in np.linspace(-2*abs(d), 3*abs(d), 53):
        ee = np.linalg.eigvalsh(H(a,d))
        assert ee[-1]-ee[0] >= expected -1e-10
        checks +=1

print('VERIFY_OK', checks, 'finite checks; C=', repr(C))
