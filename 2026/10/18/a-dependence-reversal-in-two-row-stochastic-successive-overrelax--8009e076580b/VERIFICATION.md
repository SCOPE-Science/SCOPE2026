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

The self-contained Python-standard-library `verify.py` uses exact `fractions.Fraction` arithmetic. It checks the two unit-relaxation rates, all realized-matrix discriminants and determinants, the positive-definite Lyapunov matrix with its strictly positive residual, the positive-definite covariance eigenmatrix with eigenvalue greater than one, and identical univariate factor marginals. Run `python verify.py` and expect `VERIFY_OK`.

The code checks finite algebraic identities. Infinite-time statements follow from repeated conditional expectation, strict Lyapunov contraction, the exact positive covariance eigenmatrix, and independence of draws between sweeps. No empirical experiment is presented as an infinite proof. Independence or external validation has not been performed.
