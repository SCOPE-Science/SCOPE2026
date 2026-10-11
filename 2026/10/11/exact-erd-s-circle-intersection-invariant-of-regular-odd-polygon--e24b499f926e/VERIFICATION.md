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

The theorem was checked analytically and by finite sanity checks.

The analytic proof derives the squared-distance derivative along each regular-polygon edge and uses strict convexity to prove monotonicity to the farthest vertex; symmetry of the opposite edge proves strict decrease to its midpoint. This proves the at-most-four assertion for every odd order.

The included script samples odd orders from \(3\) through \(31\), checks the derivative signs and opposite-edge midpoint condition, solves the circle/segment equations directly, and confirms four intersections for representative radii between the opposite-midpoint and farthest-vertex distances. These finite checks do not prove the all-orders statement.

The primary source was inspected from the author-hosted PDF. Its publication date, primary MSC, definition of \(N(K)\), and the regular-odd four-intersection lower-bound statement were verified directly.

Limit: the search process cannot rule out an unindexed equivalent observation; this remains an originality risk.
