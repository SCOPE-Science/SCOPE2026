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
# Verification

The proof uses the exact two-by-two recurrence. The packaged `verify.py` performs four checks: exact rational evaluation of trace and determinant against the matrix entries; exact rational verification of the discriminant numerator; coefficient-level verification of the polynomial identity used to prove monotonicity for the balanced branch; and deterministic numerical probes confirming the location and value of the predicted minima for products on both sides of \(1/2\).

The numerical probes are not used as proofs of the continuum statements. The proof in `RESULT.md` supplies the sign arguments and boundary analysis. The computation assumes ordinary real arithmetic only for the probes and uses exact rational arithmetic for the algebraic sample checks.
