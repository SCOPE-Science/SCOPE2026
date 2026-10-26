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

The included standard-library Python checker independently assembles the graph-incidence projection for each ladder with 2 through 11 rungs and compares all coefficients exactly against the analytic block form. It also verifies symmetry, idempotence, every rung-row and rail-row absolute sum, the central extremizer and an attaining sign vector over all sizes from 2 through 22. The observed result was `ALL EXACT CHECKS PASSED: 67101`.

The proof is analytic for every integer size and does not depend on exhausting infinitely many graphs. Computational checks do not independently establish the published-literature priority claim. The checker uses Python's exact rational fractions and needs no additional packages.
