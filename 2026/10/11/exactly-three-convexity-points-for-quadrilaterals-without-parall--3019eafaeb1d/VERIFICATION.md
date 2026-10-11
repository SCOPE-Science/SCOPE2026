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

The domain was normalized affinely to \(A=(0,0)\), \(B=(1,0)\), \(D=(0,1)\), \(C=(p,q)\). Oriented edge determinants give \(p>0\), \(q>0\), \(p+q>1\); the two possible pairs of parallel opposite sides are exactly \(p=1\) and \(q=1\).

The proof then uses Schneider’s exact criterion: for no parallel edges, \(z\) is a convexity point if and only if every middle line through \(z\) has \(z\) in its corresponding middle set. This lemma was materially checked in the full paper. The support-function difference is odd, so at least one middle line passes through every \(z\); therefore any convexity point belongs to the middle hedgehog.

For a quadrilateral, the unoriented normal circle has four open cones. Inside each cone the opposite support faces are singleton vertices, making the middle set one vertex-pair midpoint and the middle line linear in the normal. Substitution on the four edge-generated middle segments gives exactly the four case rows stated in RESULT.md; every segment-interior point violates the criterion in a second cone, and one corner is excluded in each region.

The convex-hull check is independent algebra: in each region the excluded corner is a strict convex combination of the other three with the positive coefficients printed in RESULT.md. Thus the middle-hedgehog hull is triangular, and Schneider’s exposed-point lemma confirms all three surviving corners are convexity points.

No finite numerical experiment is used to establish the infinite family. No statement is made for the boundary cases with parallel sides.
