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

The standalone source `verify_truncated_tetrahedron.py` uses only Python's standard library and executes with `python3 verify_truncated_tetrahedron.py`. Its core finite computation uses exact integer/rational arithmetic: it reconstructs the eight-facet polyhedron, verifies all twelve vertices, all eighteen edges, the nonzero determinants of all \(220\) vertex triples, the \(132\) signed pairwise great-circle intersections, and all \(4096\) sign masks. Integer-based cyclic wall signatures reproduce the six classes of \(134\) chambers and the complete side-count distribution. Spherical areas are evaluated by the stated exact inverse-cosine formula. The independent edge-angle identity confirms the mean without reusing the chamber area calculation.

Additional numerical corroborations reconstruct section vertices directly by solving intersections with pairs of the eight facet planes for \(600\) orientations and compare with edge-crossing counts; \(80{,}000\) deterministic-seed Gaussian directions produce frequencies consistent with the exact law. Neither sample check replaces the exact finite enumeration or analytic spherical area argument. The correctness claim concerns this model and its stated generic orientations, not arbitrary polytopes. No external independent audit has been performed.
