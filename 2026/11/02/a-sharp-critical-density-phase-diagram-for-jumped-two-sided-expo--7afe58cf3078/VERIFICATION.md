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

# Reproducibility and proof limits

The result is an analytical theorem. Its proof obtains the exact Zak multiplier by summing both exponential tails, proves sharp frequency extrema with equality at the phases 0 and pi, minimizes and maximizes the resulting scalar functions over a unit cell, and obtains the spectral and conditioning consequences. This verifies infinitely many parameter values symbolically; no finite grid is treated as exhaustive proof.

The included standard-library `verify.py` can be run with `python verify.py`. The tested program completed 81,136 checks covering pointwise Zak identities, independent truncated Fourier series, frequency extremizers, jump thresholds, lower/upper bounds, and the conditioning barrier. Truncation and finite-grid errors are explicitly tolerated only in these supplementary checks.

Limitations: exact coefficients assume this window normalization and unit critical lattice; positive amplitudes and identical decay rates on both sides. Historical priority remains provisional. Independent audit and independent validation are not performed.
