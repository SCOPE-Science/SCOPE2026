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

# Reproducibility and mathematical boundaries

Run `python3 check.py` from this directory, using only the Python standard library. The completed run reported `EXACT_CUMULANTS_NEWTON_CUBIC_AND_DISCRIMINANT_PASSED`, `TWO_MOMENT_NONUNIQUENESS_AND_OPTIMAL_ONE_THIRD_EXPONENT_PASSED`, `INDEPENDENT_HAAR_POINT_PAIR_SAMPLING_PASSED`, and `ALL_CHECKS_PASSED`. The independent Monte Carlo method sampled two points on each product circle and directly computed the least wraparound distance, rather than sampling the moment-law variables; all first three raw moments agreed within the specified numerical tolerance.

The exact rational tests cover five chosen triples, including the cube and a repeated-axis case; they are not an exhaustive parameter enumeration. The inverse cubic formula, positivity/discriminant equivalence, two-moment classification, and Rouché root-stability estimate are proved symbolically for all positive periods in RESULT.md. Independent expert review, finite-sample stability, and an exhaustive historical-priority review have not been performed.
