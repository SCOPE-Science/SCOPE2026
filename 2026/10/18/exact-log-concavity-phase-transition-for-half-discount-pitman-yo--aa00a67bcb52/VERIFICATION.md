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

# Verification details

The analytic proof is contained in `RESULT.md`. Run `python check.py` with a standard Python installation to recheck the half-discount generalized Stirling recurrence, Lagrange coefficient expression, partition-count probability masses obtained via two independent recurrences, normalization, neighboring-ratio formula, exact strength boundary, and sample witness. The executable reports 19,764 exact-rational checks for sample sizes one through 42 and a separate exact negative-strength counterexample.

These finite calculations do not establish the infinite sample-size theorem; its proof is the explicit rational curvature factorization in `RESULT.md`. The test program has no random sampling and no third-party dependencies. An independent scientific audit has not been performed.
