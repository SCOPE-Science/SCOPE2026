---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Read the complete proof: x=t1+sqrt(ε)v on the zero-sum hyperplane H has Jacobian sqrt(n) ε^{(n−1)/2}, not n or 1. Since n(c−1)=−1, the endpoint density is t^{−1+nλ/L}; substitution t=ε^{u/2} produces (L/2)e^{−nλu/2}du, and similarly near 1 with μ. For t≫sqrt(ε), the residual density is asymptotically independent of v; corner t≲sqrt(ε) contributes O(ε^{(n−1)/2}) without the leading logarithm, and fixed interior contributes the same smaller order. The two endpoint terms give the probability constant and conditional independence/uniform unit-ball law. Independently computed Φ_n tilt integrals for n=2,...,9 and direct arcsine n=2 probabilities via conditional exact CDF quadrature at 10^−4,10^−6,10^−8; ratios to the stated leading formula decreased toward one. The quantitative corner estimates, not finite ratios, justify limits.

## originality

PASS

Royen’s primary theorem already gives fixed-parameter sample-variance distribution and critical logarithmic lower tails for bounded supports. The published three-sample Beta phase diagram similarly handles fixed shapes and includes the equal-critical coefficient. A fixed-shape pointwise asymptotic cannot automatically be substituted into α,β moving at 1/log(1/ε), and neither source supplies the conditional joint endpoint/log-location/transverse law. The particular two-drift crossover is the surviving novelty claim.

## value

PASS

A critical moving-parameter window is mathematically natural where two boundary singularities tie; its exact crossover probabilities and an entire conditional geometric limit distinguish how rare, nearly constant Beta samples form. It is not merely re-evaluating the fixed-shape logarithmic coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
