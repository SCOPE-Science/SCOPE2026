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

# Verification

Run `python3 verify.py` (Python standard library only). The checker performs exact arithmetic in the ordered quadratic field of \(\sqrt5\). It reconstructs all icosahedral facets and edges, all dual adjacency edges, all simple great-circle arrangement chambers, the five polygon-type chamber classes, and all 20 nontrivial cone-containment certificates. The four generic integer-coordinate witnesses \((-3,-2,0)\), \((-3,-3,-3)\), \((-3,-3,-1)\), and \((-3,0,-2)\) certify nonempty open interiors of the four supported joint outcomes. Each sign test compares rational coefficients exactly; the exhaustive search is justified because all chamber vertices occur at pairwise great-circle intersections and there are no triple intersections.

The checker executed from the actual standalone path, and its terminal line was `ALL_CHECKS_PASSED`. Specific passed stages include `EXACT_SHADOW_92_CHAMBERS_20_HEX_60_TRI_12_PENT_PASSED`, `EXACT_SECTION_32_CHAMBERS_20_TRI_12_PENT_PASSED`, `EXACT_ALL_20_SECTION_TWELVE_CONES_NESTED_IN_SHADOW_SIX_CONES_PASSED`, and `EXACT_GIRARD_JOINT_PROBABILITY_FORMULAS_AND_CROFTON_EXPECTATION_PASSED`.

The exact finite computation is exhaustive for the algebraically established finite arrangement; it is not Monte Carlo or a numerical substitute for the reduction to a finite list. Floating-point values are used only to display inverse-trigonometric evaluations after the exact geometric characterization. Independent mathematical audit has not been performed. Historical priority outside the cited accessible material remains unresolved.
