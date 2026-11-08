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

Scaling each power-mesh cell gives the exact distributional identity Q_n-I=n^{-q}sum_{j<=n}Z_j, with independent centered Z_j and explicit integrated variance. For 0<alpha<1/2, v_j~(alpha^2p^4/12)j^{2q-4}; the derivative/width Taylor remainder is uniformly lower order on j>=2. When q<3/2 the independent series converges in L2 and almost surely. Only its first term has the unbounded power right tail P(Z_1>x)~x^{-1/alpha}; the remainder is sub-Gaussian by Hoeffding with square-summable bounds, giving the exact tail equivalence. At q=3/2 variance grows c log n and at q>3/2 it grows c n^(2q-3)/(2q-3), with Lindeberg since bounded later summands are negligible relative to the normalization. Differentiating c/(2q-3) finds p*=2/(1-alpha). Independently exact-rational cell variance calculations verified v_j=3/4 for alpha=1/3,p=3 and v_j=2(6j^2-6j+1)/9 for alpha=1/4,p=4 for all j=1..30.

## originality

PASS

The smooth-function stratified-sampling and adaptive oracle literature establishes general methods and rates under differentiability assumptions excluding t^-alpha at zero. The present result is a separate exact triangular-array distribution classification including non-Gaussian tails and a logarithmic boundary for one sample per power cell. Older specialized randomized singular quadrature is a real residual priority risk; this is a best-of-knowledge verdict, not proof by negative search.

## value

PASS

Failure of Gaussian reliability at the insufficient grading threshold is mathematically and practically motivated for singular integrands. Exact tail exponent, normal/log-normal transition, optimized fixed power and all-n equal-variance benchmark are nontrivial distinctions, not a smooth-theory constant substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
