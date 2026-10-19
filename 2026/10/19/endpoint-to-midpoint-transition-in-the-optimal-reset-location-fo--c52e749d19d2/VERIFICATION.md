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

The exact proof computes the first-passage Laplace transforms from \(D\phi''=r\phi\) with appropriate Dirichlet and Neumann boundary conditions. Poisson renewal transforms yield the mean, and elementary factorization reduces the optimization to the signs of a quadratic and of \(2b^2-b-2\). Those steps apply to all fixed positive \(D,L,r\), without a finite truncation assumption.

Run `python3 verify.py` using only the Python standard library. In the delivered run it completed **748 assertions**, comprising exact rational endpoint identities, phase-diagram location tests, finite-difference derivatives, and a separately discretized second-order first-passage boundary-value equation. The finite-difference calculation is a cross-check of the mean law; it is not proof of a continuous-domain global minimum. The derivative and root-sign proof supplies that proof.

The source mean-cover-time formula and midpoint specialization are existing literature, not independent new discoveries. The claimed contribution is the full deterministic-location optimization and its spinodal. No independent audit or validation has been conducted.
