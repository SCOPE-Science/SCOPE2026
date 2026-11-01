---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Uniform ordinal-sum points are obtained by uniformly permuting consecutive order-statistic rank blocks, yielding volume ∏m_i!/n!. Covariances of uniform order statistics are c_rs=min(r,s)(n+1-max(r,s))/((n+1)^2(n+2)). Within-layer contrast variance λ_i=(m_i+1)(m_i+2)/[12(n+1)(n+2)]; group-average covariance has normalized k×k block B. Orthogonal block determinant then gives exact detΣ. For fixed k and positive α, n c_rs converges to Brownian-bridge covariance; Riemann sums give B→C positive definite. Uniform Taylor for λ_i and Stirling for volume cancel O(n) terms, leaving −(k−1)log n+γ_k(α). Independently enumerated rank permutations and exact Fractions for (2,2),(1,2,1),(2,1,2) verify determinant; finite enumeration is not asymptotic proof.

## originality

PASS

Best-of-knowledge statement-and-implication comparison after querying Resultary and checking relevant primary literature: the actual full claim, not just title, is not entailed by an inspected stronger theorem. Any acknowledged known special cases are explicitly excluded from novelty. Residual risks are itemized below.

## value

PASS

An exact full-dimensional uniform covariance determinant reduced to fixed k block sums and a universal interface-count (k−1) logarithmic deficit from the cube isotropic constant is a useful structural result for nonsymmetric order polytopes. It is not a routine consequence of merely knowing combinatorial volume or a lattice free-sum structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
