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

# Reproduction and verification

Run `python verify.py` using Python's standard library. The program recomputes the harmonic-mode velocity variance with a stationary Lyapunov equation; reconstructs periodic covariance and precision independently by Fourier summation and Gauss–Jordan inversion; verifies the cold nearest-neighbor kernel and warm reciprocal-spectrum kernel; and tests the distance-indexed maxima and large-distance coefficients for multiple choices of positive model parameters. The packaged file executed successfully with the output `PASSED 6020 independent numerical and algebraic-reconstruction checks`.

These are finite numerical tests, not a proof of uniqueness or all-separation statements. The independent symbolic proof of Fourier inversion, Gaussian conditioning, strict monotonicity of the log derivative, uniqueness, and asymptotic coefficient limits is given in `RESULT.md`. Nothing asserts an independent mathematical audit or external certification.
