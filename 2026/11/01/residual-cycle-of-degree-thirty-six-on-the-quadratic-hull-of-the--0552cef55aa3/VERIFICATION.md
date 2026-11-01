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

# Verification of the local Jacobian certificate

The standard-library script `checker.py` was executed directly from this package and returned:

`VERIFY_OK: six quadrics, exact nonzero Jacobian determinant, residual degree 36`

It checks all six quadratic equations at the witness binary form, reconstructs their normal Jacobian from the classical transvectant definition, checks the primitive integer matrix and its nonzero determinant \(-1890000\), and verifies the projective degree arithmetic \(64-28=36\). The standalone global proof uses the cited complete-intersection theorem and elementary geometry of the osculating parametrization; it does not infer global properties from an unbounded finite search. The result has not received an independent mathematical audit.
