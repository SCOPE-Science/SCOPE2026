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

The recurrence update is implemented directly in `verify.py` from the neighbour rule, without fitted parameters or external dependencies. The program exhausts all \(3^{n+1}\) labelled states for \(3\le n\le8\), checks full extinction by time five, records exact depth distributions, and constructs witnesses of depth four or five for \(4\le n\le80\). See `verify_output.txt` for actual output.

The universal bound and all-size sharpness require the formal rim-exclusion lemma and explicit witnesses proved in `RESULT.md`; finite checks are independently corroborating and close the bounded exceptional cases only. Published prior-work coverage remains a bounded literature assessment, not external certification.
