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
# Verification

Run `python3 verify.py` in the directory containing the checker. The script uses only Python's standard library. It enumerates parent-selection histories through nine vertices with exact rational probabilities. It compares the root degree-1 and degree-2 masses and the leaf-count means under those events with the theorem, and checks the conditional mean at maximum root degree. The history loop also checks the covariance, both marginal means and the root-degree second moment, not a separate exact leaf-count second-moment identity. Further recurrence and numerical asymptotic checks include the previously published covariance and the variance scales. The packaged execution reported 397 deterministic assertions. The finite checks corroborate the all-size proof in `RESULT.md`; they do not establish publication priority.
