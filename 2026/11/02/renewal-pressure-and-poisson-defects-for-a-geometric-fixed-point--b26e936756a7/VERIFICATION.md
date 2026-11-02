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

The standalone `verify.py` was executed for \(\theta\in\{1/4,1/2,3/4\}\) and \(\beta\in\{4,8,12,16\}\), numerically solving the exact renewal-root equation with its infinite geometric tail evaluated analytically and rapidly decaying finite corrections summed to 500 terms. The root residual was below \(10^{-12}\) in every numerical test. It checked the exact excursion-energy identity for return lengths from one through eleven. The printed correction ratios approach their analytically predicted values where numerically resolved.

The conclusions involving every \(\beta\), infinitely many return intervals, asymptotic low-temperature pressure coefficients and stationary Poisson point-process convergence depend on the included mathematical proof. Numerical diagnostics alone cannot establish any such universal or limit statement.

The low-temperature expansion holds for each fixed \(0<\theta<1\) and has no asserted parameter-uniform remainder. No independent audit was performed.
