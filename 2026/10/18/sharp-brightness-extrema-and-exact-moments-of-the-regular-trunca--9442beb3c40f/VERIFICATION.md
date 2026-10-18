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

The exact proof is given in `RESULT.md`. Run `python3 check_brightness.py` from the same directory; it uses only Python's standard library. Observed successful execution:

`TRUNCATED_OCTAHEDRON_BRIGHTNESS_OK vertices=24 edges=36 facets=14 directions=1500 projection_hulls=6 pair_classes=3/6/12 quadrature_nodes=259200`

`area_range=5.656854249492..7.141428428543 mean=6.696152422707 second=44.931769717265 variance=0.093312449145`

The two-chamber extremal proof and the exact spherical moment kernel are mathematical arguments; finite numerical checks are corroboration, not exhaustive proof for continuously many orientations. No independent audit, publisher priority certification, or finite-sample statistical guarantee has been performed.
