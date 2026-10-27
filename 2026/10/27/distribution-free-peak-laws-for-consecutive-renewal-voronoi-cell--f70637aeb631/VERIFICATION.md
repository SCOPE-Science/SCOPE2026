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

# Reproducibility and verification

Execute `python3 verify_peak_law.py` using the Python standard library. The checker independently enumerates all strict orderings of the gap variables for every specified lag from one through four and for each peak-count window size from one through six. It tests 28 independent exact-rational equalities and raises an exception on any discrepancy.

No simulation or finite enumeration proves the general case: infinite-size correctness is supplied by the two-gap comparison factorization, the three finite overlap orderings, the 3-dependence variance summation, and a bounded-block Lyapunov central-limit argument in RESULT.md. The input law needs only independent identically distributed atomless positive gaps; a stationary renewal process in physical space additionally needs finite mean gaps. The Gaussian limit concerns indexed-cell windows, not fixed-length physical windows.
