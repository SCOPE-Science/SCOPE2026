---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS. Read actual RESULT.md and verification/check.py. Set B=sδ/(s+δ), H=h+B, sigma=H−1/m, a=δ/(s+δ), z=v−s/(s+δ)−au. Exact u'=-Fσ(u)+δuz and z'=−(s+δ)vz−au', with Fσ=σu²+u³/[m(m+u)]. Inward signs at z=±CFσ, C>4a/s, ensure an invariant tube and u'=-Fσ(1+O(u)). Reciprocal powers give tu²→1/(2H²) at σ=0 and tu→1/σ when σ>0. Hitting-time scaling u=σV/H² leads by dominated convergence to Θ(V)=1/V+log(V/(1+V)), strictly decreasing. Independently verified Θ'(V)=−1/[V²(1+V)]. The finite ODE checks cannot prove the singular limit.

## originality

PASS

PASS at best knowledge. Xia et al. introduced the same nonlinear-dispersal two-patch model and studied its equilibrium and center manifold, not the exact trajectory-level singular crossover. Generic cubic normal forms suggest t^(-1/2), not all the precise tube, clock and locally uniform quantifiers. An unindexed equivalent critical slowing theorem remains a risk.

## value

PASS

PASS. Sharp two-regime extinction clock at a natural quadratic-degeneracy threshold, with model-specific coefficients and an explicit transition profile, is a motivated dynamical theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
