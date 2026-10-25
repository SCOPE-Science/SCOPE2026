---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The analytical theorem follows from (i) the barycentric half-space description of simplex intersections, (ii) the exact Euclidean radial covariogram integral, (iii) the maximum of finitely many subset-gradient linear forms, (iv) a geometrically justified interval of pairwise disjoint first caps, and (v) an elementary beta-function limit. These are complete proof steps for every integer dimension at least three. The numerical program verifies examples and does not independently certify the infinite-dimensional theorem or establish historical novelty.

The standalone file `simplex_distance_checker.py` uses Python 3, NumPy and SciPy. Execute `OPENBLAS_NUM_THREADS=1 python simplex_distance_checker.py`. It independently constructs original/translated facet half-spaces and enumerates the feasible intersection vertices; ConvexHull volumes test the closed simplex covariogram. For tetrahedra it separately performs Sobol-sphere integration of the radial correction and compares with the analytically integrated cap expression. The tested polyhedra are an orthogonal-coordinate tetrahedron, a regular tetrahedron, a scalene planar triangle (control only), and a four-dimensional coordinate simplex. Direct numerical cap integrals also verify the predicted power and leading coefficient. In the checked execution all four cases reported `INTERSECTION_AND_CAP_CHECK_OK`, ending in `SIMPLEX_DISTANCE_ONSET_CHECK_OK`.

The first branch is certified analytically only until the explicitly defined positive threshold \(\(r_1\)\). The later distribution remains outside scope. Independence of scientific review and priority certification have not been established.
