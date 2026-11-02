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
# Verification details

The proof establishes the exact weighted-Bergman monomial moments and the positive gap separating the top radial disk eigenvalue. Endpoint differentiation of the trace-class moving-boundary operator produces the second-order eigenvalue perturbation series. The one-sign-change polynomial \(P_n(T)\) has positive value at \(T=1\), which proves positivity for all \(0<T<1\) and hence strict ordering of the Fourier Hessian coefficients. These are analytical arguments and apply to all stated parameters and fixed bounded real mean-zero profiles.

Run `python verify.py` in the package directory with the scientific Python dependencies specified in `requirements.txt`. The checker was run from the package source directory and completed 212 independent supplementary finite checks: beta-integral spectral identities, coefficient ordering, finite Toeplitz-matrix eigenvalue finite differences, and fixed-area discretization. Replaying the exact embedded files and rerunning the checker provides reproducibility but is not an infinite-dimensional proof or an independent validation.

For \(c=1\), \(T=1/2\), \(h(\theta)=\cos(2\theta)\), the predicted quadratic deficit is \(\varepsilon^2/32\). The remainder is \(O(|\varepsilon|^3)\) for each fixed bounded profile; it is not claimed uniformly over arbitrary shapes. Historical priority remains provisional and the strongest prior second-variation comparison is arXiv:2411.16010, Section 4.1. Independent mathematical audit and validation have not been performed.
