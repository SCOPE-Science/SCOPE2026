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

# Verification scope

The theorem is proved in `RESULT.md` through explicit singularity and normalized-cover computations and an all-extension finite-field character sum. `verify_markoff_cover.py` independently enumerates rational points, quadratic splitting, and the eight branch points over six prime fields \(17,41,73,89,97,113\) and three quadratic fields \(9,25,49\). It checks the stated signed difference and a weight-two upper bound. The final successful output lines are `MARKOFF_EIGHT_NODE_COVER_FINITE_FIELD_CHECKS_PASS` and `MARKOFF_EIGHT_NODE_COVER_EXACT_DISCREPANCY_PASS`.

The tests do not establish the theorem for untested fields. The infinite-field proof and all-extension trace are algebraic. No independent audit or validation has been performed. The geometric isomorphism classification of other K3 models and individual orbit transitivity are outside the claim.
