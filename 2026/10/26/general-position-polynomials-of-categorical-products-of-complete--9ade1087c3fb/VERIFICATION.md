---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For categorical K_p x K_q with p,q>=3, adjacency iff row and column both differ, so distance 2 precisely for same row/column pairs. A general-position set is exactly an induced P3-free cluster graph. Its components are exclusively an independent row/column layer, a partial/complete 2x2 rectangle (one or two edge components), or a transversal clique using distinct rows/columns. Counting disjoint types gives Ψ=1+pq z+Σ_{k>=2}(p C(q,k)+q C(p,k))z^k+2R z²+4R z³+R z⁴+Σ_{k>=3}C(p,k)C(q,k)k!z^k, R=C(p,2)C(q,2). The inclusion-maximal polynomial M=p z^q+q z^p+R z⁴+C(max,min)min! z^min follows because only full layers, full rectangles and maximum transversals resist extension. For p>=4, q=2p+4, a_{p+1}=p C(q,p+1), a_{p+2}=p C(q,p+2)>a_{p+1}, but a_p>=p! C(q,p)>a_{p+1}; a sharp strict coefficient valley follows for every p>=4. Empty/singleton and p=q=3 overlap cases were checked, with no double count of edges/rectangles/cliques.

## originality

PASS

The earlier direct-product theorem of Di Stefano et al. proves gp^-(K_p x K_q)=min(p,q,4) and in its proof characterizes some maximal configurations (full layers, transversal cliques and rectangles); these prior combinatorial shapes are credited. The new part is the all-set polynomial, the complete maximal-set enumerator, and an infinite nonunimodality construction. Existing general-position-polynomial works address other graph classes, and the surveyed published SCOPE examples (spiders, coronas, complete multipartite variants) do not imply this direct-product enumerator.

## value

PASS

The complete all-set/general-position polynomial and exact maximal enumerator are natural graph invariants; importantly the concrete infinite family of connected vertex-transitive diameter-two graphs gives a strict nonunimodality counterexample outside previously studied trees. The specific coefficient valley is an independently useful exact obstruction and is not merely a known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
