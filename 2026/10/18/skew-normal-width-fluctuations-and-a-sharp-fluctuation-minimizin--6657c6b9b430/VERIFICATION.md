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

The scientific derivation uses the exact Minkowski support function, spherical two-coordinate absolute products, a multivariate Gaussian central limit theorem and an explicit sphere-normalization expansion. The finite exact formulas were cross-checked against linear programming and simulations. A standalone `checker.py` is included and executed successfully.

Reproduction: from the same directory, run `python checker.py` with Python 3, NumPy and SciPy installed. The checker runs 300 direct linear-program support comparisons in dimensions 2 through 6, exact mean/variance formula comparisons against reproducible random spherical directions, and a finite-sample skew-normal goodness-of-fit check in dimension 800. The printed `ALL CHECKS PASSED` line was obtained from the embedded code.

Limits: randomized finite checks are not exhaustive, and a simulation cannot prove a weak limit. The analytical proof covers all stated dimensions and cant values. Independently commissioned review or formal certification was not performed.
