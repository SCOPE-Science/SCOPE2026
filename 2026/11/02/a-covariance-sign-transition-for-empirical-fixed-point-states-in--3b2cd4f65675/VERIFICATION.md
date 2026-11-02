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

The independent deterministic program `verify.py` was executed successfully under Python 3 and tests exact rational-mass recurrences for the finite Ewens singleton-count chain, analytic root signs, monotonic root order, known benchmark roots, the zero-parameter integral, and the large-d root scale. Composite Simpson quadrature and bisection are numerical checks; the exact rational recurrences verify finite-size identities. All tests were run from the packaged source file, not from a previous artifact. Mathematical validity of arbitrary-n and arbitrary-d limits rests on the explicit proof in RESULT.md, not on the program. The self-review was passed; independent mathematical assessment was not performed.
