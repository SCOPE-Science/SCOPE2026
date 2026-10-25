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

# Reproducibility

Run `python verify.py` with Python 3 and mpmath 1.3 or newer. The script was executed against the packaged candidate and passed 53 deterministic checks, including the exact Brownian exit-time moments \(\mathbb ES=1/2\), \(\mathbb ES^2=5/12\), \(\mathbb ES^3=61/120\), exact finite-exponent total-variation formulas, and convergence of the scaled error coefficient.

The proof is given in `RESULT.md`: a killed Brownian time-change, stationary mass normalization, differentiation of Mellin moments, \(L^1\) Taylor convergence, an exact total-variation identity, and a continuous-CDF layer limit. Numerical computations verify only finite special-function identities and finite-parameter instances; they do not prove the large-exponent theorem or compare finite-particle simulations with the hydrodynamic limit.

The external independent-audit channel has not been performed; no independent validation is claimed.
