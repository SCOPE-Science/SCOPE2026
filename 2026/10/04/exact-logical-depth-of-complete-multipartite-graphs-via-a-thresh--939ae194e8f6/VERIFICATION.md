---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

On a complete multipartite graph, equality-or-nonadjacency is exactly an equivalence relation whose classes are the parts, and adjacency is quantifier-free recoverable. For all nontrivial targets the candidate defining rank is at least three, so a rank-three transitivity sentence for equality-or-nonadjacency excludes arbitrary non-multipartite competitors without increasing the rank; the one-vertex case is immediate. The rank-\(q\) Ehrenfeucht-Fraïssé profile for one finite equivalence relation is correctly encoded by the truncated cumulative counts \(N_k\) and exact counts \(C_k\). Rewriting same-profile competitors in cumulative-count differences gives precisely the stated pinned, tight one-sided, exact-edge, and slack constraints. Zero upper and lower bounds propagate in the two directed paths, and failure of either propagation leaves a one-unit feasible perturbation; successful propagation forces every difference to zero. The frozen checker was inspected and tests both the EF-profile equivalence and path criterion on bounded exhaustive families; an additional independent symbolic/small-case reconstruction in this run agreed with the profile mechanism. Finite checks are only corroborative.

## originality

PASS

Pikhurko-Veith-Verbitsky provide general graph logical-depth and similarity-class bounds; accessible source text around Theorem 4.1 gives exactness under a dominant homogeneous-class condition but does not state an exact all-partition formula. Tenney's full first-page/intro material shows a second-order decidability application for one equivalence relation rather than the first-order defining rank of each finite partition. Targeted Resultary searches over complete multipartite, cluster-graph, finite-equivalence-relation, and quantifier-rank terminology did not locate a prior threshold-path criterion or equivalent full classification. The broader exact result is therefore not implied by the inspected sources, with explicit folklore risk retained.

## value

PASS

Logical depth is a standard descriptive-complexity invariant and complete multipartite graphs form a canonical symmetry-rich class. The theorem gives a complete exact classification for every heterogeneous part-size multiset, recovers important subfamilies, and turns the answer into a linear-time two-pass criterion. That is a natural structural result, not an arbitrary finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
