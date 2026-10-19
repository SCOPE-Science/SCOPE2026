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

# Checks of the new theorem

The analytical proof in RESULT.md supplies the universal quantifiers. The orientation and spectral assumptions are checked symbolically by bipartiteness, Perron--Frobenius and similarity to a positive-definite matrix. For the exact local map in real antiphase coordinates, the critical cubic coefficient follows from a left Perron eigenvector, and the Lyapunov--Schmidt equation is an odd analytic scalar equation. Its leading nonzero solution is real precisely for positive detuning; contraction is proved by first-order Jacobian perturbation.

The executable `verify_flip.py` numerically tests eight finite tree/step instances, including different branching and nonuniform positive weights. It checks the full nonlinear antipodal-cycle equation, amplitude normalization, positive Perron mode and strict Jacobian contraction. Finite experiments do not establish uniqueness or all-tree validity.

External independent audit status: not performed. This document makes no claim of independent validation.
