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

The exact-rational `CHECK.py` checker constructs row Gram matrices, inverts them by fraction-based Gaussian elimination, reconstructs the precise KO error-propagation matrices, and tests the tridiagonal-precision/finite-sweep equivalence for 69 examples. Its three-row tests also calculate the full rank-one squared norm directly as the sum of squared propagation entries and compare it to the exact precision partial-correlation fraction.

The universal claims follow from the proof's projection-kernel rank argument, positive-definite bidiagonal factorization, and three-row Schur-complement identity. Enumerated examples cannot certify statements over all invertible real matrices. Finite precision and tolerance-skipping behavior are outside the theorem.
