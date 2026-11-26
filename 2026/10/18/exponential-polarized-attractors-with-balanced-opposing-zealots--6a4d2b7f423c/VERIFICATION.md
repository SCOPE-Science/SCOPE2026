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

Fix the finite simple undirected graph and δ∈(1,4). The squared distances at every sign vector are 0 or 4; at zero they are 0 or 1. Choose disjoint fixed neighborhoods with positive cutoff margins. The weights differ from their retained/dropped limits by O(exp(−cγ)), and their first derivatives by O(γ exp(−cγ)); each denominator has a retained zealot contribution, so convergence is C¹. At each corner the limit numerator is −(I+Lσ)(x−σ). Applying the contraction x↦x+(I+Lσ)⁻¹Nγ(x) on a small ball gives a unique nearby equilibrium and displacement of order ||Nγ(σ)||=O(rγ). The exact corner force is −2rγ b/(1+rγ); integrating the uniformly convergent derivative along the displacement gives the displayed first-order term. On each sign component, a minimum of the unsigned correction solves (I+Lσ)y=1+dopp and is at least one, so the equilibria are strictly inside the cube eventually. At the zeros, the normalized Jacobians converge to negative diagonal scalings of symmetric positive definite matrices, similar to symmetric negative definite matrices. The exact center has limit with L_H+2I. In the scalar case, the uniform margins outside small neighborhoods of 0, a=√δ−1 and 1 exclude extra roots; negative slopes near 0 and 1 and inward endpoint force give the center and unique outer roots. At any transition root W−=(1−x)W+/(1+x) stays bounded away from both 0 and 1, so the γ-weighted opposing derivative gives a strictly positive slope. All transition roots would be upward crossings, hence the endpoint signs give exactly one. Its equation first gives u−a=O(γ⁻¹), then expansion of the logarithm gives the stated coefficient and O(γ⁻²) remainder. At v, the corner estimate yields γ(1−v)=o(1), justifying the sharp outer exponential rather than substituting v→1 into a γ-dependent exponent. The resulting sign diagram yields the stated basins on the physical interval, including fixed unstable endpoints. The proof checks are analytic; the frozen numerical script was inspected, not executed. No exact count for n≥2 or uniform graph-size cutoff follows.

## originality

PASS

The model, balanced-exposure center and high-steepness stability of the center are already in Brooks–Chodrow–Porter or follow directly from their exact criterion, and the frozen text credits that background. The retained contribution is the simultaneous existence of all binary polarized branches on every fixed admissible graph, their graph-dependent leading displacement, and the full scalar large-steepness classification with rates. A later same-model scalar tristability theorem materially overlaps the five-root phenomenon in a different steepness/cutoff range; it does not establish the retained quantitative result.

## value

PASS

A complete persuadable network can still have exponentially many attracting polarized states alongside its neutral attractor. The inverse within-camp Laplacian makes heterogeneous opposite-camp forces predictive at large finite steepness; in the smallest model the unstable transition-layer roots identify the basins quantitatively. These claims add resolvable dynamics rather than recomputing known center stability, without implying empirical prevalence or a higher-dimensional basin census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
