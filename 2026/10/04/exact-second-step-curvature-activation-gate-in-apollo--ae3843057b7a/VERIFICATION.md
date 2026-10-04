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
The package verifies Apollo's exact second-step curvature-activation gate on a scalar quadratic.

`verify.py` reconstructs Algorithm 1 through the second Hessian update, compares the direct recurrence with the closed forms for \(x_1\), \(m_2\), \(B_2\), and \(x_2\), and tests both sides of the sharp condition \(q=1+\beta\) over randomized parameters.

The finite checks are transcription guards. The activation dichotomy and threshold are proved analytically in `RESULT.md`.
