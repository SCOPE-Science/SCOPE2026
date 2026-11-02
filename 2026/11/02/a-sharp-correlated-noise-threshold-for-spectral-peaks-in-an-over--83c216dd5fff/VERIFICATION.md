---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytic proof in `RESULT.md` applies to every positive \(a,b,k,D_x,D_y\), every \(-1<\rho<1\), and every real \(\omega\). The positive-definite forcing covariance guarantees the stationary system is nondegenerate. The scalar spectral derivative has a strictly decreasing polynomial numerator on \(z\ge0\); no finite sampling or optimizer is used to certify the global claim.

Execute `python verify.py` from the directory containing `verify.py`, with NumPy and SciPy installed. The checker independently forms the complex transfer matrix and noise covariance, compares the exact spectral expression; independently solves the stationary Lyapunov equation and propagates it by matrix exponentials, comparing the exact autocovariance; and checks the maximizing-frequency classification. The checker has 3,058 randomized and exact cross-check assertions in its current deterministic seeded configuration.

The program is finite numerical corroboration, not a symbolic or infinite-case proof. The proof is self-contained and separately establishes the boundary at equality, the tuned coupling maximizing the correlation threshold, and the exactly-one covariance sign crossing. Exact historical priority and physical generalization outside the model remain unproved. No independent scientific audit has been performed.
