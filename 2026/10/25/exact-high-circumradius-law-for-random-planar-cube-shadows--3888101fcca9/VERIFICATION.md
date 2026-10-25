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

Run `python3 VERIFY.py` in an environment with NumPy and SciPy installed. The program constructs all eight projected cube vertices independently of the four-axis identity, verifies the triple-contact operator norm over all row triples and all eight sign corners, compares a one-dimensional latitude integral with a scrambled spherical Sobol sample of \(2^{20}\) orientations at six thresholds, and checks the first two nonzero pair-overlap Taylor coefficients as well as both endpoints.

The following checks were executed on the actual standalone verifier source:

```text
EXACT_TRIPLE_BELT_THRESHOLD_AND_TIGHT_FRAME_OK
DIRECT_EIGHT_VERTEX_PROJECTED_CIRCUMRADIUS_IDENTITY_OK
BELT_TAIL_DISTRIBUTION_OK (six parameter thresholds)
EXACT_PAIR_OVERLAP_TAYLOR_COEFFICIENTS_OK
ENDPOINT_SUPPORT_AND_SQUARE_ROOT_TAIL_NORMALIZATION_OK
ALL_CUBE_SHADOW_CIRCUMRADIUS_CHECKS_OK
```

The formal proof relies on a finite matrix identity, exact spherical conditional probabilities, analytic integrals and inclusion–exclusion—not empirical convergence. The executable checks provide corroboration, not an independent mathematical certificate or a proof of novelty. The formula does not claim the complete lower-radius distribution.
