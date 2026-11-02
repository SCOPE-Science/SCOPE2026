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

# Reproducible verification and its limits

The single standalone script `verify.py` uses Python's standard library and independent fixed-content enumeration. Execute `python3 verify.py` in the extracted package. It enumerates all cyclically indexed binary words of lengths 4 through 14 with at least two symbols of each color, not just a random sample. For each of 66 fixed-content profiles it checks the run-count distribution, conditional factorization of singleton-run counts, expected singleton counts conditioned on the common number of runs, the falling-factorial covariance expression, strict positivity of the singleton covariance, every singleton upper-orthant threshold covariance, and every cross-color pair of cumulative short-run count coordinates (strict covariance and positive quadrant dependence at all attainable thresholds). It prints a PASS summary or terminates at the first failed assertion.

The all-size positive-association theorem is justified by the explicit marking/counting argument and nested-cut refinement coupling in RESULT.md, not by extrapolating these enumerations. The finite checker does not exhaust arbitrary increasing functions of entire multithreshold profiles for all sizes. No independent external audit has been performed.
