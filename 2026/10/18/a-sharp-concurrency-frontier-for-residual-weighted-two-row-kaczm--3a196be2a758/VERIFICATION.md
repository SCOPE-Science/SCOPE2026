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

The accompanying `verify.py` is standalone and uses Python's standard library rational arithmetic. It directly enumerates finite binomial distributions, checks their equality to the derived quadratic formula, verifies endpoint maxima, and tests prescribed minimizers against finite rational grids. Execution completed successfully with 120482 exact-arithmetic assertions.

All-integer and all-real claims are established by the analytical proof in RESULT.md, not by grid search. The calculation assumes independent sampling conditional on the same initial error, exact addition of worker corrections, and no delayed overlap between distinct batches. No independent mathematical audit has been performed.
