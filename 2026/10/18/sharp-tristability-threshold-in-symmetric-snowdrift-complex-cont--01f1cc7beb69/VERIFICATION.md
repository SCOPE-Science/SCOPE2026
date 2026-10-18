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

# Verification of the symmetric Snowdrift phase theorem

The analytic proof appears in `RESULT.md` and applies to every real \(k>0\) and \(0<\lambda<2\) within the specified symmetric family. For the exact witness \(k=1/2\), \(\lambda=10/9\), the standalone script `verify_symmetric_snowdrift.py` verifies the complete interior-root cubic factorization and the three exact interior slopes together with both endpoint derivatives. It also samples sign patterns for eight specified admissible parameter pairs.

Command: `python verify_symmetric_snowdrift.py`.

Observed result: `PASS: exact cubic factorization, all five fixed points, exact slopes, and 8 qualitative parameter samples`.

The script verifies the stated symbolic witness and provides finite illustrative tests. It does not prove the global all-parameter threshold, which follows from strict convexity/concavity of the transformed hyperbolic tangent and the one-dimensional flow argument in `RESULT.md`. It does not simulate the discrete finite-population stochastic process. Independent audit has not been performed.
