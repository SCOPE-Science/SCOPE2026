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

Reconstructed the base minimization, the smooth competitors and the nonsmooth perturbation argument. With fixed side normals one may tighten to polygon supports. A bounded tightened four-normal configuration has gaps <π; all 511 such choices, with feasibility of all consecutive intersections, were checked exactly. The seven minimizing choices tie exactly with R*=4/7+3/(7 cos(2π/7)); the incircle gives a strict three-side exclusion (moving lines to tangency and applying Jensen to tan of half the normal gaps). The seven edge-supported competitors are smooth and feasible nearby. Cyclic symmetry forces the full-space derivative of their sum to have coefficients a v_j+b Jv_j, and scale and rotation invariance kill both. Independent replay is python3 /workspace/branches/heptagon_exact.py (SymPy exact cubic-field arithmetic, rational root isolation for signs). It uses y scaled by sin(π/7) and directional coefficients from recursively solving the support-line intersections rather than interval jets. It verifies exact zero gradient sum, a nonzero six-row minor (−4.5458439150×10⁻⁶ in scaled coordinates) and a negative definite mean Hessian on the two-dimensional kernel (first diagonal −0.2793676660, determinant 0.0087125651 in the scaled basis). The geometric and exact algebraic checks are consistent with the frozen numbers after undoing the coordinate scaling. Off the kernel the minimum linear variation is uniformly negative on a complementary unit sphere. For complementary size ≥ L times kernel size squared the negative linear term absorbs the quadratic remainder; otherwise the averaged Hessian gives the required quadratic deficit, with mixed terms of smaller order. This proves a local result only, without claiming an explicit radius or sharp c.

## originality

PASS

Credit the known exact regular-heptagon ratio and the seven support minimizers, including the matching same-day base-point computation. The distinct result is the quadratic stability inequality for actual chord-eligible enclosures under arbitrary small affine-normalized perturbations. Available strongest comparisons are numerical local evidence or discrete gaps at the single base polygon; neither gives the common-kernel computation or the resulting local perturbation theorem.

## value

PASS

Proves a local observation in the literature for a natural constrained version of a circumscription problem, and distinguishes actual geometric stability from the already known discrete gap at a fixed polygon. The common kernel has two genuine non-affine directions, so the second-order argument addresses perturbations not separated by first variation; the result is a quantitative strict local maximum, not an exact-value recomputation or a global conjecture claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
