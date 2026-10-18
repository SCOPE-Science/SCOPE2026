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

# Reproducible checks and limits

Run `python verify.py` with Python 3 and NumPy. The program computes the three-dimensional covariance matrix directly, its spectral radius, and the independent analytic Perron expression for multiple coupled heat/noise parameters, checking the unique threshold and the two asymptotic limits. It passed 185 deterministic tests in the actual submitted package source. The proof's infinitely many step sizes and asymptotic time indices are addressed by symbolic covariance decomposition, positivity and eigenvalue algebra, not finite enumeration or Monte Carlo sampling. No independent audit or formal certification has been performed.
