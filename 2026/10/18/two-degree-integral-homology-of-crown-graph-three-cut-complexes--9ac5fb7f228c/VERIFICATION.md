---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Directly reconstructed the connected/disconnected triple iff test for the crown adjacency i!=j. The dual forbids all disconnected triples; its faces are the two-row capacity-(2,2) chessboard complex X_n plus exactly n isolated matched-pair edges, with no additional higher faces involving matched pairs. Verified the cited Theorem 4.4 shellability threshold n>=2+2+2-1=5 in its original proof. Since X_n is pure 3-dimensional and shellable, its integral homotopy is a wedge of 3-spheres; the exact four face counts yield B_n by reduced Euler characteristic. Each added edge joins vertices in path-connected X_n and contributes a circle. Integral combinatorial Alexander duality on 2n vertices gives H_j(K;Z)=H^{2n-j-3}(K^*;Z), including free groups and zero elsewhere. Every disconnected triple is a facet complement (pure dim 2n-4); every complement of >=5 vertices contains a same-side triple and provides the complete (2n-6)-skeleton. B_n>0 implies nonshellability.

## originality

PASS

Best-of-knowledge: the actual crown Alexander-dual decomposition X_n with n matched-pair edges and consequent free integral two-degree homology are not implied by the published complete-bipartite/prism classifications nor by the cited core shellability theorem alone. Structural construction and degree n top classes are distinct; residual alias/unindexed priority risk remains.

## value

PASS

Exact integral homology for a natural infinite crown family K_{n,n}-M, a symmetric deletion of a perfect matching from a classical benchmark graph. The new graph-to-dual decomposition explains structural non-shellability and the appearance of n top-degree classes absent for complete bipartite graphs, beyond a routine table calculation. A future researcher studying graph cut complexes, edge deletions, or representation of bipartite double covers can use the precise groups and n>=5 boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
