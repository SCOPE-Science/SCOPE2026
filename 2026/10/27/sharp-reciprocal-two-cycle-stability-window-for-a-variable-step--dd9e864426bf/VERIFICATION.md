---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact homogeneous 3×3 companion matrix C(w,v) has unit constant vector. For alternating reciprocal ratios t,1/t, direct symbolic multiplication produces characteristic polynomial (λ−1)(λ²−S(t)λ+P(t)), with S,P rational as stated. For t>0, the Jury expressions 1−P and 1−S+P are everywhere strictly positive; the third 1+S+P is positive precisely for 4(t+t^(−1))²−10(t+t^(−1))−49<0. This yields closed zero-stable [t*,t*^(−1)], strict interior parasitic stability, and simple −1 root on the boundaries; outside one parasitic modulus exceeds 1. The explicit determinant of the frozen C(t,1/t) exceeds 1 in modulus for 0<t<1/4, providing a strict stable-product/unstable-factor interval, reciprocal counterpart by phase reversal. Independently recomputed symbolic trace, determinant and critical Jury factor with exact SymPy algebra. No claim about arbitrary variable-step schedules.

## originality

PASS

Best-of-knowledge: primary same-object comparisons, alias/implication checks and published finding searches distinguish the assessed exact statement from covered components. Historical priority uncertainty is retained; failed search is not novelty proof.

## value

PASS

The precise period-two monodromy gives a motivated sharp necessary-and-sufficient stability window for an existing variable-step method and an explicit phenomenon where the switched product is stable although a frozen factor is unstable. This identifies a nontrivial dynamics overlooked by frozen-root checks, not a generic Jury recitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
