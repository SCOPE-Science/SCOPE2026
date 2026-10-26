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

The analytical proof checks exact definitions, endpoint normality, infected costate orientation, the continuous weighted switching derivative, and Rolle's theorem including the terminal zero. The time-zero hypothesis counts *zeros*, not merely changes of sign. Terminal transversality for both explicit parameter families follows from exact lower bounds for the infected growth along the first-hit boundary, then a left-neighbourhood comparison excluding tangency.

The included `checker.py` is run against the precise decoded file content. It checks exact symbolic derivatives and rational inequalities at the two susceptible thresholds. It is not an exhaustive search of optimal controls and does not prove the infinite-switch upper bound computationally. Earlier source numerics demonstrating two-switch improvements remain numerical and have not been promoted to certified global optimality.

Self-review: passed. Independent audit: not yet performed.
