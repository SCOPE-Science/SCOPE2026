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

# Reproducibility
Run `python3 artifacts/check_square_root.py` with Python 3 (standard library only). It enumerates full permutation groups for input sizes two through six, checks input minimality, checks the root acceptance set and right-stabilizer sizes, and tests all ordered state pairs for sizes three through five. Compare stdout byte-for-byte with `artifacts/check_output.txt`. Computation is exhaustive only for the listed sizes; the proof of the infinite theorem is in RESULT.md.

No separate independent scientific audit or external validation has been performed.
