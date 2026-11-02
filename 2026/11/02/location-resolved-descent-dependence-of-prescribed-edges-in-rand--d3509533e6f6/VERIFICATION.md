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

# Reproducible checks and limits

Run `python3 check_matching_descents.py` with Python 3's standard library. It enumerates all 15, 105, 945, and 10,395 perfect matchings at even orders 6, 8, 10, and 12, respectively, computes the induced involution and ordinary descents, and independently compares each prescribed-edge conditional descent mean against the closed formula and a position-by-position exact-rational counting formula. It checks the moments of the short-chord count, its covariance with descents and the invariant total-edge covariance identity at every even order up to 100. The 215 assertions succeed.

The code is a finite independent arithmetic cross-check. The proof for unbounded even orders is contained in `RESULT.md`; exhaustive small-order checks alone cannot establish an infinite theorem. The priority comparison is necessarily limited to the inspected literature and available records; independent mathematical validation is not performed.
