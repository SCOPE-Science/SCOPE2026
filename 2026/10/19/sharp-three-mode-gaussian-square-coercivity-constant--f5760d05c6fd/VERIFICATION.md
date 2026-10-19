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

In normalized complex Gaussian measure, the exact moment identity \(\int z^j\overline{z}^{\,k}\,d\gamma=\delta_{jk}j!\) is the starting point. The analytical optimization is in `RESULT.md`. `checker.py` (Python 3, NumPy, SymPy) independently verifies four symbolic identities: two differentiated quotient numerators, the degree-two resultant, and the excess-over-affine formula. It also verifies the algebraic candidate stationarity and evaluates the sharp constant. It then performs 250 independent random complex-polynomial Gaussian quadratures using Gauss–Laguerre radial nodes and angular Fourier quadrature, and verifies nine scaled/rotated equality representatives.

All these checks passed. They are supplementary finite computations; global sharpness and uniqueness depend on the analytic phase reduction, one-positive-root calculus and the resultant factorization. No claim is made about higher-degree Fock functions or global phase-retrieval constants.
