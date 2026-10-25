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

The exact statements are proved by geometric convolution, localization to known maximizing directions, a two-chamber uniform expansion, and dominated convergence. A standalone Python 3 checker requires NumPy and SciPy and runs as `python3 verify_cube_section_tail.py` from this directory. The checker first constructs sections from actual intersections of cube edges with the random plane and compares 540 resulting convex-hull areas and vertex counts with the analytical chamber formula. It then integrates actual finite-threshold Haar probabilities of quadrilateral and hexagonal sections by one-dimensional root searches and quadrature. The scaled probabilities converge toward the two distinct theorem coefficients as the deficit decreases.

Expected terminal checks:

```
INDEPENDENT_CUBE_EDGE_INTERSECTION_AREAS_AND_FACE_COUNTS_OK 540
INDEPENDENT_EXACT_DIRECTIONAL_INTEGRATION_TAIL_COEFFICIENTS_OK
FOUR_VS_SIX_SIDED_ASYMPTOTIC_SPLIT_OK
ALL_CUBE_SECTION_TAIL_CHECKS_OK
```

The program checks finite examples and numerical integrals, not the mathematical validity of dominated convergence in the infinite limit. The independent-audit status above reports that no independent audit has been conducted; the scientific review status is documented separately in REVIEW.md.
