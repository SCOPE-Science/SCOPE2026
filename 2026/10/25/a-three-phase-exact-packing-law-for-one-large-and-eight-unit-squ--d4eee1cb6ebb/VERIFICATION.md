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

Exact proof review covers all quantifiers \(t\ge2\) and all axis-parallel placements. For \(L<\min\{5,t+2\}\), both complementary side widths cannot reach \(1\); any two unit-square projections in the same selected width-\(<2\) strip overlap interiorly, forcing separation of long-axis projections. Four unit intervals have an extreme lower endpoint at least \(3\). The upper endpoint of the other selected extreme unit square is at least \(t+1>L-1\). These inequalities imply strict crossing of the topmost vertical and rightmost horizontal squares. This obstruction is independent of any solver or finite sample.

Coordinate witnesses: for \(2\le t\le3\), eight units at \((t+i,j)\) with \(i\in\{0,1\}\) and \(0\le j\le3\); for \(3\le t\le4\), units at \((i,4)\), \(0\le i\le4\), and \((4,j)\), \(0\le j\le2\); for \(t\ge4\), units at \((i,t)\), \(0\le i\le4\), and \((t,j)\), \(0\le j\le2\). In every case the large square is \([0,t]^2\). Each family has exactly eight unit squares and fits in the claimed side with no positive-area overlap.

Scope limitations: no claim about \(t<2\), rotations, or completely arbitrary nine-square side vectors. Bounded novelty comparison is not an exhaustive priority guarantee; independent audit is not performed.
