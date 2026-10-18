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

# Reproduction and verification

Run `python3 CHECK.py` using the Python 3 standard library. It directly enumerates all admissible words through length fourteen and tests every binary scattered subsequence pattern of the necessary lengths. It also computes independent four-state transfer counts, compares the explicit binomial-coefficient formula to the scalar recurrence through length 120, and checks finite-length extrema.

Expected terminal line: `ALL CHECKS PASSED`.

The proof of the all-length exact enumerative identities is the complete case distinction and symbolic elimination given in `RESULT.md`; no finite computation is treated as a proof of an infinite identity. The Gaussian limit requires the analytic simple-root argument and characteristic-function expansion, not numerical sampling. Exact constants follow from explicit derivatives of the cubic characteristic equation. External independent auditing remains unperformed.
