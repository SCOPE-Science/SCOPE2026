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

The all-size claim follows from the component-decomposition proof in `RESULT.md` and the generalized Catalan coefficient identity. The included standard-library program enumerates canonical non-crossing restricted-growth words for sizes up to 10, checks the Catalan cardinalities, and compares the computed total occurrence count with the closed form. These finite checks do not prove the all-size identity. The known-sequence comparison is only a numerical cross-reference; no bijection to Dyck paths or other structures is claimed.
