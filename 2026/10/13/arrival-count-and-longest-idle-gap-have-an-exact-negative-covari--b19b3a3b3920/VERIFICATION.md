---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Conditional on count n, n uniform points on [0,t] give Dirichlet(1,...,1) normalized n+1 gaps, including the right censored last gap; integrate the exact inclusion-exclusion tail to get E[L|N=n]=t H_{n+1}/(n+1) even at n=0. The harmonic exponential generating function e^μ Ein(μ) yields E[L]=t Ein(μ)/μ. Poisson score identity Cov(N,g(N))=μ d/dμ E[g(N)] gives t/μ[1-e^{-μ}-Ein(μ)]. Its negative sign follows from derivative of Ein(μ)-1+e^{-μ} being [1-(1+μ)e^{-μ}]/μ>0. Independent 90-term direct Poisson mixture at μ=3,t=2 computed covariance -0.4924422686878027 versus analytic -0.49244226868780216; checked both small μ -λt²/4 and large μ -(log μ+γ-1)/λ. Correct only for homogeneous Poisson fixed window including both endpoint gaps.

## originality

PASS

Known uniform simplex maximum mean and Poisson longest-gap marginal laws fully credited. Their combination with the standard Poisson score identity yields an exact *joint* count/gap covariance and universal strict sign; no inspected exact formula under cross-moment aliases. This is a concise, natural quantitative extension, with sizeable old-spacing-literature residual risk.

## value

PASS

Count and maximal idle gap are canonical observables of the same Poisson process; their exact negative covariance (all intensities and windows) measures a meaningful dependence absent from the known separate marginal formulas. The derivation is short but the joint statistic and sign are independently useful, with modest rather than paper-sized mathematical scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
