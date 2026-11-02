---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Stationary renewal age A~Exp(r) and conditional Gaussian solution give V(t)=2D(t+γ²t³/3), Cov(Y_ut,X_t)=2Dγt²(u−u²/2), and Cov(X_ut,X_t)=2D u t+2Dγ²t³(u²/2−u³/6). Gaussian-tail mixture has unique saddle t=a√x, a^4=9/(4Dγ²r), f(z)=rz+3/(4Dγ²z³), f(a)=4r/a; Mills ratio/Laplace give sqrt6/4 e^(−λ√x), Gaussian age scale sqrt(a/(4r))x^(1/4), and overshoot O_p(√x). Uniform Gaussian bridge covariance projections yield normalized path shapes with residual sup O_p(t^(3/2)) longitudinal and O_p(t^(1/2)) transverse, negligible at t~√x. At endpoint, Y0≈(3X0/(2γ A))+sqrt(D A/2) Z where Z independent of (A,X0). Age-induced variance c²/(4ra)=Da/4 plus conditional variance Da/2 yields total 3Da/4 and cross correlation −sgnγ/√3. Independent symbolic verification of saddle prefactor squared=3/8 and variance ratios, plus inspected checker numerical covariance kernels. All limits fix D,r,γ with γ≠0; no extrapolation from numeric tail tests.

## originality

PASS

Best-of-knowledge PASS for fixed-parameter joint age/transverse endpoint Gaussian fluctuations with parameter-free correlation and full conditional excursion path in same shear-reset model; published marginal stretched-exponential tail and integrated-Brownian cubic optimal path are acknowledged prior results, not standalone novelty. Closest Abdoli–Olsen–Löwen same mathematical model full text inaccessible, leaving real priority risk.

## value

PASS

The posterior history of an extreme longitudinal displacement is a natural measurable rare-event statistic in coupled stochastic shear/reset dynamics. Exact parameter-independent age–transverse correlation quantifies geometric tradeoff between excursion duration and transverse endpoint and is not determined by known stationary marginals or fixed-duration bridge shapes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
