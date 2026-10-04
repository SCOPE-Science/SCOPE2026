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

The proof of the infinite statement is analytic. The accompanying `verify.py` is a finite corroboration of the witness constructions and coefficient-modulus identities, not an exhaustive proof over all moduli.

The verifier checks each integer \(4\le N\le300\). For every claimed zero count, it builds a cubic from an antipodal unit-circle root pair and a third unit root, verifies that all four coefficients have modulus \(1\), evaluates the polynomial at every \(N\)-th root of unity, and confirms the exact predicted zero count within a conservative floating-point tolerance. The parity-excluded three-zero case is proved analytically in `RESULT.md`, not inferred from the finite sweep.

Scientific limits: no claim is made for unequal coefficient magnitudes, nonconsecutive four-point supports, or support aliasing when \(N<4\).
