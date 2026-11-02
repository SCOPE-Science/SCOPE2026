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

The analytic argument establishes the all-parameter theorem independently of numerical checks: coercive strict convexity, real symmetry, a tangent-half-angle stationary integral with an exact involution, elliptic-integral algebra, and exact Fourier moment constraints for the compressed operator. Every equality needed to prove the bound and equality cases is stated in `RESULT.md`.

`CHECK.py` was executed in the candidate directory using `mpmath>=1.3` and returned `CHECK_OK 70`. It numerically verifies the optimizer for five \(r\) values, the elliptic formula, stationarity, strict local competitors, the inversion identity and the three required operator moments. These are supplementary tests, not an exhaustive check over all real parameters and not a substitute for the proof.

The claimed primary classification is 30H10 because the central new theorem is a sharp Poisson-weighted boundary \(L^1\) approximation associated with Hardy spaces; the truncated Toeplitz operator application uses the standard two-dimensional Hardy model-space correspondence. Earlier unindexed equivalent formulations remain an originality risk. Independent audit has not been performed.
