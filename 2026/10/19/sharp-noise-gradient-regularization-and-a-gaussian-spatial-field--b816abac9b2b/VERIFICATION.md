---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reassessed the complete replacement repairs/3/RESULT.md. The original Eq. (4) was numerically correct as a covariance decrement but was presented as the increment variance, which is twice the decrement because K has constant diagonal. The replacement states both the exact half-variance identity and the coefficient for the full variance, and clarifies eventual validity of the sampled indices. For the finite formula, the covariance is the sum of independent bath contributions propagated by the triangular semigroup: integration of e^(−2kτ) τ^(2ℓ−i−j) gives the stated factorial coefficient and exactly one outside factor D/k. Equivalently the stationary recursion 2k C_ij=C_(i+1)j+C_i(j+1)+2D i^(−β)1_(i=j), with zero out-of-range entries, gives the same coefficients by counting monotone paths to (ℓ,ℓ), including N=1. Central-binomial weights make the upstream summand asymptotic to D m^(−β−1/2)/√π with a summable error at β=1/2, proving all three cases. In the window with real λ, the binomial mass with 2m+d trials is bounded by C/(m+1)^(1/2) uniformly, and the damping factor stays bounded even for λ<0. The scaled sum up to εN is O(ε^(1/2−β))+o(1), including on the diagonal. On the bulk m∼Nt, the binomial deviation is d/2 with d/√N→|u−v|; uniform Stirling gives exp(−d²/(4m))/√(πm), the bath factor tends to t^(−β) after rescaling, and j/N→0. Hence the Gaussian covariance Riemann sum gives the claimed finite-dimensional limit, not a path limit. For Eq. (4), changing variables to s=h²/(4t) leaves the integrable factor s^(β−3/2)(1−e^(−s)); integration by parts gives Γ(β+1/2)/(1/2−β), with 2^(−1+2β) from scaling. The script was inspected, not executed; it checks the decrement, so needs no change. The frozen source and verification notes are preserved.

## originality

PASS

The repaired finding earns credit for the β>0 grading-dependent stationary-size classification and subcritical graded field, including its small-lag power and constants. The homogeneous finite covariance, ordinary stochastic-convolution identity and elementary finite inhomogeneous extension are not the originality basis. The precise homogeneous mesoscopic kernel is separately credited in the replacement.

## value

PASS

The stationary-size limit is not captured by the unchanged stable eigenvalue. The threshold distinguishes divergence, marginal logarithmic behavior and bounded upstream variance as one changes only the bath; the mesoscopic field gives a further measurable consequence, including a grading-dependent small-lag power. This goes beyond a routine finite covariance calculation. The repaired distinction between decrement and full increment variance is necessary for quantitative use; the demonstrated limit is finite-dimensional only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
