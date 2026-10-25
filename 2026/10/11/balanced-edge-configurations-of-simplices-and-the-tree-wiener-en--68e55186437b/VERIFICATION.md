---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Every selected point has barycentric mass with sum (n-1)/n at each vertex; no simplex vertex can occur. If the n-vertex support multigraph (n-1 chosen edge points) were disconnected, a component of k between 1 and n-1 vertices would contain k(n-1)/n edges, impossible by integrality and gcd(n,n-1)=1. Hence it is a simple spanning tree. A cut isolates k-1 other edge points; their barycentric mass forces the unique fractions (n-k)/n and k/n. The converse holds because the branches of each vertex partition the remaining n-1 vertices. Distinct edge supports yield distinct sets and Cayley gives n^(n-2). For a regular simplex, centered Gram coordinates give squared radial displacement; sum of k(n-k) across tree cuts is the Wiener index, and the zero-mean pairwise polarization identity yields the stated energy. Elementary sharp Wiener bounds with equality give paths at the energy minimum and stars at the maximum (n=3 overlap). Independent exact-rational reconstruction tested all 1440 labeled trees at n=3,4,5,6, confirming each cut weight, centroid, Wiener sum, direct pairwise energy, extrema and multiplicities; finite checks corroborate but cannot prove the universal result.

## originality

PASS

Independent statements-and-implications comparisons found the general existence theorems but no already published theorem giving the complete centroidal tree-indexed solution fiber and its exact energy/Wiener correspondence. Resultary returns the focal result as the only direct match and related zonotope/matroid results concern distinct objects or metrics. The classical tree count and Wiener bounds are not credited as new. Historical flow-zonotope alias coverage remains a genuine residual risk.

## value

PASS

Balancing equal point masses on a polytope one-skeleton is a published geometric problem. Its canonical simplex-centroid instance admits a complete all-dimensional classification of every solution, explicit tree-cut barycentric positions and exactly n^(n-2) distinct sets. Summed squared pairwise separation is a natural regular-simplex configuration statistic; identifying it exactly with the tree Wiener index transfers substantive path/star rigidity to Euclidean geometry. This motivated exact family result is not merely an isolated table, renaming of Cayley or a minor gain; it is useful without requiring an additional downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
