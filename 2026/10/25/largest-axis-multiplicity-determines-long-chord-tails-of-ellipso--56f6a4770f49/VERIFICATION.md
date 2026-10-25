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

# Verification and reproducibility

The analytical checks reconstruct the complete-square identity in Euclidean affine-line coordinates, the Schur-complement determinant and orientation weighting, the beta radial law, the rescaled sphere measure, and the gamma integral. The endpoint exponent and constant are proved for every fixed \(d\ge2\); numerical simulation is supplementary and cannot establish the theorem in infinite families.

Run `python3 check_ellipsoid_chord_tails.py` with Python 3, NumPy, and SciPy. The embedded program was executed in the same environment as this package's construction, producing all four `SHARP_END_TAIL_OK` messages, `UNBIASED_LINE_MEASURE_VS_DIRECT_QUADRATURE_OK`, `DIRECT_QUADRATIC_LINE_INTERSECTIONS_OK`, and `ALL_ELLIPSOID_MULTIPLICITY_TAIL_CHECKS_OK`.

The numerical integration checks triaxial, prolate, oblate and spherical axis patterns in dimension three at several near-endpoint deficits. A separate geometric test solves quadratic line intersections after sampling directions uniformly and translations uniformly in a containing perpendicular disk, conditioning on intersection; this checks that the affine-line conditioning is not replaced with a different random-chord convention. The Monte Carlo tolerances and sample counts are encoded in the source.

Limits: fixed ellipsoids only; the eigenvalue-gapped expansion does not claim uniformity across coalescing axes. Historical priority and independent mathematical audit remain open.
