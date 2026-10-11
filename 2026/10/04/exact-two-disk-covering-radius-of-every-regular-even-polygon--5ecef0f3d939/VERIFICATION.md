---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The general convex-polygon two-center reduction permits assignment of complementary connected boundary chains. One chain has at least half the perimeter; any half-perimeter subchain starts at \(x=(t,a)\) on a side and ends at \(-x\), and the two fixed left-side vertices force diameter at least \(\sqrt{4a^2+(b+|t|)^2}\). This yields the lower bound \(\sqrt{a^2+b^2/4}\). For the midpoint cut, the disk centered at \((-b/2,0)\) contains every left-half vertex because \(R^2+bu+b^2/4\le R^2-3b^2/4\), and convexity fills the half-polygon. Equality forces \(t=0\), and the two diameter pairs force the center, proving the optimizer classification. Independent algebraic checks reproduced the square, hexagon and general formula.

## originality

PASS

The complete accessible primary text of Choi--Jeong--Ahn gives the exact general algorithm and the connected-subchain structural reduction, but a full-text search finds no regular-polygon specialization. Resultary returns the assigned theorem as the exact hit; broader two-center sources are algorithmic. No source located states the closed regular-even formula or the uniqueness classification.

## value

PASS

The regular even polygons are the canonical symmetric test family for the continuous two-center problem. The result gives an exact radius and complete optimizer classification for every member of that family, including the side-interior effect that distinguishes polygon covering from covering only the vertices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
