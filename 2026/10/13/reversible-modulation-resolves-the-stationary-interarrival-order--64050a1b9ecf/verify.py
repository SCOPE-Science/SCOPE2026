#!/usr/bin/env python3
import numpy as np

Q = np.array([
    [-1.0, 1.0, 0.0],
    [ 2.0,-5.0, 3.0],
    [ 0.0, 4.0,-4.0],
])
pi = np.array([8.0,4.0,3.0])/15.0
lam = np.array([1.0,4.0,2.0])
D = np.diag(lam)
A = -Q + D
one = np.ones(3)

assert np.allclose(Q @ one, 0.0)
assert np.allclose(pi @ Q, 0.0)

for i in range(3):
    for j in range(3):
        assert abs(pi[i]*Q[i,j] - pi[j]*Q[j,i]) < 1e-14

lambda_star = float(pi @ lam)
assert abs(lambda_star - 2.0) < 1e-14
alpha = pi*lam/lambda_star
assert np.allclose(alpha, np.array([4.0,8.0,3.0])/15.0)

sqrtpi = np.sqrt(pi)
B = (sqrtpi[:,None]*A)/sqrtpi[None,:]
assert np.allclose(B, B.T, atol=1e-14)

rates, U = np.linalg.eigh(B)
assert np.min(rates) > 0.0

v = sqrtpi
coeff = U.T @ v
weights = coeff*coeff
assert np.min(weights) >= -1e-15
assert abs(weights.sum()-1.0) < 1e-14

def survival_pi(t):
    return float(np.sum(weights*np.exp(-rates*t)))

def survival_alpha(t):
    # S_alpha = <lambda, exp(-At) 1>_pi / lambda_star.
    expBt = U @ np.diag(np.exp(-rates*t)) @ U.T
    # exp(-At)1 corresponds, after symmetrization, to diag(1/sqrtpi) exp(-Bt) sqrtpi.
    y = (expBt @ sqrtpi)/sqrtpi
    return float(np.sum(pi*lam*y)/lambda_star)

def hazard(t):
    z = weights*np.exp(-rates*t)
    return float(np.sum(z*rates)/np.sum(z))

assert abs(hazard(0.0)-lambda_star) < 1e-12

prev = hazard(0.0)
for t in [0.1,0.5,1.0,2.0,3.0]:
    sp = survival_pi(t)
    sa = survival_alpha(t)
    h = hazard(t)
    deriv_relation = h*sp/lambda_star
    assert abs(sa-deriv_relation) < 2e-12
    assert sp > sa
    assert h < prev
    prev = h

# Equal-rate collapse.
lam2 = np.array([2.0,2.0,2.0])
alpha2 = pi*lam2/float(pi@lam2)
assert np.allclose(alpha2, pi)

print(
    "VERIFY_OK "
    f"lambda_star={lambda_star:.12f} "
    f"min_rate={rates.min():.12f} "
    f"hazard_t3={hazard(3.0):.12f} "
    f"gap_t1={survival_pi(1.0)-survival_alpha(1.0):.12f}"
)
