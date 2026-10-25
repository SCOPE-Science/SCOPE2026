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

# Verification of the exact-lag moment calculation

Reproduce the checks using `python3 checks/verify.py` (Python 3 standard library only). The program uses 1,045 exact rational pairs of OU transition factors to confirm the invariant-variance identity, constructs the monotone derivative numerator in floating point for diagnostic brackets, computes two critical lags for each of five chosen positive discount ratios, and integrates the coupled second-moment, fourth-moment and discounted-quartic equations using a fourth-order Runge–Kutta solver for five stable cases with different physical parameters. The recorded output is `checks/output.txt`.

The numerical checks reproduce the predicted reentrant divergence region and confirm that, in finite-value cases, independent time-domain integration matches the resolvent formula with relative error below \(10^{-4}\). A finite grid or numerical ODE solution is not an infinite theorem or an exhaustive check. The exact classification instead follows from the analytic factorization of the lag profile, the sign of its derivative, and the positive forcing of the moment hierarchy, as proved in `RESULT.md`.

There is no external independent validation and no assessment of results outside the explicit mathematical assumptions.
