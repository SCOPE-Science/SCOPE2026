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

Use Python 3, with only its standard library, and run:

```sh
python3 verify.py
```

The program reconstructs the six vertices of a generic octahedron section directly and independently verifies the area identity at 250 normals. It tests the radial and angular second variations at the eight diagonal minima and twelve equatorial saddles, the first directional behavior at the axial maxima, the exact angular integral controlling the upper-tail constant, and two finite-sample consequences of the theorem using 480,000 directly sampled Gaussian normals normalized to unit length.

Observed final diagnostic messages include:

```text
DIRECT_HEXAGON_VERTEX_SHOELACE_IDENTITY_OK 250
INDEPENDENT_DIAGONAL_MINIMUM_AND_EQUATOR_SADDLE_HESSIANS_OK
AXIS_CONICAL_ENDPOINT_NORMAL_FORM_OK
EXACT_AXIS_ANGULAR_INTEGRAL_AND_UPPER_TAIL_COEFFICIENT_OK
INDEPENDENT_GAUSSIAN_HAAR_ORIENTATION_ENDPOINT_SAMPLING_OK 480000
TWELVE_SADDLE_LOGARITHMIC_NORMALIZATION_OK
ALL_OCTAHEDRAL_CENTRAL_SECTION_AREA_CHECKS_OK
```

These computations are finite and are not a proof of an asymptotic theorem. The proof uses the exact section area, an exhaustive critical-normal classification, quadratic saddle integration, and an exact endpoint angular integral. Independent mathematical audit has not been performed. Historical priority is uncertain for older potentially relevant section-volume literature unavailable in full.
