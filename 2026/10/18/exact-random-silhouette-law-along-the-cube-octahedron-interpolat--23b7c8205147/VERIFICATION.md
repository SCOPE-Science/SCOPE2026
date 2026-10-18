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

# Reproduction and verification

Run `python verify_silhouette_law.py` using Python 3 and the standard library; no external packages, downloads, or specialized proof software are needed.

The checker enumerates exact rational vertices from all feasible triples of supporting planes, derives the facet-adjacency graph independently, and verifies the two lists agree at parameter values \(1,6/5,3/2,9/5,2,11/5,5/2,14/5,3\). It then compares the shadow-edge sign test with **independently projected exact rational two-dimensional convex hulls**, including all 96 signed-permutation representatives for the two orientation chambers and additional sampled rational normal vectors. A separate seeded Monte Carlo sample of 400000 Gaussian vectors compares the predicted exact spherical probability with an empirical frequency; it does not establish that probability mathematically.

Successful actual checker output included:

```
HALFSPACE_AND_EDGE_GRAPH_OK 1 vertices 6 facets 8 edges 12
HALFSPACE_AND_EDGE_GRAPH_OK 6/5 vertices 24 facets 14 edges 36
HALFSPACE_AND_EDGE_GRAPH_OK 3/2 vertices 24 facets 14 edges 36
HALFSPACE_AND_EDGE_GRAPH_OK 9/5 vertices 24 facets 14 edges 36
HALFSPACE_AND_EDGE_GRAPH_OK 2 vertices 12 facets 14 edges 24
HALFSPACE_AND_EDGE_GRAPH_OK 11/5 vertices 24 facets 14 edges 36
HALFSPACE_AND_EDGE_GRAPH_OK 5/2 vertices 24 facets 14 edges 36
HALFSPACE_AND_EDGE_GRAPH_OK 14/5 vertices 24 facets 14 edges 36
HALFSPACE_AND_EDGE_GRAPH_OK 3 vertices 8 facets 6 edges 12
ALL_96_SIGNED_CHAMBER_REPRESENTATIVES_CHECKED_OK
EXACT_RATIONAL_HULL_VS_EDGE_SILHOUETTES_OK 2358
SPHERICAL_CONE_SOLID_ANGLE_AND_HAAR_CHECK_OK 0.649040687816356 0.649977
ALL_CUBE_OCTAHEDRON_SHADOW_CHECKS_OK
```

The full continuum classification is justified by the symbolic sign-chamber argument and spherical-triangle solid-angle computation in `RESULT.md`, not by finite testing. No independent audit has been performed. Historical priority is provisional.
