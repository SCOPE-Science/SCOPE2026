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
# Verification and reproducibility

The analytic basis decomposition, uniform \(L^2\) bounds, Lindeberg convergence, uniform integrability, and compactness argument are given in `RESULT.md`. In particular, the numerical checks are **not** used to establish the uniform limit or an infinite-dimensional operator inequality.

Execute `python checker.py` using Python 3.10+ and NumPy. The test checks exact moments for the uniform, arcsine and endpoint-mixture laws, finite polynomial-kernel algebra and the projection identity in dimensions one through four, plus seeded sampling in dimensions eighty and three hundred twenty. Sampling tolerance is deliberately loose and tests consistency, not precision or asymptotic rates.

The law is proved for one fixed symmetric marginal satisfying the stated moment and endpoint-support assumptions. No source has independently certified the proof or bibliographic originality.
