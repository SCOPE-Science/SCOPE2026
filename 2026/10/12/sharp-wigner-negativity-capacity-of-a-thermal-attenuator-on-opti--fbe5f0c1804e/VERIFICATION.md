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

Run `python verify.py` after installing `requirements.txt` (`numpy` and `scipy`). The file reconstructs the output Wigner polynomial, independently performs two-dimensional midpoint integration of its negative part, and compares with the Bessel-form polar integral, including the vacuum and one-photon boundary, mixed-input strict photon bound, and the thermal Wigner-positivity threshold.

The executable was run successfully: `VERIFY_OK all_checks=112`. The direct numerical spatial integrals have an absolute comparison tolerance of 0.00002. Finite grids are evidence of numerical consistency only. The arbitrary-parameter assertions follow instead from the exact Gaussian Fourier inversion, strict convexity at fixed population, and a strictly centered-maximal convolution of radial functions.

The following are not verified here: higher Fock-level inputs, squeezed or phase-sensitive channels, independent publication-priority review, and external audit. The one-dimensional Bessel integral is exact, not a numerical certificate of uniqueness.
