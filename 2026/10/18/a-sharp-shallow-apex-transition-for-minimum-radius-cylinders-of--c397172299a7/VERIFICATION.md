---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A unit direction perpendicular to the candidate axis and in the base plane always exists. The base width in that direction is unchanged by projection to the normal plane, and is bounded by the diameter of the circular cross-section. On each open direction arc with fixed extremal base vertices, the width satisfies width'' = -width < 0, so any minimizing direction must be a support tie. For a triangle its tie widths are the side altitudes 2A/|e|, with exactly the longest sides minimizing. For equality in the cylinder bound, the two projected endpoints of the corresponding longest side have the same extreme coordinate in the cross-section disk. A disk has a unique point in that supporting line, so the two projections coincide and the axis direction is horizontal and parallel to that side. Together with the opposite vertex, the common projection fixes a diameter and thus the center (w/2,0) in base-normal/vertical coordinates. The apex projects to (lambda_e*w,h); substituting into the disk inequality gives exactly h² ≤ w²*lambda_e*(1-lambda_e). Convexity reduces containment to vertices. The squared inequalities are non-strict at the endpoints, and taking their union includes all possible tied longest sides. Continuity of the optimized cross-section radius follows because changing every projected vertex by at most epsilon changes its minimum enclosing disk radius by at most epsilon (or measure all centers in ambient space and project their centers back). Compactness of the direction sphere gives an attained minimum, so impossibility of equality for h>H_* is strict. Checked the illustrative radius and cutoff squares algebraically; the inspected check_examples.py was not executed and the examples are not needed for the exact proof.

## originality

PASS

The flat triangle width bound and general minimum-cylinder formulations are established. Petitjean’s exact five-point circumscription theorem yields the endpoint cylinder and, with the base lower bound, the radius plateau up to that endpoint for the equilateral centroid specialization. It is not the arbitrary-base, arbitrary-interior-projection formula or the complete optimizer classification. The indexed pyramid-width statement treats another invariant, and the closest indexed cylinder plateau is for a later square-pyramid problem with restricted directions. The supported distinct claim is the general sharp barycentric cutoff with equality rigidity.

## value

PASS

The exact robustness of an enclosing-cylinder optimum under lifting a new vertex is a natural parametric question for outer radii. The cutoff needs only the base minimum width and the opposite-vertex barycentric weights, and rigidity identifies all axes rather than just constructing a covering cylinder. For example, the two tied long sides of the base with planar vertices (−2,0),(2,0),(0,4) can be assigned opposite barycentric weights 1/6 and 1/3, giving different cutoffs, so one orientation really can disappear with no radius increase. The theorem is useful on the plateau without purporting to solve the post-plateau optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
