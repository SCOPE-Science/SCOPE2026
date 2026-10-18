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

The analytic proof uses the canonical free p-convex norm, a finite concave edge-budget optimization, strong Lagrangian duality under strictly feasible affine budget constraints, and an exact equality classification through fractional perfect matchings. The complete multipartite formula follows from convex averaging in log-prices and a one-variable minimum.

A standalone Python 3 verifier with no third-party requirements checks all ordered complete multipartite profiles with 2 through 12 vertices. It enumerates 3,711 balanced and 372 dominant profiles and checks 35,832 rational antipodal edge/cross-edge certificate entries. Representative floating-point comparisons are supplementary and explicitly bounded. No finite enumeration is taken as proof of a statement for every graph or dimension.

The baseline norm representation is a published theorem; it has not been independently reproved here. Independent audit of the new result has not been performed.
