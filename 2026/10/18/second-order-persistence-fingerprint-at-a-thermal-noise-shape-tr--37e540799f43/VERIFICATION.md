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

The result was reconstructed analytically using the tilted-beta moment recurrence, the Gaussian heat equation, a quartic nondegeneracy test, and the implicit-function theorem. The stationary-mode count uses the classical variation-diminishing theorem for Gaussian convolution. These steps are presented in RESULT.md.

Run `python verify.py` with NumPy and SciPy. The checker implements Gauss–Jacobi quadrature for two *different* integral representations: tilted-beta moments in the squared coordinate and direct symmetric-beta Gaussian-convolution derivatives in the original coordinate. It independently solves for the critical point and two postcritical peak positions. The actual command passed 34 assertions in the execution that produced this report. Typical results: \(\nu_c(0.5)=0.316464340348\), \(K(0.5)=-4.588276495\); \(\nu_c(0.9)=0.119126237471\), \(K(0.9)=3.008043493\). The measured second coefficients at deficit 0.0003 are approximately -4.5871 and +3.0402; the latter has a larger next-order effect. These finite computations are independent checks, not an infinite-precision certificate or independent audit.

The theory covers a fixed persistence ratio strictly between zero and one. It does not prove uniqueness of the persistence ratio at which the next correction vanishes, or the stability of inferring persistence from finite, noisy samples.
