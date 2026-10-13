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
# Verification and limits

The exact symbolic identities are equations (3)–(10) of RESULT.md and were independently expanded in exact polynomial arithmetic. Matrix positivity, monotonicity, uniqueness, endpoint treatment, and recovery of both point configurations are reasoned in the proof itself. Execute the included dependency-free rational checker using `python artifacts/verify_two_point_simplex.py`; its exact-arithmetic samples check formula reconstruction, all three regimes and both transition scales, with randomized samples testing for computational mistakes.

Such samples **cannot prove** universal optimality. That rests on the reduction to an explicit positive definite quadratic and two global one-variable optimizations. The translated-reference hypervolume equivalence is prior mathematics rather than novelty. No independent audit, external verification or future-study certification is represented.
