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

The analytical verification consists of the energy identity, two transversal crossing integrals, uniform replacement error, exact rational moments, strict monotonicity of the rescaled return, and the derivative calculation for the multiplier. All steps are contained in RESULT.md.

The accompanying standalone check.py was executed with Python 3, yielding 13 passed assertions: three exact rational-moment checks; four far-field energy asymptotic checks; four negative-parameter return-sign checks; and two positive/nonnegative-parameter signs. Its assertions test finite radii only, and do not substitute for the proof of asymptotics, uniqueness, or hyperbolicity.

No external or independent validation has been conducted. The 2026 Jia–Meng primary text and the 2026 discontinuous-case bound preprint were not completely available for source-to-source priority comparisons.
