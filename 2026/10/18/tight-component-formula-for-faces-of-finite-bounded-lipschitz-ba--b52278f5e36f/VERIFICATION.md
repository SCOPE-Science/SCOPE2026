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

The sum of the two maxima is the maximum over all products of a signed coordinate and an ordered-pair slope. Equality occurs exactly when both separate maxima are attained. For a nonconstant boundary point the anchor and tight-edge sets are nonempty and L>0. By finiteness, the inactive inequalities are strict along all sufficiently small segments in the nullspace of the active rows, making its nullity exactly the face dimension. Comparing all active-pair rows first with one edge fixed and then with one anchor fixed gives a common r=sign(f_i) h_i at all anchors, and slope change -r on all oriented tight edges. Consequently h_i+(r/L)f_i is a constant c_C on each component. A positive anchor fixes c_C=r/L, a negative one fixes c_C=-r/L, and both signs together force r=0; no anchor gives an independent offset. These relations suffice for all active rows and yield exactly u+epsilon. The constants ±1 are extreme by coordinatewise equality in the sup-norm bound; interior points are not extreme and the singleton case is an interval. Scanning all pairs and traversing the tight graph is quadratic in arithmetic operations and comparisons, not a bit-complexity or floating-point guarantee.

## originality

PASS

The supported distinct claim is the explicit dimension of every minimal face at nonconstant boundary points for the finite real sum norm, including the resulting full extremality characterization. The same-norm LP description is classical; the closest indexed graph result uses the same anchoring mechanism to prove vertex conditions for unit-edge graph metrics. Neither comparator supplies the full affine nullity formula for arbitrary faces and real finite metrics. No priority claim is made for the anchor mechanism itself.

## value

PASS

The criterion addresses a natural finite sum-norm extremality problem where the motivating literature supplies exact examples but local saturation alone is insufficient. The graph invariant detects both unanchored degrees of freedom and an independent global slope degree of freedom, yielding all minimal-face dimensions by an O(|S|^2) scan and traversal instead of forming and ranking product constraints. It also explains why a disconnected tight graph can support an extreme point. This all-face, arbitrary-metric calculation is useful independently of the discrete grid problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
