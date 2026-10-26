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

# Reproducibility

Execute `python verify.py` with Python 3 and the standard library; compare stdout against `verification_output.txt`. This exact-rational script recomputes the stationary embedded and physical-time distributions, all fresh-entrance passage-time entries, the stationary-observation means for both destination-mark assignments, their \(15/7\) and \(17/7\) weighted sums, and the unit squared coefficients of variation. It checks 64 independent-marked three-state comparison kernels with varying rational parameters. The previously executed run ended `All assertions passed.`

The Gamma law is fixed by shape \(5/3\) with conditional scales \(3/5\) and \(9/5\); these imply the first and second moments recorded in RESULT.md. The analytical proof establishes the general identity and the two-state boundary. Exact-rational finite checks do not verify all possible kernels and no independent external verification has been performed. Source novelty is qualified by incomplete access to the 2025 follow-up discussed in REVIEW.md.
