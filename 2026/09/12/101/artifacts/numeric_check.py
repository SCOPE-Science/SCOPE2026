"""End-to-end audit script for the emergent finding (commuting-Gaussian EOT stability).

Verifies exact Bures-Wasserstein joint-vs-marginal ratios against the claimed
constants C1(r) = 1 + (1 + 4 F*^2) r^2, Ctwo(r) = 2 C1(r), with
F* = sqrt(s*-1)/(sqrt(2) s* (s*+1)), s* = (3+sqrt(33))/6, r = M/eps,
over 2000 randomized commuting trials, n = 1..16, including means and
regularization scales r in [1e-3, 1e3]. Exits nonzero on violation.

Also contains a regression test for the degenerate mean-shift limit:
b = M, a = a' -> 0 with a pure mean shift, where the true
Bures-Wasserstein joint-vs-marginal ratio is exactly 1 (the value 1+r^2
is only the loose triangular-coupling cost there, not a lower bound).
"""
import numpy as np
import sys

SSTAR = (3 + np.sqrt(33)) / 6.0
FSTAR = np.sqrt(SSTAR - 1) / (np.sqrt(2) * SSTAR * (SSTAR + 1))
C1_COEF = 1 + 4 * FSTAR * FSTAR  # = 1.071321... <= 1.0719


def c_of(a, b, e):
    D = np.sqrt(e * e + 4 * a * b)
    return 2 * a * b / (D + e)


def sqrt_spd(A):
    w, Q = np.linalg.eigh((A + A.T) / 2)
    return (Q * np.sqrt(np.clip(w, 0, None))) @ Q.T


def w2g(M0, M1, A, B):
    d = float(np.dot(M0 - M1, M0 - M1))
    As = sqrt_spd(A)
    T = float(np.trace(sqrt_spd(As @ ((B + B.T) / 2) @ As)))
    return d + max(0.0, float(np.trace(A) + np.trace(B) - 2 * T))


def joint(A, B, C, ma, mb):
    n = A.shape[0]
    S = np.zeros((2 * n, 2 * n))
    S[:n, :n] = A
    S[n:, n:] = B
    S[:n, n:] = C
    S[n:, :n] = C.T
    return np.concatenate([ma, mb]), (S + S.T) / 2


def C1_of(r):
    return 1 + C1_COEF * r * r


rng = np.random.default_rng(5)
worst1 = 0.0
worst2 = 0.0
for t in range(2000):
    n = int(rng.integers(1, 17))
    r = 10 ** rng.uniform(-3, 3)
    e, M = 1.0, r
    a = rng.uniform(0.0001, 1.0, n) * M
    ap = rng.uniform(0.0001, 1.0, n) * M
    b = rng.uniform(0.0001, 1.0, n) * M
    bp = rng.uniform(0.0001, 1.0, n) * M
    A, Ap, B, Bp = np.diag(a), np.diag(ap), np.diag(b), np.diag(bp)
    C = np.diag(c_of(a, b, e))
    Cp = np.diag(c_of(ap, b, e))
    C2 = np.diag(c_of(ap, bp, e))
    ma, map_ = rng.normal(scale=5, size=n), rng.normal(scale=5, size=n)
    mb, mbp = rng.normal(scale=5, size=n), rng.normal(scale=5, size=n)
    mS, S = joint(A, B, C, ma, mb)
    mSp, Sp = joint(Ap, B, Cp, map_, mb)
    mS2, S2 = joint(Ap, Bp, C2, map_, mbp)
    C1 = C1_of(r)
    Ct = 2 * C1
    n1, d1 = w2g(mS, mSp, S, Sp), w2g(ma, map_, A, Ap)
    n2, d2 = w2g(mS, mS2, S, S2), w2g(ma, map_, A, Ap) + w2g(mb, mbp, B, Bp)
    if d1 > 1e-300:
        worst1 = max(worst1, n1 / d1 / C1)
    if d2 > 1e-300:
        worst2 = max(worst2, n2 / d2 / Ct)
print(f"C1 coefficient 1+4F*^2 = {C1_COEF:.6f} (F* = {FSTAR:.8f})")
print(f"worst one-sided ratio / C1(r): {worst1:.6f}")
print(f"worst two-sided ratio / Ctwo(r): {worst2:.6f}")

# Regression test: degenerate mean-shift limit. b = M, a = a' tiny and equal,
# pure mean shift d != 0 on the first marginal, second marginal fixed.
# Both joint plans share identical covariances, so the true ratio is 1.
e, M = 1.0, 1.0
for tiny in (1e-6, 1e-8, 1e-10):
    a = np.array([tiny])
    b = np.array([M])
    A = np.diag(a)
    B = np.diag(b)
    Cc = np.diag(c_of(a, b, e))
    mS, S = joint(A, B, Cc, np.array([1.0]), np.array([0.0]))
    mSp, Sp = joint(A, B, Cc, np.array([0.0]), np.array([0.0]))
    num = w2g(mS, mSp, S, Sp)
    den = w2g(np.array([1.0]), np.array([0.0]), A, A)
    ratio = num / den
    print(f"mean-shift limit a=a'={tiny:g}: true ratio = {ratio:.12f} (must be 1)")
    assert abs(ratio - 1.0) < 1e-6, f"mean-shift regression failed at a={tiny}"

if worst1 <= 1 + 1e-9 and worst2 <= 1 + 1e-9:
    print("ALL CHECKS PASSED")
else:
    print("VIOLATION DETECTED")
    sys.exit(1)
