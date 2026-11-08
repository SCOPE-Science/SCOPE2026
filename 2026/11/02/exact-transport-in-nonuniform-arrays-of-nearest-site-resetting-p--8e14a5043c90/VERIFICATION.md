---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The proposed density solves Dp-rp=0 within each gap, integrates to one and its derivative jumps exactly cancel reset-point delta fluxes; stationarity and irreducibility follow. Harmonic coordinate H on Voronoi cells has matching values and first derivatives at midpoints, H(x+L)-H(x)=L, and generator LH=0, giving bounded-corrector martingale and drift zero. Its continuous/jump quadratic variation integrates to E cosh^2=(T+2S)/(3T), E sinh^2=2(S/T-1)/3 and D_eff=rL^2/(4ST); bounded jump size and ergodicity give CLT. Taylor and max-gap estimates yield the stated low/high rate terms. Independent Gaussian/jump-bracket quadrature and numerical unequal-vs-equal reversal checks pass; these are corroboration, not a replacement for the all-gap analytic proof.

## originality

PASS

Best-of-knowledge, scoped novelty for the exact theorem and parameter regime after checking actual primary results and Resultary; prior methods/ingredients and exact overlaps are acknowledged rather than used as evidence of novelty. No decisive stronger theorem covering this precise claim was identified; remaining priority uncertainty is explicit.

## value

PASS

Exact arbitrary-spacing transport coefficients are natural homogenized observables in a physically motivated resetting model; the fixed-rate ordering reversal and largest-spacing bottleneck make a real structural addition to the known rate-optimized regular-array optimum. This is not a renamed regular-grid formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
