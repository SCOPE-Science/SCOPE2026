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

The standalone checker verifies the basis transformation and determinant recurrences for even sizes \(N\in\{4,6,8,10\}\), all allowed mirror-pair positions, and four nonnegative gain/loss strengths including values below and above \(2J\). It uses only the Python standard library and checks matrix entries and characteristic-polynomial coefficients with a stated floating-point tolerance. These finite checks are consistency checks; the proof of the all-size result is the invariant-subspace decomposition and exact determinant recurrence in RESULT.md. No independent validation or audit has been performed.
