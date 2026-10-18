---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

In the unreduced chronological/vaccination-age SISUV transport system, disease-free susceptible cohorts have Q_0=p e^(−νx), S_0(x,y)=ν p(x)e^(−ν(x−y)), so protection Pν(x)=∫_0^x νe^(−νa)e^(−(x−a))da, with P0=0, P1=xe^−x and P∞=e^−x for x>0. Infected vaccination flux cancels from H=J+∫I dy; linearized H/p transport and mosquito v equation yield characteristic s+ρ=(Λ/(ρN))∫θ(a)gν(a)∫_a^A σ(x)p(x)e^{−(γ+s)(x−a)}dx da. For positive coefficients the real right side decreases with nonnegative s, while modulus excludes ANY Re(s)≥0 when K(ν)<1; K>1 gives positive real root. Explicit A4, μ=γ=ρ=σ=1, Λ28, b=1/(1−e^−4), θ=.001+1_[2,3] gives independent high-precision integrals K0=1.17302280127..., K1=.91682546196..., K∞=1.05777130035...; IVT gives at least two ν threshold crossings. Independent integration used separate quadrature and original rational verifier was read. No nonlinear endemic or global stability assertion.

## originality

PASS

Best-of-knowledge PASS narrowly for the fully specified counterexample in the original Banerjee–Götz–Panda non-averaged equations. Their endemic fixed-point analysis substitutes a constant average efficacy and low-infection mosquito approximation; the claimed linearization retains vaccination-age dynamics and an age-specific θ. General vaccination-age reproduction-number methods and known timing/waning intuitions are prior and not claimed new. Webb 2025 is a plausible broader source but the exact parameter example and implication were not found in accessible descriptions; full Webb 2025 text was not fully inspected and remains risk.

## value

PASS

A mathematically exact nonmonotone vaccination-rate invasion counterexample in a specified full age-structured vector/host system; timing of a one-time dose and waning efficacy can make extremely rapid vaccination worse than an intermediate rate in a late-exposure window. This establishes a precise boundary for naive monotonicity of control, without being a clinical recommendation or a claim of real-world parameter calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
