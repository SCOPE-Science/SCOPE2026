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

All finite six maxima are proved by explicit exhaustive finite certificates, not an extrapolation. Inspected actual frozen certificates.json and verify.py and independently implemented the eligibility and compatibility predicates in JavaScript: n=4,6,8,10,12,14 yield 2,6,10,24,52,128 eligible unbordered words; for each case every same-color pair in the upper partition is incompatible and every witness pair compatible. At length14 verified all 335 same-color upper pairs and all 276 witness pairs, with 24 distinct eligible witnesses. Therefore M=(1,2,3,5,11,24). The restricted Dyck Construction 7 counts (1,2,3,5,11,20) are separate published construction sizes, not upper bounds. No claim beyond n14.

## originality

PASS

The earlier polarity-balanced and bounded-run code construction is explicitly treated as a feasible lower-bound construction, not a proof of maximum at length14. A complete independent 24-word optimality certificate supplies a genuinely different extremal invariant, subject to possibility of an unindexed existing finite table.

## value

PASS

A complete sharp finite classification under two physically motivated code constraints; the first improvement from a published 20-code to an optimal 24-code at n14 is a meaningful extremal cutoff supported by portable short certificates, not a merely heuristic numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
