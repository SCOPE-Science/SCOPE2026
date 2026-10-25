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

# Reproducible mathematical checks

Run `python3 verification/verify_pentagonal_prism.py` with Python 3 and no third-party modules. The file independently reconstructs original vertex positions and all fifteen edges, tests the six transition intervals against direct edge crossing, compares the exact four probabilities to independent spherical quadrature for five heights, checks the full mean using endpoint-angle probabilities, samples 240,000 independent Haar normals, and tests both endpoint constants.

Observed output:

```text
EXACT_FOUR_MASS_NORMALIZATION_AND_ANGLE_INTEGRATION_OK
EXHAUSTIVE_THRESHOLD_CHAMBER_RECONSTRUCTION_OK
INDEPENDENT_FIFTEEN_EDGE_MEAN_IDENTITY_OK
INDEPENDENT_HAAR_FIFTEEN_EDGE_MONTE_CARLO_OK 240000 0.248058 0.498117 0.186579 0.067246
SHARP_THIN_AND_TALL_HEPTAGON_TAIL_CONSTANTS_OK
ALL_PENTAGONAL_PRISM_SECTION_CHECKS_OK
```

The 200-point grid in each aspect checks all six symbolic interval predictions at sampled azimuths, not all real azimuths. Numerical integration, Monte Carlo, and endpoint spot checks are finite corroboration. The actual universal argument is the exact edge-incidence identity, the complete ordering of threshold cosines and integration of the Haar density. No external or independent audit has been performed.
