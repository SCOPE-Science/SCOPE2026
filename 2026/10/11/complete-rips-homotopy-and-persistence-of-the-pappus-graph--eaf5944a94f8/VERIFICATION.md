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

Execute `python3 verify_pappus_rips.py` using only the Python standard library. The code defines the Pappus graph from its standard LCF presentation, independently reconstructs all 18 shortest-path distance rows, and checks that precisely six disjoint 3-vertex groups contain the distance-four pairs. Its graph-side partition test is the discrete input to the radius-two and radius-three homotopy arguments.

The code exhaustively enumerates all nonempty simplices at radii 1, 2, and 3, checking the exact face vectors `(18,27)`, `(18,81,108,18)`, and `(18,135,540,1215,1458,729)`. It verifies that the radius-two cover has no simplex containing two vertices from each color, that its mixed edges are the incidence edges, and that each of the 18 closed-neighborhood tetrahedra has a free triangular face. An independent triangle-relator elimination checks that a 17-edge tree together with the radius-two triangular relators kills all 64 other 1-skeleton edges, corroborating simple connectivity.

The exact mod-two boundary ranks are `(17)`, `(17,64,18)`, and `(17,118,422,793,665)`, giving Betti vectors `(1,10)`, `(1,0,26,0)`, and `(1,0,0,0,0,64)` at radii 1, 2 and 3 respectively. This agrees with the sphere-wedge homotopy calculations. The code also checks all 729 maximal 5-simplices at radius 3, each selecting one vertex from each distance-four triple.

A successful execution prints `VERIFY_OK`. The structural proof in `RESULT.md`, not finite numerical agreement by itself, establishes the integral homotopy type and all-field persistence. No independent external audit has been performed.
