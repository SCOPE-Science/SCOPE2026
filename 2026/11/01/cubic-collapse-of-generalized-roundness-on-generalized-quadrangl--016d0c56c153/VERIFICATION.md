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

The analytic argument in `RESULT.md` proves the general result. The standalone `verify_gq_negative_type.py` was executed with NumPy and SciPy and returned `ALL_GQ_NEGATIVE_TYPE_CHECKS_OK`. It constructs actual symplectic GQ incidence matrices for prime orders 2, 3, and 5, validates every ordered shortest-path distance (900, 6400, and 97344 cases), checks the integer graph spectral parameters, and compares independent powered-distance eigenvalues with the theoretical zero-sum sectors. The roots are numerical approximations; the theorem defines them through a proved unique positive zero. No independent scientific audit has been performed.
