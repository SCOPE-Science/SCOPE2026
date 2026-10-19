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

The scientific claim concerns an ideal eigenpair-deflation, exact-quadratic-form estimator. No implementation of random Nyström sketching or Lanczos truncation is purported to prove the result.

The accompanying `verify.py` is self-contained (Python 3 standard library). Execute `python verify.py`. It tests finite-spectrum shifted-tail inequalities with exact rational arithmetic; explicit finite geometric spectra on both sides of the threshold; the integer minimizer in an infinite-geometric risk formula; large-budget power-law allocation through deterministic tail quadrature; and sample second moments of Gaussian quadratic-form errors. The observed total was 7,205 checks with no failures. For the stochastic comparisons, the random seed and tolerance are specified in the program.

The universal sharp threshold follows from the analytic shifted-tail inequality and an explicit finite witness, rather than enumeration. The infinite-geometric optimizer follows from the adjacent-risk ratio, and the polynomial asymptotics from the integral test and a unique interior minimizer. Infinite-series validity follows from summability, not the existence of an infinite-dimensional standard Gaussian vector.

Independent audit has not been performed.
