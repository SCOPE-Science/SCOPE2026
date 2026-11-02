---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For each n=3,...,16, independently enumerated the cyclic binary strings avoiding both 11 and 000, checked all candidate shattered fixed vertex subsets, and solved the complete finite Littlestone minimax recurrence over version-space bitsets. Reproduced all 14 rows, counts 39 and 90 at n=13,16, VC values 4 and 5 and adaptive values 5 and 6. The recurrence strictly descends on smaller nonempty hypothesis sets, proving termination and exhaustive upper/lower bounds. Product maximal-independent-set families on disjoint components give additive VC; standard optimal-online-mistake characterization gives additive Ldim. No inference for connected n>16.

## originality

PASS

The compared work on explicit-class Ldim/VC hardness, cycle maximal-independent-set counting and maximal-independent-set hypergraph static VC does not state the exact cycle adaptive ranks. The particular C13 first separation and C16 recurrence are not a title or parameter alias of an identified earlier theorem. Absence of exact published tables remains a priority risk.

## value

PASS

Natural first finite transition between static and adaptive shattering for canonical graph-solution memberships: C13 is the smallest cycle with gap, gap disappears at C14/C15 then returns C16. Disjoint 2-regular graph unions force an unbounded separation, so the sharp finite boundary is mathematically motivated and not just a convenience table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
