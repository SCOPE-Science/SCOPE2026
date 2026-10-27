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

# Verification

Execute `python3 verify.py` with Python 3 and SymPy installed. The script checks the Gaussian transfer characteristic polynomial, the exact signed/Gaussian angular comparison identity and threshold factorization, an exact rational reversal example, Gaussian angular Fourier moments at four anisotropies and finite-grid transfer eigenvalues. It prints `VERIFY_OK: symbolic identities, exact conflict, Fourier moments, transfer eigenvalues` on success.

These checks corroborate, but do not replace, the general analytical proof based on a stationary ergodic logarithmic law, Poisson-kernel integration, positive finite-rank transfer and Bernoulli switching. The signed zero-overlap and initial-line exceptions are material limits. No independent scientific validation was performed.
