---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The only vertex-disjoint odd cycles possible are the two triangles, joined by matching edges, so the odd-cycle criterion applies to the projective monomial model. The vertex differences span the full rank-five lattice. An independent exact computation builds the facet system from coordinate inequalities and x(S)<=x(N(S)) for independent S: for any weight vector nonnegative on each edge, its negative t-level set is independent and its neighbors lie in the positive t-level set; integration over t proves those inequality vectors generate the dual edge cone. This gives the stated facet supports, 135 nonempty faces and orbit counts (9,24,15); all simplicial cones pass saturation and the maximal singular face list matches exactly. The twelve unimodular triangles and three unit parallelograms give the stated projective embeddings and degree 18. For each of the fifteen normal cones, the four rays span the intrinsic rank-three lattice and have sole relation (+1,+1,-1,-1). The dual cone semigroup is the set of nonnegative integral quadruples with equal sums in the two groups; choosing pairs across groups generates it, with the single 2x2 binomial relation. Splitting off the two orbit directions and completing over their function field yields the claimed generic ring in any characteristic. Smoothness and Q-factoriality fail on exactly the same cones.

## originality

PASS

The supported contribution is the complete singular-support, projective degree, and saturated generic-transverse classification for the triangular-prism edge toric fivefold. The odd-cycle normality input, global simplicity tests and toric computation methods are known. The structurally closest indexed records concern different polytopes and have different component counts; the bounded comparison did not establish equivalent coverage.

## value

PASS

The triangular prism is a natural small nonbipartite graph with disjoint odd cycles and a normal edge embedding. Its complete singular support exhibits two kinds of projective surface closures with the same transverse singularity, and supplies explicit degree and local lattice data that global smoothness criteria do not predict. These are useful exact benchmarks for graph-toric singularities, not just an isolated facet count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
