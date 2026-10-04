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
The algebraic proof derives the random state matrix directly from the exact scalar quadratic proximal map and then computes the averaged first-moment transition. Its characteristic polynomial factors into one refresh root and one quadratic factor.

`verify.py` reconstructs the two realized transition matrices, averages them, computes the cubic characteristic coefficients from matrix invariants, and compares them with the closed-form factorization over a parameter grid. It then compares the explicit quadratic roots with the closed-form Schur inequality and checks the two displayed \(t=20\) cases.

The executable verification is finite and is used only to detect algebra or transcription errors. The theorem itself is justified by the exact determinant factorization and the Jury criterion. No second-moment, almost-sure, or sample-path verification is claimed.
