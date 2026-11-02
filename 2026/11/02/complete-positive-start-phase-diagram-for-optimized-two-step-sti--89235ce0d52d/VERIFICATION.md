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

# Reproduction and evidence boundary

The accompanying `VERIFY.py` uses exact symbolic identities and high-precision recurrence replays; invoke `python VERIFY.py` with Python 3.10+ and SymPy 1.12+. It verifies the source-to-recurrence algebra, factored discriminant, ordering of the sign-change surfaces, boundary values, and positive, singleton, and negative examples in the complete startup phase diagram. The output reports an exact test count. No external computations or unverifiable files are required beyond the documented SymPy dependency.

Finite replays cannot certify the continuous-parameter or all-time statements. Those statements follow from the discriminant sign, explicit second-order recurrence solutions, positive-root eigenvector decomposition, and a trigonometric sign argument in RESULT.md. No independent validation, nonlinear positivity guarantee or finite-precision certification is claimed.
