---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed each parametric map and the iff cross-transversal criterion: equal-rank isotone transformations are semigroup inverses exactly when their ordered images hit corresponding blocks of the other kernel. For rank two the three cases (cut a, image b<c) pair a<b<c with (c-1;a,b) and b<c<=a with (b;c,a+1), fixing b<=a<c. For rank n-1 the unique adjacent double kernel block a and omitted image b pair b<a with (b;a+1), and b>a+1 with (b-1;a), fixing b=a,a+1. These piecewise maps satisfy the two sandwich equations, invert themselves and fix exactly idempotents. Counts follow: fixed binom(n+1,3), swaps binom(n,3), respectively 2(n-1) and binom(n-1,2); n=3 overlapping classes checked. Reimplemented exact composition and exhausted all parameter tuples independently n=3..8; proof covers all n.

## originality

PASS

Higgins 2026 Theorem B supplies a permutation inverse matching for the entire monoid, not an involution or explicit rankwise two-cycles. The 2019 involution for the larger orientation-preserving monoid does not automatically restrict to isotone maps. The two explicit extreme-rank involutions and fixed-point spectrum survive as a narrower stronger structural statement, with priority risk from earlier inverse incidence studies.

## value

PASS

The strongest already-known all-monoid result leaves order-two inverse matchings structurally unresolved. Exact involutive pairings of the two natural extreme nontrivial Green classes at every n, with idempotents fixed and explicit pair-count spectrum, form a useful boundary theorem for the remaining intermediate ranks; no claim of whole-monoid solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
