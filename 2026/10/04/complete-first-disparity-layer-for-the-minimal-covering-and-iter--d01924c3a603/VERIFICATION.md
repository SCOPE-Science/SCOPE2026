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

Independent all-32768 enumeration reproduced the full histogram: 20240 equal (3,3), 6144 equal (1,1), 4704 equal (5,5), 1440 equal (6,6), and 240 strict (3,6). Canonicalization gives one strict class, encoding 1332, orbit size 240 and stabilizer order 3.

## originality

PASS

The published exhaustive disparity study gives \(d(MC,UC^\infty)=6\), not the 240-case/one-class strict layer.

## value

PASS

The theorem identifies the unique finite obstruction at the first disparity order and shows the uncovered operator fixes all six vertices while MC selects a three-vertex core.

The dated certificate retains the supplied scientific assessment, sources and limitations.
