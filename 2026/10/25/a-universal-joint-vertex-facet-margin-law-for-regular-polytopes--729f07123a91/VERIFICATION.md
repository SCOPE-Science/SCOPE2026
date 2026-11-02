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

For a full-dimensional Euclidean flag-transitive regular d-polytope d>=2 and a volume-uniform X, compare squared distances to all vertices (equal vertex norms) and slacks to all supporting facet hyperplanes (unit normals, equal inradius). On each characteristic simplex of a complete face flag, the nearest/second-nearest vertex squared-distance difference is s² times barycentric coordinate lambda_v: all comparisons are affine, v is nearest at every simplex vertex and flagged edge-neighbor w is next, with exact gap s² at v and zero at other flag-face centers. Dual argument on ridge-adjacent facets gives slack difference q lambda_F, q>0 at the flagged facet center. Thus U=lambda_v, V=lambda_F have Dirichlet(1,1,d-1) marginal pair on each volume-uniform d-simplex; mixing flag simplex volumes preserves it. This proves survival (1-u-v)^d on nonnegative simplex and zero beyond, beta marginals, covariance -(d+1)^(-2)(d+2)^(-1), correlation -1/d, and joint exponential scaling. Independently simulated 80,000 uniform tetrahedron points, finding normalized means .2514,.2508 and correlation -.3312 versus .25,.25,-1/3; this diagnostic is not the proof.

## originality

PASS

Known flag subdivision and Dirichlet coordinates are standard, and an isolated nearest-vertex margin beta marginal may be known; this claim is the *joint primal–dual* law with facet supporting-hyperplane slack and exact negative dependence. Bäsel 2012 computes regular polygon line chords and two-point distances; Kabluchko–Litvak–Zaporozhets 2015 analyze Gaussian directional widths, neither a uniform interior point’s two order-statistic margins. Searches for same normalization and joint dependency returned no dominating prior result, with bibliographic uncertainty retained.

## value

PASS

This exact finite/all-dimensional joint geometric-probability law links two canonical Voronoi-type margins for every regular Euclidean polytope, including exceptional 3D/4D cases; support U+V<=1, covariance, and independent-exponential scaling give structural information absent from either isolated beta marginal. The invariant and objects are natural and the dependence is not a routine independent product.

The dated certificate retains the supplied scientific assessment, sources and limitations.
