---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

A coherent rim cycle with n pendants has 2n arcs and a multipath face iff it selects at most one incoming and outgoing rim/pedant arc at each vertex and omits the complete rim cycle. Each pendant conflicts with exactly one rim edge; partitioning pendants by that rim arc yields local face factor (1+t)+(1+t)^k−1 for k=0,1,2. A cyclic orientation word with q transitions of each type gives exactly q k=0, q k=2 and n−2q k=1 factors, hence (1+t)^q(1+2t)^(n−2q)(1+3t+t²)^q−t^n. Uniform words give boundary crosspolytope (S0)^{*n} minus one facet, hence a PL (n−1)-ball. A mixed word has an in→out boundary giving rim arc e_j with no pendant conflict; pairing each pendant-bearing face not containing e_j with its e_j augmentation in descending lower-cardinality order is a finite sequence of actual free-face elementary collapses to all proper rim-edge subsets ∂Δ(E)≃S^(n−2). The rim inclusion intertwines any orientation-preserving cyclic rotation, giving sign (−1)^(n−gcd(n,k)) on top integral homology. Independently enumerated and compared complete direct-arc multipath face sets to local-factor predictions for all 8,16,32,64 orientation words at n=3,4,5,6, checked polynomial and each mixed relative collapse; the all-n proof is structural, not an extrapolation.

## originality

PASS

A best-of-knowledge comparison of specific mathematical implications and exact model/normalization found no identified earlier theorem proving this new claimed part. Previously published overlapping objects, numerical invariants and limitations are credited. The four explicit checks, primary-source inspections and risk list below bound this assessment. A known subcomplex homotopy type does not predict whether additional independently oriented pendant arcs fill or preserve its fundamental class; the contrasting uniform/mixed cases require the explicit free-edge method. Neither earlier theorem implies this dichotomy or enumerator.

## value

PASS

The directed sunlet is a canonical cycle-with-one-leaf-per-vertex family; its 2^n orientation choices pose a natural complete topological classification. The dichotomy is sharp: uniform pendants fill the rim sphere into a PL ball, while every mixed pattern simplicially collapses to the original rim sphere. The transition-count face polynomial and rotation character give additional concrete invariant structure. The proof supplies a reusable free-unconstrained-rim-edge collapse and is not an arbitrary small instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
