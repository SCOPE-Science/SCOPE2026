---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For invertible A and Euclidean surface-area measure on ∂(AB²ᵈ), Jacobian is |det A| ||A⁻¹u|| (orthogonal/diagonal reduction), while volume covariance is A²/(d+2). The Gaussian identity ||A⁻¹u||=√(π/2) E_G |⟨A⁻¹G,u⟩| plus spherical |⟨z,u⟩|-weighted second moments yields Σ_surface=A(I+Q)A/(d+1), Q=E[ZZᵀ/||Z||]/E||Z||, Z=A⁻¹G. Matrix Q positive definite, diagonal q_i>0 sum1, hence strict Loewner lower bound. A symmetric strictly log-convex mean norm Φ(log 1/a_i) has gradient q_i and implies q_i oppositely ordered to a_i²; reverse Chebyshev gives ∑a_i²q_i≤(∑a_i²)/d, ball-only equality and sharp ratio upper (d+2)/d. Flat family axes (ε,1,…,1) has q_long≤ε and infimum (d+2)/(d+1), not attained. Independently integrated 100,000 angular points for planar ellipses axes (1,1),(.7,1),(.1,1),(.003,1): ratios ≈2,1.94030,1.38135,1.33342, consistent with d=2 sharp [4/3,2]. The analytic proof, not finite quadrature, supplies all-d assertions.

## originality

PASS

Lotnikov 2026 original full-text concerns surface-vs-interior random point distance comparisons for general convex bodies and gives planar classes and higher-dimensional counterexamples, but inspected results do not include exact Euclidean ellipsoid surface-covariance or sharp all-dimensional second-moment ratios. Tokmachev 2026 planar same-centroid convex-order results imply weaker planar comparisons but do not cover all d≥3 ellipsoids, the optimal constants, or the Loewner bound. Classical Rivin and Poelaert–Schniewind–Janssens discuss ellipsoid areas/Jacobians, not the stated covariance classification. An old ellipsoid moment computation remains a potential priority risk.

## value

PASS

The distinction between Euclidean boundary sampling and affine-pushforward sphere measure is natural and important in the current interior/boundary distance program. The exact dimension-uniform interval with sphere rigidity, flattening sharpness and positive-definite covariance comparison establishes a structurally useful canonical family result amid known general convex counterexamples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
