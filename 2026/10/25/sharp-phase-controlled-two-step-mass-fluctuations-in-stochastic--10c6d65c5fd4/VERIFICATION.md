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

# Reproducibility and verification boundaries

The formula is established symbolically in `RESULT.md`, equations (1)–(5): elimination of both steps; Gaussian conditioning and the standard analytic characteristic function of a squared standard normal; trigonometric optimization and the zero-phase derivative; and a separate conditional-variance computation for isotropic complex kicks.

Run `python3 verification/mass_variance.py` with the standard Python 3 library. The original execution returned `PASS: 633 deterministic checks` and independently integrated the Gaussian variance formula numerically to the specified tolerance. The deterministic tests are finite and do not replace the analytical proof. Exactness refers solely to the scalar two-step recursion and the specified real Gaussian or separately labeled circular complex driving noise.

No independent audit was performed. Priority among unpublished, unindexed, or inaccessible related calculations is not independently certified. No claims concern asymptotic sampling error, a coupled spatial PDE, or long-time numerical stability.
