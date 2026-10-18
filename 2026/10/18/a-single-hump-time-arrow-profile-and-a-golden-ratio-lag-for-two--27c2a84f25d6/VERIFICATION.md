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
# Reproducibility and limits

Execute `python verification.py` with NumPy and SciPy. The program constructs an independent stationary Lyapunov covariance, evaluates matrix-exponential two-time cross covariances, and compares them with the spectral-integral formula. It also tests coincident poles, mixed-sign couplings, partial fractions and the triple-rate golden-ratio expression. The included execution passed 459 finite assertions.

The proof of positivity for all positive lags, the unique maximum and continuous peak-limit uses the analytic convolution and exponential-polynomial argument in `RESULT.md`; finite-grid positivity and unimodality tests cannot prove them. There has been no independent audit or empirical validation. The program uses no external data or downloaded publication.
