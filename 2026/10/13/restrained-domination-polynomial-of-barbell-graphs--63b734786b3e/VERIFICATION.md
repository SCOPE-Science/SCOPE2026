---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Any restrained dominating D must meet each clique; then domination of remaining vertices is automatic, while no isolated omitted vertices requires complement singleton only at a bridge endpoint with the other endpoint omitted. Exhaustive disjoint complement cases give C_n(q)^2 plus bridge-rescue configurations; inverse-variable transform yields exact formula and min layer. Independently enumerated all vertex subsets for n=3,4,5,6: valid 21,134,705,3310 respectively, and n² minimum sets; original verification extends n=3..8. The structural proof covers every n≥3 and the fixed bridge geometry.

## originality

PASS

The closest same-graph paper Jahari–Alikhani proves single bridge irrelevant for ordinary domination polynomial, but the additional restrained complementary-isolation condition changes the polynomial by an explicit nonnegative correction. Published restrained-domination-polynomial studies cover complete graphs, paths, cycles, joins/coronas in accessible abstracts rather than this family. The relevant 2019 full paper was inaccessible (Oxford VPN disconnected); best-of-knowledge priority, with explicit risk, supports the natural exact enumerator.

## value

PASS

A single bridge changes a canonical complement-constrained domination statistic even though it leaves ordinary domination polynomial unchanged; the complete all-cardinality enumerator and exact correction are reusable structural examples on a standard graph family and not a trivial relabeling of ordinary domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
