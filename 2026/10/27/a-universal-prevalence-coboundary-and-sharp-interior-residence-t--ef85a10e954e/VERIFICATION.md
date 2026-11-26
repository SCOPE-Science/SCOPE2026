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

Writing a=γ+μ, the interior derivatives of logit(n), log I and S+I are respectively ε₂[1+θ−(2+θ)x], βS−a and μ(1−x−S)−aI. With the stated coefficients the x and S terms cancel and the constant is μ/β−μ/[a(2+θ)], giving H'=I−I_c independently of the x equation. Interior initial conditions keep both logs defined over finite times. Integrating against an invariant probability with compact interior support eliminates the bounded endpoint differences, giving ∫I=I_c, ∫x=(1+θ)/(2+θ), ∫S=1/ℛ₀ and, by the I equation, β∫SI=aI_c. Positivity excludes such measures at and below threshold, including criticality. On the entire prescribed strip, the displayed numerator bounds the oscillation of H and (δ−I_c)T≤ΔH, yielding the bound only for δ>I_c. Above threshold S*=1/ℛ₀, x*=(1+θ)/(2+θ), I*=I_c, and R*=1−S*−I*>0 (indeed S*+I*<1/(2+θ)); βI*/(βI*+μ)=f*, so the chosen costs with n*=f* cancel the payoff. These values and the rational example satisfy all equations. No assertion about arbitrary costs, global eradication or boundary-reaching averages is supported. Replay: RESULT.md lines 37–70. VERIFICATION.md and verify.py were inspected, not run; the finite checks are corroborative.

## originality

PASS

The positive-interior equilibrium threshold allowing choice of costs is already encoded in Liu–Wu's fixed-point condition and is not credited as new. The distinct part is the exact finite-time elimination for the unreduced SIR/perceived-risk equations, including arbitrary admissible vaccination input, and its compact-invariant mean and uniform interior residence conclusions. The strongest inspected catalogue match has similar mean-balance methods for a different vaccination-memory model, not the same flow or constant.

## value

PASS

The endpoint observable removes two time-dependent quantities, S and vaccination coverage, and constrains trajectories without a fast-epidemic approximation or particular payoff dynamics. It replaces equilibrium-only information with a universal mean for compact interior recurrence and a quantitative residence obstruction even before an asymptotic regime; it does not predict global disease clearance. The threshold alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
