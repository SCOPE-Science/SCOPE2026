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
The dimensional analytic proof in `RESULT.md` is the basis for correctness. The attached `verify_joint.py` is supplemental and uses newly sampled volume-uniform points of the five Platonic solids. It checks the predicted bivariate survival probability, support inequality and correlation, with finite-sample tolerances. Monte Carlo agreement is not a proof of the universal theorem and does not constitute external validation. The theorem uses distances to supporting planes, not necessarily to finite facets.
