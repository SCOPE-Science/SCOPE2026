---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

- The proof derives the finite-dimensional joint limit from a quantitative visitation bound and exact factorization of the geometric residence time and the exit destination.
- Optional reproduction: `python3 checker.py` checks finite transition identities for \(3\le n\le17\) and finite visitation probabilities for target states up to four, by a recurrence over the departure chain. All these checks use integer or rational arithmetic. They do not establish the independence or joint limit.
