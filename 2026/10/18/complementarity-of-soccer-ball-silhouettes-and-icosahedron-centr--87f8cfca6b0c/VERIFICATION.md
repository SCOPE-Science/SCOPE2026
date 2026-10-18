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
# Reproducibility and limits

Run `python3 verify_soccer_icosahedron.py` from this package. The standard-library script reconstructs twenty exact triangular faces and thirty original edges, followed by ninety truncated edges and thirty-two exhaustive sign-chamber representatives in \(\mathbb Z[\sqrt5]\). It checks the face-normal and original-normal sign changes and the resulting \(N_T+S_I=30\) identity on every representative, with all signs decided by integer comparisons. It checks the pairwise axis geometry and spherical areas, then tests four thousand independent, newly projected convex-hull silhouettes as a supplementary numerical cross-check.

Successful replay produced: `EXACT_FACE_EDGE_GRAPH_OK`, `EXACT_SIX_AXES_GENERAL_POSITION_OK`, `EXACT_32_CHAMBER_REPRESENTATIVES_AND_COMPLEMENTARITY_OK`, `EXACT_20_CENTRALLY_SYMMETRIC_HEXAGON_FACES_OK`, `EXACT_SPHERICAL_CHAMBER_LAW_OK`, `INDEPENDENT_4000_PROJECTED_CONVEX_HULLS_OK`, and `ALL_SOCCER_SILHOUETTE_CHECKS_OK`.

The analytical proof needs the geometric reason that passing a hexagon-normal wall preserves the silhouette count, and the finite exhaustive mask construction. The four thousand floating-point projections are corroboration rather than an infinite proof. The formula excludes directions normal to original vertices and to truncated facets. The spherical-area fraction was published earlier for the icosahedron's central section, and is used, not freshly discovered. Historical priority is provisional; independent audit has not been performed.
