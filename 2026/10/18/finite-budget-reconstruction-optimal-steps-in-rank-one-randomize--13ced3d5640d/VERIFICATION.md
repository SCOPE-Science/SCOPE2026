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

The accompanying standard-library script `verify.py` enumerates every sample-index sequence for the stated small parameter cases in exact rational arithmetic. It computes the step-by-step iterate (not merely the formula), checks the unique proposed finite-horizon optimum and exact-interpolation schedule, and compares direct expected risk for constant steps with the theoretical closed form and its one-step change. It checks that the optimized schedule's residual is nonzero. Execute `python3 verify.py` from the package root. No third-party modules or external data are needed.

The general claims for arbitrary \(N\), \(b\), and deterministic schedules follow analytically from the exact bias–variance decomposition and Cauchy–Schwarz in `RESULT.md`. Enumerated cases cannot prove an unrestricted theorem. The result does not concern noisy data, nonidentical row coefficients, adaptive or randomized step sizes, or nonuniform index sampling.
