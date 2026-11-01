---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For d≥2 and u∈C⁵, Taylor expansion of Hε fε Hε⁻¹ with Hε=id+εu and v=du−u∘T_d cancels the O(ε) term and produces Gε=T_d+ε²u′(d·)v+O_C²(ε³). Consequently (log Gε′−log d)/ε²→φ=w′/d in C¹. The log derivative changes under conjugacy by a bounded coboundary, so Green–Kubo variance is invariant. Bernoulli coding with uniform inverse-branch contraction bounds correlations by Cλ^(−n/2), proving continuity and σ²(ε)/ε⁴→V_Td(φ). For u=−sin(2πx)/(2π), φ has modes −1/2 cos2πx, 3/2 cos6πx, −cos8πx: exact independent Fourier arithmetic gives covariances 7/4,0,1/4,0 thereafter, yielding 9/4. Uniform expansion holds |ε|<1/4 for this example; the general result is sufficiently small |ε|.

## originality

PASS

No inspected earlier theorem establishes the quartic maximal-entropy Lyapunov variance coefficient for a perturbation tangent to smooth conjugacy. The strongest same-observable prior supplies the fixed-map Green–Kubo/CLT framework, not the two-parameter ε→0 onset; this is a best-of-knowledge PASS.

## value

PASS

Near the linear covering the observable log f′ is cohomologically trivial. A conjugacy-tangent deformation annihilates the usual quadratic onset; the explicit quartic coefficient 9/4 measures a geometrically motivated second-order obstruction and proves small nonzero perturbations are not smoothly conjugate. This gives a precise benchmark for degenerating fluctuation variance, beyond a routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
