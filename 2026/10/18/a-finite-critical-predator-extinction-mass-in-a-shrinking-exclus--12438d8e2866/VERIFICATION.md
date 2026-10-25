---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For 0<a<L, positive d_u,d_v,r,α,β, 0<θ<1/2, and sufficiently small positive predator introductions near u≡1 at γ=α, comparison traps prey deficit w=1−u in a stable neighborhood and bounds predator v≥0. The spatial predator mean z is decreasing and cannot tend to a nonzero value: a positive Neumann heat-kernel bound would force persistent w>0 and negative z′. The positive Neumann spectral gap forces v/z→1 as t→∞. The prey stable resolvent B=d_u∂xx−λ implies w/z→βψ_a where ψ_a=(−B)^{-1}1_(0,a). Substituting into z′ gives (1/z)′→αβ s_a and thus t z→1/(αβ s_a), with uniform predator and prey profiles. Direct differentiation and Neumann/interface matching verify ψ_a is piecewise hyperbolic as stated; independent SymPy finds zero function and derivative jumps and the average s_a. The thin-zone coefficient s_a/a→κ/(λ tanh(κ L)), yielding lim_{a↓0}lim_{t→∞}t∫_0^a v dx=√(λ d_u)tanh(L√(λ/d_u))/(αβ). This is an iterated limit, not uniform in a. Key semigroup domination requires δ chosen with αδ below prey/predator gaps, available at each fixed positive a.

## originality

PASS

The 2026 Berestycki–Fagan–Safsten exclusion-zone model has subcritical predator extinction and supercritical coexistence analyses, while the submitted theorem isolates exact conversion–mortality equality, algebraic 1/t extinction, spatial Neumann resolvent amplitude and the order-sensitive thin-zone mass. The comparison is of parameter implications, not titles; threshold asymptotics are not delivered by those cited equilibrium results. Best-of-knowledge with risk from broader center-manifold asymptotic theory.

## value

PASS

The marginal predator spectral mode at exact growth/mortality balance is a motivated nonhyperbolic boundary of a concrete reaction-diffusion exclusion model. A universal leading amplitude depending on prey diffusion and vanishing zone size, but not predator diffusion, quantifies slow critical extinction and the noncommuting geometry/time limits, useful beyond merely reasserting extinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
