---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a state permutation p, A′(x)=−Σ_j M_{p(j),j}≤C=−Σ_j min_i M_{ij} and ≤R=−Σ_i min_j M_{ij}. With C≤R, equality to min{C,R} holds iff all chosen values are column minima, yielding a perfect matching in BC(M); the row case is symmetric, with C=R handled. A matching is unique iff there is no matching-alternating cycle because toggling a cycle yields another and the symmetric difference of two distinct matchings decomposes into alternating cycles. Directed cycle detection after finding one matching gives a polynomial algorithm. Independently enumerated ALL binary matrices of sizes n=1,2,3,4 (2,16,512,65536 matrices); direct grid-state permutation counts matched graph minimizer matchings at every case, including 4160 no-state matrices at n=4, 15432 unique and 45944 multiple. This finite test corroborates, but is not the universal proof.

## originality

PASS

The precise fixed-diagram minimizer bipartite-graph equivalence and zero/one/many classifier resolve a decision ambiguity explicitly noted by the source; only standard combinatorial matching theory is reused.

## value

PASS

The exact zero/unique/multiple fixed-diagram decision procedure closes an explicit ambiguity in a recent grid-knot state algorithm, is reusable for all winding matrices, and yields explicit alternating-cycle witnesses; this is mathematically motivated despite using classical matching theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
