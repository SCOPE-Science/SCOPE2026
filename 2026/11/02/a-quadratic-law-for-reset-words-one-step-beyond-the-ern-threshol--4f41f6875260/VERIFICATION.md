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

The elementary rotating-frame inverse-image proof establishes the all-\(n\) theorem. The accompanying `verify.py` is a standalone Python 3 checker requiring only the standard library; executing `python3 verify.py` produces `VERIFY_OK` after checking target-state counts for every \(2\le n\le13\), explicit candidate membership and uniqueness, and literal exhaustive second-shortest reset-word sets for \(2\le n\le8\).

The finite calculations do not prove the universal claims; they serve as independent implementation-level tests of the sharp bound and structural classification. No independent external audit or formal certificate was performed.
