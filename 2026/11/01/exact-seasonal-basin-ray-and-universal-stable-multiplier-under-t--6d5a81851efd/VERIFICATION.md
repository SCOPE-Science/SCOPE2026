---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

With positive continuous T-periodic seasonal coefficients β,μ,b,α,ξ and positive diagonal reset δ1,δ2<=1, equal crowding ξ(t)(x+y) cancels from derivative of log(x/y). The ratio r=x/y obeys r′=r[β(t)r/(r+α(t))−μ(t)−b(t)] and the annual return is R(r)=κφ_T(r)=r exp Q(r), κ=δ1/δ2. ∂_r h=βα/(r+α)^2>0 and scalar flow order preservation make Q strictly increasing. At r→0, Q→log κ−∫(μ+b)<0 by R2=δ2 exp∫b>1, μ>0, δ1<=1; at infinity Q→log κ+∫(β−μ−b)>0 by hypothesis κe^V>1. Hence unique rstar>0, and annual ratio runs monotonically to zero below it and infinity above it. For reciprocal y abundance z=1/y, direct differentiation gives z′=−b z+ξ(1+r), so z_{n+1}=[z_n+H(r_n)]/R2, H(r)=∫_0^T exp(∫_0^t b) ξ(t)(1+φ_t(r))dt. Along invariant ray rstar the unique fixed ystar=(R2−1)/H and globally exact z_n−zstar=R2^(−n)(z_0−zstar) hold. The annual derivative in (r,z) coordinates is triangular: λs=R2^−1∈(0,1), λu=1+rstar Q′(rstar)>1. Away from the ray, convergent affine reciprocal recurrences with positive limiting boundary growth show extinction of the ratio-losing competitor and convergence to respective positive single-species annual cycles. Boundary equality conditions are correctly excluded; no stochastic or unequal-crowding claim. Analytically verified algebra and conditional limits; source time-dependent numerical verifier was inspected but its output is not relied upon.

## originality

PASS

Qualified best-knowledge PASS limited to arbitrary within-season time dependence under identical crowding and exact stable multiplier/reciprocal relaxation. The original constant-rate equal-crowding seasonal Aedes model and qualitative bistability/global classification are clearly antecedents, NOT claimed new. The closest 2025 SIAM full text and 2026 arXiv full article could not be accessed; reading abstracts alone cannot establish whole-article noncoverage. This remains a material priority risk, but no decisive implication/coverage was demonstrated from accessible statements.

## value

PASS

For a nonlinear biological competition model under arbitrary strictly positive continuous intra-season forcing, an exactly straight global basin separator, all-coordinate Floquet multipliers and globally exact relaxation of reciprocal abundance are mathematically useful structural features not implied by generic unstable-equilibrium results. The extension from a constant-rate piecewise season is motivated by time-dependent forcing rather than an arbitrary one-off parameter calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
