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

# Reproducibility checks

`checks/verify_two_cap_symbolic.py` independently constructs both cap functions and verifies the order-four and order-six Taylor coefficients, including fixed-area corrections and the exact stationary cubic value.

`checks/verify_asymmetric_drums.py` evaluates the full curved-ball area and total mean curvature with 55-digit mpmath arithmetic and solves the exact area constraint for three strictly positive area excesses. It checks the strict advantage of two versus one cap, and the sign and scale of the unequal-cap penalty.

Execute from the extracted package root with `python checks/verify_two_cap_symbolic.py` followed by `python checks/verify_asymmetric_drums.py`. Dependencies are in `requirements.txt`. The analytic proof, rather than these finitely many numerical comparisons, justifies uniqueness, uniform error terms and sharpness.

The source formula comparison is to Fang Hong, arXiv:2606.01771v4, equations (4.1) and (4.2), for the equal-cap subfamily. This package has not received an independent audit.
