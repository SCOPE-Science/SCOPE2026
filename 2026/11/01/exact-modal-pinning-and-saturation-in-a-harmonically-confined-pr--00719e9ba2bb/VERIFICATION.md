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

# Reproduction

Run `python verify.py` with NumPy and SciPy installed. The program evaluates the stationary density by a parabolic-cylinder resolvent formula and, separately, by directly integrating the Gaussian Ornstein–Uhlenbeck transition density over the independent exponential time elapsed since resetting. It checks 120 parameter/position combinations at rates below and above the trapping-relaxation rate, tests six free-mode root brackets, tests six reset-distance pinning thresholds, and tests the exact \(s=1\) integral identity.

The verified maximum relative density discrepancy in the 120 comparisons was approximately \(1.43\times10^{-10}\). At normalized reset rate \(s=1/2\), the free mode is approximately \(0.764950867389776\). For normalized reset point \(y_0=1\), the unique critical normalized rate is approximately \(0.611761705293214\).

# Analytic verification boundary

The all-parameter conclusions are proved using the positive-integral representation for \(U_s\), a Riccati derivative identity, the strictly positive covariance of \(t\) and \(\log t\) under an explicit measure, the asymptotic stationary-sign test and the exactly soluble \(s=1\) case. The finite numerical comparisons corroborate the formulas but cannot prove global monotonicity, uniqueness or historical novelty. No independent scientific audit has been performed.
