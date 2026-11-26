---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Checked the ordered source/destination flux including the factor bV/2 (or rV/2) and conservation of total neighborhood mass and both household counts. The two-density log-partition is strictly convex since the six states affinely span two dimensions; subtracting the linear mean constraints makes it coercive because the target mean is strictly inside the support triangle. For a relocation, factorials cancel against source multiplicity and destination vacancy, and (β+λr)a^r=β on allowed blue-source states with r=0 or 1, with the same identity for red. The three forward/reverse tests give p_B²=4p_00 p_BB, p_R²=4p_00 p_RR, and 2p_00 p_BR=a p_B p_R. Their reaction vectors span the mass-and-density tangent space. For interior p the usual paired-flux entropy dissipation vanishes only at the unique Gibbs law. Boundary data are also covered: the marginal rates A_B=2βρ_B+λp_BR, A_R=2βρ_R+λp_BR and the vacancy-scaled departure rates give uniform lower bounds on the connected graph's enabled transitions. Integrating along a path over any unit interval gives a uniform positive transition probability, hence a uniform component floor after time 1. The local entropy production quadratic is Σ F* (ν·diag(1/p*)ξ)²; if it vanishes on the tangent, diag(1/p*)ξ is orthogonal to that tangent and ξ·diag(1/p*)ξ=0, so ξ=0. The quadratic rate near equilibrium and the strict dissipation gap on the remaining compact positive set give exponential entropy decay, hence exponential ℓ¹ convergence. For the response, holding the two means fixed gives the positive conditional covariance Schur complement for br; strictness follows because br is not affine in (b,r). Since log a strictly decreases with λ, p_BR strictly decreases, and λ=0 gives the independent baseline. Also checked the displayed factorization for direct strict suppression. The frozen checker was inspected without execution; its finite rational event tests and entropy example do not certify the infinite-time or monotonicity results.

## originality

PASS

Credit Cao–Cortez for the identical ODE and the zero-intolerance convergence theorem, and general detailed-balance theory for the positive-trajectory global-attraction implication once this network and equilibrium have been identified. The supported distinct contribution concerns the joint positive-intolerance and positive-baseline regime: model-specific detailed balance with arbitrary admissible, possibly unequal densities, an exponential bound from all compatible boundary or interior data, and strict response of the mixed fraction at fixed densities. The static two-house algebra alone is not credited as original.

## value

PASS

The regime with both background relocation and social intolerance is not settled by treating either of them alone. The exact equilibrium shows that positive baseline mobility precludes multiple compatible equilibria even while intolerance strictly suppresses mixing at fixed densities. The convergence bound includes initial distributions supported on only a few of the six types. The strict response is a useful quantitative distinction between uniqueness of the equilibrium and absence of segregation pressure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
