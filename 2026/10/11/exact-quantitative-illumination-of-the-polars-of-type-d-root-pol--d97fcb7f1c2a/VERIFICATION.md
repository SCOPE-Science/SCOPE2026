---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

Reconstructed theorem for every integer d>=3 with Q_d={x:|x_i|+|x_j|<=2}. Its vertices are exactly 2d axis vertices ±2e_i and 2^d cube corners eps∈{±1}^d: points with max absolute coordinate <=1 lie in cube, while coordinates 1<a<=2 admit the displayed convex interpolation with ±2e_i. Axis vertices are uniquely maximizers of coordinates; each corner is uniquely determined by its simultaneous active pair inequalities. Gauge is 1/2 the sum of the two largest coordinate absolute values. The strict source criterion from active facet normals is (A) s p_i>2+max_{j≠i}|p_j| for axis and (C) s_i p_i+s_j p_j>2 for every i<j at corner. There can be at most one illuminated axis and two illuminated corners; two corners must differ in one sign. Each source lighting two corners has two common coordinates with magnitudes >2, hence gauge>2. An axis+corner source has a>2+b and 2b>2 so gauge>(a+b)/2>2. Axis+two corners forces different distinguished indices and a further common magnitude >2, giving gauge>3. A single vertex is illuminated only by exterior gauge>1. Thus every source lighting k>=1 vertices has gauge>k; summing over finite sources covering all vertices gives total cost >2d+2^d. Near-vertex radial sources (1+epsilon)v each cost 1+epsilon and light every boundary point through the vertex-to-face condition, giving an infimum <=2d+2^d. Equality is an infimum, not a source configuration attaining the lower bound. The proof covers boundary signs, all d>=3 and affine images without equating polar invariants. Reconstructed the exact 1658-byte verify.py Git blob and obtained VERIFY_OK 8452; separately checked 10000 independent rational sources over d=3..7. Finite tests are diagnostics; universal conclusion rests on the analytical inequality casework.

## originality

PASS

Best-of-knowledge PASS for the complete polar family: published 2012 and 2016 primary sources define exactly the weighted Minkowski-gauge illumination invariant and propose a three-dimensional upper bound 12, rather than calculating 14 for the rhombic dodecahedron. The 2012 Archimedean table gives the cuboctahedron (opposite polar) only an upper estimate 12. A separate published result determines the type-D root polytope gauge parameter, not its polar; the d=4 self-dual 24-cell is an overlapping case and is explicitly not claimed new. Published ordinary/fractional illumination studies optimize source count, not gauge-cost sum. The per-source strict efficiency obstruction and all-dimensional polar formula are not immediate corollaries of any checked stronger theorem. Priority remains limited by the named 2006 access gap and possible unindexed prior work.

## value

PASS

A natural, shape-specific exact invariant for the polars of type-D root polytopes is determined in all d>=3, with an explicit sharp source-efficiency obstruction and infimum construction. In d=3 Q3 is the rhombic dodecahedron and ill(Q3)=14, contradicting the precisely documented conjecture that all centrally symmetric 3D convex bodies have ill<=12. This distinguishes weighted quantitative illumination from the ordinary six-source illumination number and reveals nontrivial geometry of the polar rather than a table conversion. d=4 is an already known self-dual special case, but the d=3 counterexample and uniform d>=5 classification survive. No implication is asserted for universal upper bounds or unrelated norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
