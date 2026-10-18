---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For every n≥4, crown Cr_n=K_{n,n} minus the perfect matching and the source TRDF definition, a positive support must include at least two vertices from each shore. Weight≤5 is impossible because a unique 2-defender would require all vertices on its own shore positive, violating the four-support bound (including n=4). A weight-six witness with a_i,b_j labeled 2 and a_j,b_i labeled 1 for i≠j gives gamma_tR=6. All minimum functions use exactly two 2s on opposite shores: for i≠j the cross 1s are forced; for i=j any p,q≠i provide 1s; count n(n−1)+n(n−1)^2=n²(n−1). Encode removed edges a_p b_q as directed arcs. If every minimum function is destroyed, zero-outdegree set O and zero-indegree set I are disjoint and all I→O arcs deleted. For a=|O|≥1,b=|I|≥1,k=n−a−b, |F|≥ab+k=n−1+(a−1)(b−1). If fewer than n−1 edges deleted these O and I are indeed nonempty. A directed edge 1→2 plus cycle on vertices 3..n removes n−1 edges, leaves each original vertex at least n−2 incident edges, destroys all min functions; edge deletion cannot decrease gamma_tR. Therefore b_tR(Cr_n)=n−1. Independent exhaustive TRDF and deletion-set enumeration n=4,5 reproduces optimizer counts and sharpness, but arbitrary n is proved by directed arc argument.

## originality

PASS

The initiating 2026 total-Roman-bondage article supplies the complete-bipartite baseline b_tR(K_{n,n})=n and a comparison with ordinary total bondage. A different prior crown theorem gives b_t(Cr_n)=2n−3; neither implies the sharper new value n−1 or classifies the n²(n−1) exact minimizers. Published Resultary crown entries involve perfect Roman domination, restrained domination, CIS properties and other invariants, not total Roman bondage. Best-of-knowledge PASS with acknowledged name-alias indexing risk.

## value

PASS

The crown is the canonical complement of a perfect matching within a balanced complete bipartite graph, and deleting that matching changes the exact total-Roman bondage from the known n baseline to n−1. The optimizer classification and deleted-edge survival characterization provide structural information and a sharp infinite-family robustness result; this is not an arbitrary small graph calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
