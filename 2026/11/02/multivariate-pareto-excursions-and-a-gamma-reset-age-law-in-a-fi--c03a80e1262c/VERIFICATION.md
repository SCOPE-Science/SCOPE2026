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

Run `python verify.py` with Python 3.10 or later, SciPy 1.10 or later and NumPy 1.24 or later. The checker evaluates the stationary mean cycle in two numerically independent variable transformations, then checks sharp joint negative-excursion coefficients at three thresholds, permutation symmetry, the two posterior inverse-age moments and fixed-\(k\) tail dependence for integers \(3\le N\le8\). It reports `PASS 60 numerical diagnostics` in the tested environment. The checker computes the exact finite-threshold normal-integral differences with Gauss–Legendre quadrature, avoiding catastrophic cancellation at large negative thresholds.

The analytical proof, rather than numerical approximation, certifies all \(N\ge3\), all positive directional thresholds, all nonnegative posterior inverse-age moments, and the sharp moment-existence boundary. Numerical tail ratios converge slowly for larger \(N\); diagnostic tolerances reflect finite-threshold errors, not mathematical error bars on the limiting theorem. No claim is made of an external or independent audit.
