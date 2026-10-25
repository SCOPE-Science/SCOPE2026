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

# Reproducibility and verification limits

Execute `python check.py` using Python 3 with NumPy and mpmath installed. The program was executed on the packaged scientific calculations and returned **49 passing deterministic assertions**. It computes the confluent-hypergeometric response independently of its asymptotic form, checks the time-nonlocal scalar evolution through a numerical time integral, verifies the exact two-dimensional trace distance and positivity, and integrates a representative continuous-band purity kernel.

The main infinite-dimensional claim is analytic rather than computational: spectral-measure dominated convergence gives the Hilbert–Schmidt limit; finite-block approximation gives the trace-class criterion; the uniformly small-Bohr-frequency special-function asymptotic gives the continuum purity coefficient; and a compact-resolvent two-block compression produces arbitrarily slow convergence. Finite numerical tests cannot certify these limiting steps. The finite tests are reproducible diagnostics only. No independent audit or external validation has been performed.
