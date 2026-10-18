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

# Reproducible checks and limits

Run `python verify.py` using Python 3 standard library. The checker constructs exact-rational transition matrices for all graph distances for cycles with 3 through 30 vertices, solves for first and second moments by a separate linear system, compares closed forms, tests the Bellman action inequalities and verifies exact generating-function evaluations at selected rational transform arguments. The completed execution reported 1778 passed comparisons. The proof of the uniform Gaussian limit is analytic and rests on the explicit transform and a uniform remainder estimate, not finite tests. Source comparison was restricted to material openly inspected and targeted searches, so earlier equivalent formulations remain a priority risk. No independent audit has been performed.
