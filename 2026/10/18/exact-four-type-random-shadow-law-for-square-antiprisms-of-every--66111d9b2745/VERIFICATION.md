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

# Verification of the square-antiprism shadow law

Run `python3 verify.py` from the directory containing this file and the proof. No third-party dependencies or downloaded data are required. The code reconstructs convex hulls by a planar monotone-chain algorithm, while the derived theorem counts horizon edges using facet-normal signs. Their comparison is therefore a genuinely different computational route.

Checks performed: support-plane inequalities and the exact ten-facet, sixteen-edge incidence pattern at four positive heights; 72,000 randomly sampled directions checked independently by planar hull reconstruction, horizon-edge signs and the closed chamber-count identity; separate Simpson quadrature of all four probabilities; the expectation computed from probabilities compared with the exterior-dihedral-angle identity. All tests passed, including the output `SQUARE_ANTIPRISM_SHADOW_OK projected_hulls=72000 facet_horizon=16 edges per shape and exact spherical quadratures=4`.

The checker uses floating-point arithmetic for regression testing, and its finite samples are not an exhaustive proof. The quantified mathematical proof is the explicit face-incidence reduction, the strict ordering of all azimuth-dependent thresholds and elementary spherical integration in `RESULT.md`.
