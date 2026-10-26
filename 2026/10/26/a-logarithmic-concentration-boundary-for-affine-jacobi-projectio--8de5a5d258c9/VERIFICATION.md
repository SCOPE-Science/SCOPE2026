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

# Reproducibility and scope

Run `python3 check.py` with Python 3 standard library. The executable checks 1,017 independent exact-rational assertions: integer-parameter Dirichlet kernel reproducing identities against first and second moments, beta-integral negative masses, recurrence identities, positive mass, and reduction to the previously established uniform-volume constant for all \(2\le n\le10\) and integer \(1\le\alpha\le4\). The actual check was replayed successfully from the embedded script.

The shrinking-parameter asymptotic was also numerically stress-tested with independent beta CDF calls for \(\lambda\in\{0.2,1,3,10\}\) and \(n\in\{1000,10000,100000\}\); the error after subtraction of the displayed second-order term is \(o(n^{-1})\), as shown analytically in RESULT.md. Numerical checks cannot establish an infinite asymptotic or global vertex maximization. Their proofs are the covariance, Jensen, beta-integral and gamma-limit steps in RESULT.md.

No independent audit or external validation has been performed.
