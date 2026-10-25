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

# Verification record

The analytic certificate is the facet-pair incidence count, the exact spherical-chamber decomposition, the three-ray solid-angle identity, and a separate mean-count derivation by individual edge crossings. No computer search or numerical approximation is used for those infinite-domain arguments.

To reproduce ancillary checks, run `python3 verify.py` with Python 3.9 or newer and its standard library. On the inspected copy the program reported:

```
EXACT_24_VERTICES_36_EDGES_EQUAL_VERTEX_AND_EDGE_DOT_PRODUCTS_OK
INDEPENDENT_EXACT_INTEGER_EDGE_CROSSING_VERSUS_FACE_FORMULA_OK 13297 {6: 8756, 10: 1771, 8: 2770}
SPHERICAL_TRIANGLE_CLOSED_FORM_AND_INDEPENDENT_EDGE_MEAN_IDENTITY_OK {6: 0.498450689918, 8: 0.31610885558, 10: 0.185440454502}
INDEPENDENT_PROJECTIVE_SPHERICAL_AREA_QUADRATURE_OK
INDEPENDENT_UNIFORM_SPHERE_HAAR_SAMPLING_OK 250000 {10: 46605, 6: 124422, 8: 78973}
ALL_TRUNCATED_OCTAHEDRON_CENTRAL_SECTION_LAW_CHECKS_OK
```

The rational-grid test is not exhaustive over all directions; the seeded Monte Carlo test has ordinary finite-sample uncertainty; double-precision quadrature cannot independently certify equality of exact constants. The proof in `RESULT.md` covers all generic orientations analytically. Independently performed mathematical validation is not claimed.
