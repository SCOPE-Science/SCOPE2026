---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Stationarity follows from the contraction V law = (1-beta)Z_0²+beta V independent, defining a positive infinite Gaussian quadratic form. All fixed-beta inverse p moments are finite because V dominates a positive multiple of the first n Gaussian squares for any n>2p; the finite-n cutoff follows from polar integration of an n-dimensional Gaussian quadratic form with full-rank positive weights. By Tonelli, M_p=1/Gamma(p) integral_0^infty t^{p-1} prod_{j>=0}(1+2(1-beta)t beta^j)^(-1/2) dt. For noncritical p between successive half-integers, substitute t=beta^{-k}u; the first k factors tend to their power-law limits, the remaining factors to one, and the integrable beta-function majorant yields the exact Gamma expression and exponent. For p=k/2 the same scaling is marginal; change to log-beta time x=log t/log(1/beta). The leading plateau covers one unit interval [k-1,k] with height 2^{-k/2}/Gamma(k/2), tails dominated integrably, producing a single log. The finite startup and beta=0 boundaries are explicitly separated. Independently integrated the Mellin product at beta=1e-3 and 1e-5 for p=.25,.75,1.25: scaled ratios moved toward 1. At critical k=1,2, the two-scale logarithmic slopes match predicted coefficients within 0.54%. Numerical corroboration does not prove dominated-convergence steps.

## originality

PASS

Qualified best-of-knowledge original contribution: A half-integer inverse-moment staircase for a Gaussian RMSprop variance accumulator. Closest prior work and limits are compared by implication, not title; priority risk retained.

## value

PASS

Reciprocal moments of adaptive variance estimates control singular stochastic denominators. The full all-order exact stationary asymptotic and its every-half-integer exponent switch and marginal logarithmic constant describe a natural stochastic invariant in a regime where a positive memory parameter regularizes all moments yet its removal causes a singular hierarchy. Separating finite-startup integrability from the stationary law is relevant to RMSprop analytical estimates and supplies more than a known elementary moment cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
