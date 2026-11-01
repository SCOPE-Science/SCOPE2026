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

# Reproducibility and limits

Run `python verify.py` with NumPy and SciPy installed. The verifier was executed from this package and printed `VERIFY_OK 3551 checks`.

The tests (a) enumerate every nontrivial or empty sign split for \(4\le m\le15\) and the complete finite rank range, checking the exact binomial face-count formula and balanced maximum; (b) construct sample noncentral sections directly from Haar Gaussian normals in dimensions three through six and check every crossed-edge point against the section hyperplane and the computed convex hull; (c) compare the analytic Hermite-corrected influence variance with independent Gaussian samples for seven offset values; and (d) examine finite-dimensional Gaussian and shifted chi-square normalizations for 2,500 independent experiments at \(m=2400\).

The finite checks are diagnostic. They do not prove the moving-threshold stochastic equicontinuity or any limit as the dimension tends to infinity, which follow analytically from the argument in RESULT.md. The cited central-section special case and empirical-process ingredients are known. Historical priority is not independently certified.
