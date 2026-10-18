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

# Verification

The exact theorem is proved analytically in `RESULT.md`. Execute `python check.py` with Python 3, NumPy and SciPy to reproduce the direct finite checks. The checker constructs cube incidence matrices independently, diagonalizes their Laplacians, compares the computed inverse-square-root quadratic forms with the Walsh binomial sums for dimensions three through six, and verifies strict distance bounds and the baseline spectral traces. It optimizes over **all** edge/chord row weights (not only symmetric weights) on three- and four-dimensional cubes for amplitudes both below and above the predicted screening thresholds. It also checks the large-dimension coefficient for three dimensions. The run reported: `PASS 44 independent spectral, derivative, optimization, and scaling checks`.

Floating-point tolerances are explicit in `check.py`, and finite tests neither prove the universal result nor independently audit the mathematics. No outside proof artifacts are required. The analytic proof handles all parameter ranges, simultaneous chord families, sharpness, and strictness; a post-threshold exact norm is not claimed.
