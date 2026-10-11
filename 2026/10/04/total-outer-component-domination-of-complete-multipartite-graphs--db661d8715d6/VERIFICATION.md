---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

In a complete multipartite graph, a selected set is total dominating exactly when it meets at least two partite classes. A nonempty complement induces one connected component exactly when it meets at least two parts or is a singleton; if it lies in one part with \(c\) vertices it has exactly \(c\) components. These two equivalences immediately give the profile criterion and every coefficient. For \(k\ge2\), the complement must be exactly \(k\) vertices of one part. When there are at least three parts, deleting an entire part still leaves selected vertices in at least two other parts; in the bipartite case it does not, which forces the strict endpoint. The published \(K_{m,n}\) formula therefore fails at \(k=n\), and the source's own \(C_4\) theorem independently exposes that conflict. The frozen exhaustive verifier matches the formulas for every multipartite profile through order ten.

## originality

PASS

The defining 2016 paper introduces the parameter and gives exact values for complete and complete-bipartite graphs, but not arbitrary complete multipartite graphs or an all-set enumerator. More importantly, its Proposition 3.2 includes the endpoint \(k=n\) for \(K_{m,n}\), while at that endpoint the proof's proposed selected set is an independent part and is not total dominating. The same paper's Theorem 2.6 gives \(\gamma_{tc}^2(C_4)=0\), confirming the boundary inconsistency. Fresh Resultary comparison found no later source that both repairs this endpoint and supplies the multipartite enumerator.

## value

PASS

Correcting the feasibility endpoint of the defining published exact family is mathematically meaningful, and the complete multipartite support theorem explains the error structurally while upgrading scalar minima to an exact bivariate enumeration of every feasible set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
