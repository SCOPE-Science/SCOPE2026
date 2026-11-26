---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The stationary driving Brownian motion is evaluated at a reset age of exponential law and has finite moments of every fixed order; the stable convolution gives the same moment finiteness for X. Coupling at the first common reset and exponential contraction of X give uniqueness. For the generator with diffusion term ∂yy and reset term β[f(x,0)-f(x,y)], I independently solved the stationary moment recursion in descending Y-power at each degree and used the exact resolvent (pI-Q)^-1, with Q upper triangular with diagonal (-2,-β-1,-β) and adjacent entries (2β,β). Centering removes the constant diffusion term. The reverse ordered covariance equals Aβ exp(-βt) by conditioning on Y0. Subtracting its resolvent gives the two positive products of resolvents stated in the finding; their causal convolutions are strictly positive for every t>0 and never require taking differences of coincident decay rates. Setting p=0 and dividing by Aβ, symbolic reduction gave the stated rational area, derivative and value at the unique positive root of 31β²+14β-8. The derivative is positive before and negative after that root. The area uses dimensionless lag, so the physical-time area ratio is divided by the trap relaxation rate. The frozen checker was inspected, not executed; the independent exact calculation uses only the displayed moment recursion and three-dimensional linear algebra.

## originality

PASS

The supported distinct contribution is the all-parameter positive ordered difference between squared *position and drive*, its positive convolution factorization and optimized integrated area. The exact model, moment recursion, quadratic evolution matrix and even the reverse ordered covariance are not distinct: indexed result 9942883e9395 explicitly gives the reverse ordering in its proof. However that result's forward system is initialized against X0², not Y0²; the forward ordering under review has a different initial covariance vector, and the sign of its difference with the reverse ordering and sharp area optimum do not follow from the autocovariance positivity or crossover theorem. The same-model fourth-order time arrow 2d5b968bafd9 has different observables and different sign behavior. Comparable primary papers give the model or unlike general bounds, not an implication of the supported distinct conclusions.

## value

PASS

The two squared observables probe a concrete physical distinction: whether forcing fluctuations lead trap energy or the reverse, which cannot be tested with position-only stationary variances or energy autocorrelation. Strict directionality for every positive lag and rate, robust to coincident decay rates, yields an exact benchmark. The unique maximum compares the integrated effect to its equal-time scale and sets a meaningful dimensionless rate ratio. This is not a general thermodynamic or causal-inference theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
