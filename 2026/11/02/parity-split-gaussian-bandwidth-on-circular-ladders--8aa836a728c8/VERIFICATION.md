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

# Reproducibility and limits

Run `python3 check_prism.py` to compute approximate critical parameters for ten prism orders, reconstruct full finite Gaussian kernel multiplication on antisymmetric Fourier eigenvectors, and check the signs and even/odd asymptotic approach. The checker uses only the Python standard library and has no external inputs or downloaded dependencies.

The mathematical proof is given in `RESULT.md`: it includes explicit Fourier eigenvalues, global inequalities for bandwidth at least one, uniqueness of the last failing mode, and Gaussian-tail-controlled asymptotic expansion. Finite numerical tests do **not** establish the infinite claim; no independent verification was performed. This file's front matter reports only the absence of an independent audit.
