import math
import platform
import numpy as np

SEED = 20260921
rng = np.random.default_rng(SEED)

def sharp_bound(kappa):
    return (kappa - 1.0) / (2.0 * math.sqrt(kappa))

def cg_ratios(A, r0):
    r = r0.astype(float).copy()
    p = r.copy()
    ratios = []
    n = A.shape[0]
    for _ in range(n):
        rr = float(r @ r)
        if rr <= 1e-28:
            break
        Ap = A @ p
        den = float(p @ Ap)
        alpha = rr / den
        rn = r - alpha * Ap
        rrn = float(rn @ rn)
        ratios.append(math.sqrt(max(rrn, 0.0) / rr))
        if rrn <= 1e-28:
            break
        beta = rrn / rr
        p = rn + beta * p
        r = rn
    return ratios

def equality_case(kappa):
    mu, L = 1.0, float(kappa)
    A = np.diag([mu, L])
    r0 = np.array([math.sqrt(L/(L+mu)), math.sqrt(mu/(L+mu))])
    ratio = cg_ratios(A, r0)[0]
    return ratio, sharp_bound(kappa)

print('python', platform.python_version())
print('numpy', np.__version__)
print('seed', SEED)
print('equality family:')
for kappa in [2.0, 3.0 + 2.0*math.sqrt(2.0), 10.0, 100.0]:
    ratio, bound = equality_case(kappa)
    print(f'  kappa={kappa:.15g} ratio={ratio:.15g} bound={bound:.15g} abs_err={abs(ratio-bound):.3e}')
    assert abs(ratio - bound) < 2e-13 * max(1.0, bound)

threshold = 3.0 + 2.0*math.sqrt(2.0)
print(f'threshold={threshold:.15g}')
for kappa in [5.0, threshold, 6.0]:
    ratio, bound = equality_case(kappa)
    print(f'  threshold-check kappa={kappa:.15g} equality_ratio={ratio:.15g} nonincrease={ratio <= 1.0 + 1e-13}')

# Random exact-formula sanity checks in floating point.  Matrices are generated
# with eigenvalues exactly prescribed in [1,kappa] before an orthogonal rotation.
max_ratio_over_bound = 0.0
worst = None
cases = 0
for n in [3, 5, 10, 20]:
    for kappa in [1.1, 2.0, 5.0, threshold, 10.0, 100.0]:
        eigs = np.geomspace(1.0, kappa, n)
        bound = sharp_bound(kappa)
        for _ in range(100):
            Q, _ = np.linalg.qr(rng.normal(size=(n,n)))
            A = (Q * eigs) @ Q.T
            r0 = rng.normal(size=n)
            ratios = cg_ratios(A, r0)
            for j, ratio in enumerate(ratios):
                # Ignore ratios after the residual has fallen into a roundoff-dominated
                # regime; the theorem being checked is an exact-arithmetic statement.
                if not np.isfinite(ratio):
                    continue
                q = ratio / bound if bound > 0 else 0.0
                if q > max_ratio_over_bound:
                    max_ratio_over_bound = q
                    worst = (n, kappa, j, ratio, bound)
                # Loose tolerance only guards floating-point evaluation of an exact theorem.
                assert ratio <= bound * (1.0 + 2e-8) + 2e-12
            cases += 1
print('random cases', cases)
print('max ratio/bound', f'{max_ratio_over_bound:.15g}')
print('worst', worst)

# Inverse conditioning certificate: q <= (kappa-1)/(2 sqrt(kappa))
# rearranges to kappa >= (q + sqrt(1+q^2))^2.
for q in [0.25, 1.0, 2.5]:
    kmin = (q + math.sqrt(1.0 + q*q))**2
    recovered = sharp_bound(kmin)
    print(f'certificate q={q:.8g} kappa_min={kmin:.15g} recovered_bound={recovered:.15g}')
    assert abs(recovered - q) < 2e-13 * max(1.0, q)

print('PASS')
