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

# Verification and limits

The exact formula follows analytically from orthogonality of the shift orbit, a two-constraint weighted Cauchy–Schwarz inequality, and strict positivity of the unique equality coefficients. Infinite-degree limits follow from elementary power-sum and convergent-series comparisons. No finite computation is treated as establishing either the infinite family or novelty.

Run the standalone command `python checker.py` with Python 3; no third-party packages are required. It tests exact rational coefficient formulas, normalization, positivity, energy, Euler–Lagrange equalities and comparisons against uniform averaging at multiple finite degrees and integer exponents, plus representative real exponents. The checked exponents and degrees are finite. The program's final printed PASS count is reproducible from the embedded source.

The result is specific to the first-order coboundary of the stated weighted shift. Nonzero residual error above exponent \(3/2\) does not imply the operator is not convex-cyclic. An equivalent formulation in older literature cannot be ruled out absolutely. Independent audit: not performed.
