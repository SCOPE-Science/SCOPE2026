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

On a tree the resistance distance is the sum of r_e=1/w_e along the unique path. Positive radii imply that the diameter is the largest sum of two distinct leaf radii. For fixed R_i, Hölder applied to the factors (c_e r_e^{-alpha})^{1/(alpha+1)} and r_e^{alpha/(alpha+1)} gives cost at least S_i^{alpha+1}/R_i^alpha, with equality uniquely at r_e=R_i c_e^{1/(alpha+1)}/S_i. At unit diameter the feasible radii satisfy rho_i+rho_j<=1. The positive-coordinate cost is strictly convex and diverges on zero-coordinate boundaries of the bounded feasible set. If no radius exceeds 1/2, increasing all smaller radii to 1/2 strictly improves cost. If rho_j=x>1/2, the others must be at most 1-x and all can attain this bound, which uniquely minimizes cost at fixed x. The strictly convex one-variable cost has derivative at 1/2 with the sign of C-2C_j, and an interior minimum precisely at strict dominance. Solving its first-order equation gives rho_j=U/(U+V) and the value (U+V)^{alpha+1}; at threshold equality the balanced endpoint alone minimizes it. There cannot be two strict majority indices. Both optimal vectors attain unit diameter. Scaling to diameter d makes the minimum expenditure F/d^alpha, so matching B gives the displayed attained minimum and strict uniqueness, including for concave pricing in w. With unit prices the competing ratio sum (ell_i/L)^{alpha+1} decreases strictly from sum ell_i/L to zero for the unique-longest-arm case; this verifies both boundary regimes and the stated exponent for (3,2,2).

## originality

PASS

Do not credit the introduction of minimax resistance design, its linear-budget SDP formulation, or the exact linear-budget weighted star majority transition. The latter is explicitly covered by an earlier Resultary record. The supported advance is the arbitrary-price multi-edge spider law for every positive conductance-cost exponent: unique per-edge and radial allocation, normalized threshold on arm aggregates, and the resulting exponent-driven transition. The inspected general optimization papers do not provide or mechanically yield that classification.

## value

PASS

The optimization depends on every conductance and does not appear convex in the original coordinates for all exponents. Nonetheless an explicit unique design and tight sharp criterion distinguish when all radii coincide and when exactly one can differ, even under heterogeneous prices. The (3,2,2) example shows a genuine change in the geometry of the optimizer caused solely by the exponent. This gives exact benchmark solutions and a structural explanation beyond numerical optimization or redoing the linear weighted-star case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
