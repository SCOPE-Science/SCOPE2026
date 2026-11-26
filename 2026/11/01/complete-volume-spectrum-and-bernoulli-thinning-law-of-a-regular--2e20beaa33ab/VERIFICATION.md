---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently re-enumerated all 4096 masks with exact determinant arithmetic in Z[sqrt(5)] on doubled coordinates. A mask is three-dimensional exactly when at least one affine four-point determinant is nonzero. For each full-dimensional hull, sign-homogeneous supporting triples identify the facets, deduplicated by their planar vertex sets. The common circumsphere excludes three collinear vertices. Taking any selected off-plane point as a witness, exact determinant signs identify the perimeter edges of each facet. A fan from a facet vertex gives the boundary triangles; coning these to the strict interior barycenter of the selected vertices yields tetrahedra with disjoint interiors. Summing their absolute affine determinants avoids the source verifier's oriented volume sum about the origin. The replay checks each boundary edge has two incident facets and the Euler count, reverses the factor of eight from doubling, and converts exactly to six-volume pairs in 1,phi. All printed census rows and expectation coefficients agree, including the 29 values, coefficient divisibility, and the separate mask identities for 12 five-neighbor rings, their 60 distinct planar four-subsets, and 15 additional antipodal-pair planes. No six-or-larger mask has zero volume. An individual labelled mask of size k has weight p^k(1-p)^(12-k), so the exact mass and expectation polynomials, including their deterministic endpoint cases, follow by summation. At p=1/2 exact arithmetic independently gives 3710 full-dimensional masks, E[V]=(4601+7113 phi)/3072, and relative volume (2089+2512 phi)/20480.

## originality

PASS

Two previously indexed tables are exact subfamily overlaps: the entire four-vertex layer and the 64 six-vertex transversals of the antipodal pairs. These data and the general Bernoulli sampling model are credited. The supported distinct result is the complete joint cardinality–volume census on all masks, especially the uncovered parts of layers k≥5, which determines the entire Bernoulli volume law. The novelty is the specific exact data, not the hull algorithm or probability reweighting.

## value

PASS

Vertex retention is a natural model and the whole icosahedron, rather than a handpicked slice, gives a complete exact small-solid benchmark for volume under thinning. The joint data distinguish masks with the same retained count but different volumes and masks of different counts with equal volume; they supply exact atoms, expectation and the dimension-collapse probability for every p. Neither the isolated tetrahedral spectrum nor the antipodal-transversal layer gives these probabilities. The geometric description of all lower-dimensional exceptions is useful beyond a numerical hull histogram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
