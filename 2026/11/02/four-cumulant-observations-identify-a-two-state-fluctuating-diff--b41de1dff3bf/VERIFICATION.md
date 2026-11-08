---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For stationary two-state continuous-time switching, the Brownian displacement conditional on occupation is centered Gaussian of variance 2A_t. Thus K2=2E[A], K4=12Var(A), K6=120cum3(A). The centered indicator Y has covariance p(1-p)exp(-lambda|u-v|), and three-time centered correlation p(1-p)(1-2p)exp(-lambda(max-min)); integration yields K2=2mu*t, K4=24w*t^2 F(lambda*t), K6=720c*t^3 G(lambda*t), F=(z-1+exp(-z))/z^2, G=(z-2+(z+2)exp(-z))/z^3. The elasticity H=-z F'/F has H'>0 (positive cosh remainder), so F(lambda*t1)/F(lambda*t2) is strictly increasing on lambda>0 from 1 to t2/t1 for 0<t1<t2. Consequently four cumulant values uniquely determine lambda,mu,w,c, and algebraically delta=sqrt((c/w)^2+4w), p=(1-c/(w*delta))/2 and both diffusivities/rates. All boundaries checked: positive rates, strictly ordered positive diffusivities, stationary start, any distinct positive observation times, symmetric p=1/2 allowed. Fixing mu,w,lambda and varying admissible p gives a nonidentifiable continuum for complete K2,K4 curves; invariance of domain excludes any three-continuous-scalar injection from the open four-dimensional parameter space. Numeric ODE checks corroborate but are not the proof. No claim about noisy finite-sample inference or other switching models.

## originality

PASS

Qualified PASS: the finite-observation inverse-identifiability theorem, unique monotone time-ratio inversion, and fourth-cumulant insufficiency are not established as such in the inspected forward or inference results. Existing same-model full forward characteristic transforms cover much underlying moment physics, which is credited; a stronger inverse corollary remains a priority risk.

## value

PASS

Exact global identifiability with a minimally sized fixed observation protocol is an independently useful inverse-problem classification for an established stochastic transport model; the failure of all second/fourth cumulant time courses is a meaningful impossibility boundary. The result is not merely a forward-moment recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
