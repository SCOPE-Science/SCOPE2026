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

Translating and scaling the threshold simplex gives P(M>t)=(1−mt)^(m−1) and D|M>t=(1−u)e+uX with u=1−mt and e the barycenter. On every nonconstant ray the sum of powers decreases strictly toward e for a>1 and increases strictly for 0<a<1, by strict convexity or concavity. Integrating the conditional-mean difference against survival proves the three signs, including the trivial constant at a=1. For integer q, the k-th term uses E[X₁^k]=k!(m−1)!/(m+k−1)! and a beta integral; it contributes q!(m−1)!m^(−(q−k))/(m+q)! to E[MP]. Subtracting E[M]E[P] gives the stated bracket. The q=2 covariance, normalized correlation, and conditional Greenwood mean follow with E[G]=2/(m+1) and the indicated variance formulas. In the fixed-q limit, expansion of the factorial ratios gives variance coefficient (2q)!−(q!)²(q²+1), strictly positive as the variance of Y^q−q q!Y for Y exponential of mean one and q≥2. Its combination with the leading covariance and Var(M) yields the stated normalized limit.

## originality

PASS

Credit the classical minimum survival law, the known subtraction/residual construction and the Greenwood marginal moments. The checked prior work on the same simplex gives ordered-spacing or square-sum marginals and an exact-minimum residual construction, not the real-power covariance transition and explicit mixed-moment and correlation formulas. Nearby Resultary records change at least one of the two statistics. The pass concerns the particular dependence statements and their evaluations, not priority for the conditional simplex law.

## value

PASS

The canonical minimum-gap and spacing-dispersion summaries measure different departures from evenness. The result quantifies their dependence uniformly in sample size, distinguishes concave from convex powers, and supplies directly usable null covariance and correlation instead of requiring a new simplex integral for each size. The q=2 magnitude and the threshold response provide more information than the sign alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
