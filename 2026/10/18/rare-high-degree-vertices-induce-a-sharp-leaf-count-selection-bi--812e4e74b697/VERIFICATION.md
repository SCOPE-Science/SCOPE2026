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

The standalone `verify.py` computes the exact distribution-free Prüfer-code covariance in two different ways: direct enumeration of all codes for small labeled trees, and the dynamic-programming count of allocations with a bound on every box load. The checks use Python integers and rational numbers. Larger dynamic-programming instances additionally test the sign and magnitude of finite covariances.

Run `python3 verify.py` from the directory containing this file and the script. The expected terminal sentinel is `VERIFY_OK 45`. These finite computations do **not** establish the limiting theorem, which is proved analytically in `RESULT.md` by uniform factorial-moment bounds and inclusion-exclusion. The cited historical works address marginal degree extremes and fixed-degree counts; a complete older maximum-degree article was not available for full-text priority comparison.
