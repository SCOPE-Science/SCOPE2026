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

# Reproducibility and limitations

Run `python verify.py` using a standard Python 3 installation. Exact rational checks cover transition maps, finite-state detailed balance, boundary-inclusive Poisson equations and stationary averaging identities over a range of finite sizes and asymmetric sample probabilities. Floating-point characteristic-polynomial, eigenvalue and critical-limit checks are supplementary consistency tests.

The all-size lattice-absorption result is proved through invariant-interval dynamics and the almost-sure occurrence of an \(N\)-consecutive-noise block; finite simulations do not establish almost-sure absorption. The continuum critical law is proved by weighted Riemann sums, and the integrated autocorrelation formula by an explicitly verified Poisson solution and finite reversible-chain summability. The verifier does not claim exhaustive computation over infinite parameter spaces or independent validation. The result applies only to the parameterized quadratic, independent two-atom noise, reciprocal-curvature learning rate, and commensurate clipping cap stated in RESULT.md.
