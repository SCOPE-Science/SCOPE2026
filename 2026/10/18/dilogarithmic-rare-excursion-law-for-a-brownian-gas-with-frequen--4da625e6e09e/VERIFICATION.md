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

# Reproducibility checks
The standalone `verify.py` script evaluates the exact finite-strength stationary product generating function against its dilogarithm limit for three points and four strengths, computes the rate independently by scalar root solving and by one-dimensional Legendre optimization, and checks strict common-clock versus independent-clock inequalities at several parameters. All executable comparisons passed. The exact product identity and rigorous exponential-tilting proof establish the result independently of these finite checks. The calculations do not certify growing-dimensional, variable-threshold, or interaction extensions.
