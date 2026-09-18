import math
import numpy as np


def covariance_block(gamma, alpha, h):
    e1 = math.exp(-gamma*h)
    e2 = math.exp(-2.0*gamma*h)
    A = h/gamma**2 - 2.0*(1.0-e1)/gamma**3 + (1.0-e2)/(2.0*gamma**3)
    B = (1.0-e1)**2/(2.0*gamma**2)
    C = (1.0-e2)/(2.0*gamma)
    return 2.0*gamma*alpha*np.array([[A, B], [B, C]], dtype=float), A, B, C


def analytic_det_unscaled(gamma, h):
    x = gamma*h
    return ((math.exp(x)-1.0) *
            (x*math.exp(x) + x - 2.0*math.exp(x) + 2.0) *
            math.exp(-2.0*x) / (2.0*gamma**4))


gamma = 1.7
alpha = 0.8
d = 5
print(f"gamma={gamma}, alpha={alpha}, d={d}")
print("h        det_relerr      rank    W2opt/asymptotic   spectral_identity")
for h in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    block, A, B, C = covariance_block(gamma, alpha, h)
    det_num = A*C-B*B
    det_exact = analytic_det_unscaled(gamma, h)
    det_rel = abs(det_num-det_exact)/det_exact
    lam_minus, lam_plus = np.linalg.eigvalsh(block)
    Sigma = np.kron(block, np.eye(d))
    rank = np.linalg.matrix_rank(Sigma, tol=1e-13)

    # The optimal rank-d Bures approximation is the spectral truncation:
    # it keeps d copies of lam_plus and discards d copies of lam_minus.
    w2sq = d*lam_minus
    spectral_sum = np.sum(np.sort(np.linalg.eigvalsh(Sigma))[:d])
    spectral_rel = abs(w2sq-spectral_sum)/w2sq
    asym = math.sqrt(d*gamma*alpha/6.0)*h**1.5
    ratio = math.sqrt(w2sq)/asym
    print(f"{h:<8g} {det_rel:12.3e} {rank:8d} {ratio:18.12f} {spectral_rel:18.3e}")

# Two independent scalar normals per coordinate suffice by Cholesky.
h = 0.13
block, _, _, _ = covariance_block(gamma, alpha, h)
L = np.linalg.cholesky(block)
print("\nCholesky reconstruction residual:", np.linalg.norm(L@L.T-block, ord='fro'))
print("Cholesky rank:", np.linalg.matrix_rank(L))
print("smallest block eigenvalue:", np.linalg.eigvalsh(block)[0])
assert np.linalg.eigvalsh(block)[0] > 0
assert np.linalg.matrix_rank(L) == 2
