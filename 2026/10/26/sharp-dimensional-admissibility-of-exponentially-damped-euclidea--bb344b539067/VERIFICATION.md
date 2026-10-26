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

The mathematical conclusion is proved by the integral identity for the three-dimensional Fourier transform, the Bessel dimension-walk identity, and the monotone complex argument calculation. These are infinite-dimensional arguments, not extrapolations from numerics.

Run `python verify.py` with Python 3 and SymPy. The checker verifies exact symbolic formulas for dimensions five and seven, matches the complex-power Fourier transform for dimensions three through eleven at stated parameter values, and samples signs above and below the predicted boundary. The spectral integral and phase proof fix all normalizations independently of these finite checks.

The conclusion covers only odd ambient dimensions at least three with strictly positive damping and wave frequency. The boundary is included: at equality the density vanishes at frequency zero but is strictly positive away from zero. Literature comparisons are bounded; no external mathematical audit or independent validation has been performed.
