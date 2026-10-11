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

# Verification and limitations

Run `python verify.py` using Python 3 and NumPy. A successful run prints `VERIFY_OK`. The script has no network dependency, consumes no hidden research files, and reconstructs its own positive-curvature support function.

The script computes its initial isoperimetric deficit from Fourier spectral weights and independently from a direct normal-angle integral of the support function and its derivative after an explicit reflected projection. It integrates one- and two-step angle laws on \(128\) equally spaced axes in each angular variable and compares the means, variances, and first/second-step covariance with the exact analytic formulas. For the finite test harmonics, grid trapezoidal sums are exact in algebraic trigonometric arithmetic apart from floating-point roundoff. It verifies the strict two-frequency variance deficit and the single-mode equality case. The displayed convexity diagnostic \(1-\sum_m(m^2-1)\sqrt{a_m^2+b_m^2}>0\) ensures that the test trigonometric support function represents a smooth strictly convex body.

The all-orders covariance proof uses the planar support-function area identity, independent increments of Haar-uniform angles modulo \(\pi\), the three elementary angular moments \(1/2\), \(3/8\), and \(1/4\), and Tonelli's theorem on nonnegative Fourier energies. For a general nonsmooth body its support function lies in \(W^{1,2}\); polygonal bodies are included. The almost-sure limit uses a nonnegative martingale, the strong law of logarithmic mode multipliers, and an infinite-mode tail expectation argument. Neither finite quadrature nor simulated paths are evidence of an almost-sure or infinite-dimensional statement.

The literature comparison is limited to inspected materials and indexed searches, not a proof that an equivalent historical result cannot exist. Scientific claims have received same-model review only; independent audit and independent validation have not been performed.
