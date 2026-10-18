---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

On the pairwise-identical strain-parameter subspace, let r=μ_L+δ, τ=Σω_j, s=exp(−Σα_jω_j)>0 and K=rμ_Iμ_V/(sδθ). The equilibrium stage-chain balances with viral concentration v>0 cancel v to give γH/(1+ψv)=K, while the H equation gives φ−η_HH−K(C+B)=0. If ψ=0, H=K/γ and every C+B=T=(φγ−η_HK)/(γK)>0, including two endpoints, solves all seven equations under R=φγ/(η_H K)>1; if ψ>0 both positive strains force C=B=vψ=(φγ−η_HK)/[K(2γ+η_Hψ)] and H=K(1+ψvψ)/γ, giving unique strict coexistence. Antisymmetric perturbations u=L−E,w=Y−Z,z=C−B have zero H tangent and form a 3-stage linear retarded block; eliminating gives (λ+r)(λ+μ_I)(λ+μ_V)−rμ_Iμ_V exp(−λτ)/(1+ψvψ)=0. For real x>−min rates, the polynomial product increases, delayed term decreases, and real F(x) has one simple zero λψ in (−min,0], λ0=0. Modulus of every complex root gives Re λ≤λψ, with equality only for real root. ψvψ is strictly increasing, so λψ strictly decreases. Implicit-function derivative at ψ=0 yields λψ=−rμ_Iμ_Vv0 ψ/[rμ_I+rμ_V+μ_Iμ_V+rμ_Iμ_V τ]+O(ψ²). This proves only the antisymmetric *linear* decay scale ~ψ^(−1), not nonlinear global stability; zero-delay boundaries included.

## originality

PASS

The original seven-state model has saturated-incidence equilibria and Lyapunov stability results; the exact strictly symmetric zero-saturation continuum, exchange-sector real spectral abscissa, and leading small-saturation delay coefficient are not stated in its inspected equations/equilibrium section. General two-strain quasineutral literature treats different stochastic SIS/SIR systems and does not imply this model-specific characteristic root. This is best-of-knowledge subject to specialized bifurcation literature risks.

## value

PASS

The delayed seven-compartment two-virus model is a natural published competition system, and its degenerate identical-strain limit exposes a genuine neutral equilibrium manifold. Exact saturation selection and an all-delay leading real exchange root with explicit singular weak-saturation damping coefficient quantify an otherwise missing slow mode. This is a motivated parameter-boundary statement in an existing model, not merely checking that a known equilibrium satisfies the equations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
