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

At stationarity, fresh N(0,sigma²) Poisson redraws preserve the Gaussian one-time velocity distribution; two velocities are correlated only if their interval has no collision, so covariance is sigma² exp[-(gamma+r)|t-s|]. For ordered four-time gaps a,b,c, conditional Gaussian block pairings yield cumulant 2 sigma⁴ exp[-lambda(a+2b+c)](exp(rb)-1), lambda=gamma+r; checked independent enumeration of 8 collision-pattern configurations for two parameter sets. Integrating the connected cumulant over the ordered four-time simplex gives cum4(X_T)=48 sigma⁴∫_0^T exp[-2lambda b](exp(rb)-1)J_lambda(T-b)db>0; J_lambda(L)=∫_0^L q(L-q)exp(-lambda q)dq. Var X_T=sigma² B_lambda(T), B=2∫_0^T(T-h)e^-lambda h dh. The ratio B_lambda(T2)/B_lambda(T1) for 0<T1<T2 strictly decreases with lambda by monotone likelihood ratio of weighted lags; determines lambda, first variance determines sigma, strict monotonicity of positive cum4 integral at fixed lambda determines r, then gamma=lambda-r. Boundaries require gamma,r,sigma>0 and exact ensemble moments, not empirical finite sample certainty.

## originality

PASS

Qualified best-of-knowledge original evaluated final claim relative to the inspected primary results and actual Resultary semantic search, not a universal historical priority certificate. Prior renewal switching frameworks contain general propagator tools but no verified same exact stationary cumulant and two-window inversion conclusion.

## value

PASS

A natural renewal thermalization model is invisible to every quadratic observation despite distinct non-Gaussian fourth-order behavior; the exact three-displacement-moment inverse theorem provides a practically motivated structural identifiability result, with sharp strict positivity/monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
