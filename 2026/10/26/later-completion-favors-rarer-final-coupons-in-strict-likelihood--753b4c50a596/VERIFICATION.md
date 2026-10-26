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

The proof establishes the exact joint exponential generating function and a strict convolution determinant inequality from log-concavity; it applies for every positive probability vector and every supported integer completion time. No large-sample limit is invoked.

The independently implemented dynamic program and coefficient-extraction computation in `verify.py` agree exactly for seven rational parameter vectors of two through five types and for completion times through 22. Running `python verify.py` requires only the Python standard library and gives seven `PASS` lines and an `ALL FINITE CHECKS PASS` summary.

Finite checks corroborate but do not prove the infinite theorem. Independent audit has not been performed. The cited sources contain substantially related joint-distribution formulas, so independent priority verification remains valuable.
