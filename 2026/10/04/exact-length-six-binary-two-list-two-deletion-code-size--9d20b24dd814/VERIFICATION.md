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

Run `python3 verify.py` in this package. The script uses only exact rational arithmetic and exhaustive iteration over the complete finite ambient set. It verifies: (1) the pointwise weighted inequality for all 64 binary words of length six; (2) the weight sum 16/5 and resulting global bound 36/5; and (3) that the displayed seven-word code has two-deletion output multiplicity at most two.

The upper proof is finite and exhaustive, not statistical. No conclusion is drawn for lengths other than six. The script's success marker is `VERIFY_OK`.
