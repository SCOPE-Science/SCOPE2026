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
The package verifies the exact period-two orbit and two-step Floquet polynomial for the scalar \(n=1\) asynchronous AdaShift recurrence.

`verify.py` checks exact state substitution, compares analytic one-step Jacobians with finite differences, verifies the characteristic polynomial, tests both sides of the sharp \(2\varepsilon<\alpha\lambda<4\varepsilon\) stability window, and checks the exact zero-epsilon multiplier modulus \(2-\beta_2\).

The finite computations are transcription guards. Existence and stability are proved analytically in `RESULT.md`.
