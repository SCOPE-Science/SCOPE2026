---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. For the unit-edge regular octahedron, four top/bottom face rhombi unfold the fixed vertex N to N′=(√3,0) on each bottom triangle. A globally continuous facewise Euclidean 1-Lipschitz distance candidate gives a lower bound for all surface paths, while straight rhombus paths realize it, so it is globally exact (including cut-locus points). For r<=1 each rhombus gives a π/3 disk sector, resulting F=πr²/(3√3). For 1<r<√3 the complement comprises four equal corner triangles minus circular segments with t=(3−√(4r²−3))/2 and s=√3(1−t/2), giving the stated arccosine branch. Barycentric second moments on top/bottom faces are 5/12,17/12 hence E[R²]=11/12; differentiating gives F″ jump −4, and radial expansion at S yields tail (2/3)ε². Independent face-grid CDF computations agree. Universal proof is geometric.

## originality

PASS

Qualified best-of-knowledge novelty of the full fixed-vertex intrinsic surface-area distance distribution on the regular octahedron; no originality credit for known polyhedral source-unfolding methods, ambient octahedron chord laws, or farthest-point maps.

## value

PASS

PASS. The vertex-centered metric-ball area profile is a natural intrinsic polyhedral invariant. The complete distribution, squared moment 11/12, unique antipodal radius √3, exact differentiability break and tail coefficient give reusable exact data for geodesic probability and wavefront comparison, not just a numerical one-point computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
