import math
import numpy as np

SQ33 = math.sqrt(33.0)
zp = (3.0 + SQ33) / 12.0
zm = (3.0 - SQ33) / 12.0
wp = 0.5 - 13.0 * SQ33 / 198.0
Aeq = np.diag([zp, zm])
e = np.array([math.sqrt(wp), math.sqrt(1.0-wp)])

def step(A, e):
    r = A @ e
    Ar = A @ r
    alpha = float(r @ Ar) / float(Ar @ Ar)
    en = e - alpha * r
    rn = A @ en
    return alpha, en, np.linalg.norm(en)/np.linalg.norm(e), np.linalg.norm(rn)/np.linalg.norm(r)

alpha1, e1, er1, rr1 = step(Aeq, e)
alpha2, e2, er2, rr2 = step(Aeq, e1)
assert abs(alpha1 - 1.0) < 5e-14
assert abs(alpha2 + 2.0) < 5e-13
assert abs(er1 - 2.0/math.sqrt(3.0)) < 5e-14
assert abs(er2 - 1.0/math.sqrt(3.0)) < 5e-14
assert abs(rr1 - math.sqrt(2.0/3.0)) < 5e-14
assert abs(rr2 - math.sqrt(2.0/3.0)) < 5e-14
assert np.linalg.norm(e2 - (2.0/3.0)*e) < 5e-14

rng = np.random.default_rng(20260920)
max_ratio = 0.0
violations = 0
spd_increases = 0
trials = 5000
for j in range(trials):
    n = int(rng.integers(2, 12))
    if j % 5 == 0:
        lam = rng.uniform(0.05, 10.0, size=n)
    else:
        lam = rng.uniform(-10.0, 10.0, size=n)
        small = np.abs(lam) < 0.05
        lam[small] = np.where(lam[small] >= 0.0, 0.05, -0.05)
    Q, _ = np.linalg.qr(rng.normal(size=(n,n)))
    A = Q @ np.diag(lam) @ Q.T
    e0 = rng.normal(size=n)
    _, _, q, _ = step(A, e0)
    max_ratio = max(max_ratio, q)
    if q > 2.0/math.sqrt(3.0) + 2e-12:
        violations += 1
    if np.all(lam > 0.0) and q >= 1.0 + 2e-12:
        spd_increases += 1
assert violations == 0
assert spd_increases == 0

# Every absolute spectral condition number t>1 admits a nearby indefinite error increase.
for t in [1.0001, 1.01, 1.1, 2.0, 3.0, 10.0]:
    r0 = t**-3
    r = r0 * (1.0 + 1e-4)
    A = np.diag([1.0, -t])
    et = np.array([1.0, math.sqrt(r)])
    _, _, q, _ = step(A, et)
    assert q > 1.0

# Nonsymmetric contrast: one GMRES(1) step can have unbounded solution-error amplification.
M = 1000.0
An = np.array([[1.0, M], [0.0, 1.0]])
en0 = np.array([0.0, 1.0])
_, _, nonsym_ratio, nonsym_rr = step(An, en0)
assert nonsym_ratio > 400.0
assert nonsym_rr < 0.001

print(f'numpy_version={np.__version__}')
print(f'equality_eigenvalues={zp:.15f},{zm:.15f}')
print(f'equality_positive_weight={wp:.15f}')
print(f'equality_abs_condition={(7.0+SQ33)/4.0:.15f}')
print(f'alpha_sequence={alpha1:.15f},{alpha2:.15f}')
print(f'error_ratio_sequence={er1:.15f},{er2:.15f}')
print(f'residual_ratio_sequence={rr1:.15f},{rr2:.15f}')
print(f'two_step_error_factor={np.linalg.norm(e2)/np.linalg.norm(e):.15f}')
print(f'random_dense_symmetric_trials={trials}')
print(f'random_max_error_ratio={max_ratio:.15f}')
print(f'bound={2.0/math.sqrt(3.0):.15f}')
print(f'random_bound_violations={violations}')
print(f'random_spd_increases={spd_increases}')
print('near_condition_one_indefinite_checks=passed')
print(f'nonsymmetric_M={M:.1f}')
print(f'nonsymmetric_error_ratio={nonsym_ratio:.15f}')
print(f'nonsymmetric_residual_ratio={nonsym_rr:.15f}')
