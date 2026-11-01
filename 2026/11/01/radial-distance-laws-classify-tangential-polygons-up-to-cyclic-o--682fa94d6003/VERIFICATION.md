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

The general mathematical result has an analytic proof in `RESULT.md`, steps 1–7. The reproducible checker `verification/check_radial_fingerprint.py` is supplementary rather than a substitute for that proof.

Run `python3 verification/check_radial_fingerprint.py` using Python 3 standard-library modules only. On the prepared package it printed:

`RADIAL_INVERSE_CHECK_OK: 12578 exact rational comparisons; 15 numerical ray checks; 6 rational polygon families; 3 quadrilateral congruence classes`

The checker creates rational tangent normal vectors and line intersections, checks all incidences, independently computes exact area and second/fourth radial moments, verifies exact boundary hinge tails over permuted tangent-gap data, recovers prescribed multiplicities from slope jumps, and checks all three dihedral classes of the explicit four-gap example. Separately, it numerically compares the analytic angular-level function with direct radial-ray intersection data in 15 trials.

The exact-rational comparisons and finite angular quadrature cannot by themselves establish the infinite family of polygons or the distributional inverse result. Those follow analytically from tangent-fan geometry, polar integration, piecewise-linear jump inversion, and polygonal normal-order rigidity. Full law data are assumed; statistical stability and noisy recovery are not proved.
