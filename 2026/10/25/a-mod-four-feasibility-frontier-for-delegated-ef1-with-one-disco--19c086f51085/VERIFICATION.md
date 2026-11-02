---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For positive and constant per-good value, agent inter-EF1 for every ordered pair is equivalent to maximum minus minimum assigned count at most 1. Hence counts consist of q and q+1 with exactly r larger counts, m=4q+r. Item-based realized center EF1, under exact published definitions, gives a+b>=c+d-1 and c+epsilon*d>=a+b-1. Exhausting each residue r=0,1,2,3 forces canonical count patterns (q,q|q,q), (q,q|q+1,q), (q,q+1|q+1,q), (q,q+1|q+1,q+1). The remaining center inequality gives inclusive thresholds (q-1)/q, max(0,(q-2)/q), (q-1)/q, (q-1)/(q+1). Every allowed epsilon supplies an explicit allocation, and excluded patterns require epsilon>=1 or violate center-1 fairness. Independent exact enumeration verified 1,748 parameter/inventory pairs for 4<=m<=200 and m=8,9,10 reversal; infinite range is covered by four-case proof.

## originality

PASS

The direct source Deligkas et al. (2026) gives an explicit twelve-good nonexistence witness using the same special agent but does not state or imply exact inventory thresholds, an eight-good first obstruction, or nine-good restoration. Broader balanced EF1 existence guarantees omit the independent delegated-center constraints. The classification and nonmonotonicity are new in inspected statements, with residual unindexed-priority risk.

## value

PASS

The classification directly refines a concrete published impossibility example, resolves the entire discount and inventory frontier for its smallest natural two-center pattern, and exhibits the surprising loss and recovery of feasibility as indivisible items are added. This is a complete exact mathematical fact with allocation-theoretic motivation, not an arbitrary finite census or known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
