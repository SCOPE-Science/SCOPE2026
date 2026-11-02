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

# Reproducibility and verified scope

Run \(\texttt{python verify.py}\) with Python 3 and \(\texttt{mpmath}\) version at least 1.2. A completed execution reported 100 passed tests, checking Mellin integration, complex-Gamma Fourier reconstruction of the ideal scale sum, scale covariance, finite-grid tail bounds, and the leading small-grid amplitude for the dimensions and selected ratios described in \(\texttt{RESULT.md}\).

The equations and bounds for **all** real \(q>1\), all separations \(r>0\), and both permitted spatial dimensions rely on the analytic arguments in \(\texttt{RESULT.md}\), not numerical extrapolation. The infinite bilateral increment sum is mathematically well defined but its associated sum of zero-lag covariances diverges. Empirical turbulence statistics, downstream solvers and independent validation are not verified here.
