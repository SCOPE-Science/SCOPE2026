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

# Reproducibility

Run `python3 verify.py` with the Python 3 standard library; this file is embedded alongside the mathematical exposition. All comparisons of expressions \(a+b\varphi\), where \(\varphi^2=\varphi+1\), are exact integer operations. There is no numerical tolerance.

The code reconstructs the original twelve vertices, thirty length-two edges, thirty edge-sum vertices and complete thirty-two-facet hull, including its twelve pentagonal and twenty triangular facets. It checks all 360 original-vertex reflection incidences, identifies one generic direction with \((3,7)\) illumination counts, and verifies the four generic integer directions cover every polar vertex (five-valent count one each; three-valent counts twelve once and eight twice). It also checks 150 generic test directions for additional diagnostics; those samples are not used for global coverage.

Expected successful output:
```
EXACT_OK original_vertices=12 roots=30 hull_facets=32 pentagons=12 triangles=20
EXACT_OK reflections=30x12 generic_incidence=(3,7) witnesses=4 min_vertex_coverage=1
EXACT_OK ordinary_illumination=4 fractional_illumination=4
```

The global statement for all generic directions is a theorem about connected reflection chambers; it does not follow from 150 tests. The count for all directions is extended using strict-inequality continuity. Neither external mathematical priority nor independent proof audit is asserted.
