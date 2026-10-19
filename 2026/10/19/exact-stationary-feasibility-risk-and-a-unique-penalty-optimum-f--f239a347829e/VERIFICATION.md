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

# Verification of the stationary feasibility theorem

Reproduce with Python 3 standard library using `python verify.py`. The program independently forms the affine state matrix and solves the six symmetric discrete Lyapunov covariance equations by exact rational Gaussian elimination. It crosschecks the explicit risk, three auxiliary covariance identities, strict log-convexity signs, exact optimal-penalty brackets, and seeded stationary second moments. It completed 1716 checks successfully in the present evaluation.

The analytical proof covers every real \(0<lpha<1\), \(0<eta/\eta<4/3\), finite-variance independent zero-mean oracle and finite-second-moment initial state. Rational grids and seeded simulations are finite sanity checks, not proof for the uncountable parameter domain. The sharp stability boundary follows from the Schur polynomial and nondegenerate controllability/observability.

Only internal mathematical consistency was assessed; an independent audit has not been performed.
