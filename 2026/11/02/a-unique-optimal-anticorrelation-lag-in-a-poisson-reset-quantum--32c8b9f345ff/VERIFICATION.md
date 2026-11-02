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

The proof is in `RESULT.md` and the reproducible diagnostic script is `CHECKER.py`.

Run `python CHECKER.py` with NumPy and SciPy installed. The script independently integrates the stationary exponential-age trigonometric covariance for 30 parameter/lag instances; checks strict sign change around the first positive zero; tests the closed-form global minimizer against a bounded numeric optimization; confirms separation of the static/temporal optima; and compares with a million draws of a stationary Poisson reset-age trajectory. The finite test results only cross-check the algebra.

The infinite-family proof uses the completely positive reset-channel decomposition, conditional product-state means, four elementary Laplace transforms, and a quartic derivative with exactly one positive root. The quantum observable is defined as a two-time regression correlation between distinct factors. The reset-induced temporal joint distribution is not reconstructed by drawing two independent stationary snapshots.

No independent validation or external proof certificate has been performed.
