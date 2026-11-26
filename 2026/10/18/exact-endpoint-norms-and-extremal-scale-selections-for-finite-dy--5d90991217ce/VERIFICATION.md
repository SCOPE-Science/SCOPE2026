---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Run `python checker.py` with the retained standard-library checker. It constructs every column of the conditional-expectation matrices for depths 1–6 and checks the shell formula. At depths 1–15 it exhausts the selectors in exact rational arithmetic and compares each full maximizing set with the stated classification. The formula for the sharp value is retained as a check against the known Walsh/discrepancy maximum, not as a new result. Finite tests cannot prove the classification at arbitrary depth; the proof uses the strict two-action Bellman comparison with the sole reachable tie before the last step.
