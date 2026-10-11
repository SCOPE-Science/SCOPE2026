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

Verification uses only Python 3 standard-library arithmetic. Execute `python3 artifacts/verify.py` from the report directory. For nine prime-power/exponent parameter cases, the script constructs fields from specified irreducible polynomials, checks every ordered-pair addition fiber, verifies the exact number and size of root-of-unity orbits, and evaluates the integer-amplitude deficit algebraically. It also checks phase equality for trace-quadratic examples and tests non-affinity for all nonplanar cases; direct Fourier sums are compared to convolution fourth moments on the small fields.

Expected final marker: `VERIFY_OK field_parameter_cases=9 exact_collision_and_deficit=all nonlinear_phase=all_nonplanar direct_Fourier=small_cases`.

These checks are finite corroboration only. The arbitrary-field proof uses additive-character orthogonality, the Frobenius midpoint identity, the multiplicative-root orbit partition, a finite exact variance identity, and an elementary gcd identity, and a real additive-Fourier proof that nonplanar phase constraints have only constant infinitesimal solutions. Full classification of nonplanar phase solutions in a closed parametric form is not asserted.
