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

Consolidate parallel molecular edges, and vary cycle circulations until an edge vanishes at no greater cost: the cost is concave between zeros and grows at infinity, so a finite segment ending at a zero or at a higher-cost distant point suffices even if all zeros are initially on one side. Augment each resulting forest to a spanning tree. The ordinary optimal transport is then supported on at most three edges, and concavity gives the p-to-1 norm factor 3^(1/p−1). Coordinatewise monotone Bernoulli coupling costs exactly the source distance; for p=1 any edge realizes equality. For B=b/a→∞ the unit midpoint direction has the listed masses. A tree retaining the two horizontal edges has three loads tending to 1/3 (the long edge carries cut mass 1/(3B)); any omitted horizontal edge leaves a nonzero limiting imbalance that cannot be met by long flows tending to zero. The finite minimum therefore has p-cost tending to 3^(1−p). Axis exchange gives the other limit. For the square baseline, a midpoint tangent is enough to represent any secant exactly. By reflections use nonnegative direction coordinates u,v with u+v=1. In a monotone four-side flow, the two horizontal edges can reach loads min(u,Q) or min(u,1−Q) respectively by cycle adjustment, where Q is the outflow from 00; the vertical analog has v. Thus a cycle endpoint can retain one load ≥1/2 on at most three edges, giving the square upper bound by concavity. At s=t=1/4 and u=v=1/2 the masses are (−3,1,1,1)/4. Exact cut profiles, or the tree rooted at 00, give minimal loads (1,1,2)/4: all edges have at least one unit and the path to 11 forces at least one edge of load two units or more. The resultant square norm is strictly below the uniform anisotropic value for p<1. The independent replay computed exact tree-cut loads and a finite anisotropic diagnostic; it is not a proof of the limit.

## originality

PASS

Credit earlier finite spanning-tree norm machinery and exact equal-edge interpolation, as well as the exact matching p=1/2 specialization in a same-day distinct record. The supported distinct contribution is the sharp, aspect-uniform limit for the general exponent range, not any of those results or the upper-bound norm comparison in isolation. Neither the equal-side result nor the single-exponent profile entails sharpness for variable p; the three balanced loads and exclusion of all other trees in the degeneration resolve that additional issue. No claim of priority for the shared special case.

## value

PASS

For the canonical cell interpolation used in free p-space extensions, a sharp distortion guarantee across aspect ratios answers a natural geometric question: the exact square bound fails uniformly even in dimension two for every p<1. The general saturation mechanism explains how two short transport legs coexist with a long leg carrying vanishing mass but comparable weighted cost. This is useful information beyond a coarse upper bound or an isolated exact exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
