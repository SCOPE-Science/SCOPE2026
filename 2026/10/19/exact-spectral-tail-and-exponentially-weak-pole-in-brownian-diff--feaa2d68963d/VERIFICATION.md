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

# Reproducible checks

Run `python verify.py` with Python 3 and `mpmath` installed. The program evaluates the exact secular equation and analytic spectral identities using 70-digit arithmetic. It performs 125 deterministic assertions for root intervals, isolation from the essential spectrum, positive eigenweights, resolvent and Fourier-transform identities, a reconstructed continuous spectral measure, finite-difference sensitivity, and small/large refresh limits. It returned `PASS 125 deterministic checks; direct secular equation, Fourier transform, spectral normalization, resolvent, both limits.`

The code nondimensionalizes the mean intensity to one; arbitrary positive intensity scale follows by replacing the refresh parameter with its ratio to the mean intensity. Its spectral-integral quadratures and asymptotic comparisons are finite numerical corroborations, not a proof of exactness or novelty. The analytic proof is provided in `RESULT.md`; no independent validation has been performed.
