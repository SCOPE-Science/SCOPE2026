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

The independent Brownian drivers give conditional iid positions, not independent stationary particles after averaging over the common clock. The stationary age T has exponential rate r and V=exp(−2μT) has CDF v^β. The OU variance (D/μ)(1−v) gives the stated increasing binomial parameter p(v), with derivative c at zero. For v=w/√N the count threshold, centered at Np(v) and divided by √N, tends to s−cw; conditional variance divided by N tends to σ²>0. The triangular binomial CLT then gives the stated integrand; the floor shifts the centered threshold by O(N^−1/2). The continuous positive secant slope (p(v)−p*)/v has a positive minimum δ on the closed interval when extended at zero. Beyond a fixed w the centered left tail is bounded by exp(−δ²w²/2) uniformly in N on w≤√N; extend the integrand by zero outside that range. Multiplying by w^(β−1) gives integrability at zero and infinity for every fixed β>0. The limit is c^(−β) E[(s−σZ)_+^β] by integrating over the Gaussian, giving the claimed positive finite profile and gamma constant at s=0. Conditional variances of K_N/N are bounded by 1/(4N), giving the macroscopic limit p(V); the change-of-variables density β[p^−1(z)]^(β−1)/p'(p^−1(z)) gives the three edge regimes. The supplied script was inspected, not run: its limit ratios are numerical illustrations, and its assertion compares two quadratures of the same mixture with different variables and tail cutoffs.

## originality

PASS

The supported distinction is the fixed-window count's finite-N lower-edge boundary layer with explicit coefficients in the noninteracting, common-Poisson-reset OU model. The same model's stationary age mixture was established previously; the generic binomial mixture mechanism and the macroscopic exponent in a different trapped reset gas are not new. None of the inspected formulas for free diffusion counts, interacting trapped counts, or other observables in the same model gives this count-specific finite-size law. The bounded comparison does not certify historical priority or a resetting-specific universality claim.

## value

PASS

The boundary layer answers a fixed-window counting question in an established model and distinguishes finite-sample events below the equilibrium fraction from the hard endpoint of the macroscopic law. It gives a quantitative relationship between the reset rate, equilibrium sampling fluctuations, and the probability and shape of that rare event, including the normalization an analyst would need. A macroscopic edge-density exponent alone would not supply this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
