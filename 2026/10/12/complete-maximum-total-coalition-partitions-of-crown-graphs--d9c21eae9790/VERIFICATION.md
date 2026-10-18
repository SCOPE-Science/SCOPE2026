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

Write the crown H_n=K_{n,n}-M on opposite size-n sides A,B. For n>=5 and any S, every vertex (including those in S) has a selected neighbor iff |S∩A|>=2 and |S∩B|>=2: with at least two selected opposite vertices at most one is the deleted partner, and if at most one opposite selected vertex its own matching mate has no selected neighbor. In a total-coalition partition P, each block alone fails this predicate but has a distinct partner meeting both inequalities jointly. Let deficit s=2n-|P|=sum_B(|B|-1) and let non-singleton-vertex total <=2s. The standard two opposing mixed triple construction yields 2n-4 blocks, hence optimal P has s<=4, and for n>=5 some singleton exists. If one side had no singleton, a singleton on the other forces a partner with at least two vertices on the missing-singleton side; saturating the <=4 deficit with its own partners and a pure block leaves a forced singleton on the first side, contradiction. Therefore both sides have singletons; their partners must be distinct blocks of respective mixed occupancies (2,1) and (1,2), each costing >=2 deficit, so s>=4. Equality forces exactly two triple blocks, all others singleton, with n-3 singleton blocks of each color. Choice count C(n,2)*n*(n-2)*C(n-1,2), no double-counting because the triple profiles distinguish them. Coalition edges connect opposite-profile triple hubs to each other and n-3 singleton leaves each, and no others: a double-star. Independent arithmetic gives 900,3600,11025 for n=5,6,7; actual embedded verifier exhaustively checks n=5 all partitions and candidate-size partitions for n<=7, but those bounded tests are not the universal proof.

## originality

PASS

The scalar optimum 2n−4 and a two-mixed-triple construction already follow from 2025 Brešar–Henning–Samadi Theorem 5.3 for total k=2 coalitions of complete bipartite K_{n,n}, whose feasibility predicate agrees with ordinary total domination of the crown. The source’s proof exhibits an extremal example but does not enumerate all extremizers or force the shape/coalition graph in that case; thus it does not imply the number C(n,2)n(n−2)C(n−1,2) or unique double-star partnership. Another 2024 double-total-coalition article gives same scalar/prototype. Broader crown domination papers found by Resultary concern different invariants; the full equality classification/graph and labeled count are not found. Possible unindexed extremizer classifications remain a residual risk.

## value

PASS

Classifying all optima of a natural perfect-matching-deleted complete bipartite graph is a mathematically motivated equality case, beyond recalculating the known scalar. It gives exact labeled optimizer entropy/polynomial count and the rigidity of the associated coalition graph despite multiple distinct partitions, natural invariants in the existing total-coalition graph literature. A complete all-n classification need not prove a downstream theorem to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
