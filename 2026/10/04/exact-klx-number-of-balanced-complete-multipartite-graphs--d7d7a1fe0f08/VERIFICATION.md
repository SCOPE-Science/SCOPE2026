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

The DFS comparability property forces every branch vertex in a complete multipartite graph to have only singleton child subtrees: different child roots must lie in one part, while any proper descendant of one child lies outside that part and would be adjacent to a vertex in another child subtree. Thus every DFS tree is a spine with at most a terminal fan. For \(r\ge3\) the spine crosses the middle cut. At a prefix of size \(t\), the cut is \(t(N-t)-\sum_i x_i(m-x_i)=t(N-m-t)+\sum_i x_i^2\), minimized by balanced part counts, yielding the stated lower bound. The cyclic Hamiltonian DFS path has balanced prefixes; its cut increment formula is nonnegative up to the midpoint and symmetric thereafter, so its maximum equals the same middle-cut value. Because a path has no enveloping contribution beyond crossing back edges, the upper and lower bounds match.

## originality

PASS

The KLX parameter was introduced in 2026. Its full primary paper characterizes small KLX values and gives algorithmic/tree-width results but contains no complete, bipartite, or multipartite exact-family formula. The closest published SCOPE result gives exact KLX only for cliques and complete bipartite graphs. Classical spanning-tree congestion does have complete-multipartite formulas, but minimizes over all spanning trees rather than ordered DFS trees and therefore does not imply the DFS-restricted KLX value. The submitted balanced \(r\ge3\) theorem requires a new DFS-tree structure reduction plus a balanced middle-cut argument.

## value

PASS

Balanced complete multipartite graphs are a canonical dense family beyond the previously solved clique and biclique boundaries. The exact KLX formula exposes how the DFS constraint forces a long spine and a balanced middle-cut bottleneck, a structural phenomenon not captured by ordinary spanning-tree congestion. This is a natural complete classification for a newly introduced invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
