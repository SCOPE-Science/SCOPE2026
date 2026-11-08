---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For K_{m,n}, m,n>=2, graph-continuity means every vertex and edge inverse image is empty, singleton or an edge. Pure image in one part iff restrictions from each source part are partial injections; mixed image necessitates an injective bipartition-preserving or swapping map. Inclusion-exclusion on a fixed pure image set yields P_k; selecting mixed images yields M_k. A continuous section exists for mixed-image maps, whereas for pure image it exists iff one source part alone maps onto the image, giving R_k via inclusion-exclusion; idempotents are exactly maps fixing their image yielding E_k. Nonregular rank-two count 2mn[binom m2+binom n2]. Independently enumerated every partial function and checked inverse-simplex continuity, explicit section, and idempotence for (m,n)=(2,2): total/regular/idempotent 169/153/36 and (2,3):874/700/86; analytical combinatorial decomposition gives the all-m,n theorem.

## originality

PASS

The full graph-continuous monoid rank-by-rank regular/idempotent enumeration for K_{m,n} is distinct from the earlier strictly continuous balanced K_{r,r} enumeration. The 2026 Margolis–Rhodes full graph monoid preprint is highly relevant and inaccessible in full, creating a substantial historical-priority risk.

## value

PASS

A complete natural monoid census, exact regularity criterion, sharp onset of nonregularity, and idempotent spectrum are mathematically useful beyond a scalar element count; structural graph/semigroup link is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
