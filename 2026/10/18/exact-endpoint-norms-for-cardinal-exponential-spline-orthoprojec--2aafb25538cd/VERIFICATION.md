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

The analytic derivation is self-contained in `RESULT.md`: compute the two nonzero Gram diagonals, invert the tridiagonal Toeplitz symbol, use strict convexity of the absolute projection kernel between knots, and integrate the sole crossing of the nodal kernel. The signed-integral Taylor calculation proves the exact weak-tension term; no finite sample is used to infer it.

Run `python3 check.py` using Python's standard library. In this package it reports `PASS: 34 analytical-formula and independent finite-section consistency assertions`. It evaluates tridiagonal finite-section projectors, integrates their kernel rows over grid cells, evaluates the infinite geometric row separately, and checks weak-tension consistency. The finite-section convergence is justified analytically by the geometric inverse; numerical tests by themselves do not certify the infinite-dimensional assertions.

Source scope: arXiv:math/0408418 was available as abstract and overview rather than a complete thesis; the full 2005 Unser–Blu primary text was not retrieved. Historical coverage therefore requires further independent bibliographic review.
