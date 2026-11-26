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

The narrowed finding is exact synchronous stopping at d−1. Round r distinguishes each marker distance truncated at r+1. At round d−1 the distances are exact; a distance d forces s=d−t, otherwise the needed simultaneous-decrement neighbor pair is visible at round d−2 (the count is zero if a target distance is negative). Recovering s recovers the whole triple, and these are orbits of a color-preserving subgroup, so the partition is equitable. For the lower bound the pairs (d,d) and (d−1,d) are indistinguishable through d−2 by regular-graph locality but split in the next round. The complete-graph case d=1 starts equitable. A separate direct-graph replay corroborated the stopping round and orbit data in 24 nonbinary cases (up to 243 vertices) and reproduced the antipodal binary exception. The frozen finite outputs are recorded evidence, not a proof; the uploaded script was not executed.

## originality

PASS

The original broad package presented two already published conclusions alongside the stopping law: stabilizer orbit recovery and the accompanying class count and sizes. The repaired statement claims only exact nonbinary stopping from the three-color start and explicitly credits the earlier invariant and formulas. The previous general orbit result explicitly excludes exact round count from that start; its proof gives no d−1 stopping claim. The binary timing classification does not dominate q≥3. No covering statement for the narrowed stopping law was established in the inspected evidence.

## value

PASS

Exact synchronous iteration count for this canonical two-marker seed is a separate algorithmic invariant from the stable partition. The boundary shortcut removes an otherwise needed round, and the locality example proves that no faster round bound is possible for any separation in the nonbinary case. This is a sharp timing classification, not a reassertion of the known orbit table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
