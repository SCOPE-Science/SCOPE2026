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

The proof is symbolic and covers every integer triple \(p,q\ge2\), \(n\ge3\). Its critical steps are: the four exhaustive image-shape cases, the unique-common-upper-neighbor property for two consecutive crown minima, and the standard finite-space fact that pointwise comparable maps are homotopic.

`artifacts/verify.py` performs an independent finite replay. It enumerates every function for all \(1\le p,q\le3\), \(3\le n\le5\), filters by order preservation, checks
\[
|\operatorname{Map}(P_{p,q},\mathfrak C_n)|=n(3^p+3^q-2),
\]
classifies every map into the same four proof cases, and verifies the claimed pointwise comparison with a constant. It separately analyzes \(\operatorname{Map}(\mathfrak C_2,\mathfrak C_2)\), obtaining \(36\) maps in components of sizes \(32,1,1,1,1\), with the identity outside the constant component.

The replay result is:

`VERIFY_OK exhaustive_parameter_triples=27 sharp_n2_maps=36 sharp_n2_components=[1, 1, 1, 1, 32]`

Limits: finite enumeration is not an infinite certificate and is used only as a stress test. No computation is offered for the full homotopy type or Stong core of the mapping space when \(n\ge3\).
