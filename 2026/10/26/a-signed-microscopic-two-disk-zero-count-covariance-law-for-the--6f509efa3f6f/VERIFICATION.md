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

## Reproducibility
Run `python check.py` with NumPy, SciPy and mpmath. The 29 tests compare the exact all-radius covariance from the Bessel series to the scaled polylogarithmic limit, check the coincident-radius variance, bracket the crossover root, and confirm the predicted covariance signs. The coincident-radius numerical sum includes an explicitly stated asymptotic tail correction to avoid falsely treating truncated infinite sums as complete.

## Proof-dependent checks
The proof reconstructs the Gaussian logarithm identity from the Laguerre expansion, differentiates the Bessel series to obtain the exact zero-count covariance, controls the large-radius expansion with summable uniform remainder estimates, and proves uniqueness of the sign change by a geometric-distribution comparison. These are analytic arguments; numerical checks alone do not prove any infinite statement.

## Limitations
The asymptotic holds for bounded physical radius offsets. It does not address joint limit laws, gaps increasing with radius, or the finite-radius sign exactly at the crossover. Independent validation has not been performed.
