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

The proof uses the centroid variance identity, a strictly decreasing two-variance upper envelope, a matching orthogonal-simplex construction, and an explicit two-hop feasibility inequality. These steps establish the unrestricted theorem analytically, without relying on finite extrapolation.

The standalone `check_barbell.py` was executed with the Python standard library and returned `CHECK_OK parameter_pairs= 1369 exact_orbit_bounds= 10952 full_coordinate_pairs= 28223`. The 1,369 size pairs and 28,223 constructed coordinate pairs are finite consistency tests, not an exhaustive proof for arbitrary graph sizes. Independently reproducing the complete mathematical proof and historical novelty comparison remains outstanding.
