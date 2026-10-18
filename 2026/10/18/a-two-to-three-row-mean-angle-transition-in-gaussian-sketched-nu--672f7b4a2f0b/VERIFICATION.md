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

Install the dependencies listed in `requirements.txt` in an isolated Python environment and run `python verify.py` from the directory containing both files. The deterministic verifier checks 1,500 direct Gaussian Gram eigenvector identities, 18 numerical angular-integral identities at three sketch rows, and 10 moment-integral/asymptotic sanity checks. These checks passed when executed with the accompanying package.

The full continuum in sketch conditioning and the singular small-eigenvalue limit are proved by the algebraic eigenprojector formula, exact Wishart angle integration for three rows, singular integral asymptotics for two rows, and dominated convergence for fixed larger row counts. Numerical quadrature and finite sample checks cannot prove asymptotic or all-parameter results. No independent validation or experimental reproducibility certification has been performed.
