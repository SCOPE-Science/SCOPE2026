---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A stationary mild age profile is J S(a) by applying characteristics for a time longer than a, with J=λTV. Local integrability at zero gives the trace S(0)=1, and absolute continuity gives S′=−sS and ∫sS=1−S(∞)=σ. For J>0 its L¹ norm is finite exactly if m=∫S<∞, in which case sJS is also integrable and the stationary age balance holds with its boundary trace. At stationarity L=rA/(η+μ) and A=cV/p give Jσ=dA, where d=δ+rμ/(η+μ). If V=0 these balances and the age boundary force i=A=L=0 and T=ψ/γ. If V>0, cancellation forces T=dc/(λpσ)=ψ/(γR₀); the T balance gives V=γ(R₀−1)/λ and J=ψ(1−1/R₀). These coordinates are unique, require R₀>1 strictly, and all balances hold on substitution if m is finite. An integrable hazard has S(∞)>0, so excludes such an equilibrium even when R₀>1 in the source's stated L¹ space. The explicit integrable-hazard example gives d=3/2, σ=1/2, R₀=2 and J=3, so its profile tends to 3/2. For s(a)=k/(1+a), S=(1+a)^(−k), σ=1 and the finite-mass threshold is exactly k>1; with J=3/2 this gives mass 3/[2(k−1)]. For transients the initial-age part is the integral of i₀(b)S(b+t)/S(b), bounded by ||i₀||₁. In the influx convolution with divergent K, the discrepancy from jK is bounded by εK plus a fixed early-time bound when J tends to j; division by K gives the claimed conditional limit. The floor S(∞) gives the stated unconditional lower bound in the source regime. The frozen numerical/algebraic checker was inspected, not executed; the infinite-age statements have analytic proofs.

## originality

PASS

Credit the model-specific correction: the exact source's positive-equilibrium threshold is incompatible with its own phase space under the printed hazard assumption, and the missing integrability condition is sharp for an explicit extended class in which R₀ alone stays fixed. This is not priority for the general stationary survival profile, characteristics, or the elementary weighted-average limit principle.

## value

PASS

The result corrects an actual published equilibrium assertion in the specified space, not a numerical normalization or algebraic restatement. The source-admissible counterexample rules out interpreting the formal positive coordinates as an L¹ equilibrium. The heavy-tail boundary shows why eventual transactivation alone does not rescue the existence claim and identifies precisely the additional residence-time property that does. This prevents confusing local-in-age finite profiles or truncated-grid states with finite total stationary mass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
