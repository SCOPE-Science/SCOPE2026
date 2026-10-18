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

The exact proof is in `RESULT.md`. Reproduce bounded cross-checks with `python3 verify.py` (Python standard library). The checker independently computes small divisor sums and distinct prime supports and enumerates instances of the classified forms against all odd bases 3 through 151. A successful run prints `VERIFY_OK` and the counts. The infinite classification relies on the stated exact arithmetic and Ren–Chen's established theorem. Finite trials are neither an exhaustive search of all bases nor independent certification.
