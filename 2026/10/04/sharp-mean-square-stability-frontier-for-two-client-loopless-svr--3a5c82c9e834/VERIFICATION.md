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
The analytical proof derives the exact branch-averaged second-moment matrix for the original pre-step-refresh Loopless SVRG convention.

`verify.py` performs three independent checks: exact rational branch enumeration against the matrix recurrence; exact rational verification of the determinant identity
\[
\det(I-N)=\frac{\alpha}{4}\left[2+\alpha-(1+4h^2)\alpha^2\right];
\]
and a deterministic grid test of all four cubic Jury inequalities immediately below and above the claimed frontier.

The grid tests are not used as proof of stability. The necessary-and-sufficient result follows from the exact moment recursion and the analytic Jury inequalities in `RESULT.md`.
