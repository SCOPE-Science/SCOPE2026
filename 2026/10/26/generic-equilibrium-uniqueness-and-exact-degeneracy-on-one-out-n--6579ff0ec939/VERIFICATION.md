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
# Reproducibility and limits

Run `python3 verify.py` with Python 3 standard library. It performs exact-rational exhaustive tests on directed cycles of lengths 2 through 7 with threshold coordinates 1, 2, and 3, compares the compact clipping recursion against independently expanded affine pieces, and verifies individual best-response equations on computed endpoints and midpoints. It reports 3276 cycles and 16646 checks, including sharp examples. All critical universal statements follow from the separate written proof rather than from finite sampling. No external certificate or independent scientific review is claimed.
