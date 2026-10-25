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

# Reproduction and verification

Run `python3 check_triaxial.py` with Python 3.10 or later; only the standard library is needed. The independently implemented function `direct_ellipsoid_radius` computes the minimum eigenvalue of the quadratic form on an explicit orthonormal basis of each randomly oriented two-plane; it does not call the closed CDF or the cone test to obtain the radius.

The checker uses 90,000 seeded normalized three-dimensional Gaussian vectors to provide uniformly distributed unoriented planes. For each of five thresholds, it cross-checks the exact Boolean sublevel-cone criterion against the direct compression eigenvalue; it also checks empirical CDF against independent Simpson integration, ordering in the smallest semiaxis, attainment and approach to the two sharp envelopes, and the square-root upper-tail coefficient computed independently from the complete elliptic integral.

Observed output:

`TRIAXIAL_SECTION_CHECK_OK orientations=90000 thresholds=5 upper_coefficient=0.306288274762`

These are not exhaustive computations, an independent proof certification, or an independent scientific audit. Universal validity is supplied by the analytic proof in RESULT.md, including interlacing, weighted Cauchy--Schwarz, strict integral monotonicity, exact endpoint limits, and the repeated-top-axis linear-algebra obstruction. Absolute historical novelty is not certified.
