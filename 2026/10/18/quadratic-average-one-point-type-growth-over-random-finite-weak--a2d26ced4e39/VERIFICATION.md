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

# Reproduction notes

Run `python3 verify.py` using the Python standard library. The program does not need downloaded references or any nonstandard packages. It independently enumerates all ternary comparison patterns and their level-permutation orbit signatures for 218 positive block-size compositions through eight parameter points with at most five levels. It also uses integer exponential-generating-function convolutions to compare the proposed weighted species formulas with direct enumeration of labelled ordered partitions through ten points.

Expected terminal markers: `VERIFY_OK` and `EGF_VERIFY_OK`. The numerical values at orders 15 and 30 are diagnostic only. The proof of the infinite limits uses poles of explicit analytic EGFs and does not rely on finite experimental extrapolation. The input paper and database are cited in `RESULT.md`; no external or independent review has been conducted.
