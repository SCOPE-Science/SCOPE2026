---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction instructions

Run `python verify_crosspolytope.py` with NumPy and SciPy available. The script independently constructs the convex hulls of near-regular spherical cross-polytopes of dimensions \(2\) through \(6\), computes their volumes through SciPy and through the opposite-half-chord determinant identity, and verifies the nonlinear upper envelope. It also constructs displaced equal-singular-value configurations and verifies exactness numerically.

The all-dimensional mathematical verification is analytical: combine the oriented-boundary determinant formula with orthogonal Procrustes singular-value duality and the geometric-arithmetic mean inequality. The scalar-orthogonal equality locus follows from equality in this mean inequality. Small nonzero shape discrepancies are achieved by a cyclic shift of vertex-pair midpoints; the combinatorial facet structure is stable under sufficiently small perturbations of the regular realization.

The numerical tests use finite examples only; they are not exhaustive and cannot independently establish the infinite-dimensional-parameter claim. No independent audit is represented by this file.
