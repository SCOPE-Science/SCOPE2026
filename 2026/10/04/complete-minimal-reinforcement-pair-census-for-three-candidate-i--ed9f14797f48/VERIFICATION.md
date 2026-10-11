---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

IRV was independently implemented under the stated unique-elimination/unique-final convention. Exact enumeration gives no reinforcement pair for totals 2 through 12 and exactly 288 unordered pairs at total 13, all split 5+8. Independent symmetry counting gives 48 pair orbits of size 6; the 288 pairs produce 126 unions in 21 orbits, with partition multiplicity histogram 1:36, 2:36, 3:36, 4:18. These numbers satisfy the required weighted total 288 and reproduce the displayed witness.

## originality

PASS

Prior work establishes reinforcement failure for Hare/IRV, the 13-voter minimum, and—more recently—necessary and sufficient conditions for whether a fixed three-candidate union admits some paradox-producing partition. The audited theorem resolves a different finite boundary object: every unordered minimal pair, its candidate orbit, all 126 union profiles, and the exact 1/2/3/4 partition-multiplicity distribution. No checked source supplied that pair-and-partition census.

## value

PASS

This is a complete classification at the first possible reinforcement boundary for IRV, and the partition multiplicity is a natural refinement of the literature's union-profile existence question. It is not an arbitrary finite slice: it resolves all minimal witnesses and quantifies how many inequivalent decompositions each sharp union admits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
