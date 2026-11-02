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

Run `python3 verify_icosidodecahedron.py` with Python 3's standard library. The program reconstructs, over the exact quadratic field \(\mathbb Q(\sqrt5)\), the twelve icosahedral vertices and thirty original edges, twenty supporting triangular facets and twelve supporting pentagonal facets of their midpoint hull, all thirty rectification vertices, and exactly sixty section-relevant edges. Every facet-supporting inequality and every radial neighbor-pair cross product is checked exactly; it also checks the equal-radius edge angle \(\pi/5\). Four rational generic plane normals and fifteen thousand random plane normals are secondary checks. The full analytical proof of orientation-independent section complexity and the Crofton expectation is given in `RESULT.md`; no finite experiment stands in for that argument.

Expected successful output:

```text
EXACT_TWENTY_TRIANGLE_TWELVE_PENTAGON_SUPPORTING_FACETS_PASSED
EXACT_RECTIFIED_ICOSAHEDRON_30_VERTICES_60_EDGES_PASSED
EXACT_RADIAL_OPPOSITE_NEIGHBOR_PAIRING_AT_ALL_30_VERTICES_PASSED
EXACT_EDGE_CROFTON_ANGLE_PI_OVER_FIVE_AND_MEAN_TWELVE_PASSED
FOUR_EXACT_GENERIC_NORMAL_SECTION_COUNTS_TWELVE_PASSED
FIFTEEN_THOUSAND_INDEPENDENT_GAUSSIAN_NORMAL_DIAGNOSTICS_PASSED
ALL_CHECKS_PASSED
```

No independent audit has been performed. Historical priority, especially in specialist older geometric-section literature, remains provisional. The result excludes normal directions perpendicular to any vertex vector; it makes no claim about exceptional degeneracies.
