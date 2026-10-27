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
# Reproducibility checks

The self-contained scientific checker `VERIFY.py` uses Python 3, SymPy and mpmath. Running it on the included source file returned `VERIFY_OK: 27 symbolic/numerical assertion groups`. Its symbolic checks reproduce the exact derivatives at the critical coupling, including the first three zero derivatives and positive fourth derivative of the radial effective potential. Four near-cusp parameter choices check the two folds, their ordering and width scaling. A supercritical example checks three roots and their stability signs. Independent high-precision energy quadratures for two shrinking radial excursions check convergence toward the beta-function period and angular-winding coefficients.

These finite tests verify algebra and provide reproducibility evidence; they are not exhaustive proofs over parameter space. The infinite-domain bifurcation and limiting laws are proved analytically in `RESULT.md` using monotonicity, Taylor expansions and dominated convergence for the turning-point integrals. The scientific review is not an independent assessment.
