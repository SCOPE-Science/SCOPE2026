---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: The final k vertices of every arm except the last are black; chronological forces from deep to shallow fill these arms, then a sequence along arm 1 forces the hub and first k vertices of the last arm, then the last arm propagates. Each force has exactly one white neighbor because the inter-arm graph-power adjacency criterion is depth-sum <=k. A symmetric witness formed by within-arm sliding-window Gram C_i^T C_i, first-k coordinate coupling U^TBU and hub block h^TU has exact nonzero off-diagonal pattern. Each ker(C_i) is k-dimensional, parametrized by its first k entries; imposing sum_i E_ix_i=0 leaves (m-1)k independent null vectors. Universal inequality M_R<=Z closes equality. An independent BFS builder and exact SymPy rank/forcing closure verified cases (l,k)=((4,5,6),3),((3,4,5),2),((4,4,4,4),3),((2,3,4),1), with nullities 6,4,9,2. Does not claim short-arm or all-tree result.

## originality

PASS

PASS (best knowledge): Abiad et al. 2026 publicly describe upper bounds for spider powers, and the inspected source records their equal-arm equality as a conjecture; the current explicit rank/nullity lower construction gives the missing half and handles unequal lengths. Path powers (m=2), tree squares (k=2), and unpowered spiders (k=1) are earlier known boundaries. The primary 2026 paper was read at abstract level only during this execution; a later version or unindexed stronger result remains a priority risk.

## value

PASS

PASS: Resolving a specifically stated graph-power zero-forcing conjectural equality with an integral exact-pattern minimum-rank witness is mathematically substantial. The arbitrary unequal-arm extension is structural and nontrivial, not a single numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
