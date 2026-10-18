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

Run `python3 verify_rank_one.py` with Python 3.10 or newer. Only the Python standard library is required. The verification code accompanies these documents as a standalone file and prints `VERIFY_OK` if all checks succeed. It was executed successfully against the prepared mathematical formulas.

The checker verifies the exact rational Gram determinant \(4/45\) and spherical-ball trace \(8/15\). It tests the closed prolate and oblate moment recurrences against 36 independent Simpson quadratures, reconstructs the two-dimensional Gram-eigenvalue ratio, and independently computes 280 section areas by restricting the ellipsoid quadratic form to a plane rather than reusing the affine section formula. It checks the near-ball quadratic response for both axial deformation types and the high-axis-ratio prolate and oblate limiting constants.

These are finite consistency checks, not an exhaustive search over all ellipsoids or a proof of asymptotic limits. All universal claims follow from the exact affine section-area formula, the two-function singular-value reduction, Cauchy–Schwarz, spherical fourth moments and one-dimensional dominated convergence and recurrences as written in RESULT.md. Independent audit has not been performed.
