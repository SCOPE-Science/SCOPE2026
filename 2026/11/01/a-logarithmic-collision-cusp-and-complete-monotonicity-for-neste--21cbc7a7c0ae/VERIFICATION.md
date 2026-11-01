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

# Reproducibility and limits

The analytic proof starts from independent uniform circle angles, reduces the event of crossing two finite segments to signed line-offset containment, and integrates the arcsine endpoint-projection distribution. The exact positive coefficients, sharp \(1/3\) and \(8/\pi^3\) constants, monotonicity and radius-collision cusp are proved without relying on numerical tests.

The standalone `check.py` uses Python with NumPy and SciPy. Run `python check.py` in the directory containing this document and the program. Its deterministic checks evaluate three coefficients by an independent arcsine-kernel integral, compare two different exact quadratures at eight radii, test sharp upper/lower bounds and certified positive-series remainder, numerically check the logarithmic cusp and far-field corrections, and independently simulate direct intersections of randomly sampled Euclidean segments. The program prints `ALL_CHECKS_PASSED` on success.

The checker is supportive finite evidence, not a proof of universal quantifiers or historical originality. No additional formal verification or external validation is represented.
