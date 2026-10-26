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

The accompanying pure-Python `check_exact.py` constructs mixed-difference matrices and all active-face orthogonal projectors with exact fractions. The finite computation exhausts \(2\), \(16\), and \(512\) active subsets for square sizes \(2\), \(3\), and \(4\) and verifies every per-cardinality maximum. No sampled or floating-point matrix is substituted for the exhaustive finite enumeration.

The verifier additionally confirms the displayed active-face row, strict KKT multipliers and inactive slacks, and finite-pair attainment. The analysis uses the general polyhedral active-set reduction, proved in RESULT.md, to promote the finite classification to a global nonlinear Lipschitz theorem. This package has not been independently audited; the exact values for larger squares remain undetermined.
