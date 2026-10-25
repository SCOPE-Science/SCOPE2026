---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For fixed b>=2 and epsilon=tau/sqrt(n), the small C^0 conjugacy H_epsilon to the linear degree-b map is obtained by a contraction of the inverse-expanding cohomological equation and expanded uniformly to third order in epsilon. Along its periodic points the log-derivative sum has epsilon S_n g+epsilon² S_n h+O_b(n|epsilon|³), with g=(2pi/b)cos(2pi x), Haar mean h=pi²/b², and g’s long-run variance 2pi²/b². Sampling fixed points is within O(b^-n) total variation of uniform cyclic base-b words; digit-block truncation and Lindeberg prove S_n g/sqrt(n) Gaussian, while LLN gives S_n h/n -> pi²/b². Thus the triangular array tends to N(pi²tau²/b²,2pi²tau²/b²), tau=0 degenerate. Finite-period discrete Fourier orthogonality for n>=3 gives exact zero first derivative, variance 2npi²/b², curvature (2npi²/b²)(b^n+1)/(b^n-1). Independent root-of-unity calculations verified Fourier covariance for b=2..6, n=3..8 and curvature for b=2..5, n=3..7; those are not a CLT proof.

## originality

PASS

Best-of-knowledge priority judgment: close primary sources and published indexed findings are compared by mathematical statement, not just titles. Known general/ingredient results are credited; the precise asserted complete result is not shown to be covered by the material actually examined. Explicit source-access and possible stronger-result residual risks remain and do not become fabricated negative bibliographic claims.

## value

PASS

At the singular linear-map boundary the usual positive-variance fixed-map periodic-orbit CLT degenerates, making epsilon proportional to n^{-1/2} a mathematically distinguished crossover scale. The explicit mean shift, variance coupling and exact finite-period response illuminate a natural triangular-array transition rather than simply restate fixed-parameter CLT or general smooth dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
