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

The proof reduces two environmental states to a fractional-linear stationary occupancy response and checks its derivative has fixed sign. For a symmetric complete \(n\)-state environmental chain, the occupied-state balance equations yield an exact weighted-ratio law. In the exhibited three-regime example, symbolic rational simplification gives \(P(q)-5/8=9q/[8(9q^2+39q+28)]\), and differentiation gives the unique stationary maximum at \(2\sqrt7/3\).

The accompanying `verify.py` constructs and solves the full joint Markov generator using exact rational linear algebra. It matched the claimed closed forms in 319 deterministic cases, with symbolic verification of the example and its boundary limits. No claim of external audit or formal proof assistant certification is made. The exact statements are proved analytically; finite tests do not prove universality.
