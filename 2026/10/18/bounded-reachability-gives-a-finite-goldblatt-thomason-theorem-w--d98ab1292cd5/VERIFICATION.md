---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Run `python3 CHECK.py` for all pointed depth types over one atom and evaluation of the specific separator for both frames at each \(h=0,\ldots,6\). The checker uses componentwise truth and finite type recursion. A symbolic transfer across the two paths establishes equivalence for every depth-at-most-\(h\) formula over any finite atom set. The finite checker does not prove that unrestricted statement or the general diagram upper bound.
