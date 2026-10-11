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

# Verification

Run `python3 verify_rhombicuboctahedron.py` in the directory containing the verifier and `collapse_certificate.json`; no non-standard dependencies are required.

Observed result: `VERIFY_OK: 24 vertices, 48 original edges, 18 squares, 8 triangles; scale-two face vector (24,132,248,186,48); 252 elementary collapses; 24-vertex 2-sphere triangulation; scale-one cycle rank 17`.

The verifier reconstructs the entire graph and all shortest-path distances, all threshold-two cliques, and a fixed triangulation of the 8 triangular plus 18 square facets. It checks every vertex link is a cycle and all edges have two incident triangles, then checks that each of the 252 certificate pairs is a currently free codimension-one pair. It checks the exact remaining simplices equal the target triangulation, not just matching face counts. The evidence establishes this finite claim, not general stability for other solids, other metrics, or threshold three. Independent audit has not been performed.
