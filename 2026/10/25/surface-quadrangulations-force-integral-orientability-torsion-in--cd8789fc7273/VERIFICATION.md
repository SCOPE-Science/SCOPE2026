---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For N≥8 closed cellular triangle-free quadrangulations with each C4 facial and no K2,3, the Alexander dual Y has all vertices/edges, induced-path triples (T=∑ binom(deg,2)), and 4-element faces exactly facial squares. Mantel excludes 5-faces. Each square tetrahedron has a unique free path-triangle; collapsing that pair then a diagonal/path triangle, and removing remaining unique-common-neighbor path triangles, retains exactly a face-triangulated Σ plus q=binom(N,2)−T extra chords. Every such chord adds a free S¹ summand: Y≃Σ∨∨^q S¹. Integral combinatorial Alexander duality gives H~_(N−5)=Z or Z/2 according to orientability, H~_(N−4)=Z^(q+2g) or Z^(q+h−1). The nonzero next-to-top group precludes shellability. A horizontal translation/glide-reflection quotient of Z² with m,n≥7 gives Klein bottle, q=N(N−13)/2, hence H~_44=Z/2 and H~_45=Z^883 for N=49. Independently checked all triangle and tetrahedron dual-face sets and q for the cube and the twisted 7×7 grid; structural proof, not these finite cases, covers the all-surface theorem.

## originality

PASS

QUALIFIED PASS. Bayer et al define k-cut complexes and give graph-family homology, including some torsion examples in high-k constructed graphs; these are not ordinary k=3 face-closed nonorientable quadrangulations. Their conditional torsion-free theorem needs skeleton conditions not satisfied here. The related published edge-disjoint-four-cycle 3-cut collapse is not applicable: quadrangulations have each edge in two facial squares, producing a persistent surface instead of graph. The 2-to-3-cut collapse in C4-free diameter-two graphs excludes every quadrangulation here. An integral orientability-dependent infinite torsion family is not implied by these results.

## value

PASS

The construction makes the geometry/topology of an embedded surface directly control the integral homology of a natural graph cut complex. The orientation-detecting order-two class is a structural distinction invisible over characteristic ≠2 and yields an infinite explicit family, not a routine instance of a known open-grid computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
