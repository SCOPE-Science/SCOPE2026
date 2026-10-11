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

Run `python verify_cusp.py` with SymPy installed (versions specified in `requirements.txt`). The actual standalone checker was executed on the packaged path and returned `CHECK_OK`.

It recomputes the double-zero characteristic polynomial, the non-quasistatic center tangent, the negative-coordinate weighted blow-up, both hyperbolic saddle fixed points, and the rational algebraic coefficients of the stated limits. These are exact symbolic identities with positive symbolic parameters; no numerical samples are used to prove universality.

The existence of the invariant center manifold and the incoming/outgoing separatrix germs relies on the standard smooth center-manifold and hyperbolic stable-manifold theorems together with the explicitly stated desingularized vector field. Code does not independently verify these infinite-dimensional local existence conclusions. The result makes no full-neighborhood stability claim. Original-paper PDF acquisition was incomplete; only relevant indexed article text and previously published same-model theorem full text could be compared.
