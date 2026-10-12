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
`verify.py` checks the actual printed source-initialized AdaMod update on scalar quadratics, exact rational inequalities for the two-dimensional invariant square and its \(24/25\) Lipschitz certificate, the first-step objective decrease, and the nonzero alternating-orbit error bound. It also numerically tests the bias-corrected small-positive-moment trajectories and checks the algebraic autonomous tail fixed point.

Finite numerical checks are only transcription and arithmetic diagnostics. The infinite-time theorem uses the explicit analytical contraction and, for strictly positive moment parameters, a neighborhood-persistence and summable-perturbation argument. No assertion is made for the usual near-one rate-memory defaults or for noisy objectives.
