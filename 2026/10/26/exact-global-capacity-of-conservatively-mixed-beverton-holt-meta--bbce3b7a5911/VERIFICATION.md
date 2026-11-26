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

The frozen mathematics is correct; the repair narrows the contribution and specifies the geometry as the relative interior of a polytope. For all fixed positive stochastic D the positive Perron vector supplies a small strict lower solution (the column sums of the linearization exceed one); the growth bounds supply an upper solution. Strict subhomogeneity excludes a first-touch scaling between two distinct positive fixed points, and the iterated bounds can contain every positive initial state. In both versions, C−2B is the sum of a_i(s_i−1)^2, so the smaller root t is in (0,1); 1+b_i y_i*=s_i/t gives both the common derivative and the balance sum_i[g_i(y_i*)−y_i*]=C−B(t+t⁻¹)=0. Writing g_i as (s_i²/b_i)(1−1/(1+b_i z)) and subtracting its tangent gives exactly the displayed signed quadratic loss with denominator 1+b_i z. Summing uses equal pre- and post-recruitment totals and gives the factor 1−τ, not 1+τ. Equality forces y=y*, whence x=x*, and conversely Dx*=y* is sufficient by equilibrium uniqueness. Positive rank-one columns y*/N* realize this map. Scaling columns by x_j* gives precisely row marginals y* and column marginals x*. The last row and column are determined by the leading (p−1)×(p−1) block; the positive product array shows positivity removes no affine dimension. Any zero-entry feasible array is on a relative supporting hyperplane, so the repaired relative-interior statement is exact. At z=K the same loss formula yields equality exactly at common r, since g_i'(K_i)=1/(1+r_i). The benchmark follows from a=(1,1), s=(2,3), B=5, C=15. The frozen verify.py is a replay path for that benchmark and finite numerical equilibrium cases; it was inspected, not executed, and does not prove uniqueness of a maximizing matrix.

## originality

PASS

The frozen presentation does not pass originality as a new global-capacity theorem: a separate published Resultary result supplies the same ceiling, allocation, rank-one attainment and strict gain condition, with broader adaptive coverage and the same exact two-patch example. This is claim coverage, not a priority finding. The repaired paper credits that coverage and treats the scalar ceiling as setup. The surviving claim is the exact, pointwise matrix-equilibrium loss formula and its explicit full optimizer geometry. Adaptive allocation rigidity implies the condition Dx*=y* for a constant optimizer but supplies a different, one-sided quantitative bound, not the exact matrix-equilibrium loss. The transportation-polytope dimension is a standard geometric argument; it is the combination with the exact dynamical loss, not an originality claim for general transportation-polytope theory, that survives.

## value

PASS

The repaired claim measures how far a given fixed dispersal policy falls short, not just whether a maximizer exists or whether unequal growth can help. The weighted patch costs distinguish where inefficiency occurs and are exact away from the optimum; the adaptive curvature inequality cannot provide those costs. The optimizer geometry tells an investigator which distinct fixed dispersal networks are equivalent at optimal equilibrium, rather than privileging one rank-one choice. The elementary transport dimension calculation is useful in this combined result, not an independent contribution; no value is claimed for republishing the scalar ceiling or the numerical benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
