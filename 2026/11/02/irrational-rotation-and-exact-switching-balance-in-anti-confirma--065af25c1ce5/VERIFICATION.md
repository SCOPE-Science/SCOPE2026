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

The precise Bayesian fractional rule yields log-odds increments +a below 0 and -b at or above 0 (a=log(1/g_-)>0,b=log(g_+)>0). The half-open interval [-b,a) is forward invariant; iterations outside add a or subtract b until capture. t=(u+b)/(a+b) yields rotation mod 1 by rho=a/(a+b). Every high branch is exactly an integer wrap, telescoping to H_n=floor(t0+n*rho), giving strict discrepancy <1 even when the threshold is attained. Rotation periodicity, density and Fourier uniqueness give the rational/irrational dichotomy and the normalized logistic density. Branchwise chain derivative equals x_n(1-x_n)/[x0(1-x0)] on smooth itineraries, bounded away from zero/infinity after capture. Prime-11 valuations show irrationality for g_-=22/125,g_+=93/50; prime-17 similarly for 3/17,13/7. Independent 18,000-step orbits checked capture and exact wrap counts; finite computation does not establish irrational density.

## originality

PASS

The original Dong–Marzen model reports oscillation under this same two-ratio switching rule. It does not state exact eventual rotation conjugacy, irrationality of its printed parameters, invariant density or exact finite-horizon branch-balance law. The log-odds and rigid-rotation machinery is classical, not claimed new; the assessed contribution is the complete model-specific classification and sharp all-horizon statistics. Nishi–Masuda is a peer-signal stochastic model with a different update law.

## value

PASS

A genuine gap remains between the source observation of repeated oscillation and the exact distinction that the very parameters used to illustrate cycling are mathematically nonperiodic; every initial interior belief has identical orbit closure and strictly <1 switch-count imbalance on its local clock. The all-parameter classification and all-horizon invariant are useful for interpreting and testing the motivating Bayesian model rather than simply renaming a rotation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
