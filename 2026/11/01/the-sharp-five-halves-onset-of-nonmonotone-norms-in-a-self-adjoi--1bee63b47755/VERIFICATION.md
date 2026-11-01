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

The proof derives exact eigenvalues, the derivative-sign identity, a unique stationary-root equation, and a global asymptotic reduction. These are algebraic and analytical statements covering the full indicated real parameter ranges. The assertion about the critical coefficient depends on the uniform-in-\(b\) localization and differentiated square-root remainder, not on a finite grid.

Run `python3 checker.py` next to this file to reproduce independent finite consistency calculations. The checker uses only Python's standard library and returns a PASS count; it tests finitely many parameter values, checks a rational polynomial identity, and examines the predicted small-parameter limit. These computations are supportive and cannot establish the all-parameter monotonicity theorem or the limit by themselves.

No external independent audit or mathematical validation has been performed.
