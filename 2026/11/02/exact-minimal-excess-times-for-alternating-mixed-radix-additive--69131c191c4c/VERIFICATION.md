---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Inspected RESULT.md blob ccc5754478f57ac14b04701742e3c81b1ca738f4 and verifier e9f63bf525c858b089dff7bca673ccd370d977f6. Unique mixed-radix sum representation supplies A_k×B_k partition of [0,Q_k). For n=dQ_k+u with top-digit parity in A, the excess A(n)B(n)-(n+1) equals β_k A_k(u)-(u+1), and vice versa for odd k. At u=Q_k-1 all lower pairs count; if u<Q_k-1 a pair with larger opposite coordinate gives a strictly extra count; k=0 handled separately. Equality therefore occurs precisely at the enumerated boundaries, and disjoint radix intervals give the exact count. Independent brute counts over seven mixed-radix lists matched, but the proof treats unbounded arbitrary radices.

## originality

PASS

Best-of-knowledge priority based on comparison of actual statements and implication directions: Same construction and counting functions compared, not superficially different notation. Prior lower-bound equality infinitely often is weaker than the iff set of all times and exact frequency. A global bound or existence statement does not imply the exact equality-time distribution under arbitrary unbounded radices. Residual overlap risk retained; search absence alone is not evidence of novelty.

## value

PASS

Precisely locates and counts all minimum-excess times for an established and widely studied class of perfect additive complements. It is a natural infinite structural refinement beyond known infinitely-many attainment, useful to research on equality frequency and return-time statistics; no claim about arbitrary additive complements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
