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

# Checks and limits
The proof verifies Lebesgue invariance from inverse-Jacobian branch weights, constructs independent full-branch control symbols, derives the exact shared-tail covariance and the reflection-principle law, and sums its generating function. The two parity limits follow from the adjacent-binomial identity and summable local central-limit estimates; the integrated variance follows from absolute convergence. This constitutes an analytic infinite-lag argument.

The supplied `CHECK.py` uses only the Python 3 standard library. Run `python3 CHECK.py` in a directory containing that file. It independently compares exact rational expressions from three constructions (reflected-walk law, annealed piecewise-affine Koopman/integral iteration, generating-series coefficients). The completed run reported 24 successful triple comparisons and normalization checks for \(m=2,3,4,5\). These are finite corroboration, not infinite certification.

A complete exhaustive literature search and an independent scientific audit have not been performed. The previously established general polynomial decay exponent is explicitly excluded from the originality claim.
