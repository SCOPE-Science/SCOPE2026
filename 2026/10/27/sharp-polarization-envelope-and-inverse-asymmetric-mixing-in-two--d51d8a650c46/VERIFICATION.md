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

Execute `python verify.py` with Python 3.10 or later and the standard library. The program checks six high-precision rational mixing/contrast configurations with both optimizing stimulus orientations, including independently recovered directed weights, checks exact Jacobian stability signs, surveys 2,000 logit secant inequalities and 999 monotonicity samples, and checks disassortative sign conditions. The critical scalar comparison is checked using an explicit Runge–Kutta integration of the invariant one-dimensional subsystem.

The analytic proof in RESULT.md, not finite computation, establishes the theorem for every allowed parameter and initial state. Numerical integration tests an example of the critical coefficient and is not a proof of the limiting law. The historical literature comparison is documented separately; calculations make no originality guarantee. No independent scientific audit or external verification was performed.
