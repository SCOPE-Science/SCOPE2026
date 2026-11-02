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

Run `python verify.py` with Python 3 standard library. The supplied verifier constructs intrinsic distances via the two nearest deck images, constructs analytic maximizing target witnesses, samples additional targets, checks the diameter/Chebyshev formulas across aspect configurations, and checks the reciprocal isodiametric profile across 10,000 aspect ratios.

The recorded successful execution found 82,620 sampled point distances bounded by their exact eccentricities, 1,836 maximizing witnesses, 36 diameter/radius cross-sections, and 10,000 dual isodiametric tests. The largest sampled overshoot was zero. Floating point checks are supplementary: completeness of the rectangular Voronoi partition, global extrema, and the exact transition are established in the mathematical proof, not inferred from sample coverage.

The proof concerns the intrinsic length-metric quotient, not a Euclidean embedding. Independent audit is not performed. Historical originality remains contingent on further external review.
