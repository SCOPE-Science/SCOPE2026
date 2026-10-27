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

# Reproducibility and scope

Run `python verify_gap.py` in a Python environment with NumPy, SciPy, and mpmath. The code reproduces the exact chi-mixture density by incomplete-Gamma evaluation at fixed parameters, verifies the small-gap coefficients across several Dyson indices, computes the independent-gap spectral-density integral by a distinct angular/convolution quadrature, and samples independent and shared reset clocks to test their common exact second gap moment. The final deterministic run reported **97 passing assertion groups**, including quadrature checks for \(\beta=0.7,1.3,2,3,4\) and 3.5 million two-site simulated stationary gap draws in total. These are finite-precision corroborations; exact constants and the all-parameter assertions rely on the proof in `RESULT.md`.

The convergence toward a borderline logarithmic asymptotic is slow. The code uses finite-gap comparison tolerances that are appropriate for this behavior rather than asserting an unattained finite-size equality. It does not establish an independent audit, large-dimension asymptotics, or a finite-dimensional enumeration of all cases.
