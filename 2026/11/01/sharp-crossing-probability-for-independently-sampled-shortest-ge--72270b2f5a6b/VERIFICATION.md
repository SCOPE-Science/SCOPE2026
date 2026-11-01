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

# Reproducibility and actual checks

Run `python3 verification/check_crossing.py` with Python 3 and its standard library. The checker derives the exact double-integral polynomial via rational arithmetic at a full interpolation grid of four independent values in \(B\) and seven values in \(q\). Its bidegree certificate comes from the triangle-sector integral: at most degree three in \(B\) and degree six in \(q\); therefore the 28 exact matches establish the polynomial identity, not merely agreement at finite inputs.

The script also checks both rational sharp endpoints, then independently samples two uniform Voronoi-cell displacement vectors and a uniform relative start point on the lattice torus. It solves all potential translated geodesic-segment crossing equations within the indicated translation window and compares the resulting crossing frequencies with the analytic formula. The simulation additionally checks that no realization has more than one intersection in the tested cases. The universal no-multiple-crossings statement is proved in RESULT.md, not inferred from simulation.

Expected final output includes `EXACT_BIDEGREE_INTERPOLATION_IDENTITY_PASSED 28`, `EXACT_SHARP_ENDPOINTS_PASSED`, `INDEPENDENT_PERIODIC_SEGMENT_CROSSINGS_PASSED 3`, `NO_DUPLICATE_INTERSECTIONS_PASSED`, and `ALL_CHECKS_PASSED`.

These checks require no downloaded files or nonstandard dependencies. The analytic proof supplies the exact all-lattice and all-sample-space claims; numerical frequencies cannot independently certify historical novelty, the universal bounds, or independent validation.
