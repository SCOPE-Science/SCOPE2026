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

The exact analytic arguments are in RESULT.md. To reproduce the independent arithmetic checks, execute `python3 verify.py` from the directory containing this file and the script. No network connection or third-party Python packages are required.

The script calculates every principal-minor sum by exact `fractions.Fraction` Gaussian elimination, comparing it to the elementary-symmetric spectral identity. It uses two site layouts at each size two through six, nonuniform rational weights and a decay rate making point-to-point exponential transfers rational. It then independently constructs the two-stage two-site matrix at seven separations, verifies the determinant formula by exact fractions, and compares its spectral-root formula and discrete maximum. Expected result: `PASS: 54 exact-rational principal-minor/determinant checks`, followed by confirmation of the discrete antipodal maximum.

The all-layout, all-positive-parameter isospectrality, converse characterization, and unique continuous antipodal optimum rely on their proofs, not on these finite checks. Limitations: the center-sampled linear transfer model and two specified travel-distance distributions, not measured marine transport, finite-area reserves or externally certified ecological predictions.
