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

The proof defines every normalization and boundary multiplicity in `RESULT.md`. Execute `python verify_anisotropic.py` with NumPy and SciPy installed. The program checks the finite sample arclength intensity in the explicit positive quadrupolar family, independently integrates separation indicators on the sphere, reconstructs planar halfspace cells and geodesic edge lengths, checks convergence toward the predicted exact anisotropic constant, and recovers both the angular transform and its absolute normalization. A completed execution prints `ALL_ANALYTICAL_AND_GEOMETRIC_TESTS_PASSED`.

These finite quadratures and randomized checks are corroboration, not an infinite-family proof. The derivation of the exact intensity, uniform small-angle limit, dominated total-variation convergence, Fourier inversion and sharp Jensen equality case is mathematical and self-contained in `RESULT.md`. The distribution recovered by the theorem is based on expectation-first arclength weighting and is not a pathwise ratio of random quantities. The original public source establishes the tessellation model, not an independent validation of this theorem.
