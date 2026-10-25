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

Execute `python3 verification.py` from the extracted package directory using Python 3.10 or later; the script requires only the standard library. Its output should match `verification_output.txt`, ending with `ALL_CHECKS_PASSED`.

The exact fraction determinant checks independently construct the weighted reduced Laplacian rather than assuming the spectral polynomial. Further exact-rational checks compute grounded inverse matrices to verify the crown-graph missing-edge and present-edge resistance formulas. Deterministic seeded random feasible allocations are compared against the claimed optimum for a range of prices and sizes. Threshold and equal-price identities are also checked numerically.

Finite tests establish neither global uniqueness nor all-size coverage. The analytic argument in RESULT.md proves these conclusions using strict log-determinant concavity, automorphism invariance, exact Laplacian eigenvalues and a quadratic sign analysis. All independently performed external audits remain unperformed.
