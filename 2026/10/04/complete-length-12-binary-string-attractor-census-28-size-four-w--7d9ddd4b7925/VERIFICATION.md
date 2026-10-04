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

Run `python3 verify.py`. The script uses only the Python standard library and prints `VERIFY_OK` after two independent exhaustive implementations agree on the complete length-12 distribution, the shorter-length threshold, and the reversal/complement orbit decomposition.

The finite proof scope is exactly all binary words of length 12, plus the threshold check for lengths 1 through 11. It does not certify any larger-length formula.
