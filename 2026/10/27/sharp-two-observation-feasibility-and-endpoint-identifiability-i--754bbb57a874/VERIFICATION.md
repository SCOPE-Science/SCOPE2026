---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Integration from F=0 gives Kt=B g(F/B), g(u)=u−log(1+u), a strictly increasing forward coordinate for F>0. With u=F₁/B the inverse reduces to Rρ(u)=g(ρu)/g(u)=q and then B=F₁/u, K=F₁g(u)/(t₁u). For h=ug′/g, an independent check is h(u)⁻¹=∫₀¹ s(1+u)/(1+us) ds, whose derivative is the integral of s(1−s)/(1+us)² and is strictly positive. Thus u(log Rρ)′=h(ρu)−h(u)<0. The limits are ρ² and ρ, so neither equality endpoint yields finite positive parameters. As u→0, g=u²/2−u³/3+O(u⁴) gives δ∼2ρ²(ρ−1)u/3, giving the claimed reciprocal-depth and linear-conductivity laws. As u→∞, the exact ratio difference is [ρ log(1+u)−log(1+ρu)]/g(u), so ε∼(ρ−1)log(u)/u and log(1/ε)/log(u)→1. This verifies the logarithmic correction in B and the linear K-deficit with their stated leading constants. Independent bounded checks of the rational derivative identity, the u=1 example and both asymptotic regimes agreed (slower convergence on the logarithmic side). The uploaded script was inspected, not executed. The asymptotics fix F₁,t₁ and ρ>1; the conclusion identifies the product capillary length only and does not assert inference from noisy data.

## originality

PASS

The supported distinct result is the exact range and injectivity for the two known-origin cumulative observations together with the two sharp endpoint laws. The inspected related Resultary inverse theorem has a different data map; no compared source establishes the frozen classification or its endpoint constants. The standard forward law and generic calibration are not original here. The pass is bounded by the indicated historical-access risks.

## value

PASS

The natural minimal known-origin observation design admits a complete, exact compatibility test and a unique parameter pair when compatible. The unequal endpoint rates explain distinct analytic parameter degenerations at the two feasibility boundaries; they are not supplied by the existence of the classical forward formula or a numerical fit. This is useful as a model check and a baseline for conditioning analyses, without treating exact feasibility as statistical reliability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
