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

Execute `python check_fiber.py` from the directory containing this document and the bundled code. No nonstandard Python dependencies are required.

The checker constructs the exact rational vertical image by independently applying the piecewise-affine maps to intervals for each ternary base word of length at most eight (\(3^8=6561\) words at the largest horizon). These interval images agree word for word with the claimed dyadic depth and cell. An independently implemented birth-and-death transition computation gives the same mean fiber lengths; exact coefficients of the renewal generating function agree through order 22. The script then evaluates the two-singularity asymptotic prediction at three large finite horizons. A successful run ends with `DYADIC_FIBER_EXACT_AND_ASYMPTOTIC_CHECKS_OK`.

For example, at horizons \(n=0,1,2,3,4\), the computed mean lengths are respectively \(1,2/3,5/9,4/9,31/81\). These checks test finite consequences and the asymptotic trend, not all infinitely many iterates. The infinite statement follows instead from the exact renewal generating function, its absence of closer singularities, the two branch-point coefficient transfers, and tail summation, as detailed in `RESULT.md`. Boundary codes are a null set under Lebesgue base measure.

Self-review: passed. Independent audit: not yet performed.
