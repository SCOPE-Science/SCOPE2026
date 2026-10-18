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

# Reproducibility

From the directory containing the attached script, run `python dirichlet_log_exceedance_verify.py` with `scipy` and `mpmath` installed. The script independently evaluates beta-score quadrature against a fourth-order finite difference of the regularized incomplete beta distribution, evaluates root signs, compares a small-shape analytic limit to high-precision differentiated incomplete-beta tails, and compares dimension-250 beta-score covariance with the gamma-score tail integral. Expected output: `PASS 139 checks; gamma-alpha-one crossover 1.3714020181784`.

These checks are finite tests and do not provide independent verification or a proof for all parameter values. The analytic proof in RESULT.md establishes the stated quantifiers, the endpoint expansion, the large-shape squeeze, and the growing-dimensional gamma limit. Its growing-dimensional convergence is pointwise at fixed positive scaled threshold; no unproved uniform convergence or shape-monotonicity claim is used.
