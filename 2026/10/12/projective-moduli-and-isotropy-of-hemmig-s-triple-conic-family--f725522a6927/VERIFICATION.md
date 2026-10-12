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

The exact replay script `artifacts/verify.py` uses only the Python standard library. It verifies the six projective pullback identities over the rational-function field \(\mathbb Q(\lambda)\), checks that \(J\) is invariant under all six parameter transforms, proves by coefficient equality the six-factor numerator identity for \(J(\lambda)-J(\mu)\), and checks the fixed-point formulas that yield the three \(C_2\) points and the \(C_3\) locus.

The script is a verifier for the explicit algebraic identities used in the proof; it is not a substitute for the geometric argument that the common point and residual line force the six-permutation exhaustion. That geometric reduction is stated in `RESULT.md` and follows directly from the pairwise intersection pattern of the three conics.

No floating-point approximation, finite-field sampling, or partial enumeration is used to establish the infinite-field claim.
