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

# Reproducibility and boundaries

Run `python3 verify.py` in the folder containing the extracted standalone files. A successful run prints `VERIFY_OK 150006 checks` and independently checks: the integer-coordinate vertex and edge model; direct edge-sign changes versus the analytic triangle-inequality chamber criterion; Gaussian-sphere frequency consistency with the closed probability formula; and symmetric finite differences of the local Hessian along three logarithmic stretch directions. The exact mathematical proof is in `RESULT.md`. The verifier uses finite tests and numerical tolerances, hence is supporting evidence rather than a proof of all-direction and asymptotic claims. Independent audit has not been performed.
