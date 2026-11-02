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

The theorem follows from an exact beta--Gaussian convolution, Kummer's differential equation, the signs of its curvature zeros, monotone likelihood ratios, and a strictly decreasing ratio of Gaussian derivative kernels. The analytic kernel monotonicity proves global mode-count bounds for the entire real line without relying on finite experimental scans.

Reproduce the finite numerical cross-check by running `python check.py` using NumPy and SciPy. The checker derives five crossover roots with hypergeometric functions and independently examines ten Gaussian-convolution derivative sign profiles using 200-node Gauss--Jacobi quadrature. Expected final line: `PASS: 5 thresholds, 10 global derivative sign-change scans, strict monotonicity`. Numerical tests cannot establish any of the universal mathematical assertions by themselves. No external or independent validation is claimed.
