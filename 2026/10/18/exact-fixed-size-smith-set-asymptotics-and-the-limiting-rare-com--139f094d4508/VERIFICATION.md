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

Independent continuous uniform scores generate the specified independent voter permutations. Strong components of a tournament have uniformly oriented cross-edges and their condensation is a totally ordered tournament. Hence a fixed s-subset is the Smith set exactly if its own tournament is strongly connected and it beats every outsider. Conditional on its scores x, each outsider is forbidden by the union of the majority cylinder boxes with volume b(x), independently of other outsiders. The exact probability is therefore binom(n,s) times the integral of H(x)(1−b(x))^(n−s). At x=n^(−1/ℓ)y group the cylinders by their ℓ-coordinate voter subsets. The union within a group has volume n^−1 V_J(y) exactly; an intersection across distinct groups constrains at least ℓ+1 coordinates and contributes O(n^(−1−1/ℓ)) uniformly on bounded y. This yields the limiting kernel H(y) exp(−Φ(y)). For the global bound, b is at least the average of its s binom(m,ℓ) cylinder volumes, so the scaled kernels extended by zero are bounded by a product of e^(−a σ_ℓ(y_i)) with a>0 for n≥2s. To check integrability, order a row, let t be its ℓth-largest coordinate, and write the larger coordinates as t u_i with u_i≥1. The smaller coordinates contribute a factor proportional to t^(m−ℓ), and σ_ℓ is at least t^ℓ∏u_i. Integrating t then bounds the row integral by a finite constant times ∏∫₁^∞u^(−m/ℓ)du since m>ℓ. Dominated convergence gives L¹ convergence of scaled kernels. The binomial asymptotic and the score Jacobian give factor 1/s! and exponent ms/ℓ−s=s(ℓ−1)/ℓ. Positivity follows from three cyclic orders of three nonempty blocks (the directed inter-block cycle makes the whole tournament strongly connected), with the extra voters in opposite pairs; this gives an open positive-volume set of scores. Exchangeability for the increasing-label lists contributes the same binomial factor in the unnormalized conditional density, so normalizing cancels it and yields the stated TV convergence. The proof requires fixed ℓ,s, and the conditional law uses the specified score representation. The frozen finite-profile and rational overlap checks were inspected but not run; they do not prove either limit.

## originality

PASS

The supported increment is the exact fixed-s≥3 union-volume coefficient and the TV law for all rescaled scores of the rare core. The exponent and the basic score/conditional-independence representation are prior, and the exact one-candidate equivalent (with a TV deduction) is already covered. None of the inspected stronger-looking statements gives this multi-candidate law.

## value

PASS

For a rare event in a standard voting model, the order theorem left the coefficient and the law of the conditioning event’s score geometry unresolved. The shared-outside-alternative union volumes distinguish the law from a product of one-candidate laws, and TV convergence controls bounded measurable features of this fixed-size core, not just its occurrence rate. This is a concrete probabilistic improvement within the fixed-parameter regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
