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
The package reconstructs constant-step Yogi on a deterministic scalar quadratic.

`verify.py` checks the fixed-state ray, the exact transverse characteristic polynomial, the Jury boundary, the \(-1\) boundary root, the accumulator threshold, and the independence of the first-order transverse spectrum from \(\beta_2\).

Numerical roots are transcription guards. The invariant manifold and sharp threshold follow analytically from the recurrence and Jury inequalities in `RESULT.md`.
