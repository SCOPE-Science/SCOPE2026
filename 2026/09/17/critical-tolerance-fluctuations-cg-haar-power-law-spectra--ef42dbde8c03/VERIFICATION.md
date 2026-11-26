---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Pass applies to the repaired RESULT.md and SLOGAN.txt, not the standalone literal parameter statement in the frozen result. The frozen inequality (4d+2)p<1 does not specify positive decay. At p=0 the formula has p^(−1), and CG on the identity stops at one step at zero tolerance rather than following the stated law. Negative p is not fixed by excluding the singular point: for example p=−1 under the literal inequality gives a non-probability density on the asserted support [1,∞), whereas (n/j)^p lies in (0,1]. The repaired theorem specifies 0<p<1/(4d+2), the intended decay regime. Independently checked its proof: after scaling the spectral variable, the common normalization of Haar coordinates cancels and the weights are Y_{j,n}E_j with independent mean-one exponentials (real model: chi-squares with one degree of freedom). The real minimizer suffices since imaginary coefficients add nonnegative energy with zero constraint at the origin. Under x=1/y, the normalization r(0)=1 makes x^d r(1/x) monic and the weight becomes x^(p^(−1)−2d−2). The shifted Jacobi leading coefficient is binom(p^(−1)−2,d), and its squared norm before making it monic is 1/(p^(−1)−1); the density prefactor cancels this norm, giving F_d. A mesh-vs-integral bound O(n^(ap−1)) on the a-th raw mean is o(n^(−1/2)) for ap<1/2; the largest centered coefficient in each √n-scaled linear combination is O(n^((2d+1)p−1/2)), and the quadratic covariances tend to 1/(1−(a+b)p). Bounded total coefficient squares and a vanishing largest coefficient imply Lindeberg by integrability of the squared centered weights. The limiting Gram block is positive definite, so the optimizing polynomial coefficients and the Schur-complement quotient are smooth near the limit. Differentiating the optimized quotient gives (1−p)y(r(y)^2−F_d) at a grid point; its squared integral against t on (0,1] changes to (1−p) times the integral of y(r²−F_d)² against ν_p. It is positive because the degree-d polynomial is nonconstant, and finite since the tail exponent is 4d+1−1/p<−1. A variance-two raw weight multiplies the covariance and the final variance by two. Since (2d+3)p<1, a weighted law of large numbers applies to degree d+1 as well (integrable deterministic means and maximal unscaled weight tending to zero). The binomial ratio gives F_{d−1}>F_d>F_{d+1}, with F_0=1. Monotonicity of the actual errors then leaves only steps d and d+1 with high probability, and continuity and symmetry of the nondegenerate limiting Gaussian give the two equal masses. No claim at the variance boundary, for growing degree, or in finite precision was accepted.

## originality

PASS

The repaired files credit the earlier 50/50 half-step law explicitly; neither that general phenomenon nor the Jacobi optimization method is novel here. Credit the explicit Gaussian fluctuation theorem, variance and consequent critical stopping distribution specifically in the fixed-interior-degree deterministic power-law spectrum/Haar-source model. The positive exponent repair delimits the checked model and does not assert a new claim beyond it. The assessment is limited to the inspected statements and the bounded search.

## value

PASS

At a strict interior limiting error floor, first-order convergence alone cannot predict the iteration count. The explicit, nondegenerate variance resolves the critical transition for this spectrum and source model (and distinguishes real and complex sources), even though the normal-sign argument for the stopping count is familiar. The parameters specify the exact finite-variance window for the displayed influence integral, not an arbitrary finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
