---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For all n≥3 and permutations phi, spoke s_i conflicts only with o_i sharing tail and t_i sharing head after reindexing inner rim; the ONLY directed cycles in an admissible partial injection are the full coherent outer and inner rims. Local join has five faces per index; excluding the two full rims yields 5^n−2^(n+1)+1 augmented faces. Decompose X=L∪W where L=∂Δ(O)*∂Δ(T)=S^(2n−3), W=union of closed spoke stars, with every nonempty intersection contractible and nerve a full simplex, hence W contractible. Overlap B=L∩W covered by n simplices with nerve ∂Δ^(n−1)=S^(n−2). Cofibration pushout and nullhomotopic B→L (dimension n−2<2n−3) give wedge S^(n−1)∨S^(2n−3). Reindex t_i makes phi immaterial. Independent 5-letter local enumeration returned 110,594,3062,15498 faces for n=3,4,5,6 as formula predicts; source direct directed graph-vs-local checker covers small cases. Infinite result relies on exact topological cover, not enumeration.

## originality

PASS

Underlying object is the multipath/acyclic partial injection complex on two coherently oriented n-rims and one outward perfect matching, equivalently a path-system complex with local 3-arc exclusions and two full-rim circuits. Compare graph not ordinary undirected matching complex. General 2022 multipath-complex framework and 2026 bidirectional polygon computations do not include the coupled one-way matching of two coherent cycles. Bidirectional means two arcs per edge, incompatible with only one rim orientation here. The single directed-cycle formulas cannot be joined naïvely because s_i shares both a tail and an inner head and forbids local configurations; proof uses the two-star-cover pushout, not a graph-family inclusion theorem.

## value

PASS

A uniform integral homotopy splitting for coherent double-cycle ladders resolves nontrivial interactions between spoke matching, two forbidden directed rim cycles and path compatibility. Permutation independence is a structural result applicable across circular ladders and generalized Petersen orientations; two different-dimensional sphere summands are not just a numerical homology census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
