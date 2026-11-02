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

# Reproducibility and verification

The standard-library `verify.py` is included in this package and can be run using `python verify.py`. It implements the actual source compact-support product, all four local degree-one interpolants, all four residual indicator sets, and nonlinear normalization with `fractions.Fraction`.

The verifier exercises 420 exact-rational witness variants and 1,800 seeded bounded-data inequality checks. It computes the witness's local interpolation and indicator Lebesgue constants exactly as \(L_x=H_x=2\). It also verifies inactive small stencils, the equal active geometric factors, clean indicator zeros and the precise perturbed output formula.

Finite tests do not establish the universal Lipschitz inequality or the infinite family of perturbation scales; the covariance/absolute-continuity argument and exact rational algebra in `RESULT.md` provide those proofs. No independent audit or external certification has been performed.
