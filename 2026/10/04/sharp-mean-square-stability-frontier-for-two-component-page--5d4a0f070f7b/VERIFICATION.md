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
The analytical proof reconstructs the exact PAGE branch order for \(b=2\), \(b'=1\), \(p=1/3\), scales the estimator by \(\mu\), and derives the closed three-moment recursion.

`verify.py` enumerates all refresh/component branches, checks the displayed moment matrix, verifies the characteristic coefficients and \(P(1)\) factor, tests all four cubic Jury conditions immediately below and above the analytic frontier, and confirms the endpoint values.

The grid checks are transcription guards only. Necessity and sufficiency follow from the exact second-moment recursion and the analytic Jury inequalities in `RESULT.md`.
