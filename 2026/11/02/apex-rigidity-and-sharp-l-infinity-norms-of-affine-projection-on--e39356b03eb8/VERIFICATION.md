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

# Reproducibility and verification

Run `python3 check_bicone.py` using a standard Python 3 installation. The script performs exact-rational algebraic checks for dimensions 1 through 50, including the decisive dimension-two strict comparison. It uses a fixed pseudo-random seed to sample uniform points in the exact convex body through the axial beta law and conditional radial Gaussian directions. For seven dimensions, 40,000 samples each approximate both axial and equatorial absolute-kernel row integrals; reported sampling tolerances are deliberately wider than typical errors.

Observed: 249 exact-rational assertions and 280,000 independent pseudo-random volume samples, with every programmed test passing. This is not a finite certification of the analytical result: the proof for all integer dimensions is in RESULT.md and depends on explicit covariance identities, the elementary second-moment inequality, and the beta integral. No independent external audit is represented.
