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

# Reproducibility and checks

Run `python3 artifacts/verify_asynchronous.py` using a standard Python 3 installation, without third-party packages. The program uses `fractions.Fraction` and a fixed seed only to choose rational test parameters. It independently evaluates the exact stochastic covariance map from its four-by-four transition matrices, verifies the supplied stationary covariance and four eigenvalue identities, independently evaluates the fresh-read covariance map, and verifies the stationary-risk difference. Result: **6,908 exact-rational assertions passed**.

The general stability frontier is proved by a positive-definite two-step Lyapunov certificate and a positive-semidefinite stationary-covariance obstruction; numerical checks are neither exhaustive over real parameters nor a substitute for those arguments. No independent audit or formal proof certification has been performed. The stochastic model assumes centered, mutually independent finite-variance update noise and uniform independent coordinate selection.
