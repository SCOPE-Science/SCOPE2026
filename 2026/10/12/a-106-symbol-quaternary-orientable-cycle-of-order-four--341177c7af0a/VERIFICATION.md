---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The literal 106-character four-symbol witness was fetched from witness.txt at the assigned tree, and independently re-enumerated modular length-four windows. All 106 are nonpalindromic and occupy distinct reversal classes; 106 choose 2 = 5,565 unordered pairs checked. There are (4^4−4^2)/2=120 nonpalindromic reversal orbits and 14 unused. Hence M_4(4)≥106; this is existence, not optimality or any general alphabet statement.

## originality

PASS

The complete 106-letter witness yields a larger fixed-parameter existence bound than the primary 2025 Table 7 and the later 2026 table. General asymptotic sequence constructions and the 112 upper bound do not imply this witness. Best-of-knowledge priority is subject to other unindexed cycles.

## value

PASS

A finite extremal combinatorial construction can be valuable when it materially tightens a natural fixed-parameter bound: 106 improves the documented 88 by 18 (about 20%) and reduces the remaining gap to the 112 upper bound from 24 to 6. The exact witness is reusable for reversal-avoiding cycles and bidirectional sequence design; a general proof of the optimum is not required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
