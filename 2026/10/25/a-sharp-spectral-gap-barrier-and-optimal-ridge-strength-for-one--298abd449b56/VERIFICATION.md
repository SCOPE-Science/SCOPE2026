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

# Verification and proof scope

The accompanying `verify_ridge_sketch.py` was executed with Python 3, with result `VERIFY_OK 276`. It independently evaluates the exact reduction from trace and determinant to the improvement polynomial for rational parameters; checks the underlying \(2\times2\) matrices on another rational grid; and compares integrated indicator probabilities against the closed arcsine formula. The independent symbolic identities used by the mathematical proof were also factored algebraically, including the discriminant, the two endpoint evaluations, and the derivative-sign identity.

The mathematical proof in `RESULT.md`, not finite grid sampling, establishes the result for every real \(r>1\), \(\ell>0\) and sketch orientation. The probability law additionally requires a continuously uniform orientation. Ties, the exact threshold and the limiting parameter regime are covered analytically.

Scientific limitations: exact arithmetic; two real columns; diagonal positive coefficients (orthogonal changes of coordinates leave the isotropic-sketch distribution unchanged); ridge-augmented conditioning only; one row per sketch. No higher-dimensional or finite-precision claim is asserted. The originality comparison is limited to the inspected accessible literature and searched published records, and independent scientific validation has not been performed.
