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

The supplied `verify_spherical_fourth.py` uses exact symbolic integration to evaluate ten rational Legendre-square integrals. It also compares the first three against numerically truncated original Bessel fourth moments, and applies high-order Gauss--Legendre quadrature to six degrees in the asymptotic regime. The check is executed directly from the embedded file before record acceptance. Its output is:

`VERIFY_OK 10 exact modal rationals; 3 Bessel integrals; 6 two-term asymptotic quadratures; sharp stability coefficient 44.345108577528364`

The finite computations cannot establish an all-degree identity or the limit. The analytic proof in RESULT.md is required. The three-dimensional sharp stability constant uses Xu's Theorem 1.3 under the stated surface-measure and Fourier conventions; it is not independently established by the script.
