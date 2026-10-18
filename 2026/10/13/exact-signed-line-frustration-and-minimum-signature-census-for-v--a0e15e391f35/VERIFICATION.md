---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Bal Lemma 2 identifies frustration with min_orientation sum_v outdeg(v)*indeg(v). Each vertex-disjoint odd cycle must contain a mixed vertex, whose contribution is at least min_{v on C}deg(v)-1. Orient each cycle alternately with exactly one min-degree mixed vertex on odd cycles, then propagate consistent pure orientations along the bridge block tree; even cycles introduce no obstruction. Equality forces exactly these chosen mixed vertices, and independent binary phase choices for their external edges yield product_C sum_{min vertices}(1+1_{d>2}) labeled signatures after dividing the globally reversed orientations by 2. Recomputed all orientations for triangle, triangle+leaf, two triangles joined by a bridge, and two triangles joined by a length-2 path; both minima and optimal-signature counts agree.

## originality

PASS

The orientation objective and its special cubic reduction are prior work of Bal. In particular, for cubic vertex-disjoint-cycle cacti the frustration value is covered by Bal exact cubic 2*oct theorem; only the genuinely broader noncubic, degree-weighted cactus formula and complete minimum-signature count remain original on inspected evidence. Belardo-Stanic-Zaslavsky treat the signed line/total graph conventions and general frustration properties without an exact cactus minimizer census.

## value

PASS

A complete structural optimization and equality-case enumeration on the entire class with pairwise vertex-disjoint cycles; it gives degree-weighted odd-cycle costs even when bridge-attached degrees vary, and precise counts of labeled minimum switchings. Unlike an arbitrary small cactus computation this is a natural tractable boundary below general NP-hard frustration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
