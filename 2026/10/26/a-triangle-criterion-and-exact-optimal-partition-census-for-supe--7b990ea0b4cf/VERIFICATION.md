---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The complement of any super-dominating union omits at most two vertices; one-vertex deletions always qualify and two-vertex deletions qualify exactly at B-edges. In a four-block partition, choosing a largest block L of size>1 forces other three blocks singleton; each singleton requires a union with L and hence its opposite pair to be a B-edge, giving precisely a triangle. A nonedge yields an admissible three-block partition; when B complete, two disjoint two-sets and a remainder work because each part has at least one partner (not because every union must qualify). For three blocks, admissibility is equivalent to at least two singleton-or-B-edge small blocks and a nonsuper remaining block; counting pair types yields C(n,2)+(n-3)e+m2-2*[n=5]m2-2*[n=6]m3. Complete-multipartite case reduces B to edges between distinct qualifying non-singleton parts. Independent direct graph/set-partition enumeration checks the counting at small n.

## originality

PASS

Best-of-knowledge source/implication comparison: The sharp-bound saturation theorem has more information than the general inequality, so it is not equivalent to the earlier bound. The multipartite deletion characterization is credited as prior, but neither cited theorem covers the B-triangle and matching enumeration on every isolate-free gamma_sp>=n-2 graph. All specific risks are retained; inaccessible literature alone did not determine the outcome.

## value

PASS

Sharp attainment criterion and exact extremizer/census formulas for a natural near-maximal domination regime on every finite graph, plus infinite-family multipartite specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
