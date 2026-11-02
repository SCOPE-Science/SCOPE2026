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

For flag-regular full-dimensional Euclidean P, face-center c_F lies in the relative interior of F-exposing normal cone; regular orthoscheme flag-reflection symmetry forces its ray to the face-center ray. In every characteristic simplex associated to v=edge[v,u] subset faces, v remains nearest and u second-nearest: squared distance differences are affine; at v their gap is edge length squared, at all higher face centers both are minimizing co-nearest. Hence (D2^2-D1^2)/s^2 equals first barycentric coordinate lambda_0 on every simplex. Uniform measure restricts to uniform simplex and lambda_0~Beta(1,d), independent of simplex volume. Boundary sets null. Independently verified exact cube formula Z=1-max/min? Specifically for cube [-1,1]^d Z=min_i |X_i| (nearest two vertices differ by flipping minimum absolute coordinate), with s^2=4, yielding P(Z>t)=(1-t)^d, and bounded Monte Carlo d=2,3,4,6.

## originality

PASS

Characteristic orthoschemes and Dirichlet(1,...,1) barycentric law are textbook ingredients, but their combination with Voronoi first/second vertex order gives an all-regular-polytope shape-independent Beta(1,d) invariant. Prior regular-polygon distance papers fix a reference point and random locations, not two closest fixed vertices; regular polytope mean width/Gaussian extrema are different observables. Possible alternative Voronoi margin wording is residual priority risk.

## value

PASS

A distributional universality theorem across all regular polygons, Platonic solids and higher-dimensional regular polytopes, including all moments and dimension-only tails for a geometrically natural nearest/second-nearest squared-distance statistic; not a numerical sample or arbitrary invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
