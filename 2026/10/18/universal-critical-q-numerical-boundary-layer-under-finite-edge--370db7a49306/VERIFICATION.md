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

# Verification and reproducibility

Run `python verify.py` in a Python environment with `numpy` and `scipy`. The checker builds the finite tridiagonal singular-value matrix directly from prescribed edge weights, independently checks the analytic sandwich on multiple test parameters, minimizes the exact scalar envelope, and compares scaled finite-size deficits against the analytical limit. The recorded run passed 276 assertions.

The tests sample only finitely many \(K,n,c\) and edge weights. They do not certify a universal limit. The mathematical proof of the theorem is in `RESULT.md`; the critical steps are the equality of the constrained norm envelope, Perron comparison, the compactness bound for its minimizers, and the separate \(c=0\) spectral calculation.
