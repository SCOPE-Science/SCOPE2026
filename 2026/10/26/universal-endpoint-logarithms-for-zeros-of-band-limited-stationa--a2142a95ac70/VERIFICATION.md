---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For fixed disjoint positive-length spectral arcs E, K(re^{iθ},re^{iθ})=(2π/ℓ)u_t(θ)/(1-r²), u_t the Poisson harmonic measure of E, and Edelman–Kostlan yields EN=r²/(1-r²)-(r/2)〈∂_t log u_t〉. Outside O(t) layers the gap-side u_t=tH_0(1+O(t+t²/d²)) contributes (2π-ℓ)/t, while on the band side 1-u_t=tH_1(1+...), H_1=1/(πd)+O(1) near each endpoint. The derivative errors integrate to O_E(1), so 〈∂_t log u_t〉=(2π-ℓ)/(2πt)-J/(2π²)log(1/t)+O_E(1). Substitution gives support fraction ℓ/(2π) times r²/(1-r²) plus J/(4π²)log(1/(1-r))+O_E(1). Poisson kernel scaled at θ_*+(1-r)x yields Fσ=1/2+atan(σx)/π and derivatives, and Δlog u=-|∇u|²/u² yields π(1-r²)²ρ→1-1/[π²(1+x²)Fσ(x)²] compact-uniformly. An independently written numerical script directly compared Poisson convolutions, derivatives and one/two-band endpoint-log coefficients; the finite tests do not prove the limiting remainder.

## originality

PASS

Shirai 2025 explicitly considers the SAME half-circle spectrum in Example 2.4, but the inspected relevant primary sections calculate a fixed-direction interior-gap density; its smooth-direction theorem does not determine simultaneous θ-θ*=O(1-r) behavior or the integrated positive logarithm for arbitrary finite unions. Noda–Shirai 2021/2023 analyzes finitely dependent coefficients with trigonometric-polynomial spectral densities, without an open zero-spectral-measure gap; such a continuous nonnegative trigonometric polynomial cannot equal the indicator of a proper band. General positivity-jump formulas with both sides positive are singular as one side tends to zero, and so do not automatically imply this hard-edge coefficient. Resultary and targeted literature searches found no stronger matching assertion; this is best-of-knowledge, not proof of historical priority.

## value

PASS

Fixed spectral arcs are a natural band-limited stationary analytic Gaussian model. The exact logarithmic correction is a subleading statistic sensitive to the number of interfaces even at equal total spectral length; its local universal edge profile explains the zero-density transition. Neither is a routine restatement of the ordinary leading zero count or the previously known interior-gap limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
