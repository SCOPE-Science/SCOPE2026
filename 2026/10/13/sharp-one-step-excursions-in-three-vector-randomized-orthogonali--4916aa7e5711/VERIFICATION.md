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

# Verification and reproducibility
Run `python3 verify.py` from a directory containing that file. It uses Python's standard library only and completes with `VERIFY_OK` if all assertions hold.

The checker builds real three-by-three positive-definite rational correlation matrices over a fixed signed grid; for each of 2,351 admitted matrices it independently applies three invertible two-coordinate orthogonalizations, recomputes the complete transformed Gram matrix and inverse using exact cofactors, verifies the pair-drift identity, strict amplification ceiling and at-most-one upward step (7,053 pair transformations total). Five exact rational near-boundary matrices verify the analytic expression \(4/3-h\), and a distinct exact rational matrix verifies one of three pivots increases. This was executed against the included script and returned `VERIFY_OK`.

The universal bounds, strict inequality, full probability frontier, and asymptotic sharpness rely on the displayed analytic proof. A finite rational grid cannot establish global sharpness or exclude unobserved counterexamples. Only an independent external audit could supply independent validation, which has not occurred.
