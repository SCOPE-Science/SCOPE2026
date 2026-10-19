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
# Reproducibility and verification

The proof uses the actual SSPRK2 and SSPRK3 defining-stage formulas, and checks that their matrix-conjugated output equals composite trapezoidal and Simpson quadrature for rank-one, constant covariance forcing. The positive-node factorization and Vandermonde determinant establish the universal rank limits and attainability. Polynomial squared-integral positivity and the exact quadratic/quartic quadrature errors establish all sign cases.

The standalone `verification.py` requires only Python 3.10+ standard-library `fractions`, `math` and `itertools`; run with `python3 verification.py`. Its exact rational arithmetic independently reconstructs the stage formulas, weighted Gramian quadrature, Cauchy--Binet determinants, and the principal error entries on dimensions 1--7, step counts 1--4 and \(h=2/3\). It separately checks the closed minimal-full-rank determinant formulas. The execution prints `PASS 289 exact-rational assertion families`.

The rational test domains are finite: they do not certify statements for every dimension, number of steps, real step size, or real matrix. Those quantified statements are supported by the analytic arguments in RESULT.md, not extrapolated from the tested grid. The independent audit status recorded above is unperformed.
