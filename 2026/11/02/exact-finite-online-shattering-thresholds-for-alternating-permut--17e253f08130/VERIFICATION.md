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

# Verification

Run `python verify.py certificate.json` from the directory containing both files. This uses only the standard Python library. It checks independent concept enumerations, explicit shattered star supports at all seven sizes, exact adaptive recurrences, an independent depth-ten no-tree recursion for eight positions, and a full depth-nine tree with 511 internal queries and 512 leaf witnesses. Expected terminal line: `ZIGZAG_ALL_CHECKS_PASS`. The computation is finite; no claim for nine or more positions or independent scientific certification follows.
