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

The finding is established analytically in `RESULT.md` by a local normally hyperbolic strong-stable foliation, exact saddle and eigenslope jets, and a curvature-order estimate. The relevant initial-point intersection is smooth and invertible for each fixed \(a\in(0,1)\).

The standalone `verify.py` needs only Python 3's standard library. It passes 1,939 exact-rational identity groups across 277 distinct parameter choices, checking the polynomial equilibrium, folded relation, stable-slope characteristic equation, intersection jet and cubic inversion. Those finite exact tests verify algebraic implementation, not the full family theorem; the analytical proof supplies the infinite quantification.

Scientific limitations: the error term is pointwise in \(a\), no positive-\(\varepsilon\) expansion is established, the fourth-order coefficient at the sign-crossing parameter is not calculated, and the new formula's ultimate bibliographic priority awaits independent scrutiny. No independent audit has been performed.
