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

The symmetric irreducible Metzler star eigenvalue is simple; its second derivative along a nonzero budget direction is positive unless the diagonal perturbation is scalar. A scalar perturbation is incompatible with Σh_i=0 unless h=0, so the optimizer is unique. Leaf permutations then force equal leaf vaccines. Orthogonally decomposing the star gives m−1 leaf-difference eigenvalues and a 2x2 block whose larger eigenvalue F(x) is strictly dominant. Its derivative F′=(1/m−κ)/2 + (κ+1/m)Δ/[2√(Δ²+4mμ²)] and F″>0. The interior stationary equation solves Δ=μ(κm−1)/√κ and x=(B+mμDκ)/(κm+1); clipping to [0,B] proves the exact all-real parameter allocation and endpoint transitions. Substitution yields the affine interior λ*. Independent NumPy full eigenvalue calculations checked 84 configurations against 61 competing symmetric allocations each; finite tests corroborate the proof only.

## originality

PASS

Spectral convex vaccination allocation and symmetric epidemic Laplacians are known. The contribution asserted is the full heterogeneity-parameter exact center/leaf resource phase diagram for continuous allocations on a star, including strict uniqueness and affine interior branch. Closely related published pandemic-vaccination studies and network spectral design may subsume special cases; priority qualified.

## value

PASS

The analytic result provides a complete fixed-budget resource-allocation phase diagram on a natural symmetric mobility graph, with a non-obvious optimal center-to-leaf switch controlled by heterogeneous efficacy and mobility, strict uniqueness and exact minimized growth. This is a motivated control-theoretic invariant, limited to early linear growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
