---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## What can be reproduced

Execute `python3 verify_forest.py` from the directory containing the verification script; it uses Python 3 standard libraries only. Its reference enumerator independently checks the exact definition of super domination for every candidate subset of each tested forest. All computations use exact integer arithmetic; no floating-point thresholds are involved.

The captured expected standard output appears in `verification_output.txt`. It records 1442 labeled trees through six vertices, 400 seeded random forests through sixteen vertices, 3,363,980 tested subsets overall, 160 relabeling checks, 44 path checks, and `ALL_CHECKS_PASS`.

The program also compares the minimum nonzero polynomial degree with the separately computed forest maximum-matching cardinality. A direct induction in `RESULT.md`, not these finite tests, proves the unrestricted result. The accessible comparison literature and an abstract-only source risk are discussed in `REVIEW.md` and `AUDIT.json`.
