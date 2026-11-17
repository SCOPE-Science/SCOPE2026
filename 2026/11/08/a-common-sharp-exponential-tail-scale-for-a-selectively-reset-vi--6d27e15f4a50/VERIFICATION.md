---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

e^{At}=I+(1-e^{-lambda t})A/lambda yields exact Gaussian innovation variances U,V=2t/(gamma+1)+O(1). Embedded bath Q_j=a(T_j)Q_{j-1}+Gaussian yields unique stationary perpetuity; cosh drift shows subcritical exponential moments, Gaussian-noise moment divergence handles endpoints. Independent exponential age gives X MGF with positive bounded bath factor; Chernoff and age-saddle lower bound match rate for both coordinates. Independent matrix moment equations at gamma=1,r=2 yield (X²,XQ,Q²)=(.8,.6,1.6). Finite numeric slope checks only corroborate.

## originality

PASS

The prior lower-tail estimate is one half of the desired sandwich but leaves the other half and unreset bath asymptotics unproved; no implication of the final exact theorem.

## value

PASS

Sharp two-sided finite-memory extreme-tail behavior of both the reset observable and the retained bath coordinate resolves a physically meaningful noncommuting far-tail/quasistatic limit, beyond the published one-sided excursion obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
